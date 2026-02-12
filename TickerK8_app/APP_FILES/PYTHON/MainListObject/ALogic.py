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
    for ListName, ListElements in o.items():
        self.ListNameL.setText(ListName)
        i = 0
        for SectionName, SectionItems in ListElements.items():
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
                    ObjectIndexL.setObjectName('ObjectIndexL')
                    ObjectIconL.setObjectName('ObjectIconL')
                    ObjectTickerL.setObjectName('ObjectTickerL')
                    ObjectNameB.setObjectName('ObjectNameB')
                    ObjectIndexL.setProperty('class', '')
                    ObjectIconL.setProperty('class', '')
                    ObjectTickerL.setProperty('class', '')
                    ObjectNameB.setProperty('class', '')

                i+= 1
    conn.close()