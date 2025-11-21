""" Import packages """
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QSizePolicy
)
#______________________________________________________________________________________________________________________

def report_ui(self):
    """ Set object name """
    self.setObjectName('report_widget')
    self.textfield_textarea.setObjectName('textfield_textarea')
    self.send_button.setObjectName('send_button')
    self.clear_button.setObjectName('clear_button')
    self.exit_button.setObjectName('exit_button')
    """ Set property """
    self.send_button.setProperty('class', 'buttons')
    self.clear_button.setProperty('class', 'buttons')
    self.exit_button.setProperty('class', 'buttons')
    """ Set layout """
    self.layout.addWidget(self.textfield_textarea, 10, 10, 80, 80)
    self.layout.addWidget(self.send_button, 94, 10, 2, 22)
    self.layout.addWidget(self.clear_button, 94, 39, 2, 22)
    self.layout.addWidget(self.exit_button, 94, 68, 2, 22)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.layout
        self.layout
    self.setLayout(self.layout)
    """ Set widget """
    self.setHidden(False)
    """ Set label """
    """ Set button """
    self.send_button.setDisabled(True)
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.textfield_textarea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.send_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.clear_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def report_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/report/'+_global_config['theme']+'.css')).read())
#______________________________________________________________________________________________________________________

def report_retranslate(self):
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    _t = json.load(open(self.main_path+'/CONFIG/report/translate.json', 'r'))
    self.send_button.setText(_t['send_button'][_l])
    self.clear_button.setText(_t['clear_button'][_l])
    self.exit_button.setText(_t['exit_button'][_l])
#______________________________________________________________________________________________________________________

