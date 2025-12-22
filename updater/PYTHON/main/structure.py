""" Import packages """
import pathlib 
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
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
        self.settings_button = QPushButton_sound(self)
        self.instagram_button = QPushButton_sound(self)
        self.github_button = QPushButton_sound(self)
        self.discord_button = QPushButton_sound(self)
        self.info_label = QLabel(self)
        """ Call functions """
        main_ui(self)
        main_reload_style(self)
        main_retranslate(self)
        """ Connect functions """
        self.instagram_button.clicked.connect(lambda: open_link('https://www.instagram.com/codenestgroup/'))
        self.github_button.clicked.connect(lambda: open_link('https://github.com/CodeNestGroup'))
        self.discord_button.clicked.connect(lambda: open_link('https://discord.gg/twZ3SNcC'))
    
    def main_connect_handle(self, b):
        if b and not self.last_ping:
            main_connect(self)
            self.last_ping = True
        elif not b and self.last_ping:
            main_no_connect(self)
            self.last_ping = False
    
#______________________________________________________________________________________________________________________
