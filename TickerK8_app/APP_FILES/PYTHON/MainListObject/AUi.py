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

def MainListObjectUi(self):
    self.setObjectName('MainListObjectW')
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.Layout.setRowStretch(i, 1)
        self.Layout.setColumnStretch(i, 1)
    self.show()
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def MainListObjectReloadStyle(self):
    m = open(f'{self.Path}/APP_FILES/PYTHON/MainListObject/BMain.css').read()
    c = open(f'{self.Path}/APP_FILES/PYTHON/MainListObject/B{self.Theme}.css').read()
    self.setStyleSheet(m+c)
    
def Reset(self):
    l = [self.NullDataL, self.ListNameL, self.DataS, self.ListB]
    for o in l:
        if o:
            o.deleteLater()
            o = None

def NullDataUi(self):
    #Reset(self)
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
    #Reset(self)
    self.ListNameL.setObjectName('ListNameL')
    self.DataS.setObjectName('DataS')
    self.DataW.setObjectName('DataW')
    self.ListB.setObjectName('ListB')
    self.Layout.addWidget(self.ListNameL, 0, 0, 5, 100)
    self.Layout.addWidget(self.DataS, 7, 2, 83, 96)
    self.Layout.addWidget(self.ListB, 92, 20, 6, 60)
    self.DataL.setSpacing(0)
    self.DataL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.DataL.setColumnStretch(i, 1)
    self.DataW.setLayout(self.DataL)
    self.DataS.setWidgetResizable(True)
    self.DataS.setWidget(self.DataW)
    self.ListNameL.setAlignment(Qt.AlignCenter)
    self.DataS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.DataW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ListB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    
def DataRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/MainListObject/CDataRetranslate.json', 'r'))
    l = self.Language
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