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
    for keys, values in self.global_config['mid_object_lists'].items():
        button = QPushButton(self.lists_scroll_widget)
        button.setObjectName(f'lists_scroll_{keys}_button')
        button.setProperty('class', 'lists_scroll_button')
        self.lists_scroll_layout.addWidget(button)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setText(f'{keys}')
        button.clicked.connect(lambda _, key=keys, value=values: open_list(self, key, value))
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
""" Open lsit """
def open_list(self, title, list_objects):
    """ Set config """
    self.global_config['mid_object_list'] = {f"{title}": list_objects}
    json.dump(self.global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
#______________________________________________________________________________________________________________________
    """ Setup widget """
    if self.list_widget:
        self.list_widget.deleteLater()
        self.list_widget = None 
#______________________________________________________________________________________________________________________
    """ Create object """
    self.list_widget = QWidget(self.list_scroll)
    self.list_layout = QVBoxLayout(self.list_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.list_widget.setObjectName('list_widget')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.list_layout.setSpacing(0)
    self.list_layout.setContentsMargins(0,0,0,0)
    self.list_widget.setLayout(self.list_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.list_scroll.setWidget(self.list_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
#______________________________________________________________________________________________________________________
    """ Set size """
    self.list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set texts """
    self.title_label.setText(f'{title}')
#______________________________________________________________________________________________________________________
    """ Set graphics """
#______________________________________________________________________________________________________________________
    """ Connect """
#______________________________________________________________________________________________________________________
    """ Add items """
    for section in list_objects:
        """ Section data """
        section_dict = dict(section)
        for key, value in section_dict.items():
            """ Create widget """
            section_widget = QWidget(self.list_widget)
            section_layout = QGridLayout(section_widget)
            section_open_button = QPushButton(section_widget)
            items_widget = QWidget(section_widget)
            items_layout = QGridLayout(items_widget)
            items_hash_tag = QLabel(items_widget)
#______________________________________________________________________________________________________________________
            """ Set object name """
            section_widget.setObjectName(f'section_{key}_widget')
            section_open_button.setObjectName(f'section_{key}_open_button')
            items_widget.setObjectName(f'items_{key}_widget')
            items_hash_tag.setObjectName(f'items_{key}hash_tag')
#______________________________________________________________________________________________________________________
            """ Set property """
            section_widget.setProperty('class', 'section_widget')
            section_open_button.setProperty('class', 'section_open_button')
            items_widget.setProperty('class', 'items_widget')
            items_hash_tag.setProperty('class', 'items_hash_tag')
#______________________________________________________________________________________________________________________
            """ Set layout """
            self.list_layout.addWidget(section_widget)
            section_layout.addWidget(section_open_button,0,0)
            section_layout.addWidget(items_widget,1,0)
            section_layout.setSpacing(0)
            section_layout.setContentsMargins(0,0,0,0)
            section_widget.setLayout(section_layout)
            items_layout.addWidget(items_hash_tag, 0, 0)
            items_layout.setSpacing(0)
            items_layout.setContentsMargins(0,0,0,0)
            items_widget.setLayout(items_layout)
#______________________________________________________________________________________________________________________
            """ Set widget """
            items_widget.setHidden(False)
#______________________________________________________________________________________________________________________
            """ Set label """
            items_hash_tag.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
            """ Set size """
            section_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            section_open_button.setFixedHeight(int(self.height()*0.1))
            section_open_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            items_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            items_hash_tag.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
            """ Set text """
            section_open_button.setText(f'{key}')
            items_hash_tag.setText('#')
#______________________________________________________________________________________________________________________
            """ Connect """
            section_open_button.clicked.connect(lambda _, widget=items_widget: widget.setHidden(not widget.isHidden()))
#______________________________________________________________________________________________________________________
            """ Create tags """
            for index, tag in enumerate(self.global_config['mid_object_list_tags'], start=1):
                label = QLabel(items_widget)
                label.setObjectName(f'label_{index}')
                label.setProperty('class', 'tag')
                items_layout.addWidget(label, 0, index)
                label.setAlignment(Qt.AlignCenter)
                label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                label.setText(f'{self.main_mid_object_list_translate['list_tags'][f'{tag}'][self.global_config['__language__']]}')
#_____________________________________________________________________________________________________________________
            """ Create items """
            database = sqlite3.connect(database=self.local_database)
            cursor = database.cursor()
            if value:
                for row, item in enumerate(value, start=1):
                    index_label = QLabel(items_widget)
                    index_label.setObjectName(f'index_{row}_label')
                    index_label.setProperty('class', 'index_label')
                    items_layout.addWidget(index_label, row, 0)
                    index_label.setAlignment(Qt.AlignCenter)
                    index_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    index_label.setText(f'{row}')
                    for table, id_id in dict(item).items():
                        for column, tag in enumerate(self.global_config['mid_object_list_tags'], start=1):
                            data_label = QLabel(items_widget)
                            data_label.setObjectName(f'data_{tag}_{id_id}_label')
                            data_label.setProperty('class', 'data_label')
                            items_layout.addWidget(data_label, row, column)
                            data_label.setAlignment(Qt.AlignCenter)
                            data_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                            try:
                                text = cursor.execute(f'SELECT {tag} FROM {table} WHERE id={id_id};').fetchall()[0][0]
                            except:
                                text = '---'
                            
                            if tag == 'icon' and text != '---':
                                data_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/flags'+text+'.svg', data_label.height(), data_label.height()))
                            else:
                                data_label.setText(text)
#______________________________________________________________________________________________________________________
    """ Exit form lists widget  """
    if self.lists_background_widget:
        lists_exit(self)
#######################################################################################################################
""" Lists exit """
def lists_exit(self):
    self.lists_background_widget.deleteLater()
    self.lists_background_widget = None 

#######################################################################################################################
