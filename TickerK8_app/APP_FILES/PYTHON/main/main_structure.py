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
    QLabel,
    QScrollArea,
    QGridLayout # Grid layout.
)
#______________________________________________________________________________________________________________________

from PyQt5.QtCore import (
    Qt, # Qt.
    QTimer # Timer.
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
""" Import main object """
from main_object.main_object_structure import Main_object_scroll
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
        self.news = None # Set default.
        self.news_list = None # Set default.
        self.search_widget = None # Set default.
        self.objects_list_widget = None # Set default.
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.local_database = self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db' # Get database path.
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.layout = QGridLayout(self) # Create grid layout.
        self.search_button = QPushButton(self) # Create search button.
        self.objects_list_title_label = QLabel(self) # Create objects list title label.
        self.objects_list_scroll = QScrollArea(self) # Create objects list scroll.
        self.type_list_button = QPushButton(self) # Create typelist button.
        self.data_list_button = QPushButton(self) # Create data list button.
        self.settings_button = QPushButton(self) # Create settings button.
        self.logout_button = QPushButton(self) # Create log out button.
        self.object_icon_label = QLabel(self) # Create object icon label.
        self.object_ticker_label = QLabel(self) # Create object ticker label.
        self.object_name_label = QLabel(self) # Create object name label.
        self.object_time_widget = QWidget(self) # Create object time widget.
        self.object_statistics_widget = QWidget(self) # Create object statistics widget.
        self.object_news_button = QPushButton(self) # Create object news button.
        self.object_chart_button = QPushButton(self) # Create object chart button.
        self.object_stats_button = QPushButton(self) # Create object stats button.
        self.chart_widget = QWidget(self) # Create chart widget. 
        self.news_button_list = [] # Create news button list.
        self.news_button_index = 0 # Create news index.
        self.news_next_left_button = QPushButton(self) # Create news next left button.
        self.news_next_right_button = QPushButton(self) # Create news next right button.
        self.news_market_button = QPushButton(self) # Create news market button.
        self.news_country_button = QPushButton(self) # Create news country button.
        self.news_world_button = QPushButton(self) # Create news  world button. 

        self.timer = QTimer(self) # Create timer.
        self.news_timer = QTimer(self) # Create news timer.
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_ui(self) # Call main ui function.
        main_reload_style(self) # Call main style function .
        main_retranslate(self) # Call main retranslate function.
        self.widget_background = lambda: widget_background_painter(self) # Function for background.
        self.timer.timeout.connect(self.widget_background) # Connect.
        self.timer.start(1) # Start timer.
        objects_list_open(self)
        news_creator(self)
#______________________________________________________________________________________________________________________
        """ Connect  functions """
        self.search_button.clicked.connect(lambda: Search_widget(self))
        self.type_list_button.clicked.connect(self.objects_list_lists_open)
        self.data_list_button.clicked.connect(self.objects_list_edit_open)


        self.news_next_left_button.clicked.connect(lambda: news_next(self))
        self.news_next_right_button.clicked.connect(lambda: news_previous(self))
#______________________________________________________________________________________________________________________
    """ Main objects list lists open """
    def objects_list_lists_open(self):
        """ Set config """
        self.objects_list_title_label.hide()
        self.objects_list_scroll.hide()
        self.type_list_button.hide()
        self.data_list_button.hide()
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.objects_list_lists_title_label = QLabel(self)
        self.objects_list_lists_scroll = QScrollArea(self)
        self.objects_list_lists_widget = QWidget(self.objects_list_lists_scroll)
        self.objects_list_lists_layout = QVBoxLayout(self.objects_list_lists_widget)
        self.objects_list_lists_exit_button = QPushButton(self)
#______________________________________________________________________________________________________________________
        """ Call functions """
        object_list_lists_ui(self)
        object_list_lists_reload_style(self)
        object_list_lists_retranslate(self)
        object_list_lists_scroll_setup(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """
        self.objects_list_lists_exit_button.clicked.connect(lambda: object_list_lists_exit(self))
#______________________________________________________________________________________________________________________
    """ objects list lists open """
    def objects_list_edit_open(self):
        """ Set config """
        self.objects_list_title_label.hide()
        self.objects_list_scroll.hide()
        self.type_list_button.hide()
        self.data_list_button.hide()
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.object_list_edit_title_label = QLabel(self)
        self.object_list_edit_scroll = QScrollArea(self)
        self.object_list_edit_widget = QWidget(self.object_list_edit_scroll)
        self.object_list_edit_layout = QGridLayout(self.object_list_edit_widget)
        self.object_list_edit_icon_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_ticker_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_pe_ratio_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_eps_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_dividend_yield_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_capitalization_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_capital_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_exit_button = QPushButton(self)
#______________________________________________________________________________________________________________________
        """ Call functions """
        object_list_edit_ui(self)
        object_list_edit_reload_style(self)
        object_list_edit_retranslate(self)
        object_list_edit_check_selected(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """
        self.object_list_edit_icon_button.clicked.connect(lambda: object_list_edit_save(self, 'icon'))
        self.object_list_edit_ticker_button.clicked.connect(lambda: object_list_edit_save(self, 'ticker'))
        self.object_list_edit_pe_ratio_button.clicked.connect(lambda: object_list_edit_save(self, 'pe_ratio'))
        self.object_list_edit_eps_button.clicked.connect(lambda: object_list_edit_save(self, 'eps'))
        self.object_list_edit_dividend_yield_button.clicked.connect(lambda: object_list_edit_save(self, 'dividend_yield'))
        self.object_list_edit_capitalization_button.clicked.connect(lambda: object_list_edit_save(self, 'capitalization'))
        self.object_list_edit_capital_button.clicked.connect(lambda: object_list_edit_save(self, 'capital'))
        self.object_list_edit_exit_button.clicked.connect(lambda: object_list_edit_exit(self))
#######################################################################################################################