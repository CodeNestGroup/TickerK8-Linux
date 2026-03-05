#   --- Import ---
import json
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QGridLayout
)
from PyQt5.QtCore import (
    Qt,
    QTimer
)
from .AUi import *
from .ALogic import *
from ListObject.AStructure import ListObjectW
from Object.AStructure import ObjectW
from ListNews.AStructure import ListNewsW
#from MainSearch.Structure import MainSearchWidget
#from MainNewsList.Structure import MainNewsListWidget

#   --- Class ---
class MainW(QWidget): 
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.Path = parent.main_path
        self.Config = json.loads(parent.logged_user_config)
        self.Theme = self.Config['theme']
        self.Language = self.Config['language']
        self.ObjectList = self.Config['lists']
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.BacgroundConf = json.load(open(f'{self.Path}/APP_FILES/PYTHON/Main/CBackgroundConf.json', 'r'))
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.NavW = QWidget(self)
        self.NavL = QGridLayout(self)
        self.NavDefaultB = QPushButton(self.NavW)
        self.NavSearchB = QPushButton(self.NavW)
        self.NavListObjectB = QPushButton(self.NavW)
        self.NavObjectB = QPushButton(self.NavW)
        self.NavNewsB = QPushButton(self.NavW)
        self.NavSettingsB = QPushButton(self.NavW)
        self.NavLogoutB = QPushButton(self.NavW)
        self.OpenedW = None
        self.FooterW = QWidget(self)
        self.BackgroundT = QTimer(self)
#           --- Call functions ---
        MainUi(self)
        MainReloadStyle(self)
        MainRetranslate(self)
        DefaultPage(self)
        self.WidgetBackgroundPainter = lambda: WidgetBackgroundPainter(self)
        self.BackgroundT.timeout.connect(self.WidgetBackgroundPainter)
        self.BackgroundT.start(1)
#           --- Connect  functions ---

    def DefaultPage(self):
#           --- Create objects ---
        if OpenedW:
            self.OpenedW.deleteLater()
            self.OpenedW = None
        self.OpenedW = QWidget(self)
        self.OpenedL = QGridLayout(self)
        self.ListObjectW = ListObjectW(self.OpenedW)
        self.ObjectW = ObjectW(self.OpenedW)
        self.ListNewsW = ListNewsW(self.OpenedW)
#           --- Call functions ---
        DefaultPageUi(self)
#           --- Connect  functions ---