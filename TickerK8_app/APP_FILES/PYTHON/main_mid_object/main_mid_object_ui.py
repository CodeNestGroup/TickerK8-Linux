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
""" Main mid object Ui """
def main_mid_object_ui(self):
    """ Set object name """
    self.setObjectName('main_mid_object_widget')
    self.icon_label.setObjectName('icon_label')
    self.ticker_label.setObjectName('ticker_label')
    self.name_label.setObjectName('name_label')
#_______________________________________________________________________________________________________________________
    """ Set property """
#_______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.icon_label, 0, 0, 1, 100)
    self.main_layout.addWidget(self.ticker_label, 1, 0, 1, 100)
    self.main_layout.addWidget(self.name_label, 2, 0, 1, 100)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
#______________________________________________________________________________________________________________________

    """ Set label """
    self.icon_label.setAlignment(Qt.AlignCenter)
    self.ticker_label.setAlignment(Qt.AlignCenter)
    self.name_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.icon_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ticker_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
########################################################################################################################
def main_mid_object_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main_mid_object/'+self.global_config['__theme__']+'.css')).read())
#######################################################################################################################
