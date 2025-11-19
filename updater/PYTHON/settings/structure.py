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
        self.theme_list_combobox.addItem("Vintage Elegance Light")
        self.theme_list_combobox.addItem("Vintage Elegance Dark")
        """ Call functions """
        theme_ui(self)
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
        sound_retranslate(self)
        """ Connect functions """
#______________________________________________________________________________________________________________________

    def update_widget_open(self):
        if self.sub_menu_scroll:
            self.sub_menu_scroll.deleteLater()
        """ Create objects """
        self.sub_menu_scroll = QScrollArea(self)
        self.update_widget = QWidget(self.sub_menu_scroll)
        self.update_layout = QGridLayout(self.update_widget)
        self.update_title_label = QLabel(self.update_widget)
        self.update_version_subtitle_label = QLabel(self.update_widget)
        self.update_version_desc_title_label = QLabel(self.update_widget)
        self.update_version_desc_label = QLabel(self.update_widget)
        self.update_version_changelog_title_label = QLabel(self.update_widget)
        self.update_version_changelog_button = QPushButton_sound(self.update_widget)
        self.update_option_subtitle_label = QLabel(self.update_widget)
        self.update_option_autoupdate_title_label = QLabel(self.update_widget)
        self.update_option_autoupdate_button = QPushButton_sound(self.update_widget)
        self.update_option_check_title_label = QLabel(self.update_widget)
        self.update_option_check_button = QPushButton_sound(self.update_widget)
        self.update_advanced_subtitle_label = QLabel(self.update_widget)
        self.update_advanced_capacity_title_label = QLabel(self.update_widget)
        self.update_advanced_capacity_combobox = QComboBox(self.update_widget)
        self.update_advanced_capacity_combobox.addItem("500 KB/s")
        self.update_advanced_capacity_combobox.addItem("1000KB/s")
        self.update_advanced_capacity_combobox.addItem("2000KB/s")
        self.update_advanced_capacity_combobox.addItem("5000KB/s")
        self.update_advanced_capacity_combobox.addItem("Unlimited")
        self.update_advanced_verification_title_label = QLabel(self.update_widget)
        self.update_advanced_verification_button = QPushButton_sound(self.update_widget)
        """ Call functions """
        update_ui(self)
        update_retranslate(self)
        """ Connect functions """

#______________________________________________________________________________________________________________________

    def language_widget_open(self):
        if self.sub_menu_scroll:
            self.sub_menu_scroll.deleteLater()
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

