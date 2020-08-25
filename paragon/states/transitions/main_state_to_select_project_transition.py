import typing

from paragon.core.state_machine import Transition, State
from paragon.services.service_locator import locator
from paragon.states.main_state import MainState


class MainStateToSelectProjectTransition(Transition):
    def apply(self, start_state: State, _: State):
        start_state = typing.cast(MainState, start_state)
        locator.clear_scoped_services()
        start_state.window = None
