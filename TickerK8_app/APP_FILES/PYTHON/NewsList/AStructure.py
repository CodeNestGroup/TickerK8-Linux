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
class NewsListS(QScrollArea): 
    def __init__(self, parent, MainNewsListData):
        super().__init__(parent)
        self.Path = parent.Path
        self.Theme = parent.Theme
        self.Language = parent.Language
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Create objects ---
        self.ListW = QWidget(self)
        self.ListL = QVBoxLayout(self)
#           --- Call functions ---
        NewsListUi(self)
        NewsListReloadStyle(self)
        CreateList(self, MainNewsListData)
#           --- Connect  functions ---