""" Import """
import pathlib # For get path to folders
import json # For json files
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QGridLayout # Grid layout
)
from PyQt5.QtCore import (
        Qt,
        QTimer,
        pyqtSignal
)
#______________________________________________________________________________________________________________________
""" Import main mid news ui """
from .main_mid_news_ui import *
#______________________________________________________________________________________________________________________
""" Import main mid news logic """
from .main_mid_news_logic import *
#######################################################################################################################
""" Main widget """
class Main_mid_news_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    open_news = pyqtSignal(int)
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
        self.news_button_list = []
        self.news_button_visable = 0
        self.timer = QTimer(self)
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.main_mid_news_translate = json.load(open(self.main_path+'/CONFIG/main_mid_news/translate.json', 'r')) # Get main mid news translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.title_label = QLabel(self)
        self.next_left_button = QPushButton(self)
        self.next_right_button = QPushButton(self)
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_mid_news_ui(self) # Call main mid news ui function
        main_mid_news_reload_style(self) # Call main mid news style function 
        main_mid_news_retranslate(self) # Call main mid news retranslate function
        create_news_widget(self) 
#______________________________________________________________________________________________________________________
        """ Connect functions """
        self.next_left_button.clicked.connect(lambda: news_previous(self))
        self.next_right_button.clicked.connect(lambda: news_next(self))
#######################################################################################################################
