""" Import """
import pathlib # For get path to folders
import json # For json files
import sqlite3 # For database data 
from PyQt5.QtWidgets import (
    QWidget,
    QTableWidget,
    QComboBox,
    QLabel,
    QPushButton,
    QGridLayout,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem,
    QSizePolicy
)
from PyQt5.QtGui import QPainter, QBrush, QPen, QFont
from PyQt5.QtCore import QRectF, Qt, QPointF
#______________________________________________________________________________________________________________________
""" Charts types import """
from .candle_chart import Candle_chart
#######################################################################################################################
""" Create chart """
def create_chart(self, value):
    """ Get data """
    chart_object = self.global_config['mid_object']
    chart_data = json.load(open(self.main_path+'/test_chart_data/AGX100/agx100_1min.json', 'r'))
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
    cursor = database.cursor() # Create cursor 
    object_data = cursor.execute(f'SELECT name FROM {chart_object[0]} WHERE id={chart_object[1]};').fetchall()[0] # Get data 
    cursor.close() # Close cursor connection  
    database.close() # Close database connection
#______________________________________________________________________________________________________________________
    """ Set chart """
    if chart_type == 0:
        self.main_chart_graphics_view = Candle_chart(chart_data, self)
        self.main_chart_graphics_view.setObjectName('main_chart_graphics_view')
    self.main_layout.addWidget(self.main_chart_graphics_view, 10, 0, 80, 100)
#______________________________________________________________________________________________________________________
    """ Create main chart graphics view """
#______________________________________________________________________________________________________________________
    """ Set object name """
#______________________________________________________________________________________________________________________
    """ Set main chart graphics view to main layout """
#______________________________________________________________________________________________________________________
    """ Set alignemnt """
#______________________________________________________________________________________________________________________
    """ Set size """
#______________________________________________________________________________________________________________________
    """ Set char title """
    self.top_title_label.setText(f'{object_data[0]}')
