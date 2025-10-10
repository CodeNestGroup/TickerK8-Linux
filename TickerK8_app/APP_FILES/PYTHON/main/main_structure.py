""" Import packages """
""" Import system and operating system packages """
import pathlib 
import json
#______________________________________________________________________________________________________________________
""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QGridLayout
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt,
    QTimer
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
""" Import main news list structure """
from main_news_list.main_news_list_structure import Main_news_list_widget
#######################################################################################################################
""" Main widget """
class Main_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        self.news = None
        self.news_list = None
        self.search_widget = None
        self.objects_list_widget = None
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.local_database = self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db'
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.layout = QGridLayout(self)
        self.search_button = QPushButton(self)
        self.objects_list_title_label = QLabel(self)
        self.objects_list_scroll = QScrollArea(self)
        self.type_list_button = QPushButton(self)
        self.data_list_button = QPushButton(self)
        self.settings_button = QPushButton(self)
        self.logout_button = QPushButton(self)
        self.object_icon_label = QLabel(self)
        self.object_ticker_label = QLabel(self)
        self.object_name_label = QLabel(self)
        self.object_time_widget = None
        self.object_chart_widget = None
        self.object_info_widget = None
        self.object_statistics_widget = None
        self.object_news_button = QPushButton(self)
        self.object_chart_button = QPushButton(self)
        self.object_stats_button = QPushButton(self)
        self.chart_widget = None
        self.news_button_list = []
        self.news_button_index = 0
        self.news_next_left_button = QPushButton(self)
        self.news_next_right_button = QPushButton(self)
        self.news_market_button = QPushButton(self)
        self.news_country_button = QPushButton(self)
        self.news_world_button = QPushButton(self)

        self.timer = QTimer(self)
        self.news_timer = QTimer(self)
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_ui(self) 
        main_reload_style(self) 
        main_retranslate(self)
        self.widget_background = lambda: widget_background_painter(self)
        self.timer.timeout.connect(self.widget_background)
        self.timer.start(1)
        objects_list_open(self)
        object_setup(self)
        news_creator(self)
#______________________________________________________________________________________________________________________
        """ Connect  functions """
        self.search_button.clicked.connect(lambda: Main_search_widget(self))
        self.type_list_button.clicked.connect(self.objects_list_lists_open)
        self.data_list_button.clicked.connect(self.objects_list_edit_open)
        self.news_next_left_button.clicked.connect(lambda: news_next(self))
        self.news_next_right_button.clicked.connect(lambda: news_previous(self))
        self.news_market_button.clicked.connect(lambda: open_main_news_list(self, 0))
        self.news_country_button.clicked.connect(lambda: open_main_news_list(self, 1))
        self.news_world_button.clicked.connect(lambda: open_main_news_list(self, 2))
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