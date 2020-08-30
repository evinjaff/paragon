import logging

from paragon.services.service_locator import locator
from paragon.states.state_machine import State
from paragon.ui.main_window import MainWindow


class MainState(State):
    def __init__(self):
        super().__init__("Main")
        self.window = None

    def on_exit(self):
        locator.clear_scoped_services()
        self.window = None

    def act(self):
        logging.info("Entered Main state.")
        self.window = MainWindow()
        self.window.show()
