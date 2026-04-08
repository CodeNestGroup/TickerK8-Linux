import pathlib
import json
import datetime

from PyQt5.QtWidgets import (
    QLabel,
    QSizePolicy
)

def UpdatePageSetup(self):
    p = str(pathlib.Path(__file__).resolve().parents[4])
    u = json.load(open(p+'/updater/CONFIG/GLOBAL/changelog.json', 'r'))
#       --- Description ---
    self.UpdateDescriptionValueL.setText(u['name'])
#       --- Body ---
    ChangelogL = QLabel(self.UpdateChangelogValueW)
    ChangelogL.setObjectName('ChangelogL')
    self.UpdateChangelogValueL.addWidget(ChangelogL,0,0)
    ChangelogL.setWordWrap(True)
    ChangelogL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    ChangelogL.setText(u['body'])

def UserPageSetup(self):
    d = self.GetUserData(self.LoggedUserId)[0]
    self.UserNameValueL.setText(d[0])
    self.UserEmailValueL.setText(d[1])
    self.UserPhoneValueL.setText(f'{d[2]} {d[3]}')
    self.UserCountryValueL.setText(d[4])
    self.UserCreateDateValueL.setText(f'{d[5].strftime("%Y-%m-%d %H:%M:%S")}')

def StylePageSetup(self):

    self.

    self.StyleThemeThemesValueC.addItems("vintage_elegance_light", "vintage_elegance_dark")
    self.StyleThemeThemesValueC.setCurrent
    self.StyleThemeDayNightValueB.setText()

def SoundPageSetup(self):
    self.SoundValueB.setText()

def LanguagePageSetup(self):
    self.LanguageValueC.setCurrentIndex()


