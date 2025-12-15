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

def notification_ui(self):
    """ Set object name """
    self.setObjectName('notification_widget')
    self.widget.setObjectName('widget')
    self.text_label.setObjectName('text_label')
    self.exit_button.setObjectName('exit_button')
    """ Set property """
    """ Set layout """
    self.background_layout.addWidget(self.widget, 10, 20, 80, 60)
    self.background_layout.setSpacing(0)
    self.background_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.background_layout.setRowStretch(enc, 1)
        self.background_layout.setColumnStretch(enc, 1)
    self.setLayout(self.background_layout)
    self.layout.addWidget(self.text_label, 5, 5, 70, 90)
    self.layout.addWidget(self.exit_button, 80, 40, 10, 20)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.layout.setRowStretch(enc, 1)
        self.layout.setColumnStretch(enc, 1)
    self.widget.setLayout(self.layout)
    """ Set widget """
    self.setHidden(False)
    """ Set label """
    self.text_label.setAlignment(Qt.AlignCenter)
    """ Set size """
    self.setFixedSize(QSize(self.parent_width, self.parent_height//5))
    self.setGeometry(QRect(0, 0, self.width(), self.height()//5))
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def notification_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/notifcation/'+_global_config['theme']+'.css')).read())
#______________________________________________________________________________________________________________________

def notification_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/changelog/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    _i = self.message_index
    self.text_label.setText(_t['text_label'][_l][_i])
    self.exit_button.setText(_t['exit_button'][_l])
