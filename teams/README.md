# Built-In Agent Teams

This directory contains the built-in installable agent teams.

Each team is a self-contained directory:

```text
<team_name>/
  README.md
  agents/
    team_lead_agent.md
    *_agent.md
  protocols/
    quality_protocol.md
    delivery_protocol.md
    skill_registry.md
  skills/
    <skill_name>/
      SKILL.md
```

Use the CLI from the repository root:

```bash
agent_team list --verbose
agent_team install --name story_team --path /path/to/project
```

Custom teams do not need to live in this directory. Register them with:

```bash
agent_team add --name my_team --path /path/to/my_team
```
