from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REGISTRY_ENV = "AGENT_TEAM_REGISTRY"


@dataclass(frozen=True)
class TeamSpec:
    name: str
    path: Path
    source: str


@dataclass(frozen=True)
class InstallPlan:
    team_name: str
    team_dir: Path
    project_dir: Path
    opencode_dir: Path
    agent_files: list[Path]
    protocol_files: list[Path]
    skill_dirs: list[Path]


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.list:
            return list_teams(args)
        if args.command == "list":
            return list_teams(args)
        if args.command == "add":
            return add_team(args)
        if args.command == "update":
            return update_team(args)
        if args.command in {"remove", "rm"}:
            return remove_team(args)
        if args.command == "registry":
            return print_registry(args)
        if args.command == "install":
            return install_team(args)
        parser.print_help()
        return 1
    except AgentTeamError as exc:
        print(f"agent_team: error: {exc}", file=sys.stderr)
        return 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agent_team",
        description="Install a local agent team into an OpenCode .opencode directory.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "common commands:\n"
            "  agent_team list\n"
            "  agent_team add --name <team_name> --path <team_dir>\n"
            "  agent_team install --name <team_name> [--path <project_path>]\n\n"
            "registry commands:\n"
            "  add        Register a custom team directory for future installs.\n"
            "  update     Update a registered custom team's path.\n"
            "  remove     Remove a custom team from the registry.\n"
            "  registry   Print the registry file path.\n\n"
            "install options:\n"
            "  --name NAME   Team directory name, for example story_team, code_review_team, or paper_survey_team.\n"
            "  --path PATH   Project directory where .opencode should be created. Defaults to the current working directory.\n"
            "  --dry-run     Print planned operations without writing files.\n"
            "  --clean       Remove generated .opencode/agents, .opencode/protocols, and .opencode/skills before installing.\n\n"
            "Run `agent_team install --help` for the full install command help."
        ),
    )
    parser.add_argument(
        "--repo",
        type=Path,
        default=None,
        help="Path to the multi-agent-team repository. Defaults to AGENT_TEAM_HOME or this CLI's repository root.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available agent team names and exit.",
    )

    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser("list", help="List available agent teams.")
    list_parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON.",
    )
    list_parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show team source and path.",
    )

    add_parser = subparsers.add_parser("add", help="Register a custom agent team.")
    add_team_name_argument(add_parser)
    add_parser.add_argument(
        "--path",
        type=Path,
        required=True,
        help="Path to the custom team directory containing agents/team_lead_agent.md.",
    )
    add_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing registered team with the same name.",
    )

    update_parser = subparsers.add_parser("update", help="Update a registered custom team path.")
    add_team_name_argument(update_parser)
    update_parser.add_argument(
        "--path",
        type=Path,
        required=True,
        help="New path to the custom team directory.",
    )

    remove_parser = subparsers.add_parser("remove", aliases=["rm"], help="Remove a custom team from the registry.")
    add_team_name_argument(remove_parser)

    subparsers.add_parser("registry", help="Print the custom team registry path.")

    install_parser = subparsers.add_parser("install", help="Install one agent team.")
    install_parser.add_argument(
        "--name",
        required=True,
        help="Team directory name, for example story_team, code_review_team, or paper_survey_team.",
    )
    install_parser.add_argument(
        "--path",
        type=Path,
        default=Path.cwd(),
        help="Project directory where .opencode should be created. Defaults to the current working directory.",
    )
    install_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned operations without writing files.",
    )
    install_parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove generated .opencode/agents, .opencode/protocols, and .opencode/skills before installing.",
    )
    return parser


def add_team_name_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--name",
        required=True,
        help="Team registry name, for example my_team.",
    )


def list_teams(args: argparse.Namespace) -> int:
    repo_root = resolve_repo_root(args.repo)
    teams = discover_teams(repo_root)
    if getattr(args, "json", False):
        if getattr(args, "verbose", False):
            payload = [{"name": team.name, "source": team.source, "path": str(team.path)} for team in teams]
        else:
            payload = [team.name for team in teams]
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for team in teams:
            if getattr(args, "verbose", False):
                print(f"{team.name}\t{team.source}\t{team.path}")
            else:
                print(team.name)
    return 0


