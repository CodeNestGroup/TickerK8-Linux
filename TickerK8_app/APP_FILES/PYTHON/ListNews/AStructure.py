#   --- Import ---
import json
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QVBoxLayout
)
from PyQt5.QtCore import (
    Qt,
    QTimer
)
from .AUi import *
from .ALogic import *

#   --- Class ---
class ListNewsW(QWidget): 
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = parent.Path
        self.Theme = parent.Theme
        self.Language = parent.Language
#        self.NewsList = parent.NewsList
        self.NewsTimer = None
#           --- Create objects ---
        self.Layout = QVBoxLayout(self)
#           --- Call functions ---
        MainNewsUi(self)
        MainNewsReloadStyle(self)
        Setup(self)