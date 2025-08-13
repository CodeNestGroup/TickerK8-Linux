import json
import sqlite3
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QScrollArea, # Scroll 
    QLabel, # Simple label
    QPushButton, # Simple button
    QGridLayout, # Grid layout
    QVBoxLayout, # Vertical layout 
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt, # Qt settings
    QSize
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon, # Icon
    QPixmap,
    QPainter
)
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
#######################################################################################################################

def load_history(self):
    pass
#######################################################################################################################
def text_changed(self):
    _text = self.panel_search_lineedit.text() # Get searching text
    _active_filters = self.global_config['main_search_filters'] # Get filters 
#______________________________________________________________________________________________________________________
    """ Get data """
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
    cursor = database.cursor() # Create cursor
    all_data = []
    if _active_filters[0]:
        if _text != '':
            where = f'WHERE stock.name like "%{_text}%"'
        else:
            where = ''
        database_data = cursor.execute(f'''
            SELECT stock.icon, stock.name, market.icon, market.name FROM stock JOIN market ON stock.id_market=market.id {where};
        ''').fetchall()
        if database_data:
            for e in database_data: all_data.append(e)
    if _active_filters[1]:
        all_data.append(cursor.execute(f'''
            SELECT logo, name, logo, name FROM etf WHERE name like "%{_text}%";
        ''').fetchall()[0])
        all_data.append(database_data)
    if _active_filters[2]:
        all_data.append(cursor.execute(f'''
            SELECT logo, name, logo, name FROM WHERE name like "%{_text}%";
        ''').fetchall()[0])
        all_data.append(database_data)
    if _active_filters[3]:
        if _text != '':
            where = f'WHERE market_index.name like "%{_text}%"'
        else:
            where = ''
        database_data = cursor.execute(f'''
            SELECT market_index.icon, market_index.name, market.icon, market.name FROM market_index JOIN market ON market_index.id_market=market.id {where};
        ''').fetchall()
        if database_data:
            for e in database_data: all_data.append(e)
    if _active_filters[4]: 
        if _text != '':
            where = f'WHERE name like "%{_text}%"'
        else:
            where = ''
        database_data = cursor.execute(f'''
            SELECT icon, name FROM market {where};
        ''').fetchall()
        if database_data:
            for e in database_data: all_data.append(e)
    if _active_filters[5]:
        if _text != '':
            where = f'WHERE name like "%{_text}%"'
        else:
            where = ''
        database_data = cursor.execute(f'''
            SELECT icon, name FROM country {where};
        ''').fetchall()
        if database_data:
            for e in database_data: all_data.append(e)
    cursor.close()
    database.close()
#______________________________________________________________________________________________________________________
    """ Set up """
    if self.panel_scroll_widget:
        self.panel_scroll_widget.deleteLater()
        self.panel_scroll_widget = None 
    """ Create widget """
    self.panel_scroll_widget = QWidget(self.panel_scroll)
    self.panel_scroll_widget.setObjectName('panel_scroll_widget')
    self.panel_scroll.setWidget(self.panel_scroll_widget)
    self.panel_scroll_widget.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
    self.panel_scroll_layout = QGridLayout(self.panel_scroll_widget)
    self.panel_scroll_layout.setSpacing(0)
    self.panel_scroll_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.panel_scroll_layout.setRowStretch(enc, 1)
        self.panel_scroll_layout.setColumnStretch(enc, 1)
    self.panel_scroll_widget.setLayout(self.panel_scroll_layout)
    for i, list_object in enumerate(all_data, start=1):
        index_button = QPushButton(self.panel_widget)
        object_logo_label = QLabel(self.panel_widget)
        object_name_button = QPushButton(self.panel_widget)
        market_logo_label = QLabel(self.panel_widget)
        market_name_label = QLabel(self.panel_widget)
        index_button.setObjectName('index_button')
        object_logo_label.setObjectName('object_logo_label')
        object_name_button.setObjectName('object_name_button')
        market_logo_label.setObjectName('market_logo_label')
        market_name_label.setObjectName('market_name_label')
        self.panel_scroll_layout.addWidget(index_button, i, 2, 1, 5)
        self.panel_scroll_layout.addWidget(object_logo_label, i, 7, 1, 16)
        self.panel_scroll_layout.addWidget(object_name_button, i, 23, 1, 29)
        self.panel_scroll_layout.addWidget(market_logo_label, i, 52, 1, 16)
        self.panel_scroll_layout.addWidget(market_name_label, i, 68, 1, 29)
        object_logo_label.setAlignment(Qt.AlignCenter)
        market_logo_label.setAlignment(Qt.AlignCenter)
        market_name_label.setAlignment(Qt.AlignCenter)
        index_button.setMaximumHeight(50)
        index_button.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
        object_logo_label.setMaximumHeight(50)
        object_logo_label.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
        object_name_button.setMaximumHeight(50)
        object_name_button.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
        market_logo_label.setMaximumHeight(50)
        market_logo_label.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
        market_name_label.setMaximumHeight(50)
        market_name_label.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
        index_button.setText(f' {i}')
        object_name_button.setText(f'{list_object[1]}')
        object_logo_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+list_object[0]+'.svg', int(object_logo_label.height()), int(object_logo_label.height())))
        if len(list_object) > 2:
            market_name_label.setText(f'{list_object[3]}')
            market_logo_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+list_object[2]+'.svg', int(market_logo_label.height()), int(market_logo_label.height())))
        index_button.clicked.connect(lambda: add_object__lists(self))
