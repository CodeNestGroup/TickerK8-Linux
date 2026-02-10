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
from .ui import *
from .logic import *
from MainListObject.AStructure import MainListObjectW
from MainSearch.Structure import MainSearchWidget
from MainNewsList.Structure import MainNewsListWidget

#   --- Class ---
class MainW(QWidget): 
    def __init__(self):
        super().__init__()
        self.setParent(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.BacgroundConf = json.load(open('./j_background_conf.json', 'r'))
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.SearchB = QPushButton(self)
        self.SettingsB = QPushButton(self)
        self.LogoutB = QPushButton(self)
        self.MainListObjectW = MainListObjectW(self)
        self.MainObjectW = MainObjectW(self)
        # Dodać news widget osobna klasa
        self.BackgroundT = QTimer(self)
        self.NewsT = QTimer(self)
#           --- Call functions ---
        MainUi(self)
        MainReloadStyle(self)
        MainRetranslate(self)
        self.WidgetBackground = lambda: WidgetBackground_painter(self)
        self.BackgroundT.timeout.connect(self.widget_background)
        self.BackgroundT.start(1)
#           --- Connect  functions ---
        self.search_button.clicked.connect(lambda: Main_search_widget(self))
