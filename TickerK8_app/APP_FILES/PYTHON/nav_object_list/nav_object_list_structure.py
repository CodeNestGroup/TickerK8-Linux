""" Import packages """
""" Import system and operating system packages """
import pathlib # For get path to folders.
import json # For json files.
#______________________________________________________________________________________________________________________
""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window.
    QScrollArea, # Simple scroll widget.
    QStackedWidget, # Stacked widget .
    QLabel, # Simple label.
    QPushButton, # Simple button.
    QComboBox, # Drop down list.
    QGridLayout, # Grid layout.
    QVBoxLayout # Vertical layout .
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt, # Qt.
    pyqtSignal # Signal.
)
#______________________________________________________________________________________________________________________
""" Impport nav object list modules """
""" Import nav object list ui """
from .nav_object_list_ui import *
#______________________________________________________________________________________________________________________
""" Import nav object list logic """
from .nav_object_list_logic import *
#######################################################################################################################
""" Nav object widget """
class Nav_object_list_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    config_changed = pyqtSignal()
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background.
        self.setParent(parent) # Set parent.
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data.
        self.nav_object_list_translate = json.load(open(self.main_path+'/CONFIG/nav_object_list/translate.json', 'r')) # Get main mid object list settings translate data.
        self.local_database = self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db' # Get database path.
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.title_label = QLabel(self)
        self.list_scroll = QScrollArea(self)
        self.list_widget = None 
        self.lists_background_widget = None 
        self.lists_edit_data_background_widget = None 
#______________________________________________________________________________________________________________________
        """ Call functions """
        nav_object_list_ui(self)
        nav_object_list_reload_style(self)
        nav_object_list_retranslate(self)
        open_list(self)
        self.open_list = lambda: open_list(self)
        self.show_lists = lambda: show_lists(self)
        self.show_edit_list_data = lambda: show_edit_list_data(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """
#######################################################################################################################
