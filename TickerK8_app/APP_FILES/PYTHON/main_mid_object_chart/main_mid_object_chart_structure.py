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
""" Import main mid object chart ui """
from .main_mid_object_chart_ui import *
#______________________________________________________________________________________________________________________
""" Import main mid object chart  logic """
from .main_mid_object_chart_logic import *
#______________________________________________________________________________________________________________________
#######################################################################################################################
""" Main mid object chart widget """
class Main_mid_object_chart_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.main_translate = json.load(open(self.main_path+'/CONFIG/main_mid_object_chart/translate.json', 'r')) # Get main translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.chart_widget = None
        self.current_price_line_label = QLabel(self)
        self.price_info_widget = None
        self.type_chart_button = QPushButton(self)
        self.type_chart_background_widget = None 
        self.time_widget = QWidget(self)
        self.time_layout = QGridLayout(self.time_widget)
        self.time_day_button  = QPushButton(self.time_widget)
        self.time_five_day_button = QPushButton(self.time_widget)
        self.time_one_month_button = QPushButton(self.time_widget)
        self.time_three_month_button = QPushButton(self.time_widget)
        self.time_six_month_button = QPushButton(self.time_widget)
        self.time_one_year_button = QPushButton(self.time_widget)
        self.time_five_year_button = QPushButton(self.time_widget)
        self.time_all_button = QPushButton(self.time_widget)
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_mid_object_chart_ui(self)
        main_mid_object_chart_reload_style(self)
        main_mid_object_chart_retranslate(self)
        main_mid_object_chart_create_chart(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """
        self.type_chart_button.clicked.connect(lambda: open_type_chart(self))
#######################################################################################################################
