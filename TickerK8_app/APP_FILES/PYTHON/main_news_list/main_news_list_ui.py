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
    Qt, # Qt settings
    QRect
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon # Icon
)
#######################################################################################################################
""" Main news list Ui """
def main_news_list_ui(self):
    """ Set object name """
    self.setObjectName('main_news_list_widget')
    self.panel_widget.setObjectName('panel_widget')
    self.title_label.setObjectName('title_label')
    self.news_list_scroll.setObjectName('news_list_scroll')
    self.exit_button.setObjectName('exit_button')
#______________________________________________________________________________________________________________________
    """ Set property """
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.panel_widget, 2, 20, 96, 60)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
    self.panel_layout.addWidget(self.title_label, 0, 0, 10, 100)
    self.panel_layout.addWidget(self,news_list_scroll, 10, 0, 80, 100)
    self.panel_layout.addWidget(self.exit_button, 95, 40, 2, 20)
    self.panel_layout.setSpacing(0)
    self.panel_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.panel_layout.setRowStretch(enc, 1)
        self.panel_layout.setColumnStretch(enc, 1)
    self.panel_widget.setLayout(self.panel_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
    self.news_list_scroll.setWidgetResizable(True)
    self.news_list_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.title_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set Size """
    self.setGeometry(QRect(0,0,self.parent.width(), self.parent.height()))
    self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    self.title_label.setMaximumWidth(self.panel_widget.width())
    self.title_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.news_list_scroll.setMaximumWidth(self.panel_widget.width())
    self.news_list_scroll.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.exit_button.setMaximumWidth(self.panel_widget.width())
    self.exit_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
#######################################################################################################################
def main_news_list_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main_news_list/'+self.global_config['__theme__']+'.css')).read())
#######################################################################################################################
def main_news_list_retranslate(self):
    _t = self.main_news_translate # Translate texts 
    _l = self.global_config['__language__'] # Language
    _type = self.news_type # News type 
    self.title_label.setText(_t['title_label'][_l][_type])
    self.exit_button.setText(_t['exit_button'][_l])
