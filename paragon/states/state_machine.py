from abc import ABC, abstractmethod
from typing import Optional, Dict


class NameInUseException(Exception):
    pass


class State(ABC):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def get_name(self):
        return self.name

    def on_exit(self):
        pass

    @abstractmethod
    def act(self, **kwargs):
        pass


class StateMachine:
    def __init__(self):
        self._states: Dict[str, State] = {}
        self._current_state: Optional[State] = None

    def add_state(self, state: State):
        self._states[state.get_name()] = state

    def transition(self, new_state: str, **kwargs):
        old_state = self._current_state
        self._current_state = self._states[new_state]
        if old_state:
            old_state.on_exit()
        self._current_state.act(**kwargs)
