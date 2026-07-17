"""
Application bootstrap.

The Application class owns the lifetime of the program.
"""

from morse_trainer.controllers.app_controller import AppController


class Application:
    """
    Main application object.

    This class is responsible for creating and starting the application's
    controller. As the project grows, it will also own configuration,
    startup, shutdown, and shared resources.
    """

    def __init__(self) -> None:
        self.controller = AppController()

    def run(self) -> None:
        """
        Start the application.
        """
        self.controller.run()
