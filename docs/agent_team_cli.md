# Agent Team CLI

Install this repository's team specs into an OpenCode project:

```bash
pip install -e .
agent_team install --name story_team --path /path/to/project
```

If `--path` is omitted, the current working directory is used:

```bash
agent_team install --name story_team
```

You can also run without installing:

```bash
python -m agent_team install --name story_team --path /path/to/project
```

Built-in teams live under `teams/<team_name>/`. The CLI also supports older repository checkouts where team directories are at the repository root.

The installer creates:

```text
.opencode/
  AGENTS.md
  opencode.json
  agents/
  protocols/
  skills/
```

Rules:

- `agents/*.md` role prompts are copied to `.opencode/agents/`.
- `protocols/*.md` shared rules are copied to `.opencode/protocols/`.
- `skills/*` directories are copied to `.opencode/skills/`.
- `.opencode/opencode.json` is created or updated so OpenCode loads `.opencode/AGENTS.md` and all installed protocols through `instructions`.

Useful commands:

```bash
agent_team --help
agent_team --list
agent_team list
agent_team list --verbose
agent_team add --name my_team --path /path/to/my_team
agent_team update --name my_team --path /new/path/to/my_team
agent_team remove --name my_team
agent_team registry
agent_team install --name story_team --dry-run
agent_team install --name story_team --path /path/to/project --clean
```

Custom teams are stored in a user-level registry at `~/.config/agent_team/teams.json` by default. Override the registry path with `AGENT_TEAM_REGISTRY=/path/to/teams.json`.

Registered custom teams must contain `agents/team_lead_agent.md`. Once registered, `agent_team install --name my_team --path /target/project` works the same as installing a built-in team.
