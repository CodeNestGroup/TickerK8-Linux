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

def Ui(self):
    self.setObjectName('MainListObject')
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.Layout.setRowStretch(i, 1)
        self.Layout.setColumnStretch(i, 1)
    self.setLayout(self.Layout)
    self.show()
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def ReloadStyle(self):
    m = open(f'{self.Path}/APP_FILES/PYTHON/MainListObject/BMain.css').read()
    c = open(f'{self.Path}/APP_FILES/PYTHON/MainListObject/B{self.Theme}.css').read()
    self.setStyleSheet(m+c)
    
def Reset(self):
    l = [self.NullDataL, self.DataS, self.EditB, self.ListB]
    for o in l:
        if o:
            o.deleteLater()
            o = None

def NullDataUi(self):
    Reset(self)
    self.NullDataL.setObjectName('NullDataL')
    self.Layout.addWidget(self.NullDataL, 0, 0, 100, 100)
    self.NullDataL.show()
    self.NullDataL.setAlignment(Qt.AlignCenter)
    self.NullDataL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def NullDataRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/MainListObject/CNullDataRetranslate.json', 'r'))
    l = self.Language
    self.NullDataL.setText(t['NullDataL'][l])

def DataUi(self):
    Reset(self)
    self.DataS.setObjectName('DataS')
    self.DataW.setObjectName('DataW')
    self.EditB.setObjectName('EditB')
    self.ListB.setObjectName('ListB')
    self.EditB.setProperty('class', 'DataButton')
    self.ListB.setProperty('class', 'DataButton')
    self.Layout.addWidget(self.DataS, 0, 0, 90, 100)
    self.Layout.addWidget(self.EditB, 90, 10, 10, 30)
    self.Layout.addWidget(self.ListB, 90, 60, 10, 30)
    self.DataL.setSpacing(0)
    self.DataL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.DataL.setColumnStretch(i, 1)
    self.DataW.setLayout(self.DataL)
    self.DataS.setWidgetResizable(True)
    self.DataS.setWidget(self.DataW)
    self.DataS.show()
    self.DataW.show()
    self.EditB.show()
    self.ListB.show()
    self.DataS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.DataW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.EditB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ListB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def DataRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/MainListObject/CDataRetranslate.json', 'r'))
    l = self.Language
    self.EditB.setText(t['EditB'][l])
    self.ListB.setText(t['ListB'][l])


def LoadSvg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) # Render svg
    pixmap = QPixmap(width, height) # Create pixmap
    pixmap.fill(Qt.transparent) # Transparent
    painter = QPainter(pixmap) # Render graphic 
    renderer.render(painter) # Render graphic
    painter.end() # Render graphic
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation) # Scal pixmap
    return scaled_pixmap