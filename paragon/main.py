import logging
import sys
logging.basicConfig(handlers=[logging.FileHandler('../paragon.log', 'w', 'utf-8')], level=logging.DEBUG)

try:
    from PySide2.QtGui import QFontDatabase
    from PySide2.QtWidgets import QApplication, QStyleFactory

    from paragon.services.settings_service import SettingsService
    from paragon.states.select_project_state import SelectProjectState
    from paragon.states.transitions.main_state_to_select_project_transition import MainStateToSelectProjectTransition
    from paragon.states.transitions.reload_project_transition import ReloadProjectTransition
    from paragon.states.transitions.select_project_to_loading import SelectProjectToLoadingTransition

    from paragon.core.state_machine import StateMachine
    from paragon.services.service_locator import locator
    from paragon.states.find_project_state import FindProjectState
    from paragon.states.loading_state import LoadingState
    from paragon.states.main_state import MainState
    from paragon.states.transitions.find_project_to_loading import FindProjectToLoadingTransition
except:
    logging.exception("A critical error occurred while initializing main")
    sys.exit(1)


def _load_theme_from_settings(app: QApplication):
    theme = locator.get_static("SettingsService").get_theme()
    if theme and theme in QStyleFactory.keys():
        app.setStyle(theme)


logging.info("Paragon version: Alpha 14")
logging.info("Starting application...")
application = QApplication(sys.argv)
QFontDatabase.addApplicationFont("Assets/FOT-ChiaroStd-B.otf")
state_machine = StateMachine()
locator.register_static("SettingsService", SettingsService())
locator.register_static("StateMachine", state_machine)
_load_theme_from_settings(application)
state_machine.add_state(SelectProjectState())
state_machine.add_state(FindProjectState())
state_machine.add_state(LoadingState())
state_machine.add_state(MainState())
state_machine.add_transition(MainStateToSelectProjectTransition("Main", "SelectProject"))
state_machine.add_transition(FindProjectToLoadingTransition("FindProject", "Loading"))
state_machine.add_transition(SelectProjectToLoadingTransition("SelectProject", "Loading"))
state_machine.add_transition(ReloadProjectTransition("Main", "Loading"))
state_machine.transition("FindProject")
sys.exit(application.exec_())
