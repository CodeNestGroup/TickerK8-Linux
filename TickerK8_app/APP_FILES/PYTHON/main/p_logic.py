#   --- Import ---
import json
import datetime
import sqlite3
import requests
from io import BytesIO
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton,
    QComboBox,
    QGridLayout,
    QSizePolicy,
    QVBoxLayout
)
from PyQt5.QtCore import (
    Qt,
    QSize,
    QRect
)
from PyQt5.QtGui import (
    QLinearGradient,
    QPalette,
    QBrush,
    QColor,
    QPixmap,
    QIcon,
    QPainter
)
from PyQt5.QtSvg import (
    QSvgRenderer
)
from main_chart.structure import Main_chart
from main_news.structure import Main_news_widget
from main_news_list.structure import Main_news_list_widget

#   --- Dynamic Background ---
def widget_background_painter(self):
    _colors = self.main_conf['background']
    _color_0 = '#000000'
    _color_1 = '#000000'
    _color_2 = '#000000'
    _alpha_1 = 'ff'
    _alpha_2 = 'ff'
    _x_1 = 0.0
    _x_2 = 1.0 
#       --- Calculate index and precent ---
    _now = datetime.datetime.now()
    _today_sec = _now.hour*3600+_now.minute*60+_now.second
    if _today_sec >=86400:
        _today_sec = 86399
    _index = _today_sec//8640
    _percent = (_today_sec/8640)-_index
#       --- Set colors ---
    if _percent <= 0.5:
        _x_1 = 1-(_percent*2)
        _x_2 = 1.0
        _alpha_1 = 'ff'
        _alpha_2 = f'{int(255 *(_percent / 0.5)):02X}'
        _color_0 = f'#ff{_colors[_index-1]}'
    else:
        _x_1 = 0.0
        _x_2 = 1-(_percent-0.5)*2
        _alpha_1 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _alpha_2 = 'ff'
        _color_0 = f'#ff{_colors[_index]}' 
    _color_1 = f'#{_alpha_1}{_colors[_index-1]}'
    _color_2 = f'#{_alpha_2}{_colors[_index]}'
#       --- Paint background ---
    pixmap = QPixmap(self.size())
    pixmap.fill(QColor(_color_0))
    painter = QPainter(pixmap)
    gradient = QLinearGradient(0,0,self.width(), 0)
    gradient.setColorAt(_x_1, QColor(_color_1))
    gradient.setColorAt(_x_2, QColor(_color_2))
    painter.fillRect(self.rect(), gradient)
    painter.end()
    palette = self.palette()
    palette.setBrush(QPalette.Window, QBrush(pixmap))
    self.setAutoFillBackground(True)
    self.setPalette(palette)

#   --- Object list ---
def objects_list_open(self):
    pass
    
def objects_list_delete_object(self):
    pass

def object_set(self, object_info):
    pass

def object_list_lists_scroll_setup(self):
    pass

def object_list_lists_exit(self):
   pass

def object_list_set_list(self):
   pass

def object_list_edit_check_selected(self):
    pass

def object_list_edit_save(self):
    pass

def object_list_edit_exit(self):
    pass

#   --- Object info ---
def object_setup(self):
    pass

def object_country(self):
    pass

def object_market(self):
    pass

def object_index(self):
    pass

def object_stock(self):
    pass

#   --- News ----
def main_news_setup(self):
    pass

def news_next(self):
    self.news_timer.stop()
    self.news_timer.start(5000)
    self.news_button_list[self.news_button_index].setHidden(True)
    self.news_button_index = (self.news_button_index+1)%len(self.news_button_list)
    self.news_button_list[self.news_button_index].setHidden(False)

def news_previous(self):
    self.news_timer.stop()
    self.news_timer.start(5000)
    self.news_button_list[self.news_button_index].setHidden(True)
    self.news_button_index = (self.news_button_index-1)%len(self.news_button_list)
    self.news_button_list[self.news_button_index].setHidden(False)

def open_main_news_list(self, news_type_index):
    self.main_news_list = Main_news_list_widget(self, news_type_index)
    self.main_news_list.open_news.connect(lambda val: open_main_news(self, val))

#   --- Load svg graphic ---
def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path)
    pixmap = QPixmap(width, height)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return scaled_pixmap
