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

#   --- Class ---
class MainObjectW(QWidget): 
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = parent.Path
        self.Theme = parent.Theme
        self.Language = parent.Language
        self.ObjectList = parent.ObjectList
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.IconL = QLabel(self)
        self.TickerL = QLabel(self)
        self.ChartW = QWidget(self)
        self.InfoTitleL = QLabel(self)
        self.InfoW = QWidget(self)
        self.InfoL = QGridLayout(self.InfoW)
        self.InfoNameNameL = QLabel(self.InfoW)
        self.InfoNameValueL = QLabel(self.InfoW)
        self.InfoTickerNameL = QLabel(self.InfoW)
        self.InfoTickerValueL = QLabel(self.InfoW)
#           --- Call functions ---
        MainObjectUi(self)
        MainObjectReloadStyle(self)
        MainObjectRetranslate(self)
        Setup(self)
