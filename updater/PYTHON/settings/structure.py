""" Import packages """
import pathlib 
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QGridLayout
)
""" Import settings modules """
from .ui import *
from .logic import *
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
        self.menu_scroll_layout = QVBoxLayout(self.menu_scroll_widget)
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
        sub_menu_open(self, theme_widget_open(self))
        """ Connect functions """
        self.menu_theme_button.clicked.connect(sub_menu_ui(self, theme_widget_open(self)))
        self.menu_sound_button.clicked.connect(sub_menu_ui(self, sound_widget_open(self)))
        self.menu_update_button.clicked.connect(sub_menu_ui(self, update_widget_open(self)))
        self.menu_language_button.clicked.connect(sub_menu_ui(self, language_widget_open(self)))
        self.menu_report_button.clicked.connect(sub_menu_ui(self, report_widget_open(self)))
#______________________________________________________________________________________________________________________

    def sub_menu_open(self, open_func):
        if self.sub_menu_scroll:
            self.sub_menu_scroll.deleteLater()
        """ Create objects """
        self.sub_menu_scroll = QScrollArea(self)
        self.sub_menu_widget = QWidget(self.sub_menu_scroll)
        self.sub_menu_layout = QGridLayout(self.sub_menu_widget)
        self.title_label = QLabel(self.sub_menu_widget)
        """ Call functions """
        sub_menu_ui(self)
        open_func()
#______________________________________________________________________________________________________________________
    
    def theme_widget_open(self):
        """ Create objects """
        self.day_night_label = QLabel(self.sub_menu_widget)
        self.day_night_button = QPushButton_sound(self.sub_menu_widget)
        self.list_label = QLabel(self.sub_menu_widget)
        self.list_combobox = QComboBox(self.sub_menu_widget)
        self.list_combobox.addItem("Vintage Elegance Light")
        self.list_combobox.addItem("Vintage Elegance Dark")
        """ Call functions """
        theme_ui(self)
        theme_retranslate(self)
        """ Connect functions """
#______________________________________________________________________________________________________________________

    def sound_widget_open(self):
        """ Create objects """
        self.button_label = QLabel(self.sub_menu_widget)
        self.button_button = QPushButton_sound(self.sub_menu_widget)
        self.alert_label = QLabel(self.sub_menu_widget)
        self.alert_button = QPushButton_sound(self.sub_menu_widget)
        self.notification_label = QLabel(self.sub_menu_widget)
        self.notification_button = QPushButton_sound(self.sub_menu_widget)
        """ Call functions """
        sound_ui(self)
        sound_retranslate(self)
        """ Connect functions """
#______________________________________________________________________________________________________________________

    def update_widget_open(self):
        """ Create objects """
        self.version_heading1_label = QLabel(self.sub_menu_widget)
        self.version_desc_label = QLabel(self.sub_menu_widget)
        self.version_desc_value_label = QLabel(self.sub_menu_widget)
        self.version_changelog_label = QLabel(self.sub_menu_widget)
        self.version_changelog_button = QPushButton_sound(self.sub_menu_widget)
        self.option_subtitle_label = QLabel(self.sub_menu_widget)
        self.option_autoupdate_title_label = QLabel(self.sub_menu_widget)
        self.option_autoupdate_button = QPushButton_sound(self.sub_menu_widget)
        self.option_check_title_label = QLabel(self.sub_menu_widget)
        self.option_check_button = QPushButton_sound(self.sub_menu_widget)
        self.advanced_subtitle_label = QLabel(self.sub_menu_widget)
        self.advanced_capacity_title_label = QLabel(self.sub_menu_widget)
        self.advanced_capacity_combobox = QComboBox(self.sub_menu_widget)
        self.advanced_capacity_combobox.addItem("500 KB/s")
        self.advanced_capacity_combobox.addItem("1000KB/s")
        self.advanced_capacity_combobox.addItem("2000KB/s")
        self.advanced_capacity_combobox.addItem("5000KB/s")
        self.advanced_capacity_combobox.addItem("Unlimited")
        self.advanced_verification_title_label = QLabel(self.sub_menu_widget)
        self.advanced_verification_button = QPushButton_sound(self.sub_menu_widget)
        """ Call functions """
        update_ui(self)
        update_retranslate(self)
        """ Connect functions """

#______________________________________________________________________________________________________________________

    def language_widget_open(self):
        """ Create objects """
        self.sub_menu_scroll = QScrollArea(self)
        self.language_widget = QWidget(self.sub_menu_scroll)
        self.language_layout = QGridLayout(self.language_widget)
        self.language_title_label = QLabel(self.language_widget)
        self.language_type_label = QLabel(self.language_widget)
        self.language_type_combobox = QComboBox(self.language_widget)
        self.language_type_combobox.addItem("English / English")
        self.language_type_combobox.addItem("Polski / Polish ")
        """ Call functions """
        language_ui(self)
        language_retranslate(self)
        """ Connect functions """

#______________________________________________________________________________________________________________________
    
    def report_widget_open(self):
        if self.sub_menu_scroll:
            self.sub_menu_scroll.deleteLater()
        """ Create objects """
        self.sub_menu_scroll = QScrollArea(self)
        self.report_widget = QWidget(self.sub_menu_scroll)
        self.report_layout = QGridLayout(self.report_widget)
        self.report_title_label = QLabel(self.report_widget)
        self.report_autoreport_title_label = QLabel(self.report_widget)
        self.report_autoreport_button = QPushButton_sound(self.report_widget)
        self.report_sendreport_title_label = QLabel(self.report_widget)
        self.report_sendreport_button = QPushButton_sound(self.report_widget)
        """ Call functions """
        report_ui(self)
        report_retranslate(self)
        """ Connect functions """
#______________________________________________________________________________________________________________________

