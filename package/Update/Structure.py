#   --- Import PySide2 ---
from PySide2.QtWidgets import (
    QWidget,
    QPushButton,
    QGridLayout,
    QVBoxLayout
)
from PySide2.QtCore import (
    Qt,
    QThread,
    QTimer
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
        self.LoginOpenF = parent.LoginOpen
        self.Theme = parent.ConfigOffline['theme']
        self.Language = parent.ConfigOffline['language']
        self.PingT = QThread(self)
        parent.PingO.moveToThread(self.PingT)
        self.PingT.started.connect(parent.PingO)
        parent.PingO.Status.connect(lambda s: self.PingHandler(s))
        self.PingT.start()
        self.LastPing = False
        self.ControllerDownloadT = None
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.ChaneglogW = None
        self.ChaneglogS = None
        self.SettingsB = QPushButton(self)
        self.InstagramB = QPushButton(self)
        self.GithubB = QPushButton(self)
        self.DiscordB = QPushButton(self)
        self.FuncB = None
        self.InfoL = None
#           --- Call functions ---
        UpdateUi(self)
        UpadateReloadStyle(self)
#        --- Connect functions ---
        self.InstagramB.clicked.connect(lambda: OpenLink('https://www.instagram.com/codenestgroup/'))
        self.GithubB.clicked.connect(lambda: OpenLink('https://github.com/CodeNestGroup'))
        self.DiscordB.clicked.connect(lambda: OpenLink('https://discord.gg/twZ3SNcC'))

    def PingHandler(self, Status):
        if Status and self.LastPing:
            self.LastPing = True
        elif Status and not self.LastPing:
            self.ChangelogLoading()
            self.LastPing = True
        else:
            self.ChangelogNoConnection()
            self.LastPing = False

    def ChangelogReset(self):
        if self.ChaneglogW:
            self.ChaneglogW.deleteLater()
            self.ChaneglogW = None
        if self.ChangelogS:
            self.ChaneglogS.deleteLater()
            self.ChaneglogS = None

    def ChangelogNoConnection(self):
        self.ChangelogReset()
#           --- Create objects ---
        self.ChangelogW = QWidget(self)
        self.ChangelogL = QGridLayout(self.ChangelogW)
        self.ChangelogIconL = QLabel(self.ChangelogW)
        self.ChangelogMessageL = QLabel(self.ChangelogW)
#           --- Call functions ---
        ChangelogNoConnectionUi(self)
        ChangelogNoConnectionRetranslate(self)

    def ChangelogLoading(self):
        self.ChangelogReset()
#           --- Create objects ---
        self.ChangelogW = QWidget(self)
        self.ChangelogL = QGridLayout(self.ChangelogW)
        self.ChangelogIconL = QLabel(self.ChangelogW)
        self.ChangelogMessageL = QLabel(self.ChangelogW)
        self.ChaneglogDotsL = QLabel(self.ChangelogW)
        self.ChangelogDotsT = QTimer(self.ChaneglogDotsL)
        self.GetReleasesT = GetReleasesT()
#           --- Call functions ---
        ChangelogLoadingUi(self)
        ChangelogLoadingRetranslate(self)
#           --- Connect functions ---
        self.ChangelogDotsT.timeout.connect(lambda: DotsUpdate(self))
        self.ChangelogDotsT.start(500)
        self.GetReleasesT.Finished.connect(lambda r: self.ChangelogConnection(r))
        self.GetReleasesT.Finished.connect(lambda: self.GetReleasesT.quit())
        self.GetReleasesT.Finished.connect(lambda: self.GetReleasesT.deleteLater())
        self.GetReleasesT.start()

    def ChangelogConnection(self, r):
        self.ChangelogReset()
#           --- Create objects ---
        self.ChangelogS = QScrollArea(self)
        self.ChangelogW = QWidget(self.ChangelogS)
        self.ChangelogL = QVBoxLayout(self.ChangelogW)
#           --- Call functions ---
        ChangelogConnctionUi(self)
        ChangelogConnectionSetup(self, r)
