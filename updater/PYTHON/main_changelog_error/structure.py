""" Import packages """
import pathlib 
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QGridLayout
)
""" Import main modules """
from .ui import *
from .logic import *
#______________________________________________________________________________________________________________________

class Main_changelog_error_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        """ Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        """ Create objects """
        self.layout = QGridLayout(self)
        self.icon_label = QLabel(self)
        self.loading_message_label = QLabel(self)
        self.animation = None
        """ Call functions """
        main_changelog_error_ui(self)
        main_changelog_error_reload_style(self)
        self.setup()
        """ Connect functions """
#______________________________________________________________________________________________________________________
