#   --- Import PySide2
from PySide2.QtWidgets import (
    QWidget,
    QPushButton,
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
        
        self.LastPing = False
        self.ControllerDownloadT = None
        self.GetReleasesT = None
#           --- Create objects ---
        self.Layout = QGridLayout(self)
       
        self.SettingsB = QPushButton(self)
        self.InstagramB = QPushButton(self)
        self.GithubB = QPushButton(self)
        self.DiscordB = QPushButton(self)
#           --- Call functions ---
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
