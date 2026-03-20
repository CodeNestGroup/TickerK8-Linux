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
    Qt
)
from .AUi import *
from .ALogic import *

#   --- Class ---
class ObjectInfoS(QScrollArea): 
    def __init__(self, parent, s, t, i):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = s.Path
        self.Theme = s.Theme
        self.Language = s.Language
        if t == 'country':
                self.Country()
        elif t == 'market':
                self.Market()
        elif t == 'stock':
                self.Stock()

    def Country(self):
        pass

    def Market(self):
        pass

    def Stock(self):
#           --- Create objects ---
        self.Widget = QWidget(self)
        self.Layout = QGridLayout(self.Widget)
        self.TitleL = QLabel(self.Widget)
        self.IconL = QLabel(self.Widget)
        self.TickerL = QLabel(self.Widget)
        self.NameL = QLabel(self.Widget)
        self.MarketL = QLabel(self.Widget)
        self.CountryL = QLabel(self.Widget)

        self.InfoW = QWidget(self.Widget)
        self.InfoL = QGridLayout(self.InfoW)
        self.InfoTitleL = QLabel(self.InfoW)
        self.ActivityNameL = QLabel(self.InfoW)
        self.ActivityValueL = QLabel(self.InfoW)
        self.IndustryNameL = QLabel(self.InfoW)
        self.IndustryValueL = QLabel(self.InfoW)
        self.DateEstablishNameL = QLabel(self.InfoW)
        self.DateEstablishValueL = QLabel(self.InfoW)
        self.EmployesNameL = QLabel(self.InfoW)
        self.EmployesValueL = QLabel(self.InfoW)
        self.WebNameL = QLabel(self.InfoW)
        self.WebValueL = QLabel(self.InfoW)
        self.AdresNameL = QLabel(self.InfoW)
        self.AdresValueL = QLabel(self.InfoW)

        self.ManagmentW = QWidget(self)
        self.ManagmentL = QGridLayout(self.ManagmentW)
        self.ManagmentTitleL = QLabel(self.ManagmentW)
        self.CEONameL = QLabel(self.ManagmentW)
        self.CEOValueL = QLabel(self.ManagmentW)
        self.CFONameL = QLabel(self.ManagmentW)
        self.CFOValueL = QLabel(self.ManagmentW)
        self.ManagmentNameL = QLabel(self.ManagmentW)
        self.ManagmentValueL = QLabel(self.ManagmentW)
        self.SupervisoryBoardNameL = QLabel(self.ManagmentW)
        self.SupervisoryBoardValueL = QLabel(self.ManagmentW)
#           --- Call functions ---
        StockUi(self)
        StockReloadStyle(self)
        StockRetranslate(self)
#           --- Connect functions ---