def add_team(args: argparse.Namespace) -> int:
    repo_root = resolve_repo_root(args.repo)
    name = normalize_team_name(args.name)
    team_dir = args.path.expanduser().resolve()
    validate_team_dir(team_dir)

    registry = load_registry()
    if name in registry and not args.force:
        raise AgentTeamError(f"custom team {name!r} already exists. Use `agent_team update --name {name} --path ...` or `--force`.")

    built_in = {team.name for team in discover_builtin_teams(repo_root)}
    if name in built_in and not args.force:
        raise AgentTeamError(f"{name!r} is a built-in team name. Use a different name or pass --force to override during lookup.")

    registry[name] = str(team_dir)
    save_registry(registry)
    print(f"Registered {name} -> {team_dir}")
    print(f"Registry: {registry_path()}")
    return 0


def update_team(args: argparse.Namespace) -> int:
    name = normalize_team_name(args.name)
    team_dir = args.path.expanduser().resolve()
    validate_team_dir(team_dir)

    registry = load_registry()
    if name not in registry:
        raise AgentTeamError(f"custom team {name!r} is not registered. Use `agent_team add --name {name} --path {team_dir}` first.")

    registry[name] = str(team_dir)
    save_registry(registry)
    print(f"Updated {name} -> {team_dir}")
    return 0


def remove_team(args: argparse.Namespace) -> int:
    name = normalize_team_name(args.name)
    registry = load_registry()
    if name not in registry:
        raise AgentTeamError(f"custom team {name!r} is not registered")
    removed = registry.pop(name)
    save_registry(registry)
    print(f"Removed {name} -> {removed}")
    return 0


def print_registry(args: argparse.Namespace) -> int:
    print(registry_path())
    return 0


def install_team(args: argparse.Namespace) -> int:
    repo_root = resolve_repo_root(args.repo)
    team = resolve_team(repo_root, args.name)
    project_dir = args.path.expanduser().resolve()
    plan = build_install_plan(team.path, project_dir, team_name=team.name)

    print_plan(plan, dry_run=args.dry_run, clean=args.clean)
    if args.dry_run:
        return 0

    project_dir.mkdir(parents=True, exist_ok=True)
    plan.opencode_dir.mkdir(parents=True, exist_ok=True)

    if args.clean:
        remove_generated_dirs(plan.opencode_dir)

    copy_files(plan.agent_files, plan.opencode_dir / "agents")
    copy_files(plan.protocol_files, plan.opencode_dir / "protocols")
    copy_skill_dirs(plan.skill_dirs, plan.opencode_dir / "skills")
    write_agents_md(plan)
    merge_opencode_json(plan)

    print(f"Installed {plan.team_name} into {plan.opencode_dir}")
    return 0


def build_install_plan(team_dir: Path, project_dir: Path, *, team_name: str | None = None) -> InstallPlan:
    agents_dir = team_dir / "agents"
    protocols_dir = team_dir / "protocols"
    skills_dir = team_dir / "skills"

    validate_team_dir(team_dir)

    agent_files = sorted(agents_dir.glob("*.md"))

    protocol_files = sorted(protocols_dir.glob("*.md")) if protocols_dir.is_dir() else []
    skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir()) if skills_dir.is_dir() else []

    return InstallPlan(
        team_name=team_name or team_dir.name,
        team_dir=team_dir,
        project_dir=project_dir,
        opencode_dir=project_dir / ".opencode",
        agent_files=agent_files,
        protocol_files=protocol_files,
        skill_dirs=skill_dirs,
    )

def copy_files(files: Iterable[Path], destination_dir: Path) -> None:
    destination_dir.mkdir(parents=True, exist_ok=True)
    for source in files:
        shutil.copy2(source, destination_dir / source.name)


def copy_skill_dirs(skill_dirs: Iterable[Path], destination_dir: Path) -> None:
    destination_dir.mkdir(parents=True, exist_ok=True)
    for source in skill_dirs:
        target = destination_dir / source.name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)


def remove_generated_dirs(opencode_dir: Path) -> None:
    for name in ("agents", "protocols", "skills"):
        path = opencode_dir / name
        if path.exists():
            shutil.rmtree(path)


def write_agents_md(plan: InstallPlan) -> None:
    protocol_names = [path.name for path in plan.protocol_files]
    agent_names = [path.name for path in plan.agent_files]
    skill_names = [path.name for path in plan.skill_dirs]

    body = [
        f"# OpenCode Agent Team: {plan.team_name}",
        "",
        "This project has an installed multi-agent team. Treat this file as mandatory project guidance.",
        "",
        "## Loading Rules",
        "",
        "- Start team tasks with `@team_lead_agent`; it is the default entry point and coordinator for this team.",
        "- Follow every file listed in `.opencode/protocols/`; these are shared hard rules, not optional skills.",
        "- Use `.opencode/agents/` for role prompts and task routing.",
        "- Use `.opencode/skills/` for task-specific methods when an agent prompt names a skill.",
        "- Do not treat a revision checklist as completed work unless a new draft version and change log exist.",
        "- Do not generate final delivery files unless the installed delivery protocol and iteration gate allow it.",
        "",
        "## Installed Agents",
        "",
        *[f"- `.opencode/agents/{name}`" for name in agent_names],
        "",
        "## Installed Protocols",
        "",
        *[f"- `.opencode/protocols/{name}`" for name in protocol_names],
    ]

    if skill_names:
        body.extend(["", "## Installed Skills", ""])
        body.extend(f"- `.opencode/skills/{name}/SKILL.md`" for name in skill_names)

    body.extend(
        [
            "",
            "## Source",
            "",
            f"- Team: `{plan.team_name}`",
            f"- Installed from: `{plan.team_dir}`",
            "",
        ]
    )

    (plan.opencode_dir / "AGENTS.md").write_text("\n".join(body), encoding="utf-8")


