#   --- Improt ---
import json
from PyQt5.QtWidgets import (
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
    QSize
)

def NewsListUi(self):
    self.setObjectName('NewsListW')
    self.ListS.setObjectName('ListS')
    self.ListW.setObjectName('ListW')
    self.ReloadB.setObjectName('ReloadB')
    self.Layout.addWidget(self.ListS, 0, 0, 80, 100)
    self.Layout.addWidget(self.ReloadB, 90, 0, 5, 100)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.Layout.setRowStretch(i, 1)
        self.Layout.setColumnStretch(i, 1)
    self.setLayout(self.Layout)
    self.ListL.setSpacing(0)
    self.ListL.setContentsMargins(0,0,0,0)
    self.ListW.setLayout(self.ListL)
    self.ListS.setWidgetResizable(True)
    self.ListS.setWidget(self.DataW)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ListS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ListW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ReloadB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def NewsListReloadStyle(self):
    m = open(f'{self.Path}/APP_FILES/PYTHON/NewsList/BNewsList.css').read()
    c = open(f'{self.Path}/APP_FILES/PYTHON/NewsList/BNewsList{self.Theme}.css').read()
    self.setStyleSheet(m+c)

def NewsListRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/NewsList/CNewsListRetranslate.json', 'r'))
    l = self.Language
    self.ReloadB.setText(t['ReloadB'][l])
    