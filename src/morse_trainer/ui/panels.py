"""
Reusable Rich panels.
"""

from rich.panel import Panel
from rich.align import Align

from morse_trainer.ui.console import console


def show_title():
    """
    Display the application title.
    """

    panel = Panel(
        Align.center(
            "[title]MORSE CODE TRAINER[/title]\n"
            "[info]Learn • Practice • Master[/info]"
        ),
        border_style="title",
        expand=False,
    )

    console.print(panel)
