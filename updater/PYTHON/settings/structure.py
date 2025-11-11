""" Import packages """
import pathlib 
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QGridLayout
)
from PyQt5.QtCore import (
    Qt,
    QTimer
)
""" Import main modules """
from .ui import *
from .logic import *
""" Import application modules """
#______________________________________________________________________________________________________________________

class Settings_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        """" Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        """ Create objects """
        self.layout = QGridLayout(self)
        self.menu_scroll = QScrollArea(self)
        self.menu_scroll_widget = QWidget(self.menu_scroll)
        self.menu_theme_button = QPushButton_sound(self.menu_scroll_widget)
        self.menu_sound_button = QPushButton_sound(self.menu_scroll_widget)
        self.menu_update_button = QPushButton_sound(self.menu_scroll_widget)
        self.menu_language_button = QPushButton_sound(self.menu_scroll_widget)
        self.menu_report_button = QPushButton_sound(self.menu_scroll_widget)
        self.exit_button = QPushButton_sound(self.menu_scroll)
        self.sub_menu_scroll = None
        """ Call functions """
        settings_ui(self)
        settings_reload_style(self)
        settings_retranslate(self)
        """ Connect functions """
#______________________________________________________________________________________________________________________

    def theme_widget_open(self):
        if self.sub_menu_scroll:
            self.sub_menu_scroll.deleteLater()
        """ Create objects """
        self.sub_menu_scroll = QScrollArea(self)
        self.theme_widget = QWidget(self.sub_menu_scroll)
        self.theme_layout = QGridLayout(self.theme_widget)
        self.theme_title_label = QLabel(self.theme_widget)
        self.theme_d_n_label = QLabel(self.theme_widget)
        self.theme_d_n_button = QPushButton_sound(self.theme_widget)
        self.theme_list_label = QLabel(self.theme_widget)
        self.theme_list_combobox = QComboBox(self.theme_widget)
        """ Call functions """
        theme_ui(self)
        theme_reload_style(self)
        theme_retranslate(self)
        """ Connect functions """
#______________________________________________________________________________________________________________________

    def sound_widget_open(self):
        if self.sub_menu_scroll:
            self.sub_menu_scroll.deleteLater()
        """ Create objects """
        self.sub_menu_scroll = QScrollArea(self)
        self.sound_widget = QWidget(self.sub_menu_scroll)
        self.sound_layout = QGridLayout(self.sound_widget)
        self.sound_title_label = QLabel(self.sound_widget)
        self.sound_button_label = QLabel(self.sound_widget)
        self.sound_button_button = QPushButton_sound(self.sound_widget)
        self.sound_alert_label = QLabel(self.sound_widget)
        self.sound_alert_button = QPushButton_sound(self.sound_widget)
        self.sound_notification_label = QLabel(self.sound_widget)
        self.sound_notification_button = QPushButton_sound(self.sound_widget)
        """ Call functions """
        sound_ui(self)
        sound_reload_style(self)
        sound_retranslate(self)
        """ Connect functions """
#______________________________________________________________________________________________________________________

    def update_widget_open(self):


