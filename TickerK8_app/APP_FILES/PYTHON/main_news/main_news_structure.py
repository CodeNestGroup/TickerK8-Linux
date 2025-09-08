""" Import packages """
""" Import system and operating system packages """
import pathlib # For get path to folders.
import json # For json files.
#______________________________________________________________________________________________________________________
""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window.
    QLabel, # Simple label.
    QPushButton, # Simple button.
    QGridLayout # Grid layout.
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
        Qt, # Qt.
        QTimer, # Timer.
        pyqtSignal # Signal.
)
#______________________________________________________________________________________________________________________
""" Import main news modules """
""" Import main news ui """
from .main_news_ui import *
#______________________________________________________________________________________________________________________
""" Import main mid news logic """
from .main_news_logic import *
#######################################################################################################################
""" Main news widget """
class Main_news_widget(QWidget):
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
        self.main_news_translate = json.load(open(self.main_path+'/CONFIG/main_news/translate.json', 'r')) # Get main news translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.title_label = QLabel(self)
        self.next_left_button = QPushButton(self)
        self.next_right_button = QPushButton(self)
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_news_ui(self) # Call main mid news ui function
        main_news_reload_style(self) # Call main mid news style function 
        main_news_retranslate(self) # Call main mid news retranslate function
        create_news_widget(self) 
#______________________________________________________________________________________________________________________
        """ Connect functions """
        self.next_left_button.clicked.connect(lambda: news_previous(self))
        self.next_right_button.clicked.connect(lambda: news_next(self))
#######################################################################################################################
