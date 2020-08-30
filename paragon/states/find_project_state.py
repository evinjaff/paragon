import logging

from paragon.states.state_machine import State
from paragon.services.service_locator import locator


class FindProjectState(State):
    def __init__(self):
        super().__init__("FindProject")

    def act(self):
        logging.info("Entered FindProject state.")
        settings_service = locator.get_static("SettingsService")
        if settings_service.has_cached_project():
            locator.get_static("StateMachine").transition("Loading", project=settings_service.get_cached_project())
        else:
            locator.get_static("StateMachine").transition("SelectProject")
