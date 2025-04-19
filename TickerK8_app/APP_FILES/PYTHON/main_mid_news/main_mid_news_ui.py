""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QPushButton, # Simple button
    QGridLayout, # Grid layout
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt # Qt settings
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon # Icon
)
#######################################################################################################################
""" Main mid news ui """
def main_mid_news_ui(self):
    """ Set object name """
    self.setObjectName('main_mid_news')
    self.next_left_button.setObjectName('next_left_button')
    self.next_right_button.setObjectName('next_right_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.next_left_button.setProperty('class', 'next_buttons')
    self.next_right_button.setProperty('class', 'next_buttons')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.next_left_button, 90, 0, 10, 50)
    self.main_layout.addWidget(self.next_right_button, 90, 50, 10, 50)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Set label """
#______________________________________________________________________________________________________________________
    """ Set size """
    self.next_left_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.next_right_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Main mid news reload style """
def main_mid_news_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main_mid_news/'+self.global_config['__theme__']+'.css')).read())
#######################################################################################################################
""" Main mid news retranslate """
def main_mid_news_retranslate(self):
    _t = self.main_mid_news_translate # Translate texts 
    _l = self.global_config['__language__'] # Language
    self.next_left_button.setText(_t['next_left_button'][_l])
    self.next_right_button.setText(_t['next_right_button'][_l])
#######################################################################################################################
