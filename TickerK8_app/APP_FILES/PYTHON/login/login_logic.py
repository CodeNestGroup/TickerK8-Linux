""" Import packages """
""" Import system and operating system packages """
import json
import datetime
#______________________________________________________________________________________________________________________
""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window.
    )
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QLinearGradient,
    QPalette,
    QBrush,
    QColor,
    QPixmap,
    QPainter
)
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtCore import (
        Qt, # Qt.
    )
#######################################################################################################################
""" login widget background """
def login_widget_background(self):
    """ Colors file """
    _colors = json.load(open(self.main_path+'/CONFIG/login/conf.json', 'r'))['background']
    _t = self.login_translate
    _l = self.global_config['__language__']
    render = QSvgRenderer(self.main_path+'/STYLE/IMG/icons/main/market_vintage_elegance_light.svg')
    icon_pixmap = QPixmap(self.login_welcome_icon_label.height(), self.login_welcome_icon_label.height())
    icon_pixmap.fill(Qt.transparent)
    icon_painter = QPainter(icon_pixmap)
    render.render(icon_painter)
    icon_painter.end()
    self.login_welcome_icon_label.setPixmap(QPixmap(icon_pixmap))
    """ Time """
    if self._now == 86400:
        self._now = 0
    self._now += 6
    _today_sec = self._now
    #_today_sec = _now.hour*3600+_now.minute*60+_now.second
    _x_1 = 0.0
    _x_2 = 1.0
    _alpha_1 = None
    _alpha_2 = None
    _color_0 = None
    _color_1 = None
    _color_2 = None
    """ Position """
    if _today_sec == 0:
        _x_1, _x_2 = 0.0, 1.0
        _color_0 = f'#ff{_colors[0]}'
        _color_1 = f'#ff{_colors[0]}'
        _color_2 = _color_1
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][1][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][1][_l])

    elif _today_sec > 0 and _today_sec < 8640:
        _percent = (8640-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
            _color_0 = f'#ff{_colors[1]}'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
            _color_0 = f'#ff{_colors[0]}'
        _color_1 = f'#{_alpha_1}{_colors[0]}'
        _color_2 = f'#{_alpha_2}{_colors[1]}'
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][1][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][1][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec == 8640:
        _x_1, _x_2 = 0.0, 1.0
        _color_0 = f'#ff{_colors[1]}'
        _color_1 = f'#ff{_colors[1]}'
        _color_2 = _color_1
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][2][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][2][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec > 8640 and _today_sec < 17280:
        _percent = (17280-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
            _color_0 = f'#ff{_colors[2]}'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
            _color_0 = f'#ff{_colors[1]}'
        _color_1 = f'#{_alpha_1}{_colors[1]}'
        _color_2 = f'#{_alpha_2}{_colors[2]}'
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][2][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][2][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec == 17280:
        _x_1, _x_2 = 0.0, 1.0
        _color_0 = f'#ff{_colors[2]}'
        _color_1 = f'#ff{_colors[2]}'
        _color_2 = _color_1
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][3][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][3][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec > 17280 and _today_sec < 25920:
        _percent = (25920-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
            _color_0 = f'#ff{_colors[3]}'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
            _color_0 = f'#ff{_colors[2]}'
        _color_1 = f'#{_alpha_1}{_colors[2]}'
        _color_2 = f'#{_alpha_2}{_colors[3]}'
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][3][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][3][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())
        
    elif _today_sec == 25920:
        _x_1, _x_2 = 0.0, 1.0
        _color_0 = f'#ff{_colors[3]}'
        _color_1 = f'#ff{_colors[3]}'
        _color_2 = _color_1
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][4][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][4][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec > 25920 and _today_sec < 34560:
        _percent = (34560-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
            _color_0 = f'#ff{_colors[4]}'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
            _color_0 = f'#ff{_colors[3]}'
        _color_1 = f'#{_alpha_1}{_colors[3]}'
        _color_2 = f'#{_alpha_2}{_colors[4]}'
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][4][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][4][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec == 34560:
        _x_1, _x_2 = 0.0, 1.0
        _color_0 = f'#ff{_colors[4]}'
        _color_1 = f'#ff{_colors[4]}'
        _color_2 = _color_1
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][5][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][5][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec > 34560 and _today_sec < 43200:
        _percent = (43200-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
            _color_0 = f'#ff{_colors[5]}'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
            _color_0 = f'#ff{_colors[4]}'
        _color_1 = f'#{_alpha_1}{_colors[4]}'
        _color_2 = f'#{_alpha_2}{_colors[5]}'
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][5][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][5][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec == 43200:
        _x_1, _x_2 = 0.0, 1.0
        _color_0 = f'#ff{_colors[5]}'
        _color_1 = f'#ff{_colors[5]}'
        _color_2 = _color_1
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][6][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][6][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec > 43200 and _today_sec < 51840:
        _percent = (51840-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
            _color_0 = f'#ff{_colors[6]}'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
            _color_0 = f'#ff{_colors[5]}'
        _color_1 = f'#{_alpha_1}{_colors[5]}'
        _color_2 = f'#{_alpha_2}{_colors[6]}'
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][6][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][6][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec == 51840:
        _x_1, _x_2 = 0.0, 1.0
        _color_0 = f'#ff{_colors[6]}'
        _color_1 = f'#ff{_colors[6]}'
        _color_2 = _color_1
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][7][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][7][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec > 51840 and _today_sec < 60480:
        _percent = (60480-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
            _color_0 = f'#ff{_colors[7]}'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
            _color_0 = f'#ff{_colors[6]}'
        _color_1 = f'#{_alpha_1}{_colors[6]}'
        _color_2 = f'#{_alpha_2}{_colors[7]}'
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][7][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][7][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec == 60480:
        _x_1, _x_2 = 0.0, 1.0
        _color_1 = f'#ff{_colors[7]}'
        _color_1 = f'#ff{_colors[7]}'
        _color_2 = _color_1
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][8][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][8][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec > 60480 and _today_sec < 69120:
        _percent = (69120-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
            _color_0 = f'#ff{_colors[8]}'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
            _color_1 = f'#ff{_colors[7]}'
        _color_1 = f'#{_alpha_1}{_colors[7]}'
        _color_2 = f'#{_alpha_2}{_colors[8]}'
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][8][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][8][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec == 69120:
        _x_1, _x_2 = 0.0, 1.0
        _color_0 = f'#ff{_colors[8]}'
        _color_1 = f'#ff{_colors[8]}'
        _color_2 = _color_1
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][9][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][9][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec > 69120 and _today_sec < 77760:
        _percent = (77760-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
            _color_0 = f'#ff{_colors[9]}'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
            _color_0 = f'#ff{_colors[8]}'
        _color_1 = f'#{_alpha_1}{_colors[8]}'
        _color_2 = f'#{_alpha_2}{_colors[9]}'
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][9][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][9][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec == 77760:
        _x_1, _x_2 = 0.0, 1.0
        _color_0 = f'#ff{_colors[9]}'
        _color_1 = f'#ff{_colors[9]}'
        _color_2 = _color_1
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][0][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][0][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    elif _today_sec > 77760 and _today_sec < 86400:
        _percent = (86400-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
            _color_0 = f'#ff{_colors[0]}'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
            _color_0 = f'#ff{_colors[9]}'
        _color_1 = f'#{_alpha_1}{_colors[9]}'
        _color_2 = f'#{_alpha_2}{_colors[0]}'
        self.login_welcome_title_label.setText(_t['login_welcome_title_label'][0][_l])
        self.login_welcome_sub_label.setText(_t['login_welcome_sub_label'][0][_l])
        #self.login_welcome_icon_label.setPixmap(QPixmap())

    """ Create gradient """
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
    #print(_x_1, _x_2, _color_1, _color_2)

