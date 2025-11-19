""" Import packages """
import pathlib 
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QGridLayout
)
from PyQt5.QtCore import (
    Qt,
    QTimer
)
""" Import main modules """
from .ui import *
from .logic import *
""" Import application modules """
#______________________________________________________________________________________________________________________

class Report_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        """" Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        """ Create objects """
        self.layout = QGridLayout(self)
        self.report_textfield_textarea
        self.report_send_button
        self.report_clear_button
        self.report_exit_button
        """ Call functions """
        report_ui(self)
        report_reload_style(self)
        report_retranslate(self)
        """ Connect functions """
#______________________________________________________________________________________________________________________
