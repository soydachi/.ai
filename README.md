# .ai/ Framework

> **Single Source of Truth** for AI-assisted software engineering.

This framework provides a standardized, tool-agnostic structure for working with AI coding assistants. It integrates seamlessly with GitHub Copilot, Claude, and other AI tools while maintaining consistency across projects.

## Quick Start

```bash
# Install Python dependencies
pip install -r .ai/tools/requirements.txt

# Initialize in a new project
python .ai/tools/init_project.py --name "MyProject" --stack dotnet

# Sync to GitHub Copilot
python .ai/tools/sync_github.py

# Sync to Claude
python .ai/tools/sync_claude.py

# Validate framework structure
python .ai/tools/validate.py
```

## Architecture Overview

![Framework Overview](.ai/assets/svg/framework-overview.svg)

## Structure

```
.ai/
├── README.md                    # This file
├── config.yaml                  # Global configuration
│
├── context/                     # 🎯 PROJECT CONTEXT
│   ├── project.md               # Vision, objectives, stakeholders
│   ├── architecture.md          # System architecture (C4 compatible)
│   ├── stack.md                 # Technology stack details
│   ├── glossary.md              # Domain terminology
│   └── decisions/               # Architecture Decision Records (ADRs)
│
├── standards/                   # 📏 CODING STANDARDS
│   ├── _index.yaml              # Standards registry
│   ├── global.md                # Cross-stack rules
│   ├── dotnet/                  # .NET specific
│   ├── typescript/              # TypeScript/React specific
│   ├── python/                  # Python specific
│   ├── infrastructure/          # Terraform/IaC specific
│   └── scripting/               # PowerShell/Bash specific
│
├── prompts/                     # 💬 REUSABLE PROMPTS
│   ├── _index.yaml              # Prompts registry
│   ├── system.md                # Base system prompt
│   └── templates/               # Prompt templates by use case
│
├── skills/                      # 🔧 MODULAR SKILLS
│   ├── _index.yaml              # Skills registry
│   ├── dotnet/                  # .NET skills
│   ├── typescript/              # TypeScript skills
│   └── cross-cutting/           # Universal skills
│
├── agents/                      # 🤖 AUTONOMOUS AGENTS
│   ├── _index.yaml              # Agents registry
│   ├── feature-builder/         # Multi-step feature creation
│   ├── code-reviewer/           # Code review automation
│   └── migrator/                # Version migration assistance
│
├── specs/                       # 📋 FEATURE SPECIFICATIONS
│   ├── _template.md             # Spec template
│   └── features/                # Feature specs (spec-kit style)
│
├── learnings/                   # 📚 EVOLUTIONARY LEARNINGS
│   ├── global.md                # Cross-project learnings
│   └── by-stack/                # Stack-specific learnings
│
├── assets/                      # 🎨 VISUAL ASSETS
│   └── svg/                     # SVG diagrams
│
└── tools/                       # 🛠️ AUTOMATION SCRIPTS
    ├── sync-github.ps1          # Sync to .github/
    ├── sync-claude.ps1          # Sync to .claude/
    ├── init-project.ps1         # Initialize new project
    └── validate.ps1             # Validate structure
```

## Core Concepts

### Hierarchy: Prompts → Skills → Agents

![Concept Hierarchy](.ai/assets/svg/prompt-skill-agent.svg)

| Concept | Purpose | Autonomy | Example |
|---------|---------|----------|---------|
| **Prompt** | Define AI behavior | None (static) | "Use Result pattern" |
| **Skill** | Atomic capability | Low (invoked) | "Create API endpoint" |
| **Agent** | Orchestrate workflows | High (autonomous) | "Build complete feature" |

### When to Use What

| Task | Use |
|------|-----|
| Change base behavior | **Prompt** |
| Repetitive atomic task | **Skill** |
| Complex multi-step work | **Agent** |

## File Format Conventions

### YAML Front Matter (for tool integration)

```yaml
---
id: skill-id
name: Human Readable Name
description: Brief description for AI tools
applyTo: "**/*.cs"              # Glob pattern (optional)
tags: [dotnet, api]
---
```

### Learnings Format

```markdown
* Learning description with context (weight)
```
- Weight starts at `1`, increases with confirmation
- Higher weight = higher priority for AI consideration

### ADR Format (Architecture Decision Records)

```markdown
# ADR-001: Title

## Status
Accepted | Superseded | Deprecated

## Context
Why this decision was needed

## Decision
What was decided

## Consequences
Impact of the decision
```

## Integration

### GitHub Copilot

The `sync-github.ps1` script generates:
- `.github/copilot-instructions.md` ← from `prompts/system.md`
- `.github/instructions/*.md` ← from `standards/` and `skills/`

### Claude

The `sync-claude.ps1` script generates:
- `CLAUDE.md` ← from `prompts/system.md`
- `.claude/` folder with commands

### Other Tools

The agnostic `.ai/` structure can be adapted to any AI tool. Create a new sync script following the patterns in `tools/`.

## Contributing

1. Follow existing patterns when adding new content
2. Update `_index.yaml` files when adding skills/agents
3. Run `validate.ps1` before committing
4. Keep learnings weighted and actionable

## License

MIT - See LICENSE file for details.
