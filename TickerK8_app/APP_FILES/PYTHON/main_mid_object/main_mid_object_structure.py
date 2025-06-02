import pathlib # For get path to folders
import json # For json files
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QScrollArea, # Simple scroll widget
    QStackedWidget, # Stacked widget 
    QLabel, # Simple label
    QPushButton, # Simple button
    QComboBox, # Drop down list
    QGridLayout, # Grid layout
    QVBoxLayout # Vertical layout 
)
from PyQt5.QtCore import Qt
#______________________________________________________________________________________________________________________
""" Import main mid object ui """
from .main_mid_object_ui import *
#______________________________________________________________________________________________________________________
""" Import main mid object logic """
from .main_mid_object_logic import *
#######################################################################################################################
""" Main mid object widget """
class Main_mid_object_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.main_scroll = QScrollArea(self)
        self.main_widget = None
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_mid_object_ui(self)
        main_mid_object_reload_style(self)
        self.setup_widget = setup_widget(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """
#######################################################################################################################
