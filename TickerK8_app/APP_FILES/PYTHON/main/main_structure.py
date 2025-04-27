""" Import """
import pathlib # For get path to folders
import json # For json files
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QToolButton,
    QLineEdit, # Simple line edit
    QStackedWidget, # Stacked widget
    QScrollArea, # Scroll widget
    QGridLayout # Grid layout
)
from PyQt5.QtCore import Qt
#______________________________________________________________________________________________________________________
""" Import main ui """
from .main_ui import *
#______________________________________________________________________________________________________________________
""" Import main logic """
from .main_logic import *
#______________________________________________________________________________________________________________________
""" Import main mid object list """
from main_mid_object_list.main_mid_object_list_structure import Main_mid_object_list_widget
#______________________________________________________________________________________________________________________
""" Import main mid object """
from main_mid_object.main_mid_object_structure import Main_mid_object_widget
#______________________________________________________________________________________________________________________
""" Import main mid news """
from main_mid_news.main_mid_news_structure import Main_mid_news_widget
#______________________________________________________________________________________________________________________
""" Import main news structure """
from main_news.main_news_structure import Main_news_widget
#______________________________________________________________________________________________________________________
""" Import main news list structure """
from main_news_list.main_news_list_structure import Main_news_list_widget
#######################################################################################################################
""" Main widget """
class Main_widget(QWidget):
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
        self.main_translate = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r')) # Get main translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.top_widget = QWidget(self)
        self.top_widget_layout = QGridLayout(self.top_widget)
        self.top_exit_button = QPushButton(self.top_widget)
        self.top_window_button = QPushButton(self.top_widget)
        self.top_minimize_button = QPushButton(self.top_widget)
        self.top_search_button = QPushButton(self.top_widget)
        self.top_settings_button = QPushButton(self.top_widget)
        self.mid_widget = QWidget(self)
        self.mid_widget_layout = QGridLayout(self.mid_widget)
        self.mid_object_scroll = QScrollArea(self.mid_widget)
        self.mid_object_widget = Main_mid_object_widget(self.mid_widget)
        self.mid_object_list_widget = Main_mid_object_list_widget(self.mid_widget)
        self.mid_news_widget = Main_mid_news_widget(self.mid_widget)
        self.bottom_widget = QWidget(self)
        self.bottom_widget_layout = QGridLayout(self.bottom_widget)
        self.bottom_left_news_button = QPushButton(self.bottom_widget)
        self.bottom_left_chart_button = QPushButton(self.bottom_widget)
        self.bottom_left_stats_button = QPushButton(self.bottom_widget)
        self.bottom_center_add_button = QPushButton(self.bottom_widget) 
        self.bottom_right_market_button = QPushButton(self.bottom_widget)
        self.bottom_right_country_button = QPushButton(self.bottom_widget)
        self.bottom_right_world_button = QPushButton(self.bottom_widget)
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_ui(self) # Call main ui function
        main_reload_style(self) # Call main style function 
        main_retranslate(self) # Call main retranslate function
#______________________________________________________________________________________________________________________
        """ Connect  functions """
        self.mid_object_list_widget.config_changed.connect(self.mid_object_widget.setup_widet)
        self.mid_news_widget.open_news.connect(lambda val: open_main_news(self, val))
        self.bottom_right_market_button.clicked.connect(lambda: open_main_news_list(self,0))
        self.bottom_right_country_button.clicked.connect(lambda: open_main_news_list(self, 1))
        self.bottom_right_world_button.clicked.connect(lambda: open_main_news_list(self, 1))
#######################################################################################################################