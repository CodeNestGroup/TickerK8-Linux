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
    # Chart type data
    chart_type = self.global_config['main_mid_object_chart_type']
    # Price data


#######################################################################################################################
""" Open type chart """
def open_type_chart(self):
    """ Setup widget """
    if self.type_chart_background_widget:
        self.type_chart_background_widget.deleteLater()
        self.type_chart_background_widget = None
#______________________________________________________________________________________________________________________
    """ Create obejcts """
    self.type_chart_background_widget = QWidget(self)
    self.type_chart_background_layout = QGridLayout(self.type_chart_background_widget)
    self.type_chart_widget = QWidget(self.type_chart_background_widget)
    self.type_chart_layout = QGridLayout(self.type_chart_widget)
    self.type_chart_scroll = QScrollArea(self.type_chart_widget)
    self.type_chart_scroll_widget = QWidget(self.type_chart_scroll)
    self.type_chart_scroll_layout = QGridLayout(self.type_chart_scroll_widget)
    self.type_chart_line_button = QPushButton(self.type_chart_scroll_widget)
    self.type_chart_candle_button = QPushButton(self.type_chart_scroll_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.type_chart_background_widget.setObjectName('type_chart_background_widget')
    self.type_chart_widget.setObjectName('type_chart_widget')
    self.type_chart_scroll.setObjectName('type_chart_scroll')
    self.type_chart_scroll_widget.setObjectName('type_chart_scroll_widget')
    self.type_chart_line_button.setObjectName('type_chart_line_button')
    self.type_chart_candle_button.setObjectName('type_chart_candle_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.type_chart_line_button.setProperty('class', 'type_chart_button')
    self.type_chart_candle_button.setProperty('class', 'type_chart_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.type_chart_background_layout.addWidget(self.type_chart_widget, 10, 10, 80, 80)
    self.type_chart_background_layout.setSpacing(0)
    self.type_chart_background_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.type_chart_background_layout.setRowStretch(enc, 1)
        self.type_chart_background_layout.setColumnStretch(enc, 1)
    self.type_chart_background_widget.setLayout(self.type_chart_background_layout)
    self.type_chart_layout.addWidget(self.type_chart_scroll, 10, 10, 80, 80)
    self.type_chart_layout.setSpacing(0)
    self.type_chart_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.type_chart_layout.setRowStretch(enc, 1)
        self.type_chart_layout.setColumnStretch(enc, 1)
    self.type_chart_widget.setLayout(self.type_chart_layout)
    self.type_chart_scroll_layout.addWidget(self.type_chart_line_button, 0, 0)
    self.type_chart_scroll_layout.addWidget(self.type_chart_candle_button, 0, 1)
    self.type_chart_scroll_layout.setSpacing(0)
    self.type_chart_scroll_layout.setContentsMargins(0,0,0,0)
    self.type_chart_scroll_widget.setLayout(self.type_chart_scroll_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.type_chart_background_widget.setHidden(False)
    self.type_chart_scroll.setWidgetResizable(True)
    self.type_chart_scroll.setWidget(self.type_chart_scroll_widget)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.type_chart_background_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.type_chart_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.type_chart_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.type_chart_scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.type_chart_line_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.type_chart_candle_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    _t = self.main_translate
    _l = self.global_config['__language__']
    self.type_chart_line_button.setText(_t['type_chart_line_button'][_l])
    self.type_chart_candle_button.setText(_t['type_chart_candle_button'][_l])
#______________________________________________________________________________________________________________________
    """ Connect buttons """
    #self.type_chart_line_button.clicked.connect()
    #self.type_chart_candle_button.clicked.connect()
#######################################################################################################################
""" Open price info """
def open_price_info(self):
    """ Setup widget """
    if self.price_info_widget:
        self.price_info_widget.deleteLater()
        self.price_info_widget = None
#______________________________________________________________________________________________________________________
    """ Create obejcts """
    self.price_info_widget = QWidget(self)
    self.price_info_layout = QGridLayout(self.price_info_widget)
    self.price_h_name_label = QLabel(self.price_info_widget)
    self.price_h_value_label = QLabel(self.price_info_widget)
    self.price_o_name_label = QLabel(self.price_info_widget)
    self.price_o_value_label = QLabel(self.price_info_widget)
    self.price_c_name_label = QLabel(self.price_info_widget)
    self.price_c_value_label = QLabel(self.price_info_widget)
    self.price_l_name_label = QLabel(self.price_info_widget)
    self.price_l_value_label = QLabel(self.price_info_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.price_info_widget.setObjectName('price_info_widget')
    self.price_h_name_label.setObjectName('price_h_name_label')
    self.price_h_value_label.setObjectName('price_h_value_label')
    self.price_o_name_label.setObjectName('price_o_name_label')
    self.price_o_value_label.setObjectName('price_o_value_label')
    self.price_c_name_label.setObjectName('price_c_name_label')
    self.price_c_value_label.setObjectName('price_c_value_label')
    self.price_l_name_label.setObjectName('price_l_name_label')
    self.price_l_value_label.setObjectName('price_l_value_label')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.price_h_name_label.setProperty('class', 'price_name_label')
    self.price_h_value_label.setProperty('class', 'price_value_label')
    self.price_o_name_label.setProperty('class', 'price_name_label')
    self.price_o_value_label.setProperty('class', 'price_value_label')
    self.price_c_name_label.setProperty('class', 'price_name_label')
    self.price_c_value_label.setProperty('class', 'price_value_label')
    self.price_l_name_label.setProperty('class', 'price_name_label')
    self.price_l_value_label.setProperty('class', 'price_value_label')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.price_info_layout.addWidget(self.price_h_name_label, 0, 0)
    self.price_info_layout.addWidget(self.price_h_value_label, 0, 1)
    self.price_info_layout.addWidget(self.price_o_name_label, 1, 0)
    self.price_info_layout.addWidget(self.price_o_value_label, 1, 1)
    self.price_info_layout.addWidget(self.price_c_name_label, 2, 0)
    self.price_info_layout.addWidget(self.price_c_value_label, 2, 1)
    self.price_info_layout.addWidget(self.price_l_name_label, 3, 0)
    self.price_info_layout.addWidget(self.price_l_value_label, 3, 1)
    self.price_info_layout.setSpacing(0)
    self.price_info_layout.setContentsMargins(0,0,0,0)
    self.price_info_widget.setLayout(self.price_info_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.price_info_widget.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.price_info_widget.setGeometry(QRect())
    self.price_h_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.price_h_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.price_o_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.price_o_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.price_c_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.price_c_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.price_l_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.price_l_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    _t = self.main_translate
    _l = self.global_config['__language__']
    self.price_h_name_label.setText(_t['price_h_name_label'][_l])
    self.price_h_value_label.setText('')
    self.price_o_name_label.setText(_t['price_o_name_label'][_l])
    self.price_o_value_label.setText('')
    self.price_c_name_label.setText(_t['price_c_name_label'][_l])
    self.price_c_value_label.setText('')
    self.price_l_name_label.setText(_t['price_l_name_label'][_l])
    self.price_l_value_label.setText('')
#######################################################################################################################
