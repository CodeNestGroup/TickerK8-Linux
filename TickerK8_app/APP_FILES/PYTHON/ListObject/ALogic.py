import sqlite3
from PyQt5.QtWidgets import (
    QLabel,
    QPushButton,
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt
)

def SetupData(self, o:dict):
    conn = sqlite3.connect(f'{self.Path}/APP_FILES/CONFIG/GLOBAL/tickerk8_offline.db')
    cur = conn.cursor()
    for ListName, ListItems in o.items():
        self.NameL.setText(ListName)
        i = 0
        for SectionName, SectionItems in ListItems.items():
            SectionNameL = QLabel(self.DataW)
            SectionNameL.setObjectName(f'SectionNameL{SectionName}')
            SectionNameL.setProperty('class', 'SectionNameL')
            self.DataL.addWidget(SectionNameL, i, 0, 1, 100)
            SectionNameL.setAlignment(Qt.AlignCenter)
            SectionNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            SectionNameL.setText(SectionName)
            i += 1
            for ii, (ItemId, ItemTable) in enumerate(SectionItems.items(), 1):
                cur.execute(f'SELECT icon, ticker, name FROM "{ItemTable}" WHERE id=?;', (int(ItemId),))
                r = cur.fetchone()
                if r:
                    ObjectIndexL = QLabel(self.DataW)
                    ObjectIconL = QLabel(self.DataW)
                    ObjectTickerL = QLabel(self.DataW)
                    ObjectNameB = QPushButton(self.DataW)
                    ObjectIndexL.setObjectName(f'ObjectIndexL{ii}')
                    ObjectIconL.setObjectName(f'ObjectIconL{ii}')
                    ObjectTickerL.setObjectName(f'ObjectTickerL{ii}')
                    ObjectNameB.setObjectName(f'ObjectNameB{ii}')
                    ObjectIndexL.setProperty('class', 'IndexL')
                    ObjectIconL.setProperty('class', 'IconL')
                    ObjectTickerL.setProperty('class', 'TickerL')
                    ObjectNameB.setProperty('class', 'NameB')
                    self.DataL.addWidget(ObjectIndexL, i, 0, 1, 10)
                    self.DataL.addWidget(ObjectIconL, i, 10, 1, 15)
                    self.DataL.addWidget(ObjectTickerL, i, 25, 1, 25)
                    self.DataL.addWidget(ObjectNameB, i, 50, 1, 50)
                    ObjectIndexL.setAlignment(Qt.AlignCenter)
                    ObjectIconL.setAlignment(Qt.AlignCenter)
                    ObjectTickerL.setAlignment(Qt.AlignCenter)
                    ObjectIndexL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    ObjectIconL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    ObjectTickerL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    ObjectNameB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    ObjectIndexL.setText(f'{ii}')
                    #ObjectIconL.setText(r[0])
                    ObjectTickerL.setText(r[1])
                    ObjectNameB.setText(r[2])
                i+= 1
    conn.close()