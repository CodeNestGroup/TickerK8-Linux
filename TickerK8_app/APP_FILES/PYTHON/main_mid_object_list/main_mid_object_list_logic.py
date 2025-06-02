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
#_______________________________________________________________________________________________________________________
#######################################################################################################################
""" Create list """
def create_list(self):
    pass
#######################################################################################################################
""" Show lists """
def show_lists(self):
    """ Setup widget """
    if self.lists_background_widget:
        self.lists_background_widget.deleteLater()
        self.lists_background_widget = None 
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.lists_background_widget = QWidget(self)
    self.lists_background_layout = QGridLayout(self.lists_background_widget)
    self.lists_widget = QWidget(self.lists_background_widget)
    self.lists_layout = QGridLayout(self.lists_widget)
    self.lists_title_label = QLabel(self.lists_widget)
    self.lists_exit_button = QPushButton(self.lists_widget)
    self.lists_scroll = QScrollArea(self.lists_widget)
    self.lists_scroll_widget = QWidget(self.lists_scroll)
    self.lists_scroll_layout = QVBoxLayout(self.lists_scroll_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.lists_background_widget.setObjectName('lists_background_widget')
    self.lists_widget.setObjectName('lists_widget')
    self.lists_title_label.setObjectName('lists_title_label')
    self.lists_exit_button.setObjectName('lists_exit_button')
    self.lists_scroll.setObjectName('lists_scroll')
    self.lists_scroll_widget.setObjectName('lists_scroll_widget')
#______________________________________________________________________________________________________________________
    """ Set property """
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.lists_background_layout.addWidget(self.lists_widget, 20, 20, 60, 60)
    self.lists_background_layout.setSpacing(0)
    self.lists_background_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.lists_background_layout.setRowStretch(enc, 1)
        self.lists_background_layout.setColumnStretch(enc, 1)
    self.lists_background_widget.setLayout(self.lists_background_layout)
    self.lists_layout.addWidget(self.lists_title_label, 2, 20, 8, 60)
    self.lists_layout.addWidget(self.lists_exit_button, 2, 5, 6, 5)
    self.lists_layout.addWidget(self.lists_scroll, 15, 10, 80, 80)
    self.lists_layout.setSpacing(0)
    self.lists_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.lists_layout.setRowStretch(enc, 1)
        self.lists_layout.setColumnStretch(enc, 1)
    self.lists_widget.setLayout(self.lists_layout)
    self.lists_scroll_layout.setSpacing(0)
    self.lists_scroll_layout.setContentsMargins(0,0,0,0)
    self.lists_scroll_widget.setLayout(self.lists_scroll_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.lists_background_widget.setHidden(False)
    self.lists_scroll.setWidgetResizable(True)
    self.lists_scroll.setWidget(self.lists_scroll_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.lists_title_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.lists_background_widget.setGeometry(QRect(0,0,self.width(),self.height()))
    self.lists_background_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.lists_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.lists_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.lists_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.lists_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.lists_scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    _t = self.main_mid_object_list_translate # Translate texts
    _l = self.global_config['__language__'] # Language
    self.lists_title_label.setText(_t['lists_title_label'][_l])
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.lists_exit_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/exit_'+self.global_config['__theme__']+'.svg', 256, 256)))
#______________________________________________________________________________________________________________________
    """ Connect """
    self.lists_exit_button.clicked.connect(lambda: lists_exit(self))
#______________________________________________________________________________________________________________________
    """ Add lists items """
    for keys, value in self.global_config['mid_object_list'].items():
        button = QPushButton(self.lists_scroll_widget)
        button.setObjectName(f'lists_scroll_{keys}_button')
        button.setProperty('class', 'lists_scroll_button')
        self.lists_scroll_layout.addWidget(button)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setText(f'{keys}')
        #button.clicked.connect(open_list)
#######################################################################################################################
""" Load svg script """
def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) # Render svg
    pixmap = QPixmap(width, height) # Create pixmap
    pixmap.fill(Qt.transparent) # Transparent
    painter = QPainter(pixmap) # Render graphic 
    renderer.render(painter) # Render graphic
    painter.end() # Render graphic
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation) # Scal pixmap
    return scaled_pixmap
#######################################################################################################################
""" Set object id """
def set_to_main_mid_object(self, object_list):
    _json_load = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    _json_load['mid_object'] = object_list
    json.dump(_json_load, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    self.config_changed.emit()
#######################################################################################################################
""" Lists exit """
def lists_exit(self):
    self.lists_background_widget.deleteLater()
    self.lists_background_widget = None 

#######################################################################################################################
