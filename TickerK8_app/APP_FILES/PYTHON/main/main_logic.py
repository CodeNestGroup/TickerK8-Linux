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
""" main widget background painter """
def main_widget_background_painter(self):
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
""" main objects list open"""
def main_objects_list_open(self):
    """ Set config """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    _list_object = _global_config['mid_object_list'] # Get list objects name, key.
    _open_list_data = _global_config['mid_object_lists'][_list_object] # Get list objects, data.
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r')) # Translate texts.
#______________________________________________________________________________________________________________________
    """ Setup widget """
    if self.main_objects_list_widget:
        self.main_objects_list_widget.deleteLater()
        self.main_objects_list_widget = None 
#______________________________________________________________________________________________________________________
    """ Create object """
    self.main_objects_list_widget = QWidget(self.main_objects_list_scroll)
    self.main_objects_list_layout = QVBoxLayout(self.main_objects_list_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.main_objects_list_widget.setObjectName('main_objects_list_widget')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_objects_list_layout.setSpacing(0)
    self.main_objects_list_layout.setContentsMargins(0,0,0,0)
    self.main_objects_list_widget.setLayout(self.main_objects_list_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.main_objects_list_scroll.setWidget(self.main_objects_list_widget)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.main_objects_list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set texts """
    self.main_objects_list_title.setText(f'{_list_object}')
#______________________________________________________________________________________________________________________
    """ Add items """
    for section_index, section in enumerate(_open_list_data, start=0):
        """ Section data """
        section_dict = dict(section)
        for key, value in section_dict.items():
            """ Create widget """
            main_objects_list_section_widget = QWidget(self.main_objects_list_widget)
            main_objects_list_section_layout = QGridLayout(main_objects_list_section_widget)
            main_objects_list_section_open_button = QPushButton(main_objects_list_section_widget)
            main_objects_list_items_widget = QWidget(main_objects_list_section_widget)
            main_objects_list_items_layout = QGridLayout(main_objects_list_items_widget)
            main_objects_list_items_hash_tag = QLabel(main_objects_list_items_widget)
#______________________________________________________________________________________________________________________
            """ Set object name """
            main_objects_list_section_widget.setObjectName(f'main_objects_list_section_{key}_widget')
            main_objects_list_section_open_button.setObjectName(f'main_objects_list_section_{key}_open_button')
            main_objects_list_items_widget.setObjectName(f'main_objects_list_section_{key}_widget')
            main_objects_list_items_hash_tag.setObjectName(f'main_objects_list_section_{key}hash_tag')
#______________________________________________________________________________________________________________________
            """ Set property """
            main_objects_list_section_widget.setProperty('class', 'main_objects_list_section_widget')
            main_objects_list_section_open_button.setProperty('class', 'main_objects_list_section_open_button')
            main_objects_list_items_widget.setProperty('class', 'main_objects_list_items_widget')
            main_objects_list_items_hash_tag.setProperty('class', 'main_objects_list_items_hash_tag')
#______________________________________________________________________________________________________________________
            """ Set layout """
            self.main_objects_list_layout.addWidget(main_objects_list_section_widget)
            main_objects_list_section_layout.addWidget(main_objects_list_section_open_button,0,0)
            main_objects_list_section_layout.addWidget(main_objects_list_items_widget,1,0)
            main_objects_list_section_layout.setSpacing(0)
            main_objects_list_section_layout.setContentsMargins(0,0,0,0)
            main_objects_list_section_widget.setLayout(main_objects_list_section_layout)
            main_objects_list_items_layout.addWidget(main_objects_list_items_hash_tag, 0, 0)
            main_objects_list_items_layout.setSpacing(0)
            main_objects_list_items_layout.setContentsMargins(0,0,0,0)
            main_objects_list_items_widget.setLayout(main_objects_list_items_layout)
#______________________________________________________________________________________________________________________
            """ Set widget """
            main_objects_list_items_widget.setHidden(False)
#______________________________________________________________________________________________________________________
            """ Set label """
            main_objects_list_items_hash_tag.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
            """ Set size """
            main_objects_list_section_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            main_objects_list_section_open_button.setFixedHeight(int(self.height()*0.1))
            main_objects_list_section_open_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            main_objects_list_items_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            main_objects_list_items_hash_tag.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
            """ Set text """
            main_objects_list_section_open_button.setText(f'{key}')
            main_objects_list_items_hash_tag.setText('#')
#______________________________________________________________________________________________________________________
            """ Connect """
            main_objects_list_section_open_button.clicked.connect(lambda _, widget=main_objects_list_items_widget: widget.setHidden(not widget.isHidden()))
#______________________________________________________________________________________________________________________
            """ Create tags """
            for index, tag in enumerate(_global_config['mid_object_list_tags'], start=1):
                main_objects_list_tag_label = QLabel(main_objects_list_items_widget)
                main_objects_list_tag_label.setObjectName(f'main_objects_list_tag_label_{index}')
                main_objects_list_tag_label.setProperty('class', 'main_objects_list_tag_label')
                main_objects_list_items_layout.addWidget(main_objects_list_tag_label, 0, index)
                main_objects_list_tag_label.setAlignment(Qt.AlignCenter)
                main_objects_list_tag_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                main_objects_list_tag_label.setText(f'{_t['main_objects_list_tags'][f'{tag}'][_global_config['__language__']]}')
#_____________________________________________________________________________________________________________________
            """ Create items """
            database = sqlite3.connect(database=self.local_database)
            cursor = database.cursor()
            if value:
                for row, item in enumerate(value, start=1):
                    main_objects_list_index_button = QPushButton(main_objects_list_items_widget)
                    main_objects_list_index_button.setObjectName(f'main_objects_list_index_{row}_button')
                    main_objects_list_index_button.setProperty('class', 'main_objects_list_index_button')
                    main_objects_list_items_layout.addWidget(main_objects_list_index_button, row, 0)
                    main_objects_list_index_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    main_objects_list_index_button.setText(f'{row}')
                    main_objects_list_index_button.clicked.connect(lambda _, s_i=section_index, s_n=key, i=row-1: main_objects_list_delete_object(self, section_index=s_i, section_name=s_n, index=i))
                    for table, id_id in dict(item).items():
                        for column, tag in enumerate(_global_config['mid_object_list_tags'], start=1):
                            try:
                                text = cursor.execute(f'SELECT {tag} FROM {table} WHERE id={id_id};').fetchall()[0][0]
                            except:
                                text = '---'
                            if tag == 'name':
                                main_objects_list_data_object = QPushButton(main_objects_list_items_widget)
                                main_objects_list_data_object.setObjectName(f'main_objects_list_data_{tag}_{id_id}_button')
                                main_objects_list_data_object.setProperty('class', 'main_objects_list_data_button')
                                main_objects_list_data_object.setText(str(text))
                                main_objects_list_data_object.clicked.connect(lambda _, t=table, i=id_id: main_object_set(self, [t, i]))
                            else:
                                main_objects_list_data_object = QLabel(main_objects_list_items_widget)
                                main_objects_list_data_object.setObjectName(f'main_objects_list_data_{tag}_{id_id}_label')
                                main_objects_list_data_object.setProperty('class', 'main_objects_list_data_label')
                                main_objects_list_data_object.setAlignment(Qt.AlignCenter)
                                if tag == 'icon' and text != '---':
                                    main_objects_list_data_object.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+text+'.svg', main_objects_list_data_object.height(), main_objects_list_data_object.height()))
                                else:
                                    main_objects_list_data_object.setText(str(text))
                            main_objects_list_data_object.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                            main_objects_list_items_layout.addWidget(main_objects_list_data_object, row, column)
#######################################################################################################################
""" main objects list delete object """
def main_objects_list_delete_object(self, section_index, section_name, index):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    list_object_name = _global_config['mid_object_list']
    object_in_section = _global_config['mid_object_lists'][list_object_name][section_index][section_name]
    object_in_section.pop(index)
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4) # Save config
    main_objects_list_open(self)
#######################################################################################################################
""" main object set """
def main_object_set(self):
    pass
#######################################################################################################################
def main_object_list_lists_scroll_setup(self):
    """ Set local data """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    """ Add lists items """
    for keys, values in _global_config['mid_object_lists'].items():
        main_objects_list_lists_button = QPushButton(self.main_objects_list_lists_widget)
        main_objects_list_lists_button.setObjectName(f'main_objects_list_lists_{keys}_button')
        main_objects_list_lists_button.setProperty('class', 'main_objects_list_lists_button')
        self.main_objects_list_lists_layout.addWidget(main_objects_list_lists_button)
        main_objects_list_lists_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        main_objects_list_lists_button.setText(f'{keys}')
        main_objects_list_lists_button.clicked.connect(lambda _, name=keys: main_object_list_set_list(self, name=name))
#######################################################################################################################
def main_object_list_lists_exit(self):
    """ Set config """
    self.main_objects_list_title.show()
    self.main_objects_list_scroll.show()
    self.main_type_list_button.show()
    self.main_data_list_button.show()
#______________________________________________________________________________________________________________________
    """ Delete objects """
    self.main_objects_list_lists_title_label.deleteLater()
    self.main_objects_list_lists_exit_button.deleteLater()
    self.main_objects_list_lists_scroll.deleteLater()
#######################################################################################################################
def main_object_list_set_list(self, name):
    """ Set local data """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    _global_config['mid_object_list'] = name
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4) # Save config
    main_objects_list_open(self)
    main_object_list_lists_exit(self)
#######################################################################################################################
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