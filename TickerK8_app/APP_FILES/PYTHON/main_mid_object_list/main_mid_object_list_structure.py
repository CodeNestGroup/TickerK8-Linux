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
from PyQt5.QtCore import (
    Qt,
    pyqtSignal
)
#______________________________________________________________________________________________________________________
""" Import main mid object list ui """
from .main_mid_object_list_ui import *
#______________________________________________________________________________________________________________________
""" Import main mid object list logic """
from .main_mid_object_list_logic import *
#######################################################################################################################
""" Main mid object widget """
class Main_mid_object_list_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    config_changed = pyqtSignal()
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.main_mid_object_list_config = json.load(open(self.main_path+'/CONFIG/main_mid_object_list/config.json', 'r')) # Get main mid object list settings 
        self.main_mid_object_list_translate = json.load(open(self.main_path+'/CONFIG/main_mid_object_list/translate.json', 'r')) # Get main mid object list settings translate data
        self.local_database = self.main_path+'/CONFIG/GLOBAL/local_data.db' # Get database path
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.type_list_button = QPushButton(self)
        self.data_list_button = QPushButton(self)
        self.list_scroll = QScrollArea(self)
        self.list_widget = None 
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_mid_object_list_ui(self)
        main_mid_object_list_reload_style(self)
        main_mid_object_list_retranslate(self)
        create_list(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """



