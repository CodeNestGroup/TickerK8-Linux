""" Import """
import json
import sqlite3
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QScrollArea, # Scroll widget
    QGridLayout, # Grid layout
    QVBoxLayout, # Vertical layout 
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 QtCore """
from PyQt5.QtCore import (
    Qt,
    QSize,
    QRect,
    QTimer,
    QTime
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (QPixmap, # Graphic.
                         QPainter) # Painter.
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
#######################################################################################################################
""" Setup widget """
def setup_widget(self):
    self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Reload global config
    if self.global_config['mid_object'][0] == 'country':
        country_widget(self)
    elif self.global_config['mid_object'][0] == 'market':
        market_widget(self)
    elif self.global_config['mid_object'][0] == 'market_index':
        index_widget(self)
    elif self.global_config['mid_object'][0] == 'stock':
        stock_widget(self)
#######################################################################################################################
""" Country widget """
def country_widget(self):
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
    WHERE country.id=={self.global_config['mid_object'][1]};''').fetchall()[0] # Execute
    cursor.close()
    database.close()
#______________________________________________________________________________________________________________________
    """ Setup widget """
    if self.main_widget:
        self.main_widget.deleteLater()
        self.main_widget = None
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.main_widget = QWidget(self.main_scroll)
    self.main_layout = QGridLayout(self.main_widget)
    self.main_flag_label = QLabel(self.main_widget)
    self.main_name_label = QLabel(self.main_widget)
    self.main_timezone_label = QLabel(self.main_widget)
    self.main_statistics_widget = QWidget(self.main_widget)
    self.main_statistics_layout = QGridLayout(self.main_statistics_widget)
    self.main_population_name_label = QLabel(self.main_statistics_widget)
    self.main_population_value_label = QLabel(self.main_statistics_widget)
    self.main_capital_name_label = QLabel(self.main_statistics_widget)
    self.main_capital_value_label = QLabel(self.main_statistics_widget)
    self.main_currecny_name_label = QLabel(self.main_statistics_widget)
    self.main_currency_value_label = QLabel(self.main_statistics_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.main_widget.setObjectName('main_widget')
    self.main_flag_label.setObjectName('main_flag_label')
    self.main_name_label.setObjectName('main_name_label')
    self.main_timezone_label.setObjectName('main_timezone_label')
    self.main_statistics_widget.setObjectName('main_statistics_widget')
    self.main_population_name_label.setObjectName('main_population_name_label')
    self.main_population_value_label.setObjectName('main_population_value_label')
    self.main_capital_name_label.setObjectName('main_capital_name_label')
    self.main_capital_value_label.setObjectName('main_capital_value_label')
    self.main_currecny_name_label.setObjectName('main_currecny_name_label')
    self.main_currency_value_label.setObjectName('main_currency_value_label')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.main_population_name_label.setProperty('class', 'main_name_label')
    self.main_population_value_label.setProperty('class', 'main_value_label')
    self.main_capital_name_label.setProperty('class', 'main_name_label')
    self.main_capital_value_label.setProperty('class', 'main_value_label')
    self.main_currecny_name_label.setProperty('class', 'main_name_label')
    self.main_currency_value_label.setProperty('class', 'main_value_label')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.main_flag_label,0,0)
    self.main_layout.addWidget(self.main_name_label,1,0)
    self.main_layout.addWidget(self.main_timezone_label,2,0)
    self.main_layout.addWidget(self.main_statistics_widget,3,0)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    self.main_widget.setLayout(self.main_layout)
    self.main_statistics_layout.addWidget(self.main_population_name_label,0,0)
    self.main_statistics_layout.addWidget(self.main_population_value_label,0,1)
    self.main_statistics_layout.addWidget(self.main_capital_name_label,1,0)
    self.main_statistics_layout.addWidget(self.main_capital_value_label,1,1)
    self.main_statistics_layout.addWidget(self.main_currecny_name_label,2,0)
    self.main_statistics_layout.addWidget(self.main_currency_value_label,2,1)
    self.main_statistics_layout.setSpacing(0)
    self.main_statistics_layout.setContentsMargins(0,0,0,0)
    self.main_statistics_widget.setLayout(self.main_statistics_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.main_scroll.setWidget(self.main_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.main_flag_label.setAlignment(Qt.AlignCenter)
    self.main_name_label.setAlignment(Qt.AlignCenter)
    self.main_timezone_label.setAlignment(Qt.AlignCenter)
    self.main_population_name_label.setAlignment(Qt.AlignCenter)
    self.main_population_value_label.setAlignment(Qt.AlignCenter)
    self.main_capital_name_label.setAlignment(Qt.AlignCenter)
    self.main_capital_value_label.setAlignment(Qt.AlignCenter)
    self.main_currecny_name_label.setAlignment(Qt.AlignCenter)
    self.main_currency_value_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.main_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_flag_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_timezone_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_statistics_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_population_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_population_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_capital_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_capital_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_currecny_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_currency_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    self.main_name_label.setText(f'{country_data[0]}')
    self.main_timezone_label.setText(f'{country_data[4]}')
    self.main_population_name_label.setText(f'{self.translate['main_population_name_label'][self.global_config['__language__']]}:')
    self.main_population_value_label.setText(f'{country_data[5]}')
    self.main_capital_name_label.setText(f'{self.translate['main_capital_name_label'][self.global_config['__language__']]}:')
    self.main_capital_value_label.setText(f'{country_data[2]}')
    self.main_currecny_name_label.setText(f'{self.translate['main_currecny_name_label'][self.global_config['__language__']]}:')
    self.main_currency_value_label.setText(f'{country_data[3]}')
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.main_flag_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+country_data[1]+'.svg', int(self.width()*0.3), int(self.width()*0.3)))
#######################################################################################################################
""" Market widget"""
def market_widget(self):
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
    WHERE market.id={self.global_config['mid_object'][1]};''').fetchall()[0] # Execute
    cursor.close()
    database.close()
#______________________________________________________________________________________________________________________
    """ Setup widget """
    if self.main_widget:
        self.main_widget.deleteLater()
        self.main_widget = None
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.main_widget = QWidget(self.main_scroll)
    self.main_layout = QGridLayout(self.main_widget)
    self.main_icon_label = QLabel(self.main_widget)
    self.main_short_name_label = QLabel(self.main_widget)
    self.main_name_label = QLabel(self.main_widget)
    self.main_time_widget = QWidget(self.main_widget)
    self.main_time_close_1_label= QLabel(self.main_time_widget)
    self.main_time_pre_open_label= QLabel(self.main_time_widget)
    self.main_time_open_label= QLabel(self.main_time_widget)
    self.main_time_post_close_label= QLabel(self.main_time_widget)
    self.main_time_close_2_label= QLabel(self.main_time_widget)
    self.main_time_dot_label = QLabel(self.main_time_widget)
    self.main_statistics_widget = QWidget(self.main_widget)
    self.main_statistics_layout = QGridLayout(self.main_statistics_widget)
    self.main_capitalization_name_label = QLabel(self.main_statistics_widget)
    self.main_capitalization_value_label = QLabel(self.main_statistics_widget)
    self.main_city_name_label = QLabel(self.main_statistics_widget)
    self.main_city_value_label = QLabel(self.main_statistics_widget)
    self.main_founded_date_name_label = QLabel(self.main_statistics_widget)
    self.main_founded_date_value_label = QLabel(self.main_statistics_widget)
    self.main_website_name_label = QLabel(self.main_statistics_widget)
    self.main_website_value_label = QLabel(self.main_statistics_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.main_widget.setObjectName('main_widget')
    self.main_icon_label.setObjectName('main_icon_label')
    self.main_short_name_label.setObjectName('main_short_name_label')
    self.main_name_label.setObjectName('main_name_label')
    self.main_time_widget.setObjectName('main_time_widget')
    self.main_time_close_1_label.setObjectName('main_time_close_1_label')
    self.main_time_pre_open_label.setObjectName('main_time_pre_open_label')
    self.main_time_open_label.setObjectName('main_time_open_label')
    self.main_time_post_close_label.setObjectName('main_time_post_close_label')
    self.main_time_close_2_label.setObjectName('main_time_close_2_label')
    self.main_time_dot_label.setObjectName('main_time_dot_label')
    self.main_statistics_widget.setObjectName('main_statistics_widget')
    self.main_capitalization_name_label.setObjectName('main_capitalization_name_label')
    self.main_capitalization_value_label.setObjectName('main_capitalization_value_label')
    self.main_city_name_label.setObjectName('main_city_name_label')
    self.main_city_value_label.setObjectName('main_city_value_label')
    self.main_founded_date_name_label.setObjectName('main_founded_date_name_label')
    self.main_founded_date_value_label.setObjectName('main_founded_date_value_label')
    self.main_website_name_label.setObjectName('main_website_name_label')
    self.main_website_value_label.setObjectName('main_website_value_label')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.main_capitalization_name_label.setProperty('class', 'main_name_label')
    self.main_capitalization_value_label.setProperty('class', 'main_value_label')
    self.main_city_name_label.setProperty('class', 'main_name_label')
    self.main_city_value_label.setProperty('class', 'main_value_label')
    self.main_founded_date_name_label.setProperty('class', 'main_name_label')
    self.main_founded_date_value_label.setProperty('class', 'main_value_label')
    self.main_website_name_label.setProperty('class', 'main_name_label')
    self.main_website_value_label.setProperty('class', 'main_value_label')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.main_icon_label,0,0)
    self.main_layout.addWidget(self.main_short_name_label,1,0)
    self.main_layout.addWidget(self.main_name_label,2,0)
    self.main_layout.addWidget(self.main_time_widget,3,0)
    self.main_layout.addWidget(self.main_statistics_widget,4,0)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    self.main_widget.setLayout(self.main_layout)
    self.main_statistics_layout.addWidget(self.main_capitalization_name_label, 0, 0)
    self.main_statistics_layout.addWidget(self.main_capitalization_value_label, 0, 1)
    self.main_statistics_layout.addWidget(self.main_city_name_label, 1, 0)
    self.main_statistics_layout.addWidget(self.main_city_value_label, 1, 1)
    self.main_statistics_layout.addWidget(self.main_founded_date_name_label, 2, 0)
    self.main_statistics_layout.addWidget(self.main_founded_date_value_label, 2, 1)
    self.main_statistics_layout.addWidget(self.main_website_name_label, 3, 0)
    self.main_statistics_layout.addWidget(self.main_website_value_label, 3, 1)
    self.main_statistics_layout.setSpacing(0)
    self.main_statistics_layout.setContentsMargins(0,0,0,0)
    self.main_statistics_widget.setLayout(self.main_statistics_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.main_scroll.setWidget(self.main_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.main_icon_label.setAlignment(Qt.AlignCenter)
    self.main_short_name_label.setAlignment(Qt.AlignCenter)
    self.main_name_label.setAlignment(Qt.AlignCenter)
    self.main_capitalization_name_label.setAlignment(Qt.AlignCenter)
    self.main_capitalization_value_label.setAlignment(Qt.AlignCenter)
    self.main_city_name_label.setAlignment(Qt.AlignCenter)
    self.main_city_value_label.setAlignment(Qt.AlignCenter)
    self.main_founded_date_name_label.setAlignment(Qt.AlignCenter)
    self.main_founded_date_value_label.setAlignment(Qt.AlignCenter)
    self.main_website_name_label.setAlignment(Qt.AlignCenter)
    self.main_website_value_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.main_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_icon_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_short_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_time_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_time_close_1_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_time_pre_open_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_time_open_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_time_post_close_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_time_close_2_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_time_dot_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_statistics_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_capitalization_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_capitalization_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_city_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_city_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_founded_date_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_founded_date_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_website_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_website_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    self.main_short_name_label.setText(f'{market_data[1]}')
    self.main_name_label.setText(f'{market_data[0]}')
    self.main_capitalization_name_label.setText(f'{self.translate['main_capitalization_name_label'][self.global_config['__language__']]}:')
    self.main_capitalization_value_label.setText(f'{market_data[6]}')
    self.main_city_name_label.setText(f'{self.translate['main_city_name_label'][self.global_config['__language__']]}:')
    self.main_city_value_label.setText(f'{market_data[3]}')
    self.main_founded_date_name_label.setText(f'{self.translate['main_founded_date_name_label'][self.global_config['__language__']]}:')
    self.main_founded_date_value_label.setText(f'{market_data[5]}')
    self.main_website_name_label.setText(f'{self.translate['main_website_name_label'][self.global_config['__language__']]}:')
    self.main_website_value_label.setText(f'{market_data[4]}')
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.main_icon_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+market_data[2]+'.svg', int(self.width()*0.3), int(self.width()*0.3)))
#______________________________________________________________________________________________________________________
    """ Setup time widget """
    total_sec = 86400
    pre_open_time = int(market_data[7])
    open_time = int(market_data[8])
    close_time = int(market_data[9])
    post_close_time = int(market_data[10])
    margins_x = int(self.main_time_widget.width()*0.05)
    pos_y = int(self.main_time_widget.height()*0.45)
    width = int(self.main_time_widget.width()-margins_x)
    height = int(self.main_time_widget.height()*0.1)

    close_1_pos = int(0+(margins_x//2)) # Pos
    close_1_width = int((pre_open_time/total_sec)*width) # Width
    pre_open_time_pos = int(close_1_pos+close_1_width) # Pos
    pre_open_time_width = int(((open_time-pre_open_time)/total_sec)*width) # Width
    open_time_pos = int(pre_open_time_pos+pre_open_time_width) # Pos
    open_time_width = int(((close_time-pre_open_time)/total_sec)*width) # Width
    post_close_pos = int(open_time_pos+open_time_width) # Pos
    post_close_width = int(((post_close_time-close_time)/total_sec)*width) # Width
    close_2_pos = int(post_close_pos+post_close_width) # Pos
    close_2_width = int(width-close_1_width-pre_open_time_width-open_time_width-post_close_width) # Width
    
    self.main_time_close_1_label.setGeometry(QRect(close_1_pos, int(pos_y), close_1_width, int(height)))
    self.main_time_pre_open_label.setGeometry(QRect(pre_open_time_pos, int(pos_y), pre_open_time_width, int(height)))
    self.main_time_open_label.setGeometry(QRect(open_time_pos, int(pos_y), open_time_width, int(height)))
    self.main_time_post_close_label.setGeometry(QRect(post_close_pos, int(pos_y), post_close_width, int(height)))
    self.main_time_close_2_label.setGeometry(QRect(close_2_pos, int(pos_y), close_2_width, int(height)))
    self.main_time_dot_label.setFixedSize(QSize(int(height*1.5), int(height*1.5)))

    self.main_time_timer = QTimer(self.main_time_widget)
    self.main_time_timer.timeout.connect(lambda w=width, h=pos_y: update_dot(self, w, h))
    self.main_time_timer.start(1000)
#######################################################################################################################
""" Update dot """
def update_dot(self, width, height):
    current_time = QTime.currentTime()
    sec = (
            current_time.hour() * 3600 +
            current_time.minute() * 60 +
            current_time.second()
        )
    total_sec = 86400
    self.main_time_dot_label.move(int((sec/total_sec)*width), int(height*0.95))
#######################################################################################################################
""" Index widget """
def index_widget(self):
    """ Get data """
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
    cursor = database.cursor() # Create cursor 
    market_index_data = cursor.execute(f'''
    SELECT
    market_index.name, 
    market_index.icon 
    FROM market_index 
    WHERE market_index.id={self.global_config['mid_object'][1]};''').fetchall()[0] # Execute
    objects_of_index = cursor.execute(f'''
    SELECT 
    stock.icon, 
    stock.ticker
    FROM stock
    JOIN index_stock ON stock.id=index_stock.id_stock
    WHERE index_stock.id_index={self.global_config['mid_object'][1]};''').fetchall() # Execute
    cursor.close()
    database.close()
#______________________________________________________________________________________________________________________
    """ Setup widget """
    if self.main_widget:
        self.main_widget.deleteLater()
        self.main_widget = None
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.main_widget = QWidget(self.main_scroll)
    self.main_layout = QGridLayout(self.main_widget)
    self.main_icon_label = QLabel(self.main_widget)
    self.main_name_label = QLabel(self.main_widget)
    self.main_chart_widget = QWidget(self.main_widget)
    self.main_objects_scroll = QScrollArea(self.main_widget)
    self.main_objects_widget = QWidget(self.main_objects_scroll)
    self.main_objects_layout = QGridLayout(self.main_objects_widget)
    self.main_objects_index_label = QLabel(self.main_objects_widget)
    self.main_objects_icon_label = QLabel(self.main_objects_widget)
    self.main_objects_ticker_label = QLabel(self.main_objects_widget)
    self.main_statistics_widget = QWidget(self.main_widget)
    self.main_statistics_layout = QGridLayout(self.main_statistics_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.main_widget.setObjectName('main_widget')
    self.main_icon_label.setObjectName('main_icon_label')
    self.main_name_label.setObjectName('main_name_label')
    self.main_chart_widget.setObjectName('main_chart_widget')
    self.main_objects_scroll.setObjectName('main_objects_scroll')
    self.main_objects_widget.setObjectName('main_objects_widget')
    self.main_objects_index_label.setObjectName('main_objects_index_label')
    self.main_objects_icon_label.setObjectName('main_objects_icon_label')
    self.main_objects_ticker_label.setObjectName('main_objects_ticker_label')
    self.main_statistics_widget.setObjectName('main_statistics_widget')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.main_objects_index_label.setProperty('class', 'main_objects_label')
    self.main_objects_icon_label.setProperty('class', 'main_objects_label')
    self.main_objects_ticker_label.setProperty('class', 'main_objects_label')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.main_icon_label,0,0)
    self.main_layout.addWidget(self.main_name_label,1,0)
    self.main_layout.addWidget(self.main_chart_widget,2,0)
    self.main_layout.addWidget(self.main_objects_scroll,3,0)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    self.main_widget.setLayout(self.main_layout)
    self.main_objects_layout.addWidget(self.main_objects_index_label, 0, 0)
    self.main_objects_layout.addWidget(self.main_objects_icon_label, 0, 1)
    self.main_objects_layout.addWidget(self.main_objects_ticker_label, 0, 2)
    self.main_objects_layout.setSpacing(0)
    self.main_objects_layout.setContentsMargins(0,0,0,0)
    self.main_objects_widget.setLayout(self.main_objects_layout)
    self.main_statistics_layout.setSpacing(0)
    self.main_statistics_layout.setContentsMargins(0,0,0,0)
    self.main_statistics_widget.setLayout(self.main_statistics_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.main_scroll.setWidget(self.main_widget)
    self.main_objects_scroll.setWidgetResizable(True)
    self.main_objects_scroll.setWidget(self.main_objects_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.main_icon_label.setAlignment(Qt.AlignCenter)
    self.main_name_label.setAlignment(Qt.AlignCenter)
    self.main_objects_index_label.setAlignment(Qt.AlignCenter)
    self.main_objects_icon_label.setAlignment(Qt.AlignCenter)
    self.main_objects_ticker_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.main_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_icon_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_chart_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_objects_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_objects_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_objects_index_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_objects_icon_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_objects_ticker_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_statistics_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    self.main_name_label.setText(f'{market_index_data[0]}')
    self.main_objects_index_label.setText(f'#')
    self.main_objects_icon_label.setText(self.translate['main_objects_icon_label'][self.global_config['__language__']])
    self.main_objects_ticker_label.setText(self.translate['main_objects_ticker_label'][self.global_config['__language__']])
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.main_icon_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+market_index_data[1]+'.svg', int(self.width()*0.3), int(self.width()*0.3)))
#______________________________________________________________________________________________________________________
    """ Set main objects scroll """
    for row, item_list in enumerate(objects_of_index, start=1):
        index_label = QLabel(self.main_objects_widget)
        index_label.setObjectName(f'index_{row}_label')
        index_label.setProperty('class', 'index_label')
        self.main_objects_layout.addWidget(index_label, row, 0)
        index_label.setAlignment(Qt.AlignCenter)
        index_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        index_label.setText(f'{row}.')
        for column, item in enumerate(item_list, start=1):
            item_label = QLabel(self.main_objects_widget)
            if column == 1:
                item_label.setObjectName(f'item_icon_{column}_label')
                item_label.setProperty('class', 'item_icon_label')
                item_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+item+'.svg', item_label.height(), item_label.height()))
            else:
                item_label.setObjectName(f'item_text_{column}_label')
                item_label.setProperty('class', 'item_text_label')
                item_label.setText(f'{item}')
            self.main_objects_layout.addWidget(item_label, row, column)
            item_label.setAlignment(Qt.AlignCenter)
            item_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Stock widget """
