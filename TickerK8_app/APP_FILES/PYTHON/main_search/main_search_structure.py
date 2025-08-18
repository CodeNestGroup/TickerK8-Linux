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
        self.parent= parent # Set local parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.main_search_translate = json.load(open(self.main_path+'/CONFIG/main_search/translate.json', 'r')) # Get main search translate data
        self.add_object = None 
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.panel_widget = QWidget(self)
        self.panel_layout = QVBoxLayout(self.panel_widget)
        self.panel_search_widget = QWidget(self.panel_widget)
        self.panel_search_layout = QGridLayout(self.panel_search_widget)
        self.panel_search_lineedit = QLineEdit(self.panel_search_widget)
        self.panel_type_stock_button = QPushButton(self.panel_search_widget)
        self.panel_type_etf_button = QPushButton(self.panel_search_widget)
        self.panel_type_forex_button = QPushButton(self.panel_search_widget)
        self.panel_type_index_button = QPushButton(self.panel_search_widget)
        self.panel_type_market_button = QPushButton(self.panel_search_widget)
        self.panel_type_country_button = QPushButton(self.panel_search_widget)
        self.panel_id_label = QLabel(self.panel_search_widget)
        self.panel_object_name_label = QLabel(self.panel_search_widget)
        self.panel_market_name_label = QLabel(self.panel_search_widget)
        self.panel_scroll = QScrollArea(self.panel_search_widget)
        self.panel_scroll_widget = None 
        self.panel_exit_button = QPushButton(self.panel_search_widget)
        self.button_list = [
                self.panel_type_stock_button,
                self.panel_type_etf_button,
                self.panel_type_forex_button,
                self.panel_type_index_button,
                self.panel_type_market_button,
                self.panel_type_country_button
        ]
        self.add_object = None 
        self.panel_add_widget = None 
        self.panel_add_section_scroll = None 
        self.panel_add_section_exit_button = None 
        self.panel_add_object_scroll = None 
        self.panel_add_object_exit_button = None 
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_search_ui(self)
        main_search_reload_style(self)
        main_search_retranslate(self)
        filters_load(self)
        text_changed(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """
        self.panel_search_lineedit.textChanged.connect(lambda: text_changed(self))
        self.panel_type_stock_button.clicked.connect(lambda: filters_changed(self, 0))
        self.panel_type_etf_button.clicked.connect(lambda: filters_changed(self, 1))
        self.panel_type_forex_button.clicked.connect(lambda: filters_changed(self, 2))
        self.panel_type_index_button.clicked.connect(lambda: filters_changed(self, 3))
        self.panel_type_market_button.clicked.connect(lambda: filters_changed(self, 4))
        self.panel_type_country_button.clicked.connect(lambda: filters_changed(self, 5))
        self.panel_exit_button.clicked.connect(lambda: self.deleteLater())
#######################################################################################################################
