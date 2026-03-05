#   --- Import ---
import datetime

from PyQt5.QtGui import (
    QLinearGradient,
    QPalette,
    QBrush,
    QColor,
    QPixmap,
    QPainter
)

#   --- Dynamic Background ---
def WidgetBackgroundPainter(self):
    _colors = self.BacgroundConf['background']
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