def stock_widget(self):
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
    WHERE stock.id={self.global_config['mid_object'][1]};''').fetchall()[0] # Execute
    cursor.close()
    database.close()
#______________________________________________________________________________________________________________________
    """ Setup widget """
    if self.main_widget:
        self.main_widget.deleteLater()
        self.main_widget = None
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.main_widget = QWidget(self.main_scroll)
    self.main_layout = QGridLayout(self.main_widget)
    self.main_icon_label = QLabel(self.main_widget)
    self.main_short_name_label = QLabel(self.main_widget)
    self.main_name_label = QLabel(self.main_widget)
    self.main_chart_widget = QWidget(self.main_widget)
    self.main_statistics_widget = QWidget(self.main_widget)
    self.main_statistics_layout = QGridLayout(self.main_statistics_widget)
    self.main_capitalization_name_label = QLabel(self.main_statistics_widget)
    self.main_capitalization_value_label = QLabel(self.main_statistics_widget)
    self.main_pe_ratio_name_label = QLabel(self.main_statistics_widget)
    self.main_pe_ratio_value_label = QLabel(self.main_statistics_widget)
    self.main_eps_name_label = QLabel(self.main_statistics_widget)
    self.main_eps_value_label = QLabel(self.main_statistics_widget)
    self.main_dividend_yield_name_label = QLabel(self.main_statistics_widget)
    self.main_dividend_yield_value_label = QLabel(self.main_statistics_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.main_widget.setObjectName('main_widget')
    self.main_icon_label.setObjectName('main_icon_label')
    self.main_short_name_label.setObjectName('main_short_name_label')
    self.main_name_label.setObjectName('main_name_label')
    self.main_chart_widget.setObjectName('main_chart_widget')
    self.main_statistics_widget.setObjectName('main_statistics_widget')
    self.main_capitalization_name_label.setObjectName('main_capitalization_name_label')
    self.main_capitalization_value_label.setObjectName('main_capitalization_value_label')
    self.main_pe_ratio_name_label.setObjectName('main_pre_ratio_name_label')
    self.main_pe_ratio_value_label.setObjectName('main_pre_ratio_value_label')
    self.main_eps_name_label.setObjectName('main_eps_name_label')
    self.main_eps_value_label.setObjectName('main_eps_value_label')
    self.main_dividend_yield_name_label.setObjectName('main_dividend_yield_name_label')
    self.main_dividend_yield_value_label.setObjectName('main_dividend_yield_value_label')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.main_capitalization_name_label.setProperty('class', 'main_name_label')
    self.main_capitalization_value_label.setProperty('class', 'main_value_label')
    self.main_pe_ratio_name_label.setProperty('class', 'main_name_label')
    self.main_pe_ratio_value_label.setProperty('class', 'main_value_label')
    self.main_eps_name_label.setProperty('class', 'main_name_label')
    self.main_eps_value_label.setProperty('class', 'main_value_label')
    self.main_dividend_yield_name_label.setProperty('class', 'main_name_label')
    self.main_dividend_yield_value_label.setProperty('class', 'main_value_label')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.main_icon_label,0,0)
    self.main_layout.addWidget(self.main_short_name_label,1,0)
    self.main_layout.addWidget(self.main_name_label,2,0)
    self.main_layout.addWidget(self.main_chart_widget,3,0)
    self.main_layout.addWidget(self.main_statistics_widget,4,0)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    self.main_widget.setLayout(self.main_layout)
    self.main_statistics_layout.addWidget(self.main_capitalization_name_label,0,0)
    self.main_statistics_layout.addWidget(self.main_capitalization_value_label,0,1)
    self.main_statistics_layout.addWidget(self.main_pe_ratio_name_label,1,0)
    self.main_statistics_layout.addWidget(self.main_pe_ratio_value_label,1,1)
    self.main_statistics_layout.addWidget(self.main_eps_name_label,2,0)
    self.main_statistics_layout.addWidget(self.main_eps_value_label,2,1)
    self.main_statistics_layout.addWidget(self.main_dividend_yield_name_label,3,0)
    self.main_statistics_layout.addWidget(self.main_dividend_yield_value_label,3,1)
    self.main_statistics_layout.setSpacing(0)
    self.main_statistics_layout.setContentsMargins(0,0,0,0)
    self.main_statistics_widget.setLayout(self.main_statistics_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.main_scroll.setWidget(self.main_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.main_icon_label.setAlignment(Qt.AlignCenter)
    self.main_short_name_label.setAlignment(Qt.AlignCenter)
    self.main_name_label.setAlignment(Qt.AlignCenter)
    self.main_capitalization_name_label.setAlignment(Qt.AlignCenter)
    self.main_capitalization_value_label.setAlignment(Qt.AlignCenter)
    self.main_pe_ratio_name_label.setAlignment(Qt.AlignCenter)
    self.main_pe_ratio_value_label.setAlignment(Qt.AlignCenter)
    self.main_eps_name_label.setAlignment(Qt.AlignCenter)
    self.main_eps_value_label.setAlignment(Qt.AlignCenter)
    self.main_dividend_yield_name_label.setAlignment(Qt.AlignCenter)
    self.main_dividend_yield_value_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.main_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_icon_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_short_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_chart_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_statistics_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_capitalization_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_capitalization_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_pe_ratio_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_pe_ratio_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_eps_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_eps_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_dividend_yield_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_dividend_yield_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    self.main_short_name_label.setText(f'{stock_data[0]}')
    self.main_name_label.setText(f'{stock_data[1]}')
    self.main_capitalization_name_label.setText(f'{self.translate['main_capitalization_name_label'][self.global_config['__language__']]}:')
    self.main_capitalization_value_label.setText(f'{stock_data[3]}')
    self.main_pe_ratio_name_label.setText(f'{self.translate['main_pe_ratio_name_label'][self.global_config['__language__']]}:')
    self.main_pe_ratio_value_label.setText(f'{stock_data[4]}')
    self.main_eps_name_label.setText(f'{self.translate['main_eps_name_label'][self.global_config['__language__']]}:')
    self.main_eps_value_label.setText(f'{stock_data[5]}')
    self.main_dividend_yield_name_label.setText(f'{self.translate['main_dividend_yield_name_label'][self.global_config['__language__']]}:')
    self.main_dividend_yield_value_label.setText(f'{stock_data[6]}')
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.main_icon_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+stock_data[2]+'.svg', int(self.width()*0.3), int(self.width()*0.3)))
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
