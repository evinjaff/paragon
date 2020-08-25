import typing

from paragon.core.state_machine import Transition, State
from paragon.services.service_locator import locator
from paragon.services.settings_service import SettingsService
from paragon.states.loading_state import LoadingState


class FindProjectToLoadingTransition(Transition):
    def apply(self, _: State, ending_state: State):
        loading_state = typing.cast(LoadingState, ending_state)
        settings_service: SettingsService = locator.get_static("SettingsService")
        loading_state.project = settings_service.get_cached_project()
