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
    QComboBox, # Drop down list
    QGridLayout, # Grid layout
    QVBoxLayout # Vertical layout 
)
from PyQt5.QtCore import (
        Qt
)
#______________________________________________________________________________________________________________________
""" Import main ui """
from .main_news_ui import *
#______________________________________________________________________________________________________________________
""" Import main logic """
from .main_news_logic import *
#######################################################################################################################
""" Main news widget """
class Main_news_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent, id_news):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
        self.id_news = id_news # Set id news
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.main_news_translate = json.load(open(self.main_path+'/CONFIG/main_news/translate.json', 'r')) # Get main news translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.panel_widget = QWidget(self)
        self.panel_layout = QGridLayout(self.panel_widget)
        self.news_scroll = QScrollArea(self.panel_widget)
        self.panel_exit_button = QPushButton(self.panel_widget)
#______________________________________________________________________________________________________________________
        """ Call functions"""
        main_news_ui(self)
        main_news_reload_style(self)
        main_news_retranslate(self)
        news_widget(self, self.id_news)
#______________________________________________________________________________________________________________________
        """ Connect functions """
        self.panel_exit_button.clicked.connect(lambda: self.deleteLater())
#######################################################################################################################