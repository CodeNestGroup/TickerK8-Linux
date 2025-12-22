""" Import packages """
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
    QRectF,
    QSize
)
from PyQt5.QtGui import (
    QIcon,
    QPixmap,
    QPainter
)
from PyQt5.QtSvg import (
    QSvgRenderer
)
#______________________________________________________________________________________________________________________

def main_ui(self):
    """ Set object name """
    self.setObjectName('main_widget')
    self.settings_button.setObjectName('settings_button')
    self.instagram_button.setObjectName('instagram_button')
    self.github_button.setObjectName('github_button')
    self.discord_button.setObjectName('discord_button')
    self.info_label.setObjectName('info_label')
    """ Set property """
    self.settings_button.setProperty('class', 'button')
    self.instagram_button.setProperty('class', 'button')
    self.github_button.setProperty('class', 'button')
    self.discord_button.setProperty('class', 'button')
    """ Set layout """
    self.layout.addWidget(self.changelog_widget, 0, 0, 100, 50)
    self.layout.addWidget(self.settings_button, 30, 51, 25, 23)
    self.layout.addWidget(self.instagram_button, 30, 75, 25, 23)
    self.layout.addWidget(self.github_button, 56, 51, 25, 23)
    self.layout.addWidget(self.discord_button, 56, 75, 25, 23)
    self.layout.addWidget(self.info_label, 90, 51, 10, 49)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.layout.setRowStretch(enc, 1)
        self.layout.setColumnStretch(enc, 1)
    self.setLayout(self.layout)
    """ Set widget """
    self.setHidden(False)
    """ Set label """
    self.info_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.instagram_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.github_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.discord_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.info_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def main_reload_style(self):
    t = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['theme']
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main/'+t+'.css')).read())
    self.settings_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/settings_'+t+'.svg'), 256, 256)))
    self.settings_button.setIconSize(self.settings_button.size())
    self.instagram_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/instagram_'+t+'.svg'), 256, 256)))
    self.instagram_button.setIconSize(self.instagram_button.size())
    self.github_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/github_'+t+'.svg'), 256, 256)))
    self.github_button.setIconSize(self.github_button.size())
    self.discord_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/discord_'+t+'.svg'), 256, 256)))
    self.discord_button.setIconSize(self.discord_button.size())
#______________________________________________________________________________________________________________________

def main_retranslate(self):
    t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r'))
    l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.info_label.setText(t['info_label'][0][l])
#______________________________________________________________________________________________________________________

def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) 
    pixmap = QPixmap(width, height) 
    pixmap.fill(Qt.transparent) 
    painter = QPainter(pixmap) 
    renderer.render(painter)
    painter.end()
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return scaled_pixmap
#______________________________________________________________________________________________________________________
