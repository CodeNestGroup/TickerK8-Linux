""" Import packages """
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
)
#______________________________________________________________________________________________________________________

def update_ui(self):
    """ Set obecjt name """
    self.setObjectName('update_widget')
    """ Set propoerty """
    """ Set layout """
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    self.setLayout(self.layout)
    """ Set widget """
    self.setHidden(False)
    """ Set label """
    """ Set button """
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def update_reload_style(self):
    g = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main_update/'+g['theme']+'.css')).read())

def updated_ui(self):
    """ Set object name """
    self.label.setObjectName('label')
    self.dots_label.setObjectName('dots_label')
    """ Set property """
    """ Set layout """
    self.layout.addWidget(self.label,0,0)
    self.layout.addWidget(self.dots_label,0,1)
    """ Set widget """
    """ Set label """
    self.label.setAlignment(Qt.AlignRight)
    self.dots_label.setAlignment(Qt.AlignLeft)
    """ Set button """
    """ Set size """
    self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.dots_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def updated_retranslate(self):
    t = json.load(open(self.main_path+'/CONFIG/main_update/updated_translate.json', 'r'))
    l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.label.setText(t['label'][l][0])

def updating_ui(self):
    """ Set object name """
    self.progressbar.setObjectName('progressbar')
    self.label.setObjectName('label')
    """ Set property """
    """ Set layout """
    self.layout.addWidget(self.progressbar)
    """ Set widget """
    """ Set label """
    self.label.setAlignment(Qt.AlignLeft)
    """ Set button """
    """ Set size """
    self.progressbar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def updating_retranslate(self):
    t = json.load(open(self.main_path+'/CONFIG/main_update/updating_translate.json', 'r'))
    l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.label.setText(t['label'][0][l])
#______________________________________________________________________________________________________________________
