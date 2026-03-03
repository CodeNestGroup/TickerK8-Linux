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
from .p_ui import *
from .p_logic import *
from MainListObject.AStructure import MainListObjectW
from MainObject.AStructure import MainObjectW
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
        self.BacgroundConf = json.load(open(f'{self.Path}/APP_FILES/PYTHON/main/j_background_conf.json', 'r'))
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
        self.WidgetBackgroundPainter = lambda: WidgetBackgroundPainter(self)
        self.BackgroundT.timeout.connect(self.WidgetBackgroundPainter)
        self.BackgroundT.start(1)
#           --- Connect  functions ---
        #self.search_button.clicked.connect(lambda: Main_search_widget(self))
