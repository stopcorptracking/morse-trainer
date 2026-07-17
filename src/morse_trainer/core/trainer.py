"""
core.trainer

Manages Morse code training sessions.

This module contains no user interface code.
"""

from dataclasses import dataclass
import random

from morse_trainer.core.morse import (
    TEXT_TO_MORSE,
    text_to_morse,
)


@dataclass
class Question:
    """
    Represents a single practice question.
    """

    character: str
    morse: str


class Trainer:
    """
    Manages a Morse training session.
    """

    def __init__(self):
        self.questions_asked = 0
        self.correct_answers = 0
        self.current_question = None

    def next_question(self):
        """
        Generate and return the next random question.
        """

        character = random.choice(list(TEXT_TO_MORSE.keys()))

        self.current_question = Question(
            character=character,
            morse=text_to_morse(character),
        )

        self.questions_asked += 1

        return self.current_question

    def check_answer(self, answer):
        """
        Check the user's answer.

        Returns True if correct.
        """

        if self.current_question is None:
            raise RuntimeError("No active question.")

        answer = answer.strip().upper()

        if answer == self.current_question.character:
            self.correct_answers += 1
            return True

        return False

    @property
    def incorrect_answers(self):
        return self.questions_asked - self.correct_answers

    @property
    def accuracy(self):
        if self.questions_asked == 0:
            return 0.0

        return (self.correct_answers / self.questions_asked) * 100

    def reset(self):
        """
        Reset the current training session.
        """

        self.questions_asked = 0
        self.correct_answers = 0
        self.current_question = None
