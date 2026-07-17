"""
Application controller.

Coordinates the user interface and the application logic.
"""

from morse_trainer.ui.menu import show_main_menu
from morse_trainer.ui.practice import flashcard_mode

from morse_trainer.core.morse import (
    text_to_morse,
    morse_to_text,
)


class AppController:
    """
    Main application controller.
    """

    def run(self):

        while True:

            choice = show_main_menu()

            if choice == "1":
                self.translate_text()

            elif choice == "2":
                self.translate_morse()

            elif choice == "3":
                flashcard_mode()

            elif choice == "4":
                break

    def translate_text(self):

        text = input("\nEnter text: ")

        print()

        print(text_to_morse(text))

        input("\nPress ENTER...")

    def translate_morse(self):

        code = input("\nEnter Morse:\n")

        print()

        print(morse_to_text(code))

        input("\nPress ENTER...")
