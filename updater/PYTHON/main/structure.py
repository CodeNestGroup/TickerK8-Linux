""" Import packages """
import pathlib 
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QScrollArea,
    QGridLayout
)
""" Import main modules """
from .ui import *
from .logic import *
""" Import custom modules """
from soundbutton.structure import QPushButton_sound
from main_changelog.structure import Changelog_widget
from main_update.structure import Update_widget
#______________________________________________________________________________________________________________________

class Main_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        """" Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        self.last_ping = False
        """ Create objects """
        self.layout = QGridLayout(self)
        self.changelog_widget = Changelog_widget(self)
        self.update_widget = Update_widget(self)
        self.logo_c_n_g_label = QLabel(self)
        self.logo_ticker_label = QLabel(self)
        self.settings_button = QPushButton_sound(self)
        self.instagram_button = QPushButton_sound(self)
        self.github_button = QPushButton_sound(self)
        self.discord_button = QPushButton_sound(self)
        self.start_button = QPushButton_sound(self)
        """ Call functions """
        main_ui(self)
        main_reload_style(self)
        main_retranslate(self)
        """ Connect functions """
        self.instagram_button.clicked.connect(open_instagram)
        self.github_button.clicked.connect(open_github)
        self.discord_button.clicked.connect(open_discord)
        self.update_widget.update_status.connect(self.update_status_handel)
    
    def main_connect_controller(self, b):
        if b and not self.last_ping:
            main_connect(self)
            self.last_ping = True
        elif not b and self.last_ping:
            main_no_connect(self)
            self.last_ping = False
    
    def update_status_handel(self, b):
        update_status_controller(self, b)
#______________________________________________________________________________________________________________________

