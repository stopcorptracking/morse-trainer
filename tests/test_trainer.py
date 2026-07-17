"""
Tests for the Trainer class.
"""

from morse_trainer.core.trainer import Trainer


def test_new_trainer():
    trainer = Trainer()

    assert trainer.questions_asked == 0
    assert trainer.correct_answers == 0
    assert trainer.accuracy == 0


def test_next_question():
    trainer = Trainer()

    question = trainer.next_question()

    assert question.character
    assert question.morse
    assert trainer.questions_asked == 1


def test_correct_answer():
    trainer = Trainer()

    question = trainer.next_question()

    assert trainer.check_answer(question.character) is True
    assert trainer.correct_answers == 1


def test_wrong_answer():
    trainer = Trainer()

    trainer.next_question()

    assert trainer.check_answer("?") is False
    assert trainer.correct_answers == 0


def test_accuracy():
    trainer = Trainer()

    question = trainer.next_question()
    trainer.check_answer(question.character)

    trainer.next_question()
    trainer.check_answer("?")

    assert trainer.questions_asked == 2
    assert trainer.correct_answers == 1
    assert trainer.incorrect_answers == 1
    assert trainer.accuracy == 50.0


def test_reset():
    trainer = Trainer()

    question = trainer.next_question()
    trainer.check_answer(question.character)

    trainer.reset()

    assert trainer.questions_asked == 0
    assert trainer.correct_answers == 0
    assert trainer.accuracy == 0
