#   --- Import ---
import datetime
import sqlite3

from Object.AStructure import ObjectW
from ObjectInfo.AStructure import ObjectInfoS
from ObjectStats.AStructure import ObjectStatsS

from PyQt5.QtWidgets import (
    QScrollArea,
    QWidget,
    QGridLayout,
    QPushButton,
    QLabel,
    QSizePolicy
)

from PyQt5.QtCore import (
    Qt
)


from PyQt5.QtGui import (
    QLinearGradient,
    QPalette,
    QBrush,
    QColor,
    QPixmap,
    QPainter
)

#   --- Dynamic Background ---
def WidgetBackgroundPainter(self):
    _colors = self.BacgroundConf['background']
    _color_0 = '#000000'
    _color_1 = '#000000'
    _color_2 = '#000000'
    _alpha_1 = 'ff'
    _alpha_2 = 'ff'
    _x_1 = 0.0
    _x_2 = 1.0 
#       --- Calculate index and precent ---
    _now = datetime.datetime.now()
    _today_sec = _now.hour*3600+_now.minute*60+_now.second
    if _today_sec >=86400:
        _today_sec = 86399
    _index = _today_sec//8640
    _percent = (_today_sec/8640)-_index
#       --- Set colors ---
    if _percent <= 0.5:
        _x_1 = 1-(_percent*2)
        _x_2 = 1.0
        _alpha_1 = 'ff'
        _alpha_2 = f'{int(255 *(_percent / 0.5)):02X}'
        _color_0 = f'#ff{_colors[_index-1]}'
    else:
        _x_1 = 0.0
        _x_2 = 1-(_percent-0.5)*2
        _alpha_1 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _alpha_2 = 'ff'
        _color_0 = f'#ff{_colors[_index]}' 
    _color_1 = f'#{_alpha_1}{_colors[_index-1]}'
    _color_2 = f'#{_alpha_2}{_colors[_index]}'
#       --- Paint background ---
    pixmap = QPixmap(self.size())
    pixmap.fill(QColor(_color_0))
    painter = QPainter(pixmap)
    gradient = QLinearGradient(0,0,self.width(), 0)
    gradient.setColorAt(_x_1, QColor(_color_1))
    gradient.setColorAt(_x_2, QColor(_color_2))
    painter.fillRect(self.rect(), gradient)
    painter.end()
    palette = self.palette()
    palette.setBrush(QPalette.Window, QBrush(pixmap))
    self.setAutoFillBackground(True)
    self.setPalette(palette)

def SetupMainObject(self, t, i):
    if self.ObjectW:
        self.ObjectW.deleteLater()
        self.ObjectW = None
    self.ObjectW = ObjectW(self.OpenedW, self, t, i)
    self.OpenedL.addWidget(self.ObjectW, 0, 35, 100, 30)

def SetupObject(self, t, i):
    if self.ObejctInfoS:
        self.ObejctInfoS.deleteLater()
        self.ObejctInfoS = None
    if self.ObjectStatsS:
        self.ObjectStats.deleteLater()
        self.ObjectStats = None 
    self.ObejctInfoS = ObjectInfoS(self.OpenedW, self, t, i)
    self.ObjectStatsW = ObjectStatsS(self.OpenedW, self, t, i)
    self.OpenedL.addWidget(self.ObejctInfoS, 0, 16, 100, 41)
    self.OpenedL.addWidget(self.ObjectStatsW, 0, 58, 100, 41)

def ListAddSetupList(self):
    conn = sqlite3.connect(f'{self.Path}/APP_FILES/CONFIG/GLOBAL/tickerk8_offline.db')
    cur = conn.cursor()
    for ListName, ListItems in self.ObjectList.items():
        self.NameL.setText(ListName)
        i = 0
        for SectionName, SectionItems in ListItems.items():
            SectionNameL = QLabel(self.ListAddW)
            SectionNameL.setObjectName(f'SectionNameL{SectionName}')
            SectionNameL.setProperty('class', 'SectionNameL')
            self.ListAddL.addWidget(SectionNameL, i, 0, 1, 100)
            SectionNameL.setAlignment(Qt.AlignCenter)
            SectionNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            SectionNameL.setText(SectionName)
            i += 1
            for ii, (ItemId, ItemTable) in enumerate(SectionItems.items(), 0):
                cur.execute(f'SELECT name FROM "{ItemTable}" WHERE id=?;', (int(ItemId),))
                r = cur.fetchone()
                if r:
                    AddB = QPushButton(self.ListAddW)
                    AddB.setObjectName(f'AddB{ii}')
                    AddB.setProperty('class', 'AddB')
                    self.ListAddL.addWidget(AddB, i, 0, 1, 100)
                    AddB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    AddB.setText('+')
                    AddB.clicked.connect(lambda _, L_N=ListName, S_N=SectionName, I_I=ii: ListAddHandle(self, L_N, S_N, I_I))
                    i += 1
                    ObjectNameL = QLabel(self.ListAddW)
                    ObjectNameL.setObjectName(f'ObjectNameL{ii}')
                    ObjectNameL.setProperty('class', 'NameL')
                    self.ListAddL.addWidget(ObjectNameL, i, 0, 1, 100)
                    ObjectNameL.setAlignment(Qt.AlignCenter)
                    ObjectNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    ObjectNameL.setText(r[0])
                    i += 1
            AddB = QPushButton(self.ListAddW)
            AddB.setObjectName(f'AddB{ii}')
            AddB.setProperty('class', 'AddB')
            self.ListAddL.addWidget(AddB, i, 0, 1, 100)
            AddB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            AddB.setText('+')
            AddB.clicked.connect(lambda _, L_N=ListName, S_N=SectionName, I_I=ii: ListAddHandle(self, L_N, S_N, I_I))
            i += 1
    conn.close()

def ListAddHandle(self, Table, Section, IdObject):
    print(Table, Section, IdObject)
    self.ListSearchPage()

def SetupResultS(self, result):
    if self.SearchS:
        self.SearchS.deleteLater()
        self.SearchS = None
    self.ResultS = QScrollArea(self.SearchW)


def ListDeleteObject(self, ItemTable, ItemId):
    print(ItemTable, ItemId)
