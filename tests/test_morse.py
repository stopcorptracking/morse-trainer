"""
Tests for the core.morse module.
"""

from morse_trainer.core.morse import (
    TEXT_TO_MORSE,
    text_to_morse,
    morse_to_text,
    is_valid_morse,
    get_random_character,
)


def test_text_to_morse_sos():
    assert text_to_morse("SOS") == "... --- ..."


def test_text_to_morse_hello():
    assert (
        text_to_morse("HELLO WORLD")
        == ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    )


def test_morse_to_text_sos():
    assert morse_to_text("... --- ...") == "SOS"


def test_morse_to_text_hello():
    assert (
        morse_to_text(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
        == "HELLO WORLD"
    )


def test_numbers():
    assert text_to_morse("12345") == ".---- ..--- ...-- ....- ....."
    assert morse_to_text(".---- ..--- ...-- ....- .....") == "12345"


def test_invalid_text_character():
    assert text_to_morse("HELLO@") == ".... . .-.. .-.. --- ?"


def test_invalid_morse_character():
    assert morse_to_text("... --- ... ......") == "SOS?"


def test_valid_morse():
    assert is_valid_morse("... --- ...") is True


def test_invalid_morse():
    assert is_valid_morse("... --- ......") is False


def test_random_character():
    for _ in range(100):
        character = get_random_character()
        assert character in TEXT_TO_MORSE
