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
    QSize
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (QPixmap, # Graphic.
                         QPainter) # Painter.
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
#_______________________________________________________________________________________________________________________
#######################################################################################################################
""" Create list"""
def create_list(self):
    if self.main_mid_object_list_config['__list_type__'] == 'fav':
        main_mid_object_list_favourite(self)
    elif self.main_mid_object_list_config['__list_type__'] == 'hot':
        main_mid_object_list_hot(self)
#######################################################################################################################
""" Main mid object list favourite """
def main_mid_object_list_favourite(self):
    """ Set variables """
    object_list = list(self.main_mid_object_list_config['__favourite_objects__']) # Create object list
#______________________________________________________________________________________________________________________
    """ Check if list widget exists"""
    if self.list_widget:
        self.list_widget.deleteLater()
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.list_widget = QWidget(self.list_scroll)
    self.list_layout = QGridLayout(self.list_widget)
    self.list_tag_index_label = QLabel(self.list_widget)
    self.list_tag_logo_label = QLabel(self.list_widget)
    self.list_tag_name_label = QLabel(self.list_widget) 
#______________________________________________________________________________________________________________________
    """ Set object name"""
    self.list_widget.setObjectName('list_widget')
    self.list_tag_index_label.setObjectName('list_tag_index_label')
    self.list_tag_logo_label.setObjectName('list_tag_logo_label')
    self.list_tag_name_label.setObjectName('list_tag_name_label')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.list_tag_index_label.setProperty('class', 'list_tag')
    self.list_tag_logo_label.setProperty('class', 'list_tag')
    self.list_tag_name_label.setProperty('class', 'list_tag')
#______________________________________________________________________________________________________________________
    """ Set Layout """
    self.list_layout.addWidget(self.list_tag_index_label, 0, 0)
    self.list_layout.addWidget(self.list_tag_logo_label, 0 ,1)
    self.list_layout.addWidget(self.list_tag_name_label, 0, 2)
    self.list_layout.setSpacing(0)
    self.list_layout.setContentsMargins(0,0,0,0)
    self.list_widget.setLayout(self.list_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.list_scroll.setWidget(self.list_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.list_tag_index_label.setAlignment(Qt.AlignCenter)
    self.list_tag_logo_label.setAlignment(Qt.AlignCenter)
    self.list_tag_name_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    _t = self.main_mid_object_list_translate
    _l = self.global_config['__language__']
    self.list_tag_index_label.setText(_t['list_tag_index_label'][_l])
    self.list_tag_logo_label.setText(_t['list_tag_logo_label'][_l])
    self.list_tag_name_label.setText(_t['list_tag_name_label'][_l])
#______________________________________________________________________________________________________________________
    """ Create data """
    connect = sqlite3.connect(self.local_database) # Create connect 
    cursor = connect.cursor() # Create cursor 
    query = f'SELECT id, logo, ticker FROM INDEXES WHERE id IN ({','.join(['?']*len(object_list))});' # Query 
    cursor.execute(query, object_list) # Execute 
    result = cursor.fetchall() # Get result 
    for index, data in enumerate(result, start=1):
        """ Create objects """
        index_label = QLabel(self.list_widget)
        logo_label = QLabel(self.list_widget)
        ticker_button = QPushButton(self.list_widget)
#______________________________________________________________________________________________________________________
        """ Set object name """
        index_label.setObjectName(f'index_label_{index}')
        logo_label.setObjectName(f'logo_label_{index}')
        ticker_button.setObjectName(f'ticker_button_{index}')
#______________________________________________________________________________________________________________________
        """ Set property """
        index_label.setProperty('class', 'indexes')
        logo_label.setProperty('class', 'logos')
        ticker_button.setProperty('class', 'tickers')
#______________________________________________________________________________________________________________________
        """ Set layout """
        self.list_layout.addWidget(index_label, index, 0)
        self.list_layout.addWidget(logo_label, index, 1)
        self.list_layout.addWidget(ticker_button, index, 2) 
#______________________________________________________________________________________________________________________
        """ Set label """
        index_label.setAlignment(Qt.AlignCenter)
        logo_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
        """ Set size """
        index_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        index_label.setFixedHeight(64)
        logo_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  
        logo_label.setFixedHeight(64)
        ticker_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ticker_button.setFixedHeight(64)
#______________________________________________________________________________________________________________________
        """ Set text """
        index_label.setText(f'{index}')
        ticker_button.setText(data[2])
#______________________________________________________________________________________________________________________
        """ Set photo """
        logo_label.setPixmap(QPixmap(load_svg(self.main_path+data[1], 64, 64)))
#______________________________________________________________________________________________________________________
        """ Set connect """
        ticker_button.clicked.connect(lambda _, id=data[0]: set_to_main_mid_object(self, id))
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
def set_to_main_mid_object(self, id):
    _json_load = json.load(open(self.main_path+'/CONFIG/main_mid_object/config.json', 'r'))
    _json_load['__id__'] = id
    json.dump(_json_load, open(self.main_path+'/CONFIG/main_mid_object/config.json', 'w'), indent=4)
    self.config_changed.emit()
#######################################################################################################################
