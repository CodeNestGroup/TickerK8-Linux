""" Import packages """
import pathlib
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QGridLayout
        )
from PyQt5.QtCore import (
        Qt,
        QTimer
        )
""" Import login configuration modules """
from .ui import *
from .logic import *
#______________________________________________________________________________________________________________________

class Login_configuration_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
#       --- Create objects ---
        self.layout = QGridLayout(self)
        self.left_button = QPushButton(self)
        self.right_button = QPushButton(self)
        self.navi_label = QLabel(self)
#       --- Call functions ---
        ui(self)
        reload_style(self)
        retranslate(self)
#       --- Connect functions ---

    def app_configuration(self):
#       --- Create objects ---
#       --- Call functions ---
#       --- Connect functions ---

    def list_configuration(self):
#       --- Create objects ---
#       --- Call functions ---
#       --- Connect functions ---


