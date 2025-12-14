""" Import packages """
import pathlib 
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QGridLayout,
    QVBoxLayout
)
""" Import main modules """
from .ui import *
from .logic import *
""" Import button modules """
from soundbutton.structure import QPushButton_sound
#______________________________________________________________________________________________________________________

class Changelog_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.changelog_data = data
        """" Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        """ Create objects """
        self.layout = QGridLayout(self)
        self.title_label = QLabel(self)
        self.scroll = QScrollArea(self)
        self.update_widget = QWidget(self.scroll)
        self.update_layout = QVBoxLayout(self.update_widget)
        self.update_title_label = QLabel(self.update_widget)
        self.update_date_label = QLabel(self.update_widget)
        self.update_text_label = QLabel(self.update_widget)
        self.download_button = QPushButton_sound(self)
        self.exit_button = QPushButton_sound(self)
        """ Call functions """
        changelog_ui(self)
        changelog_reload_style(self)
        changelog_retranslate(self)
        """ Connect functions  """
        #self.download_button.clicked.connect()
        #self.exit_button.clicked.connect()
#______________________________________________________________________________________________________________________