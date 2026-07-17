"""
Application-wide Rich theme.

Changing colors here changes them everywhere.
"""

from rich.theme import Theme

APP_THEME = Theme(
    {
        "title": "bold cyan",
        "heading": "bold bright_white",
        "menu": "bright_cyan",
        "success": "bold green",
        "warning": "bold yellow",
        "error": "bold red",
        "prompt": "bold magenta",
        "info": "cyan",
        "morse": "bold bright_green",
        "character": "bold bright_yellow",
        "stat": "bright_white",
    }
)
