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
    self.SearchB.setObjectName('SearchB')
    self.SettingsB.setObjectName('SettingsB')
    self.LogoutB.setObjectName('LogoutB')
    self.SettingsB.setProperty('class', 'B')
    self.LogoutB.setProperty('class', 'B')
    self.Layout.addWidget(self.SearchB, 2, 40, 2, 20)
    self.Layout.addWidget(self.SettingsB, 2, 90, 2, 2)
    self.Layout.addWidget(self.LogoutB, 2, 94, 2, 2)
    self.Layout.addWidget(self.MainListObjectW, 10, 2, 80, 30)
    self.Layout.addWidget(self.MainObjectW, 10, 35, 80, 30)
    self.Layout.addWidget(self.MainNewsW, 10, 68, 80, 30)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.Layout.setRowStretch(i, 1)
        self.Layout.setColumnStretch(i, 1)
    self.setLayout(self.Layout)
    self.show()
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.SearchB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.SettingsB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.LogoutB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def MainReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/APP_FILES/PYTHON/main/s_main.css').read()
    c = open(f'{self.Path}/APP_FILES/PYTHON/main/s_{t}.css').read()
    self.setStyleSheet(m+c)
    self.SearchB.setIcon(QIcon(LoadSvg(f'{self.Path}/APP_FILES/PYTHON/main/i_search_{t}.svg', 256, 256)))
    self.SearchB.setIconSize(self.SearchB.size())
    self.SettingsB.setIcon(QIcon(LoadSvg(f'{self.Path}/APP_FILES/PYTHON/main/i_settings_{t}.svg', 256, 256)))
    self.SettingsB.setIconSize(self.SettingsB.size())
    self.LogoutB.setIcon(QIcon(LoadSvg(f'{self.Path}/APP_FILES/PYTHON/main/i_exit_{t}.svg', 256, 256)))
    self.LogoutB.setIconSize(self.LogoutB.size())

def MainRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/main/j_main_translate.json', 'r'))
    l = self.Language
    self.SearchB.setText(t['SearchB'][l])

def LoadSvg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) # Render svg
    pixmap = QPixmap(width, height) # Create pixmap
    pixmap.fill(Qt.transparent) # Transparent
    painter = QPainter(pixmap) # Render graphic 
    renderer.render(painter) # Render graphic
    painter.end() # Render graphic
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation) # Scal pixmap
    return scaled_pixmap