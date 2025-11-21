""" Import packages """
import pathlib 
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QTextEdit,
    QScrollArea,
    QGridLayout
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
        self.textfield_textarea = QTextEdit(self)
        self.send_button = QPushButton_sound(self, self)
        self.clear_button = QPushButton_sound(self, self)
        self.exit_button = QPushButton_sound(self, self)
        """ Call functions """
        report_ui(self)
        report_reload_style(self)
        report_retranslate(self)
        """ Connect functions """
        #self.send_button.clicked.connect()
        #self.clear_button.clicked.connect()
        #self.exit_button.clicked.connect()
#______________________________________________________________________________________________________________________
