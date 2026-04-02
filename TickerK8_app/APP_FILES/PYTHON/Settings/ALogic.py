import pathlib
import json

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

