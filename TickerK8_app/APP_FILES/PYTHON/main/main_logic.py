""" Import packages """
""" Import system and operating system packages """
import json # For json files.
import datetime # For get time.
import sqlite3 # For databases.
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
from PyQt5.QtGui import (
    QLinearGradient, # Gradient.
    QPalette, # Palette.
    QBrush, # Brush.
    QColor, # Color.
    QPixmap, # Image.
    QIcon, # Icon.
    QPainter # Painter.
)
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
#______________________________________________________________________________________________________________________
""" Import main news """
from main_news.main_news_structure import Main_news_widget
#_______________________________________________________________________________________________________________________
""" Import main news list """
from main_news_list.main_news_list_structure import Main_news_list_widget
#######################################################################################################################
""" widget background painter """
def widget_background_painter(self):
    """ Variables """
    """ Colors """
    _colors = json.load(open(self.main_path+'/CONFIG/main/conf.json', 'r'))['background'] # Get colors list, local.
    _color_0 = '#000000'
    _color_1 = '#000000'
    _color_2 = '#000000'
    """ Colors alpha """
    _alpha_1 = 'ff'
    _alpha_2 = 'ff'
    """ Colors positions """
    _x_1 = 0.0
    _x_2 = 1.0 
#______________________________________________________________________________________________________________________
    """ Calculate index and precent """
    _now = datetime.datetime.now() # Get current time.
    _today_sec = _now.hour*3600+_now.minute*60+_now.second # Total today time left.
    if _today_sec >=86400: # Check if extra sec.
        _today_sec = 86399
    _index = _today_sec//8640 # Index, segment of the day.
    _percent = (_today_sec/8640)-_index # Percetn of time left in segmnet.
#______________________________________________________________________________________________________________________
    """ Set colors """
    if _percent <= 0.5:
        _x_1 = 1-(_percent*2)
        _x_2 = 1.0
        _alpha_1 = 'ff'
        _alpha_2 = f'{int(255 *(_percent / 0.5)):02X}'
        _color_0 = f'#ff{_colors[_index-1]}' # Set background color.
    else:
        _x_1 = 0.0
        _x_2 = 1-(_percent-0.5)*2
        _alpha_1 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _alpha_2 = 'ff'
        _color_0 = f'#ff{_colors[_index]}' # Set background color.
    _color_1 = f'#{_alpha_1}{_colors[_index-1]}' # Set first color.
    _color_2 = f'#{_alpha_2}{_colors[_index]}' # Set sec color.
#______________________________________________________________________________________________________________________
    """ Paint background """
    pixmap = QPixmap(self.size()) # Create img, size of login widget.
    pixmap.fill(QColor(_color_0)) # Fill img by background color.
    painter = QPainter(pixmap) # Create painter.
    gradient = QLinearGradient(0,0,self.width(), 0) # Create gradient.
    gradient.setColorAt(_x_1, QColor(_color_1)) # Set first color.
    gradient.setColorAt(_x_2, QColor(_color_2)) # Set secound color.
    painter.fillRect(self.rect(), gradient) # Fill by gradient.
    painter.end() # End painting.
    palette = self.palette() # Create palette.
    palette.setBrush(QPalette.Window, QBrush(pixmap)) # Set brush.
    self.setAutoFillBackground(True) # Set fill background for login widget.
    self.setPalette(palette) # Set palette for login widget.
#######################################################################################################################
""" objects list open"""
def objects_list_open(self):
    """ Set config """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    _list_object = _global_config['object_list'] # Get list objects name, key.
    _open_list_data = _global_config['object_lists'][_list_object] # Get list objects, data.
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r')) # Translate texts.
#______________________________________________________________________________________________________________________
    """ Setup widget """
    if self.objects_list_widget:
        self.objects_list_widget.deleteLater()
        self.objects_list_widget = None 
