import logging

from paragon.states.state_machine import State
from paragon.services.service_locator import locator
from paragon.ui.controllers.project_select import ProjectSelectWindow


class SelectProjectState(State):
    def __init__(self):
        super().__init__("SelectProject")
        self.window = None

    def act(self):
        logging.info("Entered SelectProject state.")
        locator.clear_scoped_services()
        self.window = ProjectSelectWindow()
        self.window.show()
