# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\create_project_dialog.ui',
# licensing of '.\create_project_dialog.ui' applies.
#
# Created: Sat Dec 21 13:25:51 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_CreateProject(object):
    def setupUi(self, CreateProject):
        CreateProject.setObjectName("CreateProject")
        CreateProject.resize(472, 204)
        self.verticalLayout = QtWidgets.QVBoxLayout(CreateProject)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(CreateProject)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rom_field = QtWidgets.QLineEdit(self.widget)
        self.rom_field.setObjectName("rom_field")
        self.horizontalLayout.addWidget(self.rom_field)
        self.rom_button = QtWidgets.QPushButton(self.widget)
        self.rom_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.rom_button.setObjectName("rom_button")
        self.horizontalLayout.addWidget(self.rom_button)
        self.formLayout.setLayout(
            0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout
        )
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.language_box = QtWidgets.QComboBox(self.widget)
        self.language_box.setObjectName("language_box")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.language_box)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.project_path_field = QtWidgets.QLineEdit(self.widget)
        self.project_path_field.setObjectName("project_path_field")
        self.horizontalLayout_2.addWidget(self.project_path_field)
        self.project_path_button = QtWidgets.QPushButton(self.widget)
        self.project_path_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.project_path_button.setObjectName("project_path_button")
        self.horizontalLayout_2.addWidget(self.project_path_button)
        self.formLayout.setLayout(
            1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2
        )
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.game_box = QtWidgets.QComboBox(self.widget)
        self.game_box.setObjectName("game_box")
        self.game_box.addItem("")
        self.game_box.addItem("")
        self.game_box.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.game_box)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(CreateProject)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CreateProject)
        QtCore.QObject.connect(
            self.buttonBox, QtCore.SIGNAL("accepted()"), CreateProject.accept
        )
        QtCore.QObject.connect(
            self.buttonBox, QtCore.SIGNAL("rejected()"), CreateProject.reject
        )
        QtCore.QMetaObject.connectSlotsByName(CreateProject)

    def retranslateUi(self, CreateProject):
        CreateProject.setWindowTitle(
            QtWidgets.QApplication.translate("CreateProject", "Dialog", None, -1)
        )
        self.label.setText(
            QtWidgets.QApplication.translate("CreateProject", "ROM Path", None, -1)
        )
        self.rom_button.setText(
            QtWidgets.QApplication.translate("CreateProject", "...", None, -1)
        )
        self.label_2.setText(
            QtWidgets.QApplication.translate("CreateProject", "Project Path", None, -1)
        )
        self.label_3.setText(
            QtWidgets.QApplication.translate("CreateProject", "Language", None, -1)
        )
        self.language_box.setItemText(
            0,
            QtWidgets.QApplication.translate("CreateProject", "English (NA)", None, -1),
        )
        self.language_box.setItemText(
            1,
            QtWidgets.QApplication.translate("CreateProject", "English (EU)", None, -1),
        )
        self.language_box.setItemText(
            2, QtWidgets.QApplication.translate("CreateProject", "Japanese", None, -1)
        )
        self.language_box.setItemText(
            3, QtWidgets.QApplication.translate("CreateProject", "Spanish", None, -1)
        )
        self.language_box.setItemText(
            4, QtWidgets.QApplication.translate("CreateProject", "French", None, -1)
        )
        self.language_box.setItemText(
            5, QtWidgets.QApplication.translate("CreateProject", "German", None, -1)
        )
        self.language_box.setItemText(
            6, QtWidgets.QApplication.translate("CreateProject", "Italian", None, -1)
        )
        self.project_path_button.setText(
            QtWidgets.QApplication.translate("CreateProject", "...", None, -1)
        )
        self.label_4.setText(
            QtWidgets.QApplication.translate("CreateProject", "Game", None, -1)
        )
        self.game_box.setItemText(
            0, QtWidgets.QApplication.translate("CreateProject", "FE13", None, -1)
        )
        self.game_box.setItemText(
            1, QtWidgets.QApplication.translate("CreateProject", "FE14", None, -1)
        )
        self.game_box.setItemText(
            2, QtWidgets.QApplication.translate("CreateProject", "FE15", None, -1)
        )
