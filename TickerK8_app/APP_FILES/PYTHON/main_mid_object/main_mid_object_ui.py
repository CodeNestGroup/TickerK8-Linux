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
    self.setObjectName('main_mid_object')
    self.icon_label.setObjectName('icon_label')
    self.ticker_label.setObjectName('ticker_label')
    self.name_label.setObjectName('name_label')
    self.chart_button.setObjectName('chart_button')
    self.statistics_button.setObjectName('statistics_button')
#_______________________________________________________________________________________________________________________
    """ Set property """
    self.chart_button.setProperty('class', 'control_buttons')
    self.statistics_button.setProperty('class', 'control_buttons')
#_______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.icon_label, 0, 0, 1, 100)
    self.main_layout.addWidget(self.ticker_label, 1, 0, 1, 100)
    self.main_layout.addWidget(self.name_label, 2, 0, 1, 100)
    self.main_layout.addWidget(self.chart_button, 3, 0, 1, 50)
    self.main_layout.addWidget(self.statistics_button, 3, 50, 1, 50)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.icon_label.setSizePolicy(QSizeQSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ticker_label.setSizePolicy(QSizeQSizePolicy.Expanding, QSizePolicy.Expanding)
    self.name_label.setSizePolicy(QSizeQSizePolicy.Expanding, QSizePolicy.Expanding)
    self.chart_button.setSizePolicy(QSizeQSizePolicy.Expanding, QSizePolicy.Expanding)
    self.statistics_button.setSizePolicy(QSizeQSizePolicy.Expanding, QSizePolicy.Expanding)
########################################################################################################################
def main_mid_object_reload_style(self):
    self.setStyleSheet(open(self.main_path+'/STYLE/CSS/main_mid_object.css', 'r'))
#######################################################################################################################
