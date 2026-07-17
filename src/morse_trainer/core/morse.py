"""
core.morse

Core Morse code functionality.

This module contains:
- Morse code mappings
- Translation functions
- Validation helpers
- Random character selection

This module contains NO user interaction.
"""

import random

# Morse code mapping (ITU International Morse Code)
TEXT_TO_MORSE = {
    # Letters
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",

    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

# Automatically generate reverse lookup dictionary
MORSE_TO_TEXT = {
    code: character
    for character, code in TEXT_TO_MORSE.items()
}

LETTER_SEPARATOR = " "
WORD_SEPARATOR = "/"


def text_to_morse(text: str) -> str:
    """
    Convert plain text into Morse code.

    Unknown characters are replaced with '?'.

    Example:
        HELLO WORLD
        -> ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    """
    words = []

    for word in text.upper().split():
        letters = []

        for character in word:
            letters.append(TEXT_TO_MORSE.get(character, "?"))

        words.append(LETTER_SEPARATOR.join(letters))

    return f" {WORD_SEPARATOR} ".join(words)


def morse_to_text(morse: str) -> str:
    """
    Convert Morse code into plain text.

    Unknown Morse sequences become '?'.

    Example:
        ".... . .-.. .-.. ---"
        -> "HELLO"
    """
    words = []

    for word in morse.split(WORD_SEPARATOR):
        letters = []

        for code in word.strip().split():
            letters.append(MORSE_TO_TEXT.get(code, "?"))

        words.append("".join(letters))

    return " ".join(words)


def is_valid_morse(sequence: str) -> bool:
    """
    Return True if every Morse symbol in the sequence is valid.
    """

    for word in sequence.split(WORD_SEPARATOR):
        for code in word.strip().split():
            if code not in MORSE_TO_TEXT:
                return False

    return True


def get_random_character() -> str:
    """
    Return a random supported character.
    """

    return random.choice(list(TEXT_TO_MORSE.keys()))
