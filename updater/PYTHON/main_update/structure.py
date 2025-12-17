""" Import packages """
import pathlib 
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QProgressBar,
    QLabel,
    QVBoxLayout
)
""" Import main modules """
from .ui import *
from .logic import *
#______________________________________________________________________________________________________________________

class Update_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        """ Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        """ Create objects """
        self.layout = QVBoxLayout(self)
        """ Call functions """
        update_ui(self)
        update_reload_style(self)
    
    def updated(self):
        pass

    def updating(self):
        pass
