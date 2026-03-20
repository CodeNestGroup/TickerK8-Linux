#   --- Improt ---
import json
from PyQt5.QtWidgets import (
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
    QSize
)
from PyQt5.QtGui import (
    QPixmap,
    QIcon,
    QPainter
)
from PyQt5.QtSvg import (
    QSvgRenderer
)

def StockUi(self):
    self.setObjectName('ObjectInfoS')
    self.Widget.setObjectName('Widget')
    self.TitleL.setObjectName('TitleL')
    self.IconL.setObjectName('IconL')
    self.TickerL.setObjectName('TickerL')
    self.NameL.setObjectName('NameL')
    self.MarketL.setObjectName('MarketL')
    self.CountryL.setObjectName('CountryL')
    self.InfoW.setObjectName('InfoW')
    self.InfoTitleL.setObjectName('InfoTitleL')
    self.ActivityNameL.setObjectName('ActivityNameL')
    self.ActivityValueL.setObjectName('ActivityValueL')
    self.IndustryNameL.setObjectName('IndustryNameL')
    self.IndustryValueL.setObjectName('IndustryValueL')
    self.DateEstablishNameL.setObjectName('DateEstablishNameL')
    self.DateEstablishValueL.setObjectName('DateEstablishValueL')
    self.EmployesNameL.setObjectName('EmployesNameL')
    self.EmployesValueL.setObjectName('EmployesValueL')
    self.WebNameL.setObjectName('WebNameL')
    self.WebValueL.setObjectName('WebValueL')
    self.AdresNameL.setObjectName('AdresNameL')
    self.AdresValueL.setObjectName('AdresValueL')
    self.ManagmentW.setObjectName('ManagmentW')
    self.ManagmentTitleL.setObjectName('ManagmentTitleL')
    self.CEONameL.setObjectName('CEONameL')
    self.CEOValueL.setObjectName('CEOValueL')
    self.CFONameL.setObjectName('CFONameL')
    self.CFOValueL.setObjectName('CFOValueL')
    self.ManagmentNameL.setObjectName('ManagmentNameL')
    self.ManagmentValueL.setObjectName('ManagmentValueL')
    self.SupervisoryBoardNameL.setObjectName('SupervisoryBoardNameL')
    self.SupervisoryBoardValueL.setObjectName('SupervisoryBoardValueL')
    self.InfoW.setProperty('class', 'SubW')
    self.ManagmentW.setProperty('class', 'SubW')
    self.InfoTitleL.setProperty('class', 'SubTitle')
    self.ManagmentTitleL.setProperty('class', 'SubTitle')
    self.ActivityNameL.setProperty('class', 'Name')
    self.IndustryNameL.setProperty('class', 'Name')
    self.DateEstablishNameL.setProperty('class', 'Name')
    self.EmployesNameL.setProperty('class', 'Name')
    self.WebNameL.setProperty('class', 'Name')
    self.AdresNameL.setProperty('class', 'Name')
    self.CEONameL.setProperty('class', 'Name')
    self.CFONameL.setProperty('class', 'Name')
    self.ManagmentNameL.setProperty('class', 'Name')
    self.SupervisoryBoardNameL.setProperty('class', 'Name')
    self.ActivityValueL.setProperty('class', 'Value')
    self.IndustryValueL.setProperty('class', 'Value')
    self.DateEstablishValueL.setProperty('class', 'Value')
    self.EmployesValueL.setProperty('class', 'Value')
    self.WebValueL.setProperty('class', 'Value')
    self.AdresValueL.setProperty('class', 'Value')
    self.CEOValueL.setProperty('class', 'Value')
    self.CFOValueL.setProperty('class', 'Value')
    self.ManagmentValueL.setProperty('class', 'Value')
    self.SupervisoryBoardValueL.setProperty('class', 'Value')
    self.InfoL.addWidget(self.InfoTitleL, , , , , )
    self.InfoL.addWidget(self.ActivityNameL)
    self.InfoL.addWidget(self.ActivityValueL,,,,)
    self.InfoL.addWidget(self.IndustryNameL,,,,)
    self.InfoL.addWidget(self.IndustryValueL,,,,)
    self.InfoL.addWidget(self.DateEstablishNameL,,,,)
    self.InfoL.addWidget(self.DateEstablishValueL,,,,)
    self.InfoL.addWidget(self.EmployesNameL,,,,)
    self.InfoL.addWidget(self.EmployesValueL,,,,)
    self.InfoL.addWidget(self.WebNameL,,,,)
    self.InfoL.addWidget(self.WebValueL,,,,)
    self.InfoL.addWidget(self.AdresNameL,,,,)
    self.InfoL.addWidget(self.AdresValueL,,,,)
    self.InfoL.setSpacing(0)
    self.InfoL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.InfoL.setColumnStretch(i, 1)
    self.InfoW.setLayout(self.InfoL)
    self.ManagmentL.addWidget(self.,,,,)
    self.ManagmentL.addWidget(self.,,,,)
    self.ManagmentL.addWidget(self.,,,,)
    self.ManagmentL.addWidget(self.,,,,)
    self.ManagmentL.addWidget(self.,,,,)
    self.ManagmentL.addWidget(self.,,,,)
    self.ManagmentL.addWidget(self.,,,,)
    self.ManagmentL.addWidget(self.,,,,)
    self.ManagmentL.addWidget(self.,,,,)
    self.ManagmentL.addWidget(self.,,,,)
    self.ManagmentL.setSpacing(0)
    self.ManagmentL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.ManagmentL.setColumnStretch(i, 1)
    self.ManagmentW.setLayout(self.ManagmentL)





def StockReloadStyle(self):
    pass

def StockRetranslate(self):
    pass