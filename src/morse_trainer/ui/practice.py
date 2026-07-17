"""
ui.practice

Practice modes for the Morse Trainer.
"""

from morse_trainer.core.trainer import Trainer


def flashcard_mode():
    """
    Run a flashcard practice session.
    """

    trainer = Trainer()

    print("\n==============================")
    print("      FLASHCARD MODE")
    print("==============================")
    print("Type 'q' at any time to quit.\n")

    while True:

        question = trainer.next_question()

        print(f"Character:\n\n    {question.character}")

        user = input("\nPress ENTER to reveal (or q to quit): ").strip().lower()

        if user == "q":
            break

        print(f"\nMorse:\n\n    {question.morse}")

        answer = input("\nDid you get it correct? (y/n): ").strip().lower()

        if answer == "q":
            break

        if answer == "y":
            trainer.check_answer(question.character)
            print("\n✓ Correct!")

        else:
            trainer.check_answer("?")
            print(f"\n✗ Keep practicing {question.character}")

        print("\n------------------------------")
        print(f"Questions : {trainer.questions_asked}")
        print(f"Correct   : {trainer.correct_answers}")
        print(f"Incorrect : {trainer.incorrect_answers}")
        print(f"Accuracy  : {trainer.accuracy:.1f}%")
        print("------------------------------")

    print("\nSession Complete")
    print(f"Final Accuracy: {trainer.accuracy:.1f}%")
