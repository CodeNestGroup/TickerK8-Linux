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
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.Layout.setRowStretch(i, 1)
        self.Layout.setColumnStretch(i, 1)
    self.setLayout(self.Layout)
    self.setHidden(False)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.SearchB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.SettingsB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.LogoutB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def main_reload_style(self):
    t = self.theme
    m = open('./s_main.css').read()
    c = open(f'./s_{t}.css').read()
    self.setStyleSheet(m+c)
    self.SearchB.setIcon(QIcon(load_svg(f'./search_{t}.svg', 256, 256)))
    self.SearchB.setIconSize(self.search_button.size())
    self.SettingsB.setIcon(QIcon(load_svg(f'./settings_{t}.svg', 256, 256)))
    self.SettingsB.setIconSize(self.settings_button.size())
    self.LogoutB.setIcon(QIcon(load_svg(f'./exit_{t}.svg', 256, 256)))
    self.LogoutB.setIconSize(self.logout_button.size())

def main_retranslate(self):
    t = json.load(open('./j_main_translate.json', 'r'))
    l = self.language
    self.SearchB.setText(t['SearchB'][l])
