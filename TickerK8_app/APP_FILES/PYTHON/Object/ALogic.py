#   --- Import ---\
import sqlite3
from PyQt5.QtCore import (
    QTimer
)
def Setup(self):
#       --- Sort object list ---
    for ListName, ListItems in self.ObjectList.items():
        for SectionName, SectionItems in ListItems.items():
            for ObjectId, ObjectType in SectionItems.items():
                if ObjectType=="stock" or ObjectType=="market":
                    self.ObjectListSorted.append({ObjectId: ObjectType})
#       --- Set timer ---
    Update(self)
    if self.Timer:
        self.Timer.stop()
        self.Timer.deleteLater()
        self.Timer = None
    self.Timer = QTimer(self)
    self.Timer.timeout.connect(lambda: Update(self))
    self.Timer.start(5000)

def Update(self):
#   --- Database ---
    self.ObjectListSortedIndex = (self.ObjectListSortedIndex+1)%len(self.ObjectListSorted)
    d = self.ObjectListSorted[self.ObjectListSortedIndex]
    i = list(d.keys())[0]
    t = d[i]
    conn = sqlite3.connect(f'{self.Path}/APP_FILES/CONFIG/GLOBAL/tickerk8_offline.db')
    cur = conn.cursor()
    cur.execute(f'SELECT icon, ticker, name FROM "{t}" WHERE id=?;', (int(i),))
    r = cur.fetchone()
    conn.close()
    
    #self.IconL.setPixmap(QPixmap(r[0]))
    self.TickerL.setText(r[1])
    self.InfoNameValueL.setText(r[2])
    self.InfoTickerValueL.setText(r[1])
