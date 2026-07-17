"""
Main menu.
"""

from rich.panel import Panel

from morse_trainer.ui.console import console
from morse_trainer.ui.panels import show_title
from morse_trainer.ui.prompts import ask


def show_main_menu():
    """
    Display the main menu and return the user's choice.
    """

    console.clear()

    show_title()

    console.print()

    console.print(
        Panel.fit(
            "[menu]"
            "1. Text → Morse\n"
            "2. Morse → Text\n"
            "3. Flashcard Practice\n"
            "4. Exit",
            title="Main Menu",
        )
    )

    console.print()

    return ask("Select an option")
