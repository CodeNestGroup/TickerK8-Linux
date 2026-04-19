#   --- Import ---
import json
import datetime
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget
    )
from PyQt5.QtCore import (
    Qt,
    )
from PyQt5.QtGui import (
    QLinearGradient,
    QPalette,
    QBrush,
    QColor,
    QPixmap,
    QPainter
)
from PyQt5.QtSvg import (
    QSvgRenderer
)

def BackgroundPainter(self):
    l = self.Language
    _colors = self.Background['background']
    _color_0 = '#000000'
    _color_1 = '#000000'
    _color_2 = '#000000'
    _alpha_1 = 'ff'
    _alpha_2 = 'ff'
    _x_1 = 0.0
    _x_2 = 1.0 
    _icons = self.login_conf['icon']

    """ Calculate index and precent """
    _now = datetime.datetime.now()
    _today_sec = _now.hour*3600+_now.minute*60+_now.second
    if _today_sec >=86400:
        _today_sec = 86399
    _index = _today_sec//8640 
    _percent = (_today_sec/8640)-_index 

    """ Set colors """
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

    """ Paint background """
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

    """ Call text and icon change """
    if self.index_changed != _index:
        _icon = f'{self.main_path}/STYLE/IMG/icons/login/{_icons[_index]}.svg'
        ChangeTextCcon(
            self,
            self.LoginWelcomeTranslate['WelcomeTitleL'][_index][l],
            self.LoginWelcomeTranslate['WelcomeSubL'][_index][l],
            _icon)
        self.index_changed = _index

def ChangeTextIcon(self, title='', sub='', icon=''):
    _sub = sub
    _icon = icon
    self.login_welcome_title_label.setText(title)
    self.login_welcome_sub_label.setText(sub)
    render = QSvgRenderer(_icon)
    icon_pixmap = QPixmap(self.login_welcome_icon_label.height(), self.login_welcome_icon_label.height())
    icon_pixmap.fill(Qt.transparent)
    icon_painter = QPainter(icon_pixmap)
    render.render(icon_painter)
    icon_painter.end()
    self.login_welcome_icon_label.setPixmap(QPixmap(icon_pixmap))

def ResetStyle(self):
    if self.Theme == 'vintage_elegance_l':
        c = '#e0e0e0'
    elif self.Theme == 'vintage_elegance_d':
        c = '#1a1a1a'
    self.LoginL.setStyleSheet(f'border-color: {c};')
    self.PasswordL.setStyleSheet(f'border-color: {c};')

def LoginController(self):
    pass
