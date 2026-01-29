"""Utility functions for AI Way of Working."""

from ai_wow.utils.console import colors, success, error, warning, info, dim, header
from ai_wow.utils.paths import (
    get_package_root,
    get_templates_dir,
    find_ai_root,
    find_repo_root,
)

__all__ = [
    "colors",
    "success",
    "error",
    "warning",
    "info",
    "dim",
    "header",
    "get_package_root",
    "get_templates_dir",
    "find_ai_root",
    "find_repo_root",
]
