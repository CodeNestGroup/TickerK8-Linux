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
        self.main_search_widget = None # Set default.
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data.
        self.main_translate = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r')) # Get main translate data.
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self) # Create grid layout.
        self.nav_widget = QWidget(self) # Create nav widget, left side.
        self.nav_layout = QGridLayout(self.nav_widget) # Create nav layout
        self.nav_search_button = QPushButton(self.nav_widget) # Create search button, nav widget, top.
        self.nav_object_list_widget = Nav_object_list_widget(self.nav_widget) # Create object list widget, nav widget, center side.
        self.nav_type_list_button = QPushButton(self.nav_widget) # Create typelist button, nav widget, bottom, left.
        self.nav_data_list_button = QPushButton(self.nav_widget) # Create data list button, nav widget, bottom, right.
        self.nav_settings_button = QPushButton(self.nav_widget) # Create settings button, top widget.
        self.nav_logout_button = QPushButton(self.nav_widget) # Create nav log out button, left.
        self.object_scroll = Object_scroll(self) # Create object scroll, center side.
        self.news_widget = News_widget(self) # Create news widget,right side.
        self.news_object_button = QPushButton(self) # Create news button, left, left.
        self.chart_button = QPushButton(self) # Create chart button, left, mid.
        self.stats_button = QPushButton(self) # Create stats button, left, right.
        self.news_market_button = QPushButton(self) # Create market news button, bottom wigdet, right, left.
        self.news_country_button = QPushButton(self) # Create country news button, right, mid.
        self.news_world_button = QPushButton(self) # Create world news button, right, right.
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_ui(self) # Call main ui function.
        main_reload_style(self) # Call main style function .
        main_retranslate(self) # Call main retranslate function.
#______________________________________________________________________________________________________________________
        """ Connect  functions """
        self.nav_search_button.clicked.connect(lambda: Main_search_widget(self))
        self.nav_object_list_widget.config_changed.connect(lambda: main_mid_object_changed(self))
        self.news_widget.open_news.connect(lambda val: open_main_news(self, val))
        self.nav_type_list_button.clicked.connect(self.nav_object_list_widget.show_lists)
        self.nav_data_list_button.clicked.connect(self.nav_object_list_widget.show_edit_list_data)
        self.news_market_button.clicked.connect(lambda: open_main_news_list(self,0))
        self.news_country_button.clicked.connect(lambda: open_main_news_list(self, 1))
        self.news_world_button.clicked.connect(lambda: open_main_news_list(self, 1))
#######################################################################################################################