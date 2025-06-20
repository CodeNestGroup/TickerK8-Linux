""" Import """
import pathlib # For get path to folders
import json # For json files
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QScrollArea, # Scroll widget
    QGridLayout, # Grid layout
    QApplication
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import Qt
#______________________________________________________________________________________________________________________
""" Import chart ui """
from .chart_ui import *
#______________________________________________________________________________________________________________________
""" Import chart logic """
from .chart_logic import *
#######################################################################################################################
class Chart_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
        self.main_news = None # Set dafoult
        self.main_news_list = None # Set dafoult
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.chart_translate = json.load(open(self.main_path+'/CONFIG/chart/translate.json', 'r')) # Get main translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.top_widget = QWidget(self)
        self.top_layout = QGridLayout(self.top_widget)
        self.top_exit_button = QPushButton(self.top_widget)
        self.top_title_label = QLabel(self.top_widget)
        self.main_chart_label = None
        self.bottom_widget = QWidget(self)
        self.bottom_layout = QGridLayout(self.bottom_widget)
        self.bottom_1d_button = QPushButton(self.bottom_widget)
        self.bottom_5d_button = QPushButton(self.bottom_widget)
        self.bottom_1m_button = QPushButton(self.bottom_widget)
        self.bottom_3m_button = QPushButton(self.bottom_widget)
        self.bottom_1y_button = QPushButton(self.bottom_widget)
        self.bottom_ytd_button = QPushButton(self.bottom_widget)
        self.bottom_all_button = QPushButton(self.bottom_widget)
#______________________________________________________________________________________________________________________
        """ Call functions """
        chart_ui(self) # Call chart ui function
        chart_reload_style(self) # Call chart style function 
        chart_retranslate(self) # Call chart retranslate function
        create_chart(self, 2) # Create chart 
#______________________________________________________________________________________________________________________
        """ Connect  functions """
        self.bottom_1d_button.clicked.connect(lambda: create_chart(self, 0))
        self.bottom_5d_button.clicked.connect(lambda: create_chart(self, 1))
        self.bottom_1m_button.clicked.connect(lambda: create_chart(self, 2))
        self.bottom_3m_button.clicked.connect(lambda: create_chart(self, 3))
        self.bottom_1y_button.clicked.connect(lambda: create_chart(self, 4))
        self.bottom_ytd_button.clicked.connect(lambda: create_chart(self, 5))
        self.bottom_all_button.clicked.connect(lambda: create_chart(self, 6))
#######################################################################################################################