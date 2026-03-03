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

def MainObjectUi(self):
    self.setObjectName('MainObjectW')
    self.IconL.setObjectName('IconL')
    self.TickerL.setObjectName('TickerL')
    self.ChartW.setObjectName('ChartW')
    self.InfoTitleL.setObjectName('InfoTitleL')
    self.InfoW.setObjectName('InfoW')
    self.InfoNameNameL.setObjectName('InfoNameNameL')
    self.InfoNameValueL.setObjectName('InfoNameValueL')
    self.InfoTickerNameL.setObjectName('InfoTickerNameL')
    self.InfoTickerValueL.setObjectName('InfoTickerValueL')
    self.InfoNameNameL.setProperty('class', 'Name')
    self.InfoTickerNameL.setProperty('class', 'Name')
    self.InfoNameValueL.setProperty('class', 'Value')
    self.InfoTickerValueL.setProperty('class', 'Value')
    self.Layout.addWidget(self.IconL)
    self.Layout.addWidget(self.TickerL)
    self.Layout.addWidget(self.ChartW)
    self.Layout.addWidget(self.InfoTitleL)
    self.Layout.addWidget(self.InfoW)
    self.Layout.

