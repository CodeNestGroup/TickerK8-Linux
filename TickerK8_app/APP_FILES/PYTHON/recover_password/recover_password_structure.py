""" Import """
import pathlib # For get path to folders
import json # For json files
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QLineEdit, # Simple line edit
    QGridLayout # Grid layout
)
from PyQt5.QtCore import Qt
#______________________________________________________________________________________________________________________
""" Import recover password ui """
from .recover_password_ui import *
#______________________________________________________________________________________________________________________
""" Import recover password logic """
from .recover_password_logic import *
#######################################################################################################################
""" Recover password widget """
class Recover_password_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.recover_password_translate = json.load(open(self.main_path+'/CONFIG/recover_password/recover_password_translate.json', 'r')) # Get global translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.recover_password_layout = QGridLayout(self)
        

    
#######################################################################################################################
