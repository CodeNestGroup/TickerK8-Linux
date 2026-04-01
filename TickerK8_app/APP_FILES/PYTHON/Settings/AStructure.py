#   --- Import ---
import pathlib
import json
#   --- Import PyQt5 packages ---
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton,
    QComboBox, 
    QGridLayout,
    QVBoxLayout 
)
from PyQt5.QtCore import (
    Qt
)
#   --- Import settings modules ---
from .AUi import *
from .ALogic import *

#   --- Class ----
class SettingsW(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = parent.Path
        
        self.LoggedUserId = parent.logged_user_id
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.NaviS = QScrollArea(self)
        self.NaviW = QWidget(self.NaviS)
        self.NaviL = QVBoxLayout(self.NaviW)
        self.NaviUserB = QPushButton(self.NaviW)
        self.NaviStyleB = QPushButton(self.NaviW)
        self.NaviUpdateB = QPushButton(self.NaviW)
        self.NaviLanguageB = QPushButton(self.NaviW)
        self.NaviExitB  = QPushButton(self)
#           --- Call functions ---
        SettingsUi(self)
        SettingsReloadStyle(self)
        SettingsRetranslate(self)
#           --- Connect  functions ---
        self.NaviUserB.clicked.connect(self.UserPage)
        self.NaviStyleB.clicked.connect(self.StylePage)
        self.NaviUpdateB.clicked.connect(self.UpdatePage)
        self.NaviLanguageB.clicked.connect(self.LanguagePage)

    def ResetPage(self):
        if self.PanelS:
            self.PanelS.deleteLater()
            self.PanelS = None

    def UserPage(self):
        self.ResetPage()
        self.PanelS = QScrollArea(self)
        self.PanelW = QWidget(self.PanelW)
        self.PanelL = QVBoxLayout(self.PanelW)
        self.PanelTitleL = QLabel(self.PanelW)
        self.UserNameNameL = QLabel(self.PanelW)
        self.UserNameValueL = QLabel(self.PanelW)
        self.UserEmailNameL = QLabel(self.PanelW)
        self.UserEmailValueL = QLabel(self.PanelW)
        self.UserCreateDateNameL = QLabel(self.PanelW)
        self.UserCreateDateValueL = QLabel(self.PanelW)
#           --- Call functions ---
        UserUi(self)
        UserReloadStyle(self)
        UserRetranslate(self)
#           --- Connect  functions ---

    def StylePage(self):
        self.ResetPage()
        self.PanelS = QScrollArea(self)
        self.PanelW = QWidget(self.PanelW)
        self.PanelL = QVBoxLayout(self.PanelW)
        self.PanelTitleL = QLabel(self.PanelW)
        self.StyleThemeDayNightNameL = QLabel(self.PanelW)
        self.StyleThemeDayNightValueB = QPushButton(self.PanelW)
        self.StyleThemeThemesNameL = QLabel(self.PanelW)
        self.StyleThemeThemesValueC = QComboBox(self.PanelW)
#           --- Call functions ---
        StyleUi(self)
        StyleReloadStyle(self)
        StyleRetranslate(self)
#           --- Connect  functions ---
#        self.StyleThemeDayNightValueB.clicked.connect()
#        self.StyleThemeThemesValueC.clicked.connect()

    def UpdatePage(self):
        self.ResetPage()
        self.PanelS = QScrollArea(self)
        self.PanelW = QWidget(self.PanelW)
        self.PanelL = QVBoxLayout(self.PanelW)
        self.PanelTitleL = QLabel(self.PanelW)
        self.UpdateDescriptionNameL = QLabel(self.PanelW)
        self.UpdateDescriptionValueL = QLabel(self.PanelW)
        self.UpdateChangelogNameL = QLabel(self.PanelW)
        self.UpdateChangelogValueS = QScrollArea(self.PanelW)
        self.UpdateChangelogValueW = QWidget(self.UpdateChangelogValueS)
        self.UpdateChangelogValueL = QGridLayout(self.UpdateChangelogValueW)
#           --- Call functions ---
        UpdateUi(self)
        UpdateReloadStyle(self)
        UpdateRetranslate(self)
#           --- Connect  functions ---  

    def LanguagePage(self):
        self.ResetPage()
        self.PanelS = QScrollArea(self)
        self.PanelW = QWidget(self.PanelW)
        self.PanelL = QVBoxLayout(self.PanelW)
        self.PanelTitleL = QLabel(self.PanelW)
        self.LanguageNameL = QLabel(self.PanelW)
        self.LanguageValueC = QComboBox(self.PanelW)
#           --- Call functions ---
        LanguageUi(self)
        LanguageReloadStyle(self)
        LanguageRetranslate(self)
#           --- Connect functions ---
#        self.LanguageValueC.currentIndexChanged.connect()
        