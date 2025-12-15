""" Import packages """
import pathlib 
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QScrollArea,
    QGridLayout
)
""" Import main modules """
from .ui import *
from .logic import *
""" Import button modules """
from soundbutton.structure import QPushButton_sound
#______________________________________________________________________________________________________________________

class Alert_widget(QWidget):
    def __init__(self, parent, message_index=0):
        super().__init__()
        self.setParent(parent)
        self.parent_width = parent.width()
        self.parent_height = parent.height()
        """" Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        self.message_index = message_index
        """ Create objects """
        self.background_layout = QGridLayout(self)
        self.widget = QWidget(self)
        self.layout = QGridLayout(self.widget)
        self.text_label = QLabel(self.widget)
        self.download_button = QPushButton_sound(self.widget)
        self.exit_button = QPushButton_sound(self.widget)
        """ Call functions """
        alert_ui(self)
        alert_reload_style(self)
        alert_retranslate(self)
        """ Connect functions """
#______________________________________________________________________________________________________________________