#######################################################################################################################
""" Settings """
def settings_widget(self):
    """ Create objects """
    self.settings_background_widget = QWidget(self)
    self.settings_background_layout = QGridLayout(self.settings_background_widget)
    self.settings_widget = QWidget(self.settings_background_widget)
    self.settings_layout = QGridLayout(self.settings_widget)
    self.settings_title_label = QLabel(self.settings_widget)
    self.settings_tab_widget = QTabWidget(self.settings_widget)
    self.settings_theme_widget = QWidget(self.settings_tab_widget)
    self.settings_theme_layout = QGridLayout(self.settings_theme_widget)
    self.settings_theme_label = QLabel(self.settings_theme_widget)
    self.settings_theme_combo = QComboBox(self.settings_theme_widget)
    self.settings_background_background_widget = QWidget(self.settings_tab_widget)
    self.settings_background_background_layout = QGridLayout(self.settings_background_background_widget)
    self.settings_background_background_exemple_item = QGraphicsItem(self.settings_background_background_widget)
    self.settings_background_background_color_label = QLabel(self.settings_background_background_widget)
    self.settings_background_background_color_line = QLineEdit(self.settings_background_background_widget)
    self.settings_background_net_type_label = QLabel(self.settings_background_background_widget)
    self.settings_background_net_type_combo = QLineEdit(self.settings_background_background_widget)
    self.settings_background_net_color_label = QLabel(self.settings_background_background_widget)
    self.settings_background_net_color_line = QLineEdit(self.settings_background_background_widget)
    self.settings_price_widget = QWidget(self.settings_tab_widget)
    self.settings_price_layout = QGridLayout(self.settings_price_widget)
    self.settings_price_exemple_item = QGraphicsItem(self.settings_price_widget)
    self.settings_price_background_color_label = QLabel(self.settings_price_widget)
    self.settings_price_background_color_line = QLineEdit(self.settings_price_widget)
    self.settings_price_font_color_label = QLabel(self.settings_price_widget)
    self.settings_price_font_color_line = QLineEdit(self.settings_price_widget)
    self.settings_price_font_size_label = QLabel(self.settings_price_widget)
    self.settings_price_font_size_line = QLineEdit(self.settings_price_widget)
    self.settings_candle_widget = QWidget(self.settings_tab_widget)
    self.settings_candle_layout = QGridLayout(settings_candle_widget)
    self.settings_candle_exemple_p_item = QGraphicsItem(settings_candle_widget)
    self.settings_candle_exemple_m_item = QGraphicsItem(settings_candle_widget)
    self.settings_candle_size_label = QLabel(settings_candle_widget)
    self.settings_candle_size_line = QLineEdit(settings_candle_widget)
    self.settings_candle_border_label = QLabel(settings_candle_widget)
    self.settings_candle_p_border_line = QLineEdit(settings_candle_widget)
    self.settings_candle_m_border_line = QLineEdit(settings_candle_widget)
    self.settings_candle_fill_label = QLabel(settings_candle_widget)
    self.settings_candle_p_fill_line = QLineEdit(settings_candle_widget)
    self.settings_candle_m_fill_line = QLineEdit(settings_candle_widget)
    self.settings_vol_widget = QWidget(self.settings_tab_widget)
    self.settings_vol_layout = QGridLayout(self.settings_vol_widget)
    self.settings_vol_exemple_p_item = QGraphicsItem(self.settings_vol_widget)
    self.settings_vol_exemple_m_item = QGraphicsItem(self.settings_vol_widget)
    self.settings_vol_size_label = QLabel(self.settings_vol_widget)
    self.settings_vol_size_line = QLineEdit(self.settings_vol_widget)
    self.settings_vol_border_label = QLabel(self.settings_vol_widget)
    self.settings_vol_p_border_line = QLineEdit(self.settings_vol_widget)
    self.settings_vol_m_border_line = QLineEdit(self.settings_vol_widget)
    self.settings_vol_fill_label = QLabel(self.settings_vol_widget)
    self.settings_vol_p_fill_line = QLineEdit(self.settings_vol_widget)
    self.settings_vol_m_fill_line = QLineEdit(self.settings_vol_widget)
    self.settings_exit_button = QPushButton(self.settings_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.settings_background_widget
    self.settings_widget
    self.settings_title_label
    self.settings_tab_widget
    self.settings_theme_widget
    self.settings_theme_label
    self.settings_theme_combo
    self.settings_background_background_widget
    self.settings_background_background_exemple_item
    self.settings_background_background_color_label
    self.settings_background_background_color_line
    self.settings_background_net_type_label
    self.settings_background_net_type_combo
    self.settings_background_net_color_label
    self.settings_background_net_color_line
    self.settings_price_widget
    self.settings_price_exemple_item
    self.settings_price_background_color_label
    self.settings_price_background_color_line
    self.settings_price_font_color_label
    self.settings_price_font_color_line
    self.settings_price_font_size_label
    self.settings_price_font_size_line
    self.settings_candle_widget
    self.settings_candle_exemple_p_item
    self.settings_candle_exemple_m_item
    self.settings_candle_size_label
    self.settings_candle_size_line
    self.settings_candle_border_label
    self.settings_candle_p_border_line
    self.settings_candle_m_border_line
    self.settings_candle_fill_label
    self.settings_candle_p_fill_line
    self.settings_candle_m_fill_line
    self.settings_vol_widget
    self.settings_vol_exemple_p_item
    self.settings_vol_exemple_m_item
    self.settings_vol_size_label
    self.settings_vol_size_line
    self.settings_vol_border_label
    self.settings_vol_p_border_line
    self.settings_vol_m_border_line
    self.settings_vol_fill_label
    self.settings_vol_p_fill_line
    self.settings_vol_m_fill_line
    self.settings_exit_button
#______________________________________________________________________________________________________________________
    """ Set property """
    self.settings_theme_widget.setProperty('class', 'settings_sub_widget')
    self.settings_theme_label
    self.settings_background_background_widget.setProperty('class', 'settings_sub_widget')
    self.settings_background_background_color_label
    self.settings_background_background_color_line
    self.settings_background_net_type_label
    self.settings_background_net_color_label
    self.settings_background_net_color_line
    self.settings_price_widget.setProperty('class', 'settings_sub_widget')
    self.settings_price_background_color_label
    self.settings_price_background_color_line
    self.settings_price_font_color_label
    self.settings_price_font_color_line
    self.settings_price_font_size_label
    self.settings_price_font_size_line
    self.settings_candle_widget.setProperty('class', 'settings_sub_widget')
    self.settings_candle_size_label
    self.settings_candle_size_line
    self.settings_candle_border_label
    self.settings_candle_p_border_line
    self.settings_candle_m_border_line
    self.settings_candle_fill_label
    self.settings_candle_p_fill_line
    self.settings_candle_m_fill_line
    self.settings_vol_widget.setProperty('class', 'settings_sub_widget')
    self.settings_vol_size_label
    self.settings_vol_size_line
    self.settings_vol_border_label
    self.settings_vol_p_border_line
    self.settings_vol_m_border_line\
    self.settings_vol_fill_label
    self.settings_vol_p_fill_line
    self.settings_vol_m_fill_line





#######################################################################################################################
""" Full screan """
def full_screan(self):
    flag = self.main_config['full_screan']
    flag_neg != int(flag)
    self.top_widget.setHidden(flag) 
    self.bottom_widget.setHidden(flag)
    for enc in range(0, 10):
        self.main_layout.setColumnStretch(enc, flag)
    for enc in range(90, 100):
        self.main_layout.setColumnStretch(enc, flag)
    self.main_config['full_screan'] = flag_neg
    reload_main_config(self)
#######################################################################################################################
""" Reload main config """
def reload_main_config(self):
    with open(self.main_path+'/CONFIG/chart/main.json', 'w') as _w:
        json.dump(self.main_config, _w, indent=4)
    self.main_config = json.load(open(self.main_path+'/CONFIG/chart/main.json', 'r')) # Get main config data
#######################################################################################################################
