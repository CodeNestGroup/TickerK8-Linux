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

def MainUi(self):
    self.setObjectName('MainW')
    self.NavW.setObjectName('NavW')
    self.NavDefaultB.setObjectName('NavDefaultB')
    self.NavSearchB.setObjectName('NavSearchB')
    self.NavListObjectB.setObjectName('NavListObjectB')
    self.NavObjectB.setObjectName('NavObjectB')
    self.NavNewsB.setObjectName('NavNewsB')
    self.NavSettingsB.setObjectName('NavSettingsB')
    self.NavLogoutB.setObjectName('NavLogoutB')
    self.FooterW.setObjectName('FooterW')
    self.NavDefaultB.setProperty('class', 'NavButton')
    self.NavSearchB.setProperty('class', 'NavButton')
    self.NavListObjectB.setProperty('class', 'NavButton')
    self.NavObjectB.setProperty('class', 'NavButton')
    self.NavNewsB.setProperty('class', 'NavButton')
    self.NavSettingsB.setProperty('class', 'FuncButton')
    self.NavLogoutB.setProperty('class', 'FuncButton')
    self.Layout.addWidget(self.NavW, 0, 0, 10, 100)
    self.Layout.addWidget(self.FooterW, 90, 0, 10, 100)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.Layout.setRowStretch(i, 1)
        self.Layout.setColumnStretch(i, 1)
    self.setLayout(self.Layout)
    self.NavL.addWidget(self.NavDefaultB, 10, 10, 80, 10)
    self.NavL.addWidget(self.NavSearchB, 10, 25, 80, 10)
    self.NavL.addWidget(self.NavListObjectB, 10, 40, 80, 10)
    self.NavL.addWidget(self.NavObjectB, 10, 55, 80, 10)
    self.NavL.addWidget(self.NavNewsB, 10, 70, 80, 10)
    self.NavL.addWidget(self.NavSettingsB, 10, 85, 80, 5)
    self.NavL.addWidget(self.NavLogoutB, 10, 95, 80, 5)
    self.NavL.setSpacing(0)
    self.NavL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.NavL.setRowStretch(i, 1)
        self.NavL.setColumnStretch(i, 1)
    self.NavW.setLayout(self.NavL)
    self.show()
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavDefaultB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavSearchB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavListObjectB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavObjectB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavNewsB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavSettingsB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavLogoutB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.FooterW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def MainReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/APP_FILES/PYTHON/main/s_main.css').read()
    c = open(f'{self.Path}/APP_FILES/PYTHON/main/s_{t}.css').read()
    self.setStyleSheet(m+c)
    self.SearchB.setIcon(QIcon(LoadSvg(f'{self.Path}/APP_FILES/PYTHON/Main/i_search_{t}.svg', 256, 256)))
    self.SearchB.setIconSize(self.SearchB.size())
    self.SettingsB.setIcon(QIcon(LoadSvg(f'{self.Path}/APP_FILES/PYTHON/Main/i_settings_{t}.svg', 256, 256)))
    self.SettingsB.setIconSize(self.SettingsB.size())
    self.LogoutB.setIcon(QIcon(LoadSvg(f'{self.Path}/APP_FILES/PYTHON/Main/i_exit_{t}.svg', 256, 256)))
    self.LogoutB.setIconSize(self.LogoutB.size())

def MainRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/Main/CMainTranslate.json', 'r'))
    l = self.Language
    self.NavDefaultB.setText(t['NavDefaultB'][l])
    self.NavSearchB.setText(t['NavSearchB'][l])
    self.NavListObjectB.setText(t['NavListObjectB'][l])
    self.NavObjectB.setText(t['NavObjectB'][l])
    self.NavNewsB.setText(t['NavNewsB'][l])

def DefaultPageUi(self):
    self.Layout

def LoadSvg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) # Render svg
    pixmap = QPixmap(width, height) # Create pixmap
    pixmap.fill(Qt.transparent) # Transparent
    painter = QPainter(pixmap) # Render graphic 
    renderer.render(painter) # Render graphic
    painter.end() # Render graphic
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation) # Scal pixmap
    return scaled_pixmap