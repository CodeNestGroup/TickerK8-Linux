""" Import packages """
""" Import system and operating system packages """
import json # For json files.
import datetime # For get time.
import sqlite3 # For databases.
import mysql # For online databases.
import requests
from io import BytesIO
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
    self.objects_list_layout.setContentsMargins(10,10,10,10)
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
""" object setup """
def object_setup(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    if _global_config['object'][0] == 'country':
        object_country(self)
    elif _global_config['object'][0] == 'market':
        object_market(self)
    elif _global_config['object'][0] == 'market_index':
        object_index(self)
    elif _global_config['object'][0] == 'stock':
        object_stock(self)
#######################################################################################################################
""" object country """
def object_country(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    """ Get data """
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
    cursor = database.cursor() # Create cursor 
    country_data = cursor.execute(f'''
    SELECT
    country.name, 
    country.icon, 
    country.capital, 
    country.currency_code, 
    timezone.name, 
    population.number
    FROM country 
    JOIN timezone ON country.id_timezone=timezone.id
    JOIN population ON country.id=population.id_country
    WHERE country.id=={_global_config['object'][1]};''').fetchall()[0] # Execute
    cursor.close()
    database.close()
#______________________________________________________________________________________________________________________
    """ Setup dafoult for country data """
    if self.object_time_widget:
        self.object_time_widget.deleteLater()
        self.object_time_widget = None
    if self.object_chart_widget:
        self.object_chart_widget.deleteLater()
        self.object_chart_widget = None
    if self. object_info_widget:
        self.object_info_widget.deleteLater()
        self.object_info_widget = None
    if self.object_statistics_widget:
        self.object_statistics_widget.deleteLater()
        self.object_statistics_widget = None 
    self.object_ticker_label.setHidden(True)
    self.object_ticker_label.setText('')
#______________________________________________________________________________________________________________________
    """ Create """
    self.object_time_widget = QWidget(self)
    self.object_info_widget = QWidget(self)
    self.object_info_layout = QGridLayout(self.object_info_widget)
    info_title_label = QLabel(self.object_info_widget)
    info_index_name_label = QLabel(self.object_info_widget)
    info_name_name_label = QLabel(self.object_info_widget) 
    info_capitalization_name_label = QLabel(self.object_info_widget)
    self.object_statistics_widget = QWidget(self)
    self.object_statistics_layout = QGridLayout(self.object_statistics_widget)
    statistics_population_name_label = QLabel(self.object_statistics_widget)
    statistics_population_value_label = QLabel(self.object_statistics_widget)
    statistics_capital_name_label = QLabel(self.object_statistics_widget)
    statistics_capital_value_label = QLabel(self.object_statistics_widget)
    statistics_timezone_name_label = QLabel(self.object_statistics_widget)
    statistics_timezone_value_label = QLabel(self.object_statistics_widget)
    statistics_currency_name_label = QLabel(self.object_statistics_widget)
    statistics_currency_value_label = QLabel(self.object_statistics_widget)
#______________________________________________________________________________________________________________________
    """ Setup """
    """ Set object name """
    self.object_time_widget.setObjectName('object_time_widget')
    self.object_info_widget.setObjectName('object_info_widget')
    info_title_label.setObjectName('info_title_label')
    info_index_name_label.setObjectName('info_index_name_label')
    info_name_name_label.setObjectName('info_name_name_label')
    info_capitalization_name_label.setObjectName('info_capitalization_name_label')
    self.object_statistics_widget.setObjectName('object_statistics_widget')
    statistics_population_name_label.setObjectName('statisctics_population_name_label')
    statistics_population_value_label.setObjectName('statisctics_population_value_label')
    statistics_capital_name_label.setObjectName('statisctics_capital_name_label')
    statistics_capital_value_label.setObjectName('statisctics_capital_value_label')
    statistics_timezone_name_label.setObjectName('statisctics_timezone_name_label')
    statistics_timezone_value_label.setObjectName('statisctics_timezone_value_label')
    statistics_currency_name_label.setObjectName('statisctics_currency_name_label')
    statistics_currency_value_label.setObjectName('statisctics_currency_value_label')
#______________________________________________________________________________________________________________________
    """ Set property """
    statistics_population_name_label.setProperty('class', 'object_statistics_name_label')
    statistics_capital_name_label.setProperty('class', 'object_statistics_name_label')
    statistics_timezone_name_label.setProperty('class', 'object_statistics_name_label')
    statistics_currency_name_label.setProperty('class', 'object_statistics_name_label')
    statistics_population_value_label.setProperty('class', 'object_statistics_value_label')
    statistics_capital_value_label.setProperty('class', 'object_statistics_value_label')
    statistics_timezone_value_label.setProperty('class', 'object_statistics_value_label')
    statistics_currency_value_label.setProperty('class', 'object_statistics_value_label')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.layout.addWidget(self.object_time_widget, 6, 13, 3, 38)
    self.layout.addWidget(self.object_info_widget, 10, 13, 32, 38)
    self.object_info_layout.addWidget(info_title_label, 0, 0, 10, 100)
    self.object_info_layout.addWidget(info_index_name_label, 10, 0, 10, 10)
    self.object_info_layout.addWidget(info_name_name_label, 10, 10, 10, 45)
    self.object_info_layout.addWidget(info_capitalization_name_label, 10, 55, 10, 45)
    self.object_info_layout.setSpacing(0)
    self.object_info_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.object_info_layout.setRowStretch(enc, 1)
        self.object_info_layout.setColumnStretch(enc, 1)
    self.object_info_widget.setLayout(self.object_info_layout)
    self.layout.addWidget(self.object_statistics_widget, 55, 13, 32, 38)
    self.object_statistics_layout.addWidget(statistics_population_name_label,0,0)
    self.object_statistics_layout.addWidget(statistics_population_value_label,0,1)
    self.object_statistics_layout.addWidget(statistics_capital_name_label,1,0)
    self.object_statistics_layout.addWidget(statistics_capital_value_label,1,1)
    self.object_statistics_layout.addWidget(statistics_timezone_name_label,2,0)
    self.object_statistics_layout.addWidget(statistics_timezone_value_label,2,1)
    self.object_statistics_layout.addWidget(statistics_currency_name_label,3,0)
    self.object_statistics_layout.addWidget(statistics_currency_value_label,3,1)
    self.object_statistics_layout.setSpacing(0)
    self.object_statistics_layout.setContentsMargins(0,0,0,0)
    self.object_statistics_widget.setLayout(self.object_statistics_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
#______________________________________________________________________________________________________________________
    """ Set label """
    info_title_label.setAlignment(Qt.AlignCenter)
    info_index_name_label.setAlignment(Qt.AlignCenter)
    info_name_name_label.setAlignment(Qt.AlignCenter)
    info_capitalization_name_label.setAlignment(Qt.AlignCenter)
    statistics_population_name_label.setAlignment(Qt.AlignCenter)
    statistics_population_value_label.setAlignment(Qt.AlignCenter)
    statistics_capital_name_label.setAlignment(Qt.AlignCenter)
    statistics_capital_value_label.setAlignment(Qt.AlignCenter)
    statistics_timezone_name_label.setAlignment(Qt.AlignCenter)
    statistics_timezone_value_label.setAlignment(Qt.AlignCenter)
    statistics_currency_name_label.setAlignment(Qt.AlignCenter)
    statistics_currency_value_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.object_time_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_info_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_index_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_name_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_capitalization_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_statistics_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_population_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_population_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_capital_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_capital_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_timezone_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_timezone_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_currency_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_currency_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r')) # Translate texts.
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['__language__'] # Language.
    self.object_name_label.setText(country_data[0])
    info_title_label.setText(f'{_t['info_title_label'][_l]}:')
    info_index_name_label.setText('#')
    info_name_name_label.setText(f'{_t['info_name_name_label'][_l]}:')
    info_capitalization_name_label.setText(f'{_t['info_capitalization_name_label'][_l]}:')
    statistics_population_name_label.setText(f'{_t['statistics_population_name_label'][_l]}:')
    statistics_population_value_label.setText(str(country_data[5]))
    statistics_capital_name_label.setText(f'{_t['statistics_capital_name_label'][_l]}:')
    statistics_capital_value_label.setText(str(country_data[2]))
    statistics_timezone_name_label.setText(f'{_t['statistics_timezone_name_label'][_l]}:')
    statistics_timezone_value_label.setText(str(country_data[4]))
    statistics_currency_name_label.setText(f'{_t['statistics_currency_name_label'][_l]}:')
    statistics_currency_value_label.setText(str(country_data[3]))
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.object_icon_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+country_data[1]+'.svg', int(self.object_icon_label.height()), int(self.object_icon_label.height())))
#______________________________________________________________________________________________________________________
    """ Create info list """

#######################################################################################################################
""" object market """
def object_market(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    """ Get data """
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
    cursor = database.cursor() # Create cursor 
    market_data = cursor.execute(f'''
    SELECT
    market.name, 
    market.short_name,
    market.icon,
    market.city, 
    market.website, 
    market.founded_date,
    market.capitalization,
    market.pre_open_time,
    market.open_time,
    market.close_time,
    market.post_close_time,
    timezone.id
    FROM market
    JOIN country ON market.id_country=country.id
    JOIN timezone ON country.id_timezone=timezone.id
    WHERE market.id={_global_config['object'][1]};''').fetchall()[0] # Execute
    cursor.close()
    database.close()
#______________________________________________________________________________________________________________________
    """ Create """
    if self.object_statistics_widget:
        self.object_statistics_widget.deleteLater()
        self.object_statistics_widget = None 
    self.object_statistics_widget = QWidget(self)
    self.object_statistics_layout = QGridLayout(self.object_statistics_widget)
    if self.object_time_widget:
        self.object_time_widget.deleteLater()
        self.object_time_widget = None
    self.object_time_widget = QWidget(self)
    time_close_1_label = QLabel(self.object_time_widget)
    time_pre_open_label = QLabel(self.object_time_widget)
    time_open_label = QLabel(self.object_time_widget)
    time_post_close_label = QLabel(self.object_time_widget)
    time_close_2_label = QLabel(self.object_time_widget)
    time_dot_label = QLabel(self.object_time_widget)
    capitalization_name_label = QLabel(self.object_statistics_widget)
    capitalization_value_label = QLabel(self.object_statistics_widget)
    city_name_label = QLabel(self.object_statistics_widget)
    city_value_label = QLabel(self.object_statistics_widget)
    founded_date_name_label = QLabel(self.object_statistics_widget)
    founded_data_value_label = QLabel(self.object_statistics_widget)
    website_name_label = QLabel(self.object_statistics_widget)
    website_value_label = QLabel(self.object_statistics_widget)
#______________________________________________________________________________________________________________________
    """ Setup """
    """ Set object name """
    self.object_statistics_widget.setObjectName('object_statistics_widget')
    self.object_time_widget.setObjectName('object_time_widget')
    time_close_1_label.setObjectName('time_close_1_label')
    time_pre_open_label.setObjectName('time_pre_open_label')
    time_open_label.setObjectName('time_open_label')
    time_post_close_label.setObjectName('time_post_close_label')
    time_close_2_label.setObjectName('time_close_2_label')
    time_dot_label.setObjectName('time_dot_label')
    capitalization_name_label.setObjectName('capitalization_name_label')
    capitalization_value_label.setObjectName('capitalization_value_label')
    city_name_label.setObjectName('city_name_label')
    city_value_label.setObjectName('city_value_label')
    founded_date_name_label.setObjectName('founded_date_name_label')
    founded_data_value_label.setObjectName('founded_data_value_label')
    website_name_label.setObjectName('website_name_label')
    website_value_label.setObjectName('website_value_label')
#______________________________________________________________________________________________________________________
    """ Set property """
    capitalization_name_label.setProperty('class', 'object_statistics_name_label')
    city_name_label.setProperty('class', 'object_statistics_name_label')
    founded_date_name_label.setProperty('class', 'object_statistics_name_label')
    website_name_label.setProperty('class', 'object_statistics_name_label')
    capitalization_value_label.setProperty('class', 'object_statistics_value_label')
    city_value_label.setProperty('class', 'object_statistics_value_label')
    founded_data_value_label.setProperty('class', 'object_statistics_value_label')
    website_value_label.setProperty('class', 'object_statistics_value_label')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.layout.addWidget(self.object_time_widget, 14, 13, 5, 38)
    self.layout.addWidget(self.object_statistics_widget, 50, 13, 40, 38)
    self.object_statistics_layout.addWidget(capitalization_name_label,0,0)
    self.object_statistics_layout.addWidget(capitalization_value_label,0,1)
    self.object_statistics_layout.addWidget(city_name_label,1,0)
    self.object_statistics_layout.addWidget(city_value_label,1,1)
    self.object_statistics_layout.addWidget(founded_date_name_label,2,0)
    self.object_statistics_layout.addWidget(founded_data_value_label,2,1)
    self.object_statistics_layout.addWidget(website_name_label,3,0)
    self.object_statistics_layout.addWidget(website_value_label,3,1)
    self.object_statistics_layout.setSpacing(0)
    self.object_statistics_layout.setContentsMargins(0,0,0,0)
    self.object_statistics_widget.setLayout(self.object_statistics_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
#______________________________________________________________________________________________________________________
    """ Set label """
    capitalization_name_label.setAlignment(Qt.AlignCenter)
    capitalization_value_label.setAlignment(Qt.AlignCenter)
    city_name_label.setAlignment(Qt.AlignCenter)
    city_value_label.setAlignment(Qt.AlignCenter)
    founded_date_name_label.setAlignment(Qt.AlignCenter)
    founded_data_value_label.setAlignment(Qt.AlignCenter)
    website_name_label.setAlignment(Qt.AlignCenter)
    website_value_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.object_time_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_statistics_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    capitalization_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    capitalization_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    city_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    city_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    founded_date_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    founded_data_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    website_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    website_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r')) # Translate texts.
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['__language__'] # Language.
    self.object_ticker_label.setText(market_data[1])
    self.object_name_label.setText(market_data[0])
    capitalization_name_label.setText(f'{_t['capitalization_name_label'][_l]}:')
    capitalization_value_label.setText(market_data[6])
    city_name_label.setText(f'{_t['city_name_label'][_l]}:')
    city_value_label.setText(market_data[3])
    founded_date_name_label.setText(f'{_t['founded_date_name_label'][_l]}:')
    founded_data_value_label.setText(market_data[5])
    website_name_label.setText(f'{_t['website_name_label'][_l]}:')
    website_value_label.setText(market_data[4])
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.object_icon_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+market_data[2]+'.svg', int(self.width()*0.3), int(self.width()*0.3)))
#______________________________________________________________________________________________________________________
    """ Setup time widget """
    #total_sec = 86400
    #pre_open_time = int(market_data[7])
    #open_time = int(market_data[8])
    #close_time = int(market_data[9])
    #post_close_time = int(market_data[10])
    #margins_x = int(self.main_time_widget.width()*0.05)
    #pos_y = int(self.main_time_widget.height()*0.45)
    #width = int(self.main_time_widget.width()-margins_x)
    #height = int(self.main_time_widget.height()*0.1)

    #close_1_pos = int(0+(margins_x//2)) # Pos
    #close_1_width = int((pre_open_time/total_sec)*width) # Width
    #pre_open_time_pos = int(close_1_pos+close_1_width) # Pos
    #pre_open_time_width = int(((open_time-pre_open_time)/total_sec)*width) # Width
    #open_time_pos = int(pre_open_time_pos+pre_open_time_width) # Pos
    #open_time_width = int(((close_time-pre_open_time)/total_sec)*width) # Width
    #post_close_pos = int(open_time_pos+open_time_width) # Pos
    #post_close_width = int(((post_close_time-close_time)/total_sec)*width) # Width
    #close_2_pos = int(post_close_pos+post_close_width) # Pos
    #close_2_width = int(width-close_1_width-pre_open_time_width-open_time_width-post_close_width) # Width
    
    #close_1_label.setGeometry(QRect(close_1_pos, int(pos_y), close_1_width, int(height)))
    #pre_open_label.setGeometry(QRect(pre_open_time_pos, int(pos_y), pre_open_time_width, int(height)))
    #open_label.setGeometry(QRect(open_time_pos, int(pos_y), open_time_width, int(height)))
    #post_close_label.setGeometry(QRect(post_close_pos, int(pos_y), post_close_width, int(height)))
    #close_2_label.setGeometry(QRect(close_2_pos, int(pos_y), close_2_width, int(height)))
    #dot_label.setFixedSize(QSize(int(height*1.5), int(height*1.5)))

    #self.main_time_timer = QTimer(self.main_time_widget)
    #self.main_time_timer.timeout.connect(lambda w=width, h=pos_y: update_dot(self, w, h))
    #self.main_time_timer.start(1000)
#######################################################################################################################
""" object index """
def object_index(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    """ Get data """
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
    cursor = database.cursor() # Create cursor 
    index_data = cursor.execute(f'''
    SELECT
    market_index.name, 
    market_index.icon 
    FROM market_index 
    WHERE market_index.id={self.global_config['object'][1]};''').fetchall()[0] # Execute
    objects_of_index = cursor.execute(f'''
    SELECT 
    stock.icon, 
    stock.ticker
    FROM stock
    JOIN index_stock ON stock.id=index_stock.id_stock
    WHERE index_stock.id_index={_global_config['object'][1]};''').fetchall() # Execute
    cursor.close()
    database.close()
    chart_data = json.load(open(self.main_path+f'/CHART_DATA/{index_data[0]}_15.json', 'r'))
#______________________________________________________________________________________________________________________
    """ Create """
    if self.object_statistics_widget:
        self.object_statistics_widget.deleteLater()
        self.object_statistics_widget = None 
    self.object_statistics_widget = QWidget(self)
    self.object_statistics_layout = QGridLayout(self.object_statistics_widget)
    index_label = QLabel(self.object_statistics_widget)
    ticker_label = QLabel(self.object_statistics_widget)
    icon_blank_label = QLabel(self.object_statistics_widget)
    stocks_scroll = QScrollArea(self.object_statistics_widget)
    stocks_widget = QWidget(stocks_scroll)
    stocks_layout = QGridLayout(stocks_widget)
#______________________________________________________________________________________________________________________
    """ Setup widget """
    """ Set object name """
    self.object_statistics_widget.setObjectName('object_statistics_widget')
    index_label.setObjectName('index_label')
    ticker_label.setObjectName('ticker_label')
    icon_blank_label.setObjectName('icon_blank_label')
    stocks_scroll.setObjectName('stocks_scroll')
    stocks_widget.setObjectName('stocks_widget')
#______________________________________________________________________________________________________________________
    """ Set property """
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.object_statistics_layout.addWidget(index_label, 0, 0, 10, 10)
    self.object_statistics_layout.addWidget(ticker_label,0, 10, 10, 70)
    self.object_statistics_layout.addWidget(icon_blank_label,0, 80, 10, 20)
    self.object_statistics_layout.addWidget(stocks_scroll, 10, 0, 90, 100)
    self.object_statistics_layout.setSpacing(0)
    self.object_statistics_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.object_statistics_layout.setRowStretch(enc, 1)
        self.object_statistics_layout.setColumnStretch(enc,1)
    self.object_statistics_widget.setLayout(self.object_statistics_layout)
    stocks_layout.setSpacing(0)
    stocks_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        stocks_layout.setColumnStretch(enc, 1)
    stocks_widget.setLayout(stocks_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    stocks_scroll.setWidgetResizable(True)
    stocks_scroll.setWidget(stocks_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
    index_label.setAlignment(Qt.AlignCenter)
    ticker_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.object_statistics_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    index_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    ticker_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    icon_blank_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    stocks_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    stocks_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r')) # Translate texts.
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['__language__'] # Language.
    index_label.setText('#')
    ticker_label.setText(_t['ticker_label'][_l])
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.object_icon_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+index_data[1]+'.svg', int(self.width()*0.3), int(self.width()*0.3)))
#______________________________________________________________________________________________________________________
    """ Creat stocks list"""
    for row, item_list in enumerate(objects_of_index, start=0):
        """ Create objects """
        stock_index_label = QLabel(stocks_widget)
        stock_ticker_label = QLabel(stocks_widget)
        stock_logo_label = QLabel(stocks_widget)
        """ Set object name """
        stock_index_label.setObjectName(f'stokc_index_{row}_label')
        stock_ticker_label.setObjectName(f'stock_ticker_{row}_label')
        stock_logo_label.setObjectName(f'stock_logo_{row}_label')
        """ Set property """
        stock_index_label.setProperty('class', 'index_label')
        stock_ticker_label.setProperty('class', 'ticker_label')
        stock_logo_label.setProperty('class', 'logo_label')
        """ Set layout """
        stocks_layout.addWidget(stock_index_label, row, 0, 1, 10)
        stocks_layout.addWidget(stock_ticker_label, row, 10, 1, 70)
        stocks_layout.addWidget(stock_logo_label, row, 80, 1, 20)
        """ Set label """
        stock_index_label.setAlignment(Qt.AlignCenter)
        stock_ticker_label.setAlignment(Qt.AlignCenter)
        stock_logo_label.setAlignment(Qt.AlignCenter)
        """ Set size """
        stock_index_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        stock_ticker_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        stock_logo_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        """ Set text """
        stock_index_label.setText(f'{row+1}.')
        stock_ticker_label.setText(item_list[1])
        """ Set graphic """
        stock_logo_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+item_list[0]+'.svg', item_label.height(), item_label.height()))
