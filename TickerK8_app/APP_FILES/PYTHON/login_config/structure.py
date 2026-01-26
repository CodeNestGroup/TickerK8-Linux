""" Import packages """
import pathlib
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton,
    QLineEdit,
    QGridLayout,
    QComboBox
        )
from PyQt5.QtCore import (
        Qt,
        QTimer
        )
""" Import login configuration modules """
from .ui import *
from .logic import *
#______________________________________________________________________________________________________________________

class Login_configuration_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
#       --- Create objects ---
        self.layout = QGridLayout(self)
        self.title_label = QLabel(self)
        self.info_label = QLabel(self)
        self.left_button = QPushButton(self)
        self.right_button = QPushButton(self)
        self.navi_label = QLabel(self)
#       --- Call functions ---
        ui(self)
        reload_style(self)
#       --- Connect functions ---
        self.open_info_label = lambda open_info_label(self)
        self.open_app_conf = lambda open_app_conf(self)
        self.open_sub_conf = lambda open_sub_conf(self)
        self.open_list_conf = lambda open_list_conf(self)
        self.open_accept_settings = lambda open_accept_settings(self)

    def center_widget_setup(self):
        if self.center_widget:
            self.center_widget.deleteLater()
            self.center_widget = None 
        self.center_widget = QWidget(self)
        self.center_layout = QGridLayout(self.center_widget)
        center_widget_setup_ui(self)

    def app_conf(self):
#       --- Create objects ---
        self.language_subtitle_label = QLabel(self.center_widget)
        self.language_combobox = QComboBox(self.center_widget)
        self.theme_subtitle_label = QLabel(self.center_widget)
        self.theme_combobox = QComboBox(self.center_widget)
#       --- Call functions ---
        app_conf_ui(self)
        app_conf_retranslate(self)
#       --- Connect functions ---

    def sub_conf(self):
#       --- Create objects ---
        self.left_button = QPushButton(self.center_widget)
        self.center_button = QPushButton(self.center_widget)
        self.right_button = QPushButton(self.center_widget)
#       --- Call functions ---
        sub_conf_ui(self)
        sub_conf_reload_style(self)
        sub_conf_retranslate(self)
#       --- Connect functions ---

    def list_conf(self):
#       --- Create objects ---
        self.country_subtitle_label = QLabel(self.center_widget)
        self.country_search_lineedit = QLineEdit(self.center_widget)
        self.country_scroll = QScrollArea(self.center_widget)
        self.country_widget = QWidget(self.country_scroll)
        self.country_layout = QGridLayout(self.country_widget)
        self.country_number_label = QLabel(self.country_widget)
        self.country_icon_label = QLabel(self.country_widget)
        self.country_ticker_label = QLabel(self.country_widget)
        self,country_name_label = QLabel(self.country_widget)
        self.country_add_button = QPushButton(self.country_widget)
        self.country_reset_button = QPushButton(self.country_widget)
        self.country_delete_button = QPushButton(self.country_widget)
        self.country_added_scroll = QScrollArea(self.center_widget)
        self.country_added_widget = QWidget(self.country_added_scroll)
        self.country_added_layout = QGridLayout(self.country_added_widget)
        self.country_added_number_label = QLabel(self.country_added_widget)
        self.country_added_icon_label = QLabel(self.country_added_widget)
        self.country_added_ticker_label = QLabel(self.country_added_widget)
        self.country_added_name_label = QLabel(self.country_added_widget)
        self.country_error_label = QLabel(self.center_widget)
        self.market_subtitle_label = QLabel(self.center_widget)
        self.market_search_lineedit = QLineEdit(self.center_widget)
        self.market_scroll = QScrollArea(self.center_widget)
        self.market_widget = QWidget(self.market_scroll)
        self.market_layout = QGridLayout(self.market_widget)
        self.market_number_label = QLabel(self.market_widget)
        self.market_icon_label = QLabel(self.market_widget)
        self.market_ticker_label = QLabel(self.market_widget)
        self.market_name_label = QLabel(self.market_widget)
        self.market_add_button = QPushButton(self.center_widget)
        self.marlet_reset_button = QPushButton(self.center_widget)
        self.market_delete_button = QPushButton(self.center_widget)
        self.market_added_scroll = QScrollArea(self.center_widget)
        self.market_added_widget = QWidget(self.market_added_scroll)
        self.market_added_layout = QGridLayout(self.market_added_widget)
        self.market_added_number_label = QLabel(self.market_added_widget)
        self.market_added_icon_label = QLabel(self.market_added_widget)
        self.market_added_ticker_label = QLabel(self.market_added_widget)
        self.market_added_name_label = QLabel(self.market_added_widget)
        self.market_error_label = QLabel(self.market_widget)
        self.stock_subtitle_label = QLabel(self.center_widget)
        self.stock_search_lineedit = QLineEdit(self.center_widget)
        self.stock_scroll = QScrollArea(self.center_widget)
        self.stock_widget = QWidget(self.stock_scroll)
        self.stock_layout = QGridLayout(self.stock_widget)
        self.stock_number_label = QLabel(self.stock_widget)
        self.stock_icon_label = QLabel(self.stock_widget)
        self.stock_ticker_label = QLabel(self.stock_widget)
        self.stock_name_label = QLabel(self.stock_widget)
        self.stock_add_button = QPushButton(self.center_widget)
        self.stock_reset_button = QPushButton(self.center_widget)
        self,stock_delete_button = QPushButton(self.center_widget)
        self.stock_added_scroll = QScrollArea(self.center_widget)
        self.stock_added_widget = QWidget(self.stock_added_scroll)
        self.stock_added_layout = QGridLayout(self.stock_added_widget)
        self.stock_added_number_label = QLabel(self.stock_added_widget)
        self.stock_added_icon_label = QLabel(self.stock_added_widget)
        self.stock_added_ticker_label = QLabel(self.stock_added_widget)
        self.stock_added_name_label = QLabel(self.stock_added_widget)
        self.stock_error_label = QLabel(self.stock_widget)
#       --- Call functions ---
        list_conf_ui(self)
        list_conf_reload_style(self)
        list_conf_retranslate(self)
#       --- Connect functions ---
    def accept_settings(self):
#       --- Create objects ---
        self.regulations_scroll = QScrollArea(self.center_widget)
        self.regulations_widget = QWidget(self.regulations_scroll)
        self.regulations_layout = QGridLayout(self.regulations_widget)
        self.regulations_label = QLabel(self.regulations_widget)
#       --- Call functions ---
        accept_settings_ui(self)
        accept_settings_reload_style(self)
        accept_settings_retranslate(self)
#       --- Connect functions ---
