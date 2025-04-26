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
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
        Qt,
        pyqtSignal
)
#______________________________________________________________________________________________________________________
""" Import main list ui """
from .main_news_list_ui import *
#______________________________________________________________________________________________________________________
""" Import main list logic """
from .main_news_list_logic import *
#######################################################################################################################
""" Main news widget """
class Main_news_list_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    open_news = pyqtSignal(int)
    def __init__(self, parent, news_type):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
        self.parent = parent # Set parent, main widget  
        self.news_type = news_type # Set id news type
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.main_news_list_translate = json.load(open(self.main_path+'/CONFIG/main_news_list/translate.json', 'r')) # Get main news list translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self) 
        self.panel_widget = QWidget(self)
        self.panel_layout = QGridLayout(self.panel_widget)
        self.title_label = QLabel(self)
        self.news_list_scroll = QScrollArea(self)
        self.exit_button = QPushButton(self)
#______________________________________________________________________________________________________________________
        """ Call functions"""
        main_news_list_ui(self)
        main_news_list_reload_style(self)
        main_news_list_retranslate(self)
        news_list_widget(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """
        self.exit_button.clicked.connect(lambda: self.deleteLater())
#######################################################################################################################

