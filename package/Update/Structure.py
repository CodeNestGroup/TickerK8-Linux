#   --- Import PySide2
from PySide2.QtWidgets import (
    QWidget,
    QPushButton,
    QGridLayout
)
from PySide2.QtCore import (
    Qt,
)
#   --- Import Update modules ---
from .Ui import *
from .Logic import *


#   --- UpdateW ---

class UpdateW(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = parent.Path
        self.Theme = parent.Config['theme']
        self.Language = parent.Config['language']
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
        UpdateUi(self)
        UpadateReloadStyle(self)
#        --- Connect functions ---
        self.InstagramB.clicked.connect(lambda: open_link('https://www.instagram.com/codenestgroup/'))
        self.GithubB.clicked.connect(lambda: open_link('https://github.com/CodeNestGroup'))
        self.DiscordB.clicked.connect(lambda: open_link('https://discord.gg/twZ3SNcC'))

    def ChangelogNoConnection(self):
#           --- Create objects ---
        self.ChangelogW = QWidget(self)
        self.ChangelogL = QGridLayout(self.ChangelogW)
        self.ChangelogIconL = QLabel(self.ChangelogW)
        self.ChangelogMessageL = QLabel(self.ChangelogW)
#           --- Call functions ---
        ChangelogNoConnectionUi(self)
        ChangelogNoConnectionRetranslate(self)

    def ChangelogLoading(self):
#           --- Create objects ---
        self.ChangelogW = QWidget(self)
        self.ChangelogL = QGridLayout(self.ChangelogW)
        self.ChangelogIconL = QLabel(self.ChangelogW)
        self.ChangelogMessageL = QLabel(self.ChangelogW)
        self.ChaneglogDotsL = QLabel(self.ChangelogW)
        self.ChangelogDotsT = 
#           --- Call functions ---
        ChangelogLoadingUi(self)
        ChangelogLoadingRetranslate(self)

    def ChangelogConnection(self):
#           --- Create objects ---
        
#           --- Call functions ---
        ChangelogConnctionUi(self)
        ChangelogConnctionRetranslate(self)
