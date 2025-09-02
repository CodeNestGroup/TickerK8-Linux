""" Import packages """
""" Import system and operating system packages """
import pathlib # For get path to folders.
import json # For json files.
#______________________________________________________________________________________________________________________
""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window.
    QPushButton, # Simple button.
    QGridLayout # Grid layout.
)
#______________________________________________________________________________________________________________________

from PyQt5.QtCore import (
    Qt # Qt.
)
#______________________________________________________________________________________________________________________
""" Import main modules """
""" Import main ui """
from .main_ui import *
#______________________________________________________________________________________________________________________
""" Import main logic """
from .main_logic import *
#______________________________________________________________________________________________________________________
""" Import main search """
from main_search.main_search_structure import Main_search_widget
#______________________________________________________________________________________________________________________
""" Import main mid object list """
from main_mid_object_list.main_mid_object_list_structure import Main_mid_object_list_widget
#______________________________________________________________________________________________________________________
""" Import main mid object """
from main_mid_object.main_mid_object_structure import Main_mid_object_scroll
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
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background.
        self.setParent(parent) # Set parent.
        self.main_news = None # Set default.
        self.main_news_list = None # Set default.
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data.
        self.main_translate = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r')) # Get main translate data.
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self) # Create grid layout.
        self.top_widget = QWidget(self) # Create top widget. 
        self.top_widget_layout = QGridLayout(self.top_widget) # Create grid layout for top widget.
        self.top_search_button = QPushButton(self.top_widget) # Create search button, top widget.
        self.top_settings_button = QPushButton(self.top_widget) # Create settings button, top widget.
        self.mid_widget = QWidget(self) # Create mid widget.
        self.mid_widget_layout = QGridLayout(self.mid_widget) # Create grid layout for mid widget.
        self.mid_object_scroll = Main_mid_object_scroll(self.mid_widget) # Create object scroll, mid widget, left side.
        self.mid_object_list_widget = Main_mid_object_list_widget(self.mid_widget) # Create object list widget, mid widget, center side.
        self.mid_news_widget = Main_mid_news_widget(self.mid_widget) # Create news widget, mid widget, right side.
        self.bottom_widget = QWidget(self) # Create bottom widget.
        self.bottom_widget_layout = QGridLayout(self.bottom_widget) # Create grid layout for bottom widget.
        self.bottom_left_news_button = QPushButton(self.bottom_widget) # Create news button, bottom widget, left, left.
        self.bottom_left_chart_button = QPushButton(self.bottom_widget) # Create chart button, bottom widget, left, mid.
        self.bottom_left_stats_button = QPushButton(self.bottom_widget) # Create stats button, bottom widget, left, right.
        self.bottom_mid_type_list_button = QPushButton(self.bottom_widget) # Create typelist button, bottom widget, mid, left.
        self.bottom_mid_data_list_button = QPushButton(self.bottom_widget) # Create data list button, bottom widget, mid, right.
        self.bottom_right_market_button = QPushButton(self.bottom_widget) # Create market news button, bottom wigdet, right, left.
        self.bottom_right_country_button = QPushButton(self.bottom_widget) # Create country news button, bottom widget, right, mid.
        self.bottom_right_world_button = QPushButton(self.bottom_widget) # Create world news button, bottom widget, right, right.
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_ui(self) # Call main ui function.
        main_reload_style(self) # Call main style function .
        main_retranslate(self) # Call main retranslate function.
#______________________________________________________________________________________________________________________
        """ Connect  functions """
        self.top_search_button.clicked.connect(lambda: Main_search_widget(self))
        self.mid_object_list_widget.config_changed.connect(lambda: main_mid_object_changed(self))
        self.mid_news_widget.open_news.connect(lambda val: open_main_news(self, val))
        self.bottom_mid_type_list_button.clicked.connect(self.mid_object_list_widget.show_lists)
        self.bottom_mid_data_list_button.clicked.connect(self.mid_object_list_widget.show_edit_list_data)
        self.bottom_right_market_button.clicked.connect(lambda: open_main_news_list(self,0))
        self.bottom_right_country_button.clicked.connect(lambda: open_main_news_list(self, 1))
        self.bottom_right_world_button.clicked.connect(lambda: open_main_news_list(self, 1))
#######################################################################################################################