"""
Reusable prompts.
"""

from rich.prompt import Prompt


def ask(message: str) -> str:
    """
    Ask the user for text input.
    """

    return Prompt.ask(f"[prompt]{message}[/prompt]")
