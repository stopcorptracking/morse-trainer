"""
Shared Rich console instance.
"""

from rich.console import Console

from morse_trainer.ui.theme import APP_THEME

console = Console(theme=APP_THEME)
