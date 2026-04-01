#   --- Import packages ---
import json
#   --- Import PyQt5 packages ---
from PyQt5.QtWidgets import (
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
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

def SettingsUi(self):
    self.setObjectName('SettingsW')
    self.NaviS.setObjectName('NaviS')
    self.NaviW.setObjectName('NaviW')
    self.NaviUserB.setObjectName('NaviUserB')
    self.NaviStyleB.setObjectName('NaviStyleB')
    self.NaviUpdateB.setObjectName('NaviUpdateB')
    self.NaviLanguageB.setObjectName('NaviLanguageB')
    self.NaviExitB.setObjectName('NaviExitB')
    self.NaviUserB.setProperty('class', 'NaviB')
    self.NaviStyleB.setProperty('class', 'NaviB')
    self.NaviSoundB.setProperty('class', 'NaviB')
    self.NaviUpdateB.setProperty('class', 'NaviB')
    self.NaviLanguageB.setProperty('class', 'NaviB')
    self.NaviL.addWidget(self.NaviUserB)
    self.NaviL.addWidget(self.NaviStyleB)
    self.NaviL.addWidget(self.NaviUpdateB)
    self.NaviL.addWidget(self.NaviLanguageB)
    self.NaviL.addWidget(self.NaviExitB)
    self.NaviL.setSpacing(0)
    self.NaviL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.NaviL.setRowStretch(i, 1)
        self.NaviL.setColumnStretch(i, 1)
    self.NaviW.setLayout(self.NaviL)
    self.Layout.addWidget(self.NaviS, 0, 0, 100, 20)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.Layout.setRowStretch(i, 1)
        self.Layout.setColumnStretch(i, 1)
    self.setLayout(self.Layout)
    self.show()
    self.NaviS.setWidgetResizable(True)
    self.NaviS.setWidget(self.NaviW)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviUserB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviUserB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviStyleB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviUserB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviLanguageB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviExitB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def SettingsReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/APP_FILES/PYTHON/Settings/BMain.css').read()
    c = open(f'{self.Path}/APP_FILES/PYTHON/Settings/B{self.Theme}.css').read()
    self.OpenedW.setStyleSheet(m+c)
    self.NaviExitB.setIcon(QIcon(load_svg(f'{self.Path}/APP_FILES/PYTHON/Settings/Exit{t}.svg', 256, 256)))
    self.NaviExitB.setIconSize(self.NaviExitB.size())

def SettingsRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/Settings/CMenuRetranslate.json', 'r'))
    l = self.Language
    self.NaviUserB.setText(_t['NaviUserB'][_l])
    self.NaviStyleB.setText(_t['NaviStyleB'][_l])
    self.NaviSoundB.setText(_t['NaviSoundB'][_l])
    self.NaviUpdateB.setText(_t['NaviUpdateB'][_l])
    self.NaviLanguageB.setText(_t['NaviLanguageB'][_l])
   
def UserUi(self):
    self.PanelS.setObjectName('PanelS')
    self.PanelW.setObjectName('PanelW')
    self.PanelTitleL.setObjectName('PanelTitleL')
    self.UserNameNameL.setObjectName('UserNameNameL')
    self.UserNameValueL.setObjectName('UserNameValueL')
    self.UserEmailNameL.setObjectName('UserEmailNameL')
    self.UserEmailValueL.setObjectName('UserEmailValueL')
    self.UserCreateDateNameL.setObjectName('UserCreateDateNameL')
    self.UserCreateDateValueL.setObjectName('UserCreateDateValueL')
    self.UserNameNameL.setProperty('class', 'Name')
    self.UserEmailNameL.setProperty('class', 'Name')
    self.UserCreateDateNameL.setProperty('class', 'Name')
    self.UserNameValueL.setProperty('class', 'Value')
    self.UserEmailValueL.setProperty('class', 'Value')
    self.UserCreateDateValueL.setProperty('class', 'Value')

    



def UserRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/Settings/CUserPageRetranslate.json', 'r'))
    l = self.Language

def StyleUi(self):
    

def StyleRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/Settings/CStylePageRetranslate.json', 'r'))
    l = self.Language

def UpdateUi(self):

def UpdateRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/Settings/CUpdatePageRetranslate.json', 'r'))
    l = self.Language

def LanguageUi(self):

def LanguageRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/Settings/CLanguagePageRetranslate.json', 'r'))
    l = self.Language




def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path)
    pixmap = QPixmap(width, height)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return scaled_pixmap
