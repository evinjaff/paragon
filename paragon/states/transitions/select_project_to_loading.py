import typing

from paragon.core.state_machine import Transition, State
from paragon.states.loading_state import LoadingState
from paragon.states.select_project_state import SelectProjectState


class SelectProjectToLoadingTransition(Transition):
    def apply(self, source_state: State, ending_state: State):
        select_project_state = typing.cast(SelectProjectState, source_state)
        loading_state = typing.cast(LoadingState, ending_state)
        loading_state.project = select_project_state.window.current_project
