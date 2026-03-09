#   --- Import ---
import json
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QScrollArea,
    QGridLayout,
    QVBoxLayout
)
from PyQt5.QtCore import (
    Qt,
    QTimer
)
from .AUi import *
from .ALogic import *

#   --- Class ---
class NewsListW(QWidget): 
    def __init__(self, parent):
        super().__init__(parent)
        self.Path = parent.main_path
        self.Config = json.loads(parent.logged_user_config)
        self.Theme = self.Config['theme']
        self.Language = self.Config['language']
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.ListS = QScrollArea(self)
        self.ListW = QWidget(self)
        self.ListL = QVBoxLayout(self)
        self.ReloadB = QPushButton(self)
#           --- Call functions ---
        NewsListUi(self)
        NewsListReloadStyle(self)
        NewsListRetranslate(self)
        ReloadList(self)
#           --- Connect  functions ---
        self.ReloadB.clicked.connect(lambda: ReloadList(self))