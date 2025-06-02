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
    QRect
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
    if self.global_config['mid_object'][0] == 'country':
        country_widget(self)
    elif self.global_config['mid_object'][0] == 'market':
        market_widget(self)
    elif self.global_config['mid_object'][0] == 'index':
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
    country.flag, 
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
        self.main_widget.delteLater()
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
    """ Create objects """
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
    self.main_population_name_label.setText('Population:')
    self.main_population_value_label.setText(f'{country_data[5]}')
    self.main_capital_name_label.setText('Capital:')
    self.main_capital_value_label.setText(f'{country_data[2]}')
    self.main_currecny_name_label.setText('Currency:')
    self.main_currency_value_label.setText(f'{country_data[3]}')
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.main_flag_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/flags'+country_data[1]+'.svg', int(self.width()*0.3), int(self.width()*0.3)))
#######################################################################################################################
""" Market widget"""
def market_widget(self):
    pass
#######################################################################################################################
""" Index widget """
def index_widget(self):
    pass
#######################################################################################################################
""" Stock widget """
def stock_widget(self):
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
