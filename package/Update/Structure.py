#   --- Import PySide2
from PySide2.QtWidgets import (
    QWidget,
    QGridLayout
)
from PySide2.QtCore import (
    Qt
)
#   --- Import Update modules ---
from .Ui import (
    UpdateUi,
    UpdateReloadStyle
 )
from .Logic import *


#   --- UpdateW ---

class UpdateW(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = parent.Path

        """" Set paths, file name """
        
        self.last_ping = False
        self.info_label = None
        self.download_button = None
        self.controller_download_thread = None
        self.open_button = None
        self.get_releases_thread = None 
        """ Create objects """
        self.layout = QGridLayout(self)
        self.changelog_widget = Changelog_widget(self)
        self.settings_button = QPushButton_sound(self)
        self.instagram_button = QPushButton_sound(self)
        self.github_button = QPushButton_sound(self)
        self.discord_button = QPushButton_sound(self)
        """ Call functions """
        main_ui(self)
        main_reload_style(self)
        main_no_connect(self)
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
