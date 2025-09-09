""" Import packages """
""" Import system and operating system packages """
import json # For json files.
import datetime # For get time.
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QLinearGradient, # Gradient.
    QPalette, # Palette.
    QBrush, # Brush.
    QColor, # Color.
    QPixmap, # Image.
    QPainter # Painter.
)
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
    _colors = self.main_conf['background'] # Get colors list, local.
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