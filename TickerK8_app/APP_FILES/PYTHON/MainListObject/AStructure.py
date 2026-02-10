#   --- Import ---
import json
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QGridLayout
)
from .AUi import *
from .ALogic import *

#   --- Class ---
class MainListObjectW(QWidget): 
    def __init__(self):
        super().__init__()
        self.setParent(parent)
#       --- Create objects ---
        self.Layout = QGridLayout(self)
        self.NullDataL = None
        self.DataS = None
        Ui(self)
        ReloadStyle(self)

    def NullData(self):
#       --- Create objects ---
        self.NullDataL = QLabel(self)
#       --- Call functions 
        NullDataUi(self)
        NullDataReloadStyle(self)
        NullDataRetranslate(self)
    
    def Data(self):
#       --- Create objects ---
        self.DataS = QWidget(self)
        self.EditB = QPushButton(self)
        self.

#       --- Call functions ---

#       --- Connect functions ---