def merge_opencode_json(plan: InstallPlan) -> None:
    config_path = plan.opencode_dir / "opencode.json"
    config: dict[str, object]

    if config_path.exists():
        try:
            config = json.loads(config_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise AgentTeamError(f"existing {config_path} is not valid JSON: {exc}") from exc
        if not isinstance(config, dict):
            raise AgentTeamError(f"existing {config_path} must contain a JSON object")
    else:
        config = {"$schema": "https://opencode.ai/config.json"}

    existing = config.get("instructions", [])
    if isinstance(existing, str):
        instructions = [existing]
    elif isinstance(existing, list) and all(isinstance(item, str) for item in existing):
        instructions = list(existing)
    else:
        raise AgentTeamError(f"{config_path} has an unsupported instructions value")

    desired = [".opencode/AGENTS.md"]
    desired.extend(f".opencode/protocols/{path.name}" for path in plan.protocol_files)

    for item in desired:
        if item not in instructions:
            instructions.append(item)

    config["instructions"] = instructions
    config_path.write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def print_plan(plan: InstallPlan, *, dry_run: bool, clean: bool) -> None:
    prefix = "DRY RUN: " if dry_run else ""
    print(f"{prefix}Installing team: {plan.team_name}")
    print(f"Project: {plan.project_dir}")
    print(f"OpenCode dir: {plan.opencode_dir}")
    if clean:
        print("Clean: remove existing .opencode/agents, protocols, and skills first")
    print("Entry agent: team_lead_agent")
    print(f"Agents: {len(plan.agent_files)}")
    print(f"Protocols: {len(plan.protocol_files)}")
    print(f"Skills: {len(plan.skill_dirs)}")


def resolve_repo_root(arg_repo: Path | None) -> Path:
    if arg_repo is not None:
        root = arg_repo.expanduser().resolve()
    elif os.environ.get("AGENT_TEAM_HOME"):
        root = Path(os.environ["AGENT_TEAM_HOME"]).expanduser().resolve()
    else:
        root = Path(__file__).resolve().parent.parent

    if not root.is_dir():
        raise AgentTeamError(f"repository root does not exist: {root}")
    return root


def normalize_team_name(name: str) -> str:
    normalized = name.strip()
    if not normalized:
        raise AgentTeamError("team name cannot be empty")
    if "/" in normalized or "\\" in normalized:
        raise AgentTeamError("team name must be a simple registry name, not a path")
    return normalized


def validate_team_dir(team_dir: Path) -> None:
    agents_dir = team_dir / "agents"
    if not agents_dir.is_dir():
        raise AgentTeamError(f"{team_dir} does not contain an agents/ directory")
    if not (agents_dir / "team_lead_agent.md").is_file():
        raise AgentTeamError(f"{team_dir} does not contain agents/team_lead_agent.md")


def resolve_team(repo_root: Path, name: str) -> TeamSpec:
    normalized = normalize_team_name(name)
    registered = load_registry()
    if normalized in registered:
        team_dir = Path(registered[normalized]).expanduser().resolve()
        validate_team_dir(team_dir)
        return TeamSpec(name=normalized, path=team_dir, source="custom")

    for parent in builtin_team_parents(repo_root):
        team_dir = (parent / normalized).resolve()
        try:
            team_dir.relative_to(parent.resolve())
        except ValueError as exc:
            raise AgentTeamError(f"team name must resolve inside repository team directory or custom registry: {name}") from exc
        if team_dir.is_dir():
            validate_team_dir(team_dir)
            return TeamSpec(name=team_dir.name, path=team_dir, source="built-in")

    available = ", ".join(team.name for team in discover_teams(repo_root))
    raise AgentTeamError(f"unknown team {name!r}. Available teams: {available}")


def builtin_team_parents(repo_root: Path) -> list[Path]:
    parents = []
    teams_dir = repo_root / "teams"
    if teams_dir.is_dir():
        parents.append(teams_dir)
    parents.append(repo_root)
    return parents


def discover_builtin_teams(repo_root: Path) -> list[TeamSpec]:
    seen: set[str] = set()
    teams = []
    for parent in builtin_team_parents(repo_root):
        for child in sorted(parent.iterdir()):
            if child.name in seen:
                continue
            if child.is_dir() and (child / "agents").is_dir():
                seen.add(child.name)
                teams.append(TeamSpec(name=child.name, path=child, source="built-in"))
    return teams


def discover_registered_teams() -> list[TeamSpec]:
    teams = []
    for name, path_value in sorted(load_registry().items()):
        path = Path(path_value).expanduser().resolve()
        if path.is_dir():
            teams.append(TeamSpec(name=name, path=path, source="custom"))
    return teams


def discover_teams(repo_root: Path) -> list[TeamSpec]:
    teams_by_name = {team.name: team for team in discover_builtin_teams(repo_root)}
    for team in discover_registered_teams():
        teams_by_name[team.name] = team
    return [teams_by_name[name] for name in sorted(teams_by_name)]


def registry_path() -> Path:
    if os.environ.get(REGISTRY_ENV):
        return Path(os.environ[REGISTRY_ENV]).expanduser().resolve()
    config_home = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")).expanduser()
    return config_home / "agent_team" / "teams.json"


def load_registry() -> dict[str, str]:
    path = registry_path()
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AgentTeamError(f"registry {path} is not valid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise AgentTeamError(f"registry {path} must contain a JSON object")
    raw_teams = data.get("teams", {})
    if not isinstance(raw_teams, dict):
        raise AgentTeamError(f"registry {path} must contain a teams object")

    registry: dict[str, str] = {}
    for name, value in raw_teams.items():
        if isinstance(value, str):
            registry[normalize_team_name(name)] = value
        elif isinstance(value, dict) and isinstance(value.get("path"), str):
            registry[normalize_team_name(name)] = value["path"]
        else:
            raise AgentTeamError(f"registry entry {name!r} must be a path string or object with path")
    return registry


def save_registry(registry: dict[str, str]) -> None:
    path = registry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"teams": {name: {"path": registry[name]} for name in sorted(registry)}}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class AgentTeamError(Exception):
    pass