#######################################################################################################################
""" object stock """
def object_stock(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
    """ Get data """
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
    cursor = database.cursor() # Create cursor 
    stock_data = cursor.execute(f'''
    SELECT
    stock.name,
    stock.ticker,
    stock.icon,
    stock.capitalization,
    stock.pe_ratio,
    stock.eps,
    stock.dividend_yield
    FROM stock
    WHERE stock.id={_global_config['object'][1]};''').fetchall()[0] # Execute
    cursor.close()
    database.close()
    chart_data = json.load(open(self.main_path+f'/CHART_DATA/{stock_data[1]}_15.json', 'r'))
#______________________________________________________________________________________________________________________
    """ Create """
    if self.object_statistics_widget:
        self.object_statistics_widget.deleteLater()
        self.object_statistics_widget = None 
    self.object_statistics_widget = QWidget(self)
    self.object_statistics_layout = QGridLayout(self.object_statistics_widget)
    capitalization_name_label = QLabel(self.object_statistics_widget)
    capitalization_value_label = QLabel(self.object_statistics_widget)
    pe_ratio_name_label = QLabel(self.object_statistics_widget)
    pe_ratio_value_label = QLabel(self.object_statistics_widget)
    eps_name_label = QLabel(self.object_statistics_widget)
    eps_value_label = QLabel(self.object_statistics_widget)
    dividend_yield_name_label = QLabel(self.object_statistics_widget)
    dividend_yield_value_label = QLabel(self.object_statistics_widget)
#______________________________________________________________________________________________________________________
    """ Setup widget """
    """ Set object name """
    self.object_statistics_widget.setObjectName('object_statistics_widget')
    capitalization_name_label.setObjectName('capitalization_name_label')
    capitalization_value_label.setObjectName('capitalization_value_label')
    pe_ratio_name_label.setObjectName('pe_ratio_name_label')
    pe_ratio_value_label.setObjectName('pe_ratio_value_label')
    eps_name_label.setObjectName('eps_name_label')
    eps_value_label.setObjectName('eps_value_label')
    dividend_yield_name_label.setObjectName('dividend_yield_name_label')
    dividend_yield_value_label.setObjectName('dividend_yield_value_label')
#______________________________________________________________________________________________________________________
    """ Set property """
    capitalization_name_label.setProperty('class', 'object_statistics_name_label')
    pe_ratio_name_label.setProperty('class', 'object_statistics_name_label')
    eps_name_label.setProperty('class', 'object_statistics_name_label')
    dividend_yield_name_label.setProperty('class', 'object_statistics_name_label')
    capitalization_value_label.setProperty('class', 'object_statistics_value_label')
    pe_ratio_value_label.setProperty('class', 'object_statistics_value_label')
    eps_value_label.setProperty('class', 'object_statistics_value_label')
    dividend_yield_value_label.setProperty('class', 'object_statistics_value_label')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.object_statistics_layout.addWidget(capitalization_name_label,0,0)
    self.object_statistics_layout.addWidget(capitalization_value_label,0,1)
    self.object_statistics_layout.addWidget(pe_ratio_name_label,1,0)
    self.object_statistics_layout.addWidget(pe_ratio_value_label,1,1)
    self.object_statistics_layout.addWidget(eps_name_label,2,0)
    self.object_statistics_layout.addWidget(eps_value_label,2,1)
    self.object_statistics_layout.addWidget(dividend_yield_name_label,3,0)
    self.object_statistics_layout.addWidget(dividend_yield_value_label,3,1)
    self.object_statistics_layout.setSpacing(0)
    self.object_statistics_layout.setContentsMargins(0,0,0,0)
    self.object_statistics_widget.setLayout(self.object_statistics_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
#______________________________________________________________________________________________________________________
    """ Set label """
    capitalization_name_label.setAlignment(Qt.AlignCenter)
    capitalization_value_label.setAlignment(Qt.AlignCenter)
    pe_ratio_name_label.setAlignment(Qt.AlignCenter)
    pe_ratio_value_label.setAlignment(Qt.AlignCenter)
    eps_name_label.setAlignment(Qt.AlignCenter)
    eps_value_label.setAlignment(Qt.AlignCenter)
    dividend_yield_name_label.setAlignment(Qt.AlignCenter)
    dividend_yield_value_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.object_statistics_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    capitalization_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    capitalization_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    pe_ratio_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    pe_ratio_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    eps_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    eps_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    dividend_yield_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    dividend_yield_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r')) # Translate texts.
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['__language__'] # Language.
    self.object_ticker_label.setText(stock_data[1])
    self.object_name_label.setText(stock_data[0])
    capitalization_name_label.setText(f'{_t['capitalization_name_label'][_l]}:')
    capitalization_value_label.setText(stock_data[3])
    pe_ratio_name_label.setText(f'{_t['pe_ratio_name_label'][_l]}:')
    pe_ratio_value_label.setText(stock_data[4])
    eps_name_label.setText(f'{_t['eps_name_label'][_l]}:')
    eps_value_label.setText(stock_data[5])
    dividend_yield_name_label.setText(f'{_t['dividend_yield_name_label'][_l]}:')
    dividend_yield_value_label.setText(stock_data[6])
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.object_icon_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+stock_data[2]+'.svg', int(self.width()*0.3), int(self.width()*0.3)))
#######################################################################################################################
""" news creator """
def news_creator(self):
    _news_button_list = self.news_button_list # Get local data.
    connect = mysql.connector.connect( # Create connect with database
        host = "localhost",
        user = "client",
        password = "Qwerty123456#",
        database = "TickerK8"
    )
    cursor = connect.cursor() # Create cursor
    cursor.execute('SELECT id, json_file FROM news ORDER BY date DESC LIMIT 3;')
    news_list = cursor.fetchall()
    for index, data in enumerate(news_list, start=1):
        json_data = json.loads(data[1])
        news_id = data[0]
        """ Create objects """
        news_button = QPushButton(self)
        news_layout = QVBoxLayout(news_button)
        news_text_label = QLabel(news_button)
