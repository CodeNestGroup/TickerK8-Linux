#   --- Import packages ---
import json
#   --- Import PyQt5 packages ---
from PySide2.QtWidgets import (
    QLabel,
    QSizePolicy
)
from PySide2.QtCore import (
    Qt,
    QRectF,
    QSize
)
from PySide2.QtGui import (
    QIcon,
    QPixmap,
    QPainter
)
from PySide2.QtSvg import (
    QSvgRenderer
)

def UpdateUi(self):
    self.setObjectName('UpdateW')
    self.SettingsB.setObjectName('SettingsB')
    self.InstagramB.setObjectName('InstagramB')
    self.GithubB.setObjectName('GithubB')
    self.DiscordB.setObjectName('DiscordB')
    self.SettingsB.setProperty('class', 'Button')
    self.InstagramB.setProperty('class', 'Button')
    self.GithubB.setProperty('class', 'Button')
    self.DiscordB.setProperty('class', 'Button')
    self.Layout.addWidget(self.SettingsB, 30, 51, 25, 23)
    self.Layout.addWidget(self.InstagramB, 30, 75, 25, 23)
    self.Layout.addWidget(self.GithubB, 56, 51, 25, 23)
    self.Layout.addWidget(self.DiscordB, 56, 75, 25, 23)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.Layout.setRowStretch(enc, 1)
        self.Layout.setColumnStretch(enc, 1)
    self.setLayout(self.Layout)
    self.show()
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.SettingsB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.InstagramB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.GithubB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.DiscordB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def UpadateReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/assets/CSS/UpdateMain.css').read()
    c = open(f'{self.Path}/assets/CSS/Update{t}.css').read()
    self.setStyleSheet(m+c)
    self.SettingsB.setIcon(QIcon(load_svg(f'{self.Path}/assets/ICON/Settings{t}.svg', 256, 256)))
    self.SettingsB.setIconSize(self.SettingsB.size())
    self.InstagramB.setIcon(QIcon(load_svg(f'{self.Pat}/assets/ICON/Instagram{t}.svg', 256, 256)))
    self.InstagramB.setIconSize(self.InstagramB.size())
    self.GithubB.setIcon(QIcon(load_svg(f'{self.Path}/assets/ICON/Github{t}.svg', 256, 256)))
    self.GithubB.setIconSize(self.GithubB.size())
    self.DiscordB.setIcon(QIcon(load_svg(f'{self.Path}/assets/ICON/Discord{t}.svg', 256, 256)))
    self.DiscordB.setIconSize(self.DiscordB.size())

def ChangelogNoConnectionUi(self):

def ChangelogNoConnectionRetranslate(self):

def ChangelogLoadingUi(self):

def ChangelogLoadingRetranslate(self):

def ChangelogConnctionUi(self):

def ChangelogConnctionRetranslate(self):

def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) 
    pixmap = QPixmap(width, height) 
    pixmap.fill(Qt.transparent) 
    painter = QPainter(pixmap) 
    renderer.render(painter)
    painter.end()
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return scaled_pixmap
