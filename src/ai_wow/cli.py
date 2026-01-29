#!/usr/bin/env python3
"""
AI Way of Working CLI - Unified command-line interface.

This is the main entry point for the ai-wow CLI tool.
All commands are accessible through subcommands:

    ai-wow init --name "MyProject" --stack dotnet
    ai-wow sync github
    ai-wow sync claude
    ai-wow validate
    ai-wow update
"""

from __future__ import annotations

import click

from ai_wow import __version__
from ai_wow.commands import init, sync, validate, update


@click.group()
@click.version_option(version=__version__, prog_name="ai-wow")
@click.pass_context
def main(ctx: click.Context) -> None:
    """AI Way of Working - Standardized AI-assisted software engineering framework.

    This CLI helps you initialize, synchronize, and validate the .ai/ framework
    in your projects. It works seamlessly with GitHub Copilot, Claude, and
    other AI coding assistants.

    \b
    Quick Start:
        ai-wow init --name "MyProject" --stack dotnet
        ai-wow sync github
        ai-wow validate

    \b
    For more information on a command:
        ai-wow <command> --help
    """
    ctx.ensure_object(dict)


# Register commands
main.add_command(init.init_cmd, name="init")
main.add_command(sync.sync_cmd, name="sync")
main.add_command(validate.validate_cmd, name="validate")
main.add_command(update.update_cmd, name="update")


if __name__ == "__main__":
    main()
