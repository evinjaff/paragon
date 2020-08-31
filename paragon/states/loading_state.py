import logging
import sys
from typing import Optional

from PySide2 import QtCore
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QProgressDialog

from paragon.states.state_machine import State
from paragon.model.project import Project
from paragon.services.common_module_service import CommonModuleService
from paragon.services.dedicated_editors_service import DedicatedEditorsService
from paragon.services.driver import Driver
from paragon.services.module_data_service import ModuleDataService
from paragon.services.module_service import ModuleService
from paragon.services.open_files_service import OpenFilesService
from paragon.services.service_locator import locator
from paragon.ui.error_dialog import ErrorDialog


class LoadingWorker(QtCore.QThread):
    over = QtCore.Signal()
    failed = QtCore.Signal()

    def __init__(self, project: Project):
        QtCore.QThread.__init__(self)
        self.project = project

    def run(self):
        locator.clear_scoped_services()
        try:
            locator.register_scoped("Driver", Driver(self.project))
            locator.register_scoped(
                "OpenFilesService", OpenFilesService(self.project.get_filesystem())
            )
            locator.register_scoped("ModuleDataService", ModuleDataService())
            locator.register_scoped("ModuleService", ModuleService(self.project))
            locator.register_scoped("CommonModuleService", CommonModuleService())
            locator.register_scoped(
                "DedicatedEditorsService", DedicatedEditorsService(self.project.game)
            )
            locator.get_scoped("ModuleService").load_files_and_generate_model()
            locator.get_static("SettingsService").save(self.project)
            self.over.emit()
        except Exception as e:
            logging.exception(e)
            self.failed.emit()


class LoadingState(State):
    def __init__(self):
        super().__init__("Loading")
        self.loading_thread: Optional[LoadingWorker] = None
        self.progress_dialog = None
        self.error_dialog = ErrorDialog("Loading failed. See the log file for details.")
        self.error_dialog.finished.connect(self._on_error_dialog_closed)

    def act(self, **kwargs):
        project = kwargs["project"]
        if not project:
            logging.fatal("Entered loading without locating a project.")
            sys.exit(1)

        logging.info("Entered Loading state.")
        self.progress_dialog = QProgressDialog("Loading modules...", "Quit", 0, 0)
        self.progress_dialog.setWindowTitle("Paragon - Loading")
        self.progress_dialog.setWindowIcon(QIcon("paragon.ico"))
        self.progress_dialog.setAutoClose(False)
        self.progress_dialog.hide()
        self.progress_dialog.show()
        self.loading_thread = LoadingWorker(project)
        self.loading_thread.over.connect(self._on_loading_success)
        self.loading_thread.failed.connect(self._on_loading_failure)
        self.loading_thread.start()

    def _on_loading_success(self):
        self.progress_dialog.hide()
        locator.get_static("StateMachine").transition("Main")

    def _on_loading_failure(self):
        self.progress_dialog.hide()
        self.error_dialog.exec()

    @staticmethod
    def _on_error_dialog_closed(_result):
        locator.get_static("StateMachine").transition("SelectProject")
