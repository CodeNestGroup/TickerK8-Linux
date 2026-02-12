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
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.Path = parent.Path
        self.Theme = parent.Theme
        self.Language = parent.Language
        self.ObjectList = parent.ObjectList
#       --- Create objects ---
        self.Layout = QGridLayout(self)
        self.NullDataL = None
        self.ListNameL = None
        self.DataS = None
        self.EditB = None
        self.ListB = None
#       --- Call functions ---
        Ui(self)
        ReloadStyle(self)
        if self.ObjectList:
            self.Data()
        else:
            self.NullData()
#       --- Connect functions ---

    def NullData(self):
#       --- Create objects ---
        self.NullDataL = QLabel(self)
#       --- Call functions 
        NullDataUi(self)
        NullDataRetranslate(self)
    
    def Data(self):
#       --- Create objects ---
        self.ListNameL = QLabel(self)
        self.DataS = QScrollArea(self)
        self.DataW = QWidget(self)
        self.DataL = QGridLayout(self)
        self.EditB = QPushButton(self)
        self.ListB = QPushButton(self)
#       --- Call functions ---
        DataUi(self)
        DataRetranslate(self)
        SetupData(self, self.ObjectList)
#       --- Connect functions ---

    def EditData(self):
        pass

    def ListsData(self):
        pass

