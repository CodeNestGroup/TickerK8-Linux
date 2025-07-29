""" Import """
import pathlib # For get path to folders
import json # For json files
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QScrollArea, # Simple scroll widget 
    QLabel, # Simple label
    QPushButton, # Simple button
    QComboBox, # Drop down list
    QGridLayout, # Grid layout
    QVBoxLayout # Vertical layout 
)
from PyQt5.QtCore import Qt
#______________________________________________________________________________________________________________________
""" Import main ui """
from .main_settings_ui import *
#______________________________________________________________________________________________________________________
""" Import main logic """
from .main_settings_logic import *
#######################################################################################################################
""" Main settings widget """
class Main_settings_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.main_settings_translate = json.load(open(self.main_path+'/CONFIG/main_settings/translate.json', 'r')) # Get main settings translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.navi_scroll = QScrollArea(self)
        self.navi_widget = QWidget(self.navi_scroll)
        self.navi_layout = QVBoxLayout(self.navi_widget)
        self.navi_user_button = QPushButton(self.navi_widget)
        self.navi_style_button = QPushButton(self.navi_widget)
        self.navi_sound_button = QPushButton(self.navi_widget)
        self.navi_update_button = QPushButton(self.navi_widget)
        self.navi_language_button = QPushButton(self.navi_widget)
        self.navi_report_button = QPushButton(self.navi_widget)
        self.navi_exit_button  = QPushButton(self)
        self.panel_right_scroll = QScrollArea(self)
        self.panel_right_widget = QWidget(self.panel_right_scroll)
        self.panel_right_layout = QVBoxLayout(self.panel_right_widget)
        self.user_widget = QWidget(self.panel_right_widget)
        self.user_layout = QGridLayout(self.user_widget)
        self.user_title_label = QLabel(self.user_widget)
        self.user_image_button = QPushButton(self.user_widget)
        self.user_info_subtitle_label = QLabel(self.user_widget)
        self.user_name_name_label = QLabel(self.user_widget)
        self.user_name_content_label = QLabel(self.user_widget)
        self.user_email_name_label = QLabel(self.user_widget)
        self.user_email_content_label = QLabel(self.user_widget)
        self.user_create_date_name_label = QLabel(self.user_widget)
        self.user_create_date_content_label = QLabel(self.user_widget)
        self.style_widget = QWidget(self.panel_right_widget)
        self.style_layout = QGridLayout(self.style_widget)
        self.style_title_label = QLabel(self.style_widget)
        self.style_theme_subtitle_label = QLabel(self.style_widget)
        self.style_theme_d_n_name_label = QLabel(self.style_widget)
        self.style_theme_d_n_content_button = QPushButton(self.style_widget)
        self.style_theme_themes_name_label = QLabel(self.style_widget)
        self.style_theme_themes_content_combobox = QComboBox(self.style_widget)
        self.sound_widget = QWidget(self.panel_right_widget)
        self.sound_layout = QGridLayout(self.sound_widget)
        self.sound_title_label = QLabel(self.sound_widget)
        self.sound_button_name_label = QLabel(self.sound_widget)
        self.sound_button_content_button = QPushButton(self.sound_widget)
        self.sound_alert_name_label = QLabel(self.sound_widget)
        self.sound_alert_content_button = QPushButton(self.sound_widget)
        self.sound_notification_name_label = QLabel(self.sound_widget)
        self.sound_notification_content_button = QPushButton(self.sound_widget)
        self.update_widget = QWidget(self.panel_right_widget)
        self.update_layout = QGridLayout(self.update_widget)
        self.update_title_label = QLabel(self.update_widget)
        self.update_version_subtitle_label = QLabel(self.update_widget)
        self.update_version_description_name_label = QLabel(self.update_widget)
        self.update_version_description_content_label = QLabel(self.update_widget)
        self.update_version_changelog_name_label = QLabel(self.update_widget)
        self.update_version_changelog_content_button = QPushButton(self.update_widget)
        self.update_options_subtitle_label = QLabel(self.update_widget)
        self.update_options_auto_update_name_label = QLabel(self.update_widget)
        self.update_options_auto_update_content_button = QPushButton(self.update_widget)
        self.update_options_check_update_name_label = QLabel(self.update_widget)
        self.update_options_check_update_content_button = QPushButton(self.update_widget)
        self.update_advanced_subtitle_label = QLabel(self.update_widget)
        self.update_advanced_capacity_name_label = QLabel(self.update_widget)
        self.update_advanced_capacity_content_combobox = QComboBox(self.update_widget)
        self.update_advanced_file_verification_name_label = QLabel(self.update_widget)
        self.update_advanced_file_verification_content_button = QPushButton(self.update_widget)
        self.language_widget = QWidget(self.panel_right_widget)
        self.language_layout = QGridLayout(self.language_widget)
        self.language_title_label = QLabel(self.language_widget)
        self.language_langauge_name_label = QLabel(self.language_widget)
        self.language_langauge_content_combobox = QComboBox(self.language_widget)
        self.report_widget = QWidget(self.panel_right_widget)
        self.report_layout = QGridLayout(self.report_widget)
        self.report_title_label = QLabel(self.report_widget)
        self.report_auto_report_name_label = QLabel(self.report_widget)
        self.report_auto_report_content_button = QPushButton(self.report_widget)
        self.report_send_report_name_label = QLabel(self.report_widget)
        self.report_send_report_content_button = QPushButton(self.report_widget)
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_settings_ui(self)
        main_settings_reload_style(self)
        main_settings_retranslate(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """
        self.controller_settings = controller_settings()
        self.navi_user_button.clicked.connect(lambda: self.controller_settings.open_sub_widget(self.user_widget))
        self.navi_style_button.clicked.connect(lambda: self.controller_settings.open_sub_widget(self.style_widget))
        self.navi_sound_button.clicked.connect(lambda: self.controller_settings.open_sub_widget(self.sound_widget))
        self.navi_update_button.clicked.connect(lambda: self.controller_settings.open_sub_widget(self.update_widget))
        self.navi_language_button.clicked.connect(lambda: self.controller_settings.open_sub_widget(self.language_widget))
        self.navi_report_button.clicked.connect(lambda: self.controller_settings.open_sub_widget(self.report_widget))
#######################################################################################################################