#______________________________________________________________________________________________________________________
    """ Create object """
    self.objects_list_widget = QWidget(self.objects_list_scroll)
    self.objects_list_layout = QVBoxLayout(self.objects_list_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.objects_list_widget.setObjectName('objects_list_widget')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.objects_list_layout.setSpacing(0)
    self.objects_list_layout.setContentsMargins(0,0,0,0)
    self.objects_list_widget.setLayout(self.objects_list_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.objects_list_scroll.setWidget(self.objects_list_widget)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.objects_list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set texts """
    self.objects_list_title_label.setText(f'{_list_object}')
#______________________________________________________________________________________________________________________
    """ Add items """
    for section_index, section in enumerate(_open_list_data, start=0):
        """ Section data """
        section_dict = dict(section)
        for key, value in section_dict.items():
            """ Create widget """
            objects_list_section_widget = QWidget(self.objects_list_widget)
            objects_list_section_layout = QGridLayout(objects_list_section_widget)
            objects_list_section_open_button = QPushButton(objects_list_section_widget)
            objects_list_items_widget = QWidget(objects_list_section_widget)
            objects_list_items_layout = QGridLayout(objects_list_items_widget)
            objects_list_items_hash_tag = QLabel(objects_list_items_widget)
#______________________________________________________________________________________________________________________
            """ Set object name """
            objects_list_section_widget.setObjectName(f'objects_list_section_{key}_widget')
            objects_list_section_open_button.setObjectName(f'objects_list_section_{key}_open_button')
            objects_list_items_widget.setObjectName(f'objects_list_section_{key}_widget')
            objects_list_items_hash_tag.setObjectName(f'objects_list_section_{key}hash_tag')
#______________________________________________________________________________________________________________________
            """ Set property """
            objects_list_section_widget.setProperty('class', 'objects_list_section_widget')
            objects_list_section_open_button.setProperty('class', 'objects_list_section_open_button')
            objects_list_items_widget.setProperty('class', 'objects_list_items_widget')
            objects_list_items_hash_tag.setProperty('class', 'objects_list_items_hash_tag')
#______________________________________________________________________________________________________________________
            """ Set layout """
            self.objects_list_layout.addWidget(objects_list_section_widget)
            objects_list_section_layout.addWidget(objects_list_section_open_button,0,0)
            objects_list_section_layout.addWidget(objects_list_items_widget,1,0)
            objects_list_section_layout.setSpacing(0)
            objects_list_section_layout.setContentsMargins(0,0,0,0)
            objects_list_section_widget.setLayout(objects_list_section_layout)
            objects_list_items_layout.addWidget(objects_list_items_hash_tag, 0, 0)
            objects_list_items_layout.setSpacing(0)
            objects_list_items_layout.setContentsMargins(0,0,0,0)
            objects_list_items_widget.setLayout(objects_list_items_layout)
#______________________________________________________________________________________________________________________
            """ Set widget """
            objects_list_items_widget.setHidden(False)
#______________________________________________________________________________________________________________________
            """ Set label """
            objects_list_items_hash_tag.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
            """ Set size """
            objects_list_section_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            objects_list_section_open_button.setFixedHeight(int(self.height()*0.1))
            objects_list_section_open_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            objects_list_items_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            objects_list_items_hash_tag.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
            """ Set text """
            objects_list_section_open_button.setText(f'{key}')
            objects_list_items_hash_tag.setText('#')
#______________________________________________________________________________________________________________________
            """ Connect """
            objects_list_section_open_button.clicked.connect(lambda _, widget=objects_list_items_widget: widget.setHidden(not widget.isHidden()))
#______________________________________________________________________________________________________________________
            """ Create tags """
            for index, tag in enumerate(_global_config['object_list_tags'], start=1):
                objects_list_tag_label = QLabel(objects_list_items_widget)
                objects_list_tag_label.setObjectName(f'objects_list_tag_label_{index}')
                objects_list_tag_label.setProperty('class', 'objects_list_tag_label')
                objects_list_items_layout.addWidget(objects_list_tag_label, 0, index)
                objects_list_tag_label.setAlignment(Qt.AlignCenter)
                objects_list_tag_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                objects_list_tag_label.setText(f'{_t['objects_list_tags'][f'{tag}'][_global_config['__language__']]}')
#_____________________________________________________________________________________________________________________
            """ Create items """
            database = sqlite3.connect(database=self.local_database)
            cursor = database.cursor()
            if value:
                for row, item in enumerate(value, start=1):
                    objects_list_index_button = QPushButton(objects_list_items_widget)
                    objects_list_index_button.setObjectName(f'objects_list_index_{row}_button')
                    objects_list_index_button.setProperty('class', 'objects_list_index_button')
                    objects_list_items_layout.addWidget(objects_list_index_button, row, 0)
                    objects_list_index_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    objects_list_index_button.setText(f'{row}')
                    objects_list_index_button.clicked.connect(lambda _, s_i=section_index, s_n=key, i=row-1: objects_list_delete_object(self, section_index=s_i, section_name=s_n, index=i))
                    for table, id_id in dict(item).items():
                        for column, tag in enumerate(_global_config['object_list_tags'], start=1):
                            try:
                                text = cursor.execute(f'SELECT {tag} FROM {table} WHERE id={id_id};').fetchall()[0][0]
                            except:
                                text = '---'
                            if tag == 'name':
                                objects_list_data_object = QPushButton(objects_list_items_widget)
                                objects_list_data_object.setObjectName(f'objects_list_data_{tag}_{id_id}_button')
                                objects_list_data_object.setProperty('class', 'objects_list_data_button')
                                objects_list_data_object.setText(str(text))
                                objects_list_data_object.clicked.connect(lambda _, t=table, i=id_id: object_set(self, [t, i]))
                            else:
                                objects_list_data_object = QLabel(main_objects_list_items_widget)
                                objects_list_data_object.setObjectName(f'objects_list_data_{tag}_{id_id}_label')
                                objects_list_data_object.setProperty('class', 'objects_list_data_label')
                                objects_list_data_object.setAlignment(Qt.AlignCenter)
                                if tag == 'icon' and text != '---':
                                    objects_list_data_object.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+text+'.svg', objects_list_data_object.height(), objects_list_data_object.height()))
                                else:
                                    objects_list_data_object.setText(str(text))
                            objects_list_data_object.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                            objects_list_items_layout.addWidget(objects_list_data_object, row, column)
#######################################################################################################################
""" objects list delete object """
def objects_list_delete_object(self, section_index, section_name, index):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    object_name = _global_config['object_list']
    object_in_section = _global_config['object_lists'][object_name][section_index][section_name]
    object_in_section.pop(index)
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4) # Save config
    objects_list_open(self)
#######################################################################################################################
""" object set """
def object_set(self):
    pass
#######################################################################################################################
def object_list_lists_scroll_setup(self):
    """ Set local data """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    """ Add lists items """
    for keys, values in _global_config['object_lists'].items():
        objects_list_lists_button = QPushButton(self.objects_list_lists_widget)
        objects_list_lists_button.setObjectName(f'objects_list_lists_{keys}_button')
        objects_list_lists_button.setProperty('class', 'objects_list_lists_button')
        self.objects_list_lists_layout.addWidget(objects_list_lists_button)
        objects_list_lists_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        objects_list_lists_button.setText(f'{keys}')
        objects_list_lists_button.clicked.connect(lambda _, name=keys: object_list_set_list(self, name=name))
#######################################################################################################################
def object_list_lists_exit(self):
    """ Set config """
    self.objects_list_title_label.show()
    self.objects_list_scroll.show()
    self.type_list_button.show()
    self.data_list_button.show()
#______________________________________________________________________________________________________________________
    """ Delete objects """
    self.objects_list_lists_title_label.deleteLater()
    self.objects_list_lists_scroll.deleteLater()
    self.objects_list_lists_exit_button.deleteLater()
#######################################################################################################################
def object_list_set_list(self, name):
    """ Set local data """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    _global_config['mid_object_list'] = name
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4) # Save config
    objects_list_open(self)
    object_list_lists_exit(self)
#######################################################################################################################
""" object list edit check selected """
def object_list_edit_check_selected(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    for val in _global_config['object_list_tags']:
        if val == 'name':
            pass
        else:
            button = getattr(self, f'object_list_edit_{val}_button')       
            button.setStyleSheet('background-color: #282828;')
#######################################################################################################################
""" object list edit save """
def object_list_edit_save(self, val):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    button = getattr(self, f'object_list_edit_{val}_button')
    if val not in _global_config['object_list_tags']:
        _global_config['object_list_tags'].append(val)       
        button.setStyleSheet('background-color: #282828;')
    else:
        _global_config['object_list_tags'].remove(val)       
        button.setStyleSheet('background-color: #1a1a1a;')
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4) # Save confi
#######################################################################################################################
""" object list edit exit """
def object_list_edit_exit(self):
    """ Set config """
    self.objects_list_title_label.show()
    self.objects_list_scroll.show()
    self.type_list_button.show()
    self.data_list_button.show()
#______________________________________________________________________________________________________________________
    """ Delete objects """
    self.object_list_edit_title_label.deleteLater()
    self.object_list_edit_scroll.deleteLater()
    self.object_list_edit_exit_button.deleteLater()
    objects_list_open(self)
#######################################################################################################################





#######################################################################################################################
""" news create buttons """
def 




""" Open main news """
def open_main_news(self, id_news):
    self.main_news = Main_news_widget(self, id_news)
#######################################################################################################################
""" Open main news list """
def open_main_news_list(self, news_type_index):
    self.main_news_list = Main_news_list_widget(self, news_type_index)
    self.main_news_list.open_news.connect(lambda val: open_main_news(self, val))
#######################################################################################################################
""" main mid object changed """
def main_mid_object_changed(self):
    self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data.
    _o = self.global_config['mid_object'][0] # Get mid object data.
    self.mid_object_scroll.setup_widget()
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