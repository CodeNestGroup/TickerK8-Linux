""" Import msyql """
import sqlite3
import json
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QScrollArea, # Simple scroll widget
    QLabel, # Simple label
    QPushButton, # Simple button
    QComboBox, # Drop down list
    QGridLayout, # Grid layout
    QSizePolicy, # Size policy
    QVBoxLayout # Vertical layout 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 QtCore """
from PyQt5.QtCore import (
    Qt,
    QSize,
    QRect
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (QPixmap, # Graphic.
                         QIcon, # Icon 
                         QPainter) # Painter.
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
#######################################################################################################################
""" Main mid object chart create chart """
def main_mid_object_chart_create_chart(self):
    """ Set config """
    if self.chart_widget:
        self.chart_widget.deleteLater()
        self.chart_widget = None 
#______________________________________________________________________________________________________________________
    """ Create obejcts """
    self.chart_widget = QWidget(self)
    self.chart_layout = QGridLayout(self.chart_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.chart_widget.setObjectName('chart_widget')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.chart_layout.setSpacing(0)
    self.chart_layout.setContentsMargins(0,0,0,0)
    self.chart_widget.setLayout(self.chart_layout)
    self.main_layout.addWidget(self.chart_widget, 0, 0, 90, 100)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.chart_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set chart """
#######################################################################################################################
""" Open type chart """
def open_type_chart(self):
    pass
#######################################################################################################################
""" Open price info """
def open_price_info(self):
    """ Setup widget """
    if self.price_info_widget:
        self.price_info_widget.deleteLater()
        self.price_info_widget = None
    