#######################################################################################################################
def filters_changed(self, index):
    self.global_config['main_search_filters'][index] = not self.global_config['main_search_filters'][index] # Change
    json.dump(self.global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4) # Save 
    self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Reload
    filters_load(self)
    text_changed(self)
#######################################################################################################################
def filters_load(self):
    _active_filters = self.global_config['main_search_filters']
    for index, f in enumerate(_active_filters, start=0):
        if f:
            self.button_list[index].setStyleSheet('background-color: #031913;')
        else:
            self.button_list[index].setStyleSheet('background-color: #252525;')
#######################################################################################################################
""" Add object lists """
def add_object__lists(self):
    """ Set deafoult  """
    if self.panel_add_widget:
        self.panel_add_widget.deleteLater()
        self.panel_add_widget = None
    """ Create objects """ 
    self.panel_add_widget = QWidget(self.panel_scroll)
    self.panel_add_layout = QGridLayout(self.panel_add_widget)
    self.panel_add_exit_button = QPushButton(self.panel_add_widget)
    self.panel_add_title_label = QLabel(self.panel_add_widget)
    self.panel_add_path_label = QLabel(self.panel_add_widget)
    self.panel_add_scroll = QScrollArea(self.panel_add_widget)
    self.panel_add_scroll_widget = QWidget(self.panel_add_scroll)
    self.panel_add_scroll_layout = QVBoxLayout(self.panel_add_scroll_widget)
    """ Set object name """
    self.panel_add_widget.setObjectName('panel_add_widget')
    self.panel_add_exit_button.setObjectName('panel_add_exit_button')
    self.panel_add_title_label.setObjectName('panel_add_title_label')
    self.panel_add_path_label.setObjectName('panel_add_path_label')
    self.panel_add_scroll.setObjectName('panel_add_scroll')
    self.panel_add_scroll_widget.setObjectName('panel_add_scroll_widget')
    """ Set Layout """
    self.panel_layout.addWidget(self.panel_add_widget)
    self.panel_add_layout.addWidget(self.panel_add_exit_button, 2, 5, 6, 5)
    self.panel_add_layout.addWidget(self.panel_add_title_label, 5, 30, 5, 40)
    self.panel_add_layout.addWidget(self.panel_add_path_label, 15, 5, 3, 90)
    self.panel_add_layout.addWidget(self.panel_add_scroll, 20, 5, 80, 90)
    self.panel_add_layout.setSpacing(0)
    self.panel_add_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.panel_add_layout.setRowStretch(enc, 1)
        self.panel_add_layout.setColumnStretch(enc, 1)
    self.panel_add_widget.setLayout(self.panel_add_layout)
    self.panel_add_scroll_layout.setSpacing(0)
    self.panel_add_scroll_layout.setContentsMargins(0,0,0,0)
    self.panel_add_scroll_widget.setLayout(self.panel_add_scroll_layout)
    """ Set widget """
    self.panel_search_widget.setHidden(True)
    self.panel_add_widget.setHidden(False)
    self.panel_add_scroll.setWidgetResizable(True)
    self.panel_add_scroll.setWidget(self.panel_add_scroll_widget)
    """ Set label """
    self.panel_add_title_label.setAlignment(Qt.AlignCenter)
    self.panel_add_path_label.setAlignment(Qt.AlignCenter)
    """ Set size """
    self.panel_add_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_path_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Set text """
    _t = self.main_search_translate # Translate texts 
    _l = self.global_config['__language__'] # Language
    self.panel_add_title_label.setText(_t['panel_add_title_label'][_l])
    self.panel_add_path_label.setText(f"{_t['panel_add_path_label'][_l]} > ")
    """ Set graphics """
    self.panel_add_exit_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/exit_'+self.global_config['__theme__']+'.svg', 256, 256)))
    """ Add lists """
    for keys in self.global_config['mid_object_lists'].keys():
        button = QPushButton(self.panel_add_widget)
        button.setObjectName(f'panel_add_{keys}_button')
        button.setProperty('class', 'panel_add_button')
        self.panel_add_scroll_layout.addWidget(button)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setText(f'{keys}')
        button.clicked.connect(lambda _, c_l=keys: add_object__section(self, choosen_list=c_l))
    """ Connect functions """
    self.panel_add_exit_button.clicked.connect(lambda: add_object__lists_exit(self))
#######################################################################################################################
""" Add object lists exit """
def add_object__lists_exit(self):
    if self.panel_add_widget:
        self.panel_add_widget.deleteLater()
        self.panel_add_widget = None
    self.panel_search_widget.setHidden(False)
#######################################################################################################################
""" Add object section """
def add_object__section(self, choosen_list):
    self.choosen_list = choosen_list
    for index, section in enumerate(self.global_config['mid_object_lists'][self.choosen_list], start=0):
        name = section.keys()[0]
        button = QPushButton()
        button.setObjectName(f'panel_add_{name}_button')
        button.setProperty('class', 'panel_add_button')
        self.panel_add_scroll_layout.addWidget(button)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setText(f'{name}')
        button.clicked.connect(lambda _, c_s=index: add_object__objects(self, choosen_section=c_s))
#######################################################################################################################
""" Add object section exit """
def add_object__section_exit(self):
    pass
#######################################################################################################################
""" Add object objects """
def add_object__objects(self, choosen_section):
    self.choosen_section = choosen_section
    for objects in self.global_configp['mid_object_lists'][self.choosen_list][self.choosen_section].values():
        print(objects)
#######################################################################################################################
""" Add object objects exit """
def add_object__objects_exit(self):
    pass
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