""" Import """
import pathlib # For get path to folders
import json # For json files
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QScrollArea, # Simple scroll widget 
    QLabel, # Simple label
    QPushButton, # Simple button
    QLineEdit, # Input line
    QComboBox, # Drop down list
    QGridLayout, # Grid layout
    QVboxLayout # Vertical layout 
)
from PyQt5.QtCore import Qt
#______________________________________________________________________________________________________________________
""" Import main search ui """
from .main_search_ui import *
#______________________________________________________________________________________________________________________
""" Import main search logic """
from .main_search_logic import *
#######################################################################################################################
""" Main search widget """
class Main_search_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.main_search_translate = json.load(open(self.main_path+'/CONFIG/main_search/translate.json', 'r')) # Get main search translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.panel_widget = QWidget(self)
        self.panel_layout = QGridLayout(self.panel_widget)
        self.panel_search_icon_label = QLabel(self.panel_widget)
        self.panel_search_lineedit = QLineEdit(self.panel_widget)
        self.panel_type_stock_button = QPushButton(self.panel_widget)
        self.panel_type_etf_button = QPushButton(self.panel_widget)
        self.panel_type_forex_button = QPushButton(self.panel_widget)
        self.panel_type_index_button = QPushButton(self.panel_widget)
        self.panel_type_market_button = QPushButton(self.panel_widget)
        self.panel_type_country_button = QPushButton(self.panel_widget)
        self.panel_sort_id_button = QPushButton(self.panel_widget)
        self.panel_logo_label = QLabel(self.panel_widget)
        self.panel_sort_name_button = QPushButton(self.panel_widget)
        self.panel_scroll = QScrollArea(self.panel_widget)
        self.panel_exit_button = QPushButton(self.panel_widget)
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_search_ui(self)
        main_search_reload_style(self)
        main_search_retranslate(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """
#######################################################################################################################