#______________________________________________________________________________________________________________________
        """ Set object name """
        news_button.setObjectName(f'news_button_{index}')
        news_text_label.setObjectName(f'text_label_{index}')
#______________________________________________________________________________________________________________________
        """ Set property """
        news_button.setProperty('class', 'news_button')
        news_text_label.setProperty('class', 'news_text_label')
#______________________________________________________________________________________________________________________
        """ Set layout """
        self.layout.addWidget(news_button, 2, 52, 85, 47)
        news_layout.addWidget(news_text_label)  
        news_layout.setContentsMargins(0,0,0,0)
        news_layout.setSpacing(0)
#______________________________________________________________________________________________________________________
        """ Set Widget """
        news_button.setHidden(True)
#______________________________________________________________________________________________________________________
        """ Set label """
        news_text_label.setAlignment(Qt.AlignCenter)
        news_text_label.setWordWrap(True)
#______________________________________________________________________________________________________________________
        """ Set size """
        news_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        news_text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        news_text_label.setGeometry(QRect(0,0,news_button.width(),news_button.height()))
#______________________________________________________________________________________________________________________
        """ Set text """
        news_text_label.setText(json_data['title'])
#______________________________________________________________________________________________________________________
        """ Set graphics """
        #photo = requests.get(json_data["photo"]["original"])
        #photo.raise_for_status()
        #pix = QPixmap()
        #pix.loadFromData(BytesIO(photo.content).read())

        #zoomed_pix = pix.scaled(news_button.width(), news_button.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        #cropped_pix = zoomed_pix.copy(
        #    (zoomed_pix.width() - news_button.width()) // 2,
        #    (zoomed_pix.height() - news_button.height()) // 2,
        #    news_button.width(),
        #    news_button.height()
        #)
        #news_button.setIcon(QIcon(cropped_pix))
        #news_button.setIconSize(news_button.size())
#______________________________________________________________________________________________________________________
        """ Set connect function for open """
#______________________________________________________________________________________________________________________
        _news_button_list.append(news_button)
    self.news_button_list = _news_button_list
    self.news_button_list[self.news_button_index].setHidden(False)
    self.news_timer.timeout.connect(lambda: news_next(self))
    self.news_timer.start(5000)
#######################################################################################################################
""" news next  """
def news_next(self):
    self.news_timer.stop()
    self.news_timer.start(5000)
    self.news_button_list[self.news_button_index].setHidden(True)
    self.news_button_index = (self.news_button_index+1)%len(self.news_button_list)
    self.news_button_list[self.news_button_index].setHidden(False)
#######################################################################################################################
""" News previous """
def news_previous(self):
    self.news_timer.stop()
    self.news_timer.start(5000)
    self.news_button_list[self.news_button_index].setHidden(True)
    self.news_button_index = (self.news_button_index-1)%len(self.news_button_list)
    self.news_button_list[self.news_button_index].setHidden(False)
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