from PySide2 import QtGui
from PySide2.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGroupBox,
    QFormLayout,
    QLineEdit,
    QDialogButtonBox,
)

from paragon.ui.widgets.enum_combo_box import EnumComboBox
from paragon.ui.widgets.file_selector import FileSelector

from paragon.model.project import Language, Game


class Ui_ProjectEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.data_group_box = QGroupBox(title="Project Data")
        self.data_layout = QFormLayout()
        self.project_name_line_edit = QLineEdit()
        self.project_name_line_edit.setPlaceholderText("Enter project name...")
        self.project_language_combo_box = EnumComboBox(enum=Language)
        self.project_game_combo_box = EnumComboBox(enum=Game)
        self.data_layout.addRow("Name", self.project_name_line_edit)
        self.data_layout.addRow("Language", self.project_language_combo_box)
        self.data_layout.addRow("Game", self.project_game_combo_box)
        self.data_group_box.setLayout(self.data_layout)

        self.layers_group_box = QGroupBox(title="Project Directories")
        self.layers_layout = QVBoxLayout()
        self.layers_about_label = QLabel(
            '<a href="http://example.com/">What is this?</a>'
        )
        self.layers_about_label.setTextFormat(QtGui.Qt.RichText)
        self.layers_about_label.setTextInteractionFlags(QtGui.Qt.TextBrowserInteraction)
        self.layers_about_label.setOpenExternalLinks(True)
        self.layers_form_layout = QFormLayout()
        self.rom_selector = FileSelector(
            placeholder_text="Enter extracted RomFS path..."
        )
        self.output_directory_selector = FileSelector(
            placeholder_text="Enter output path..."
        )
        self.layers_form_layout.addRow("ROM", self.rom_selector)
        self.layers_form_layout.addRow(
            "Output Directory", self.output_directory_selector
        )
        self.layers_layout.addWidget(self.layers_about_label)
        self.layers_layout.addLayout(self.layers_form_layout)
        self.layers_group_box.setLayout(self.layers_layout)

        self.actions_button_box = QDialogButtonBox(
            QDialogButtonBox.Save | QDialogButtonBox.Cancel
        )

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.data_group_box)
        self.main_layout.addWidget(self.layers_group_box)
        self.main_layout.addWidget(self.actions_button_box)

        self.resize(700, 350)
