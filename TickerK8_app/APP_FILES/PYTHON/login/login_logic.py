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
    QColor
)
#######################################################################################################################
""" login widget background """
def login_widget_background(self):
    """ Colors file """
    _colors = json.load(open(self.main_path+'/CONFIG/login/conf.json', 'r'))['background']
    """ Time """
    if self._now == 86400:
        self._now = 0
    self._now += 1
    _today_sec = self._now
    #_today_sec = _now.hour*3600+_now.minute*60+_now.second
    _x_1 = 0.0
    _x_2 = 1.0
    _alpha_1 = None
    _alpha_2 = None
    _color_1 = None
    _color_2 = None
    """ Position """
    if _today_sec == 0:
        _x_1, _x_2 = 0.0, 1.0
        _color_1 = f'#ff{_colors[0]}'
        _color_2 = _color_1

    elif _today_sec > 0 and _today_sec < 8640:
        _percent = (8640-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _color_1 = f'#{_alpha_1}{_colors[0]}'
        _color_2 = f'#{_alpha_2}{_colors[1]}'

    elif _today_sec == 8640:
        _x_1, _x_2 = 0.0, 1.0
        _color_1 = f'#ff{_colors[1]}'
        _color_2 = _color_1

    elif _today_sec > 8640 and _today_sec < 17280:
        _percent = (17280-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _color_1 = f'#{_alpha_1}{_colors[1]}'
        _color_2 = f'#{_alpha_2}{_colors[2]}'

    elif _today_sec == 17280:
        _x_1, _x_2 = 0.0, 1.0
        _color_1 = f'#ff{_colors[2]}'
        _color_2 = _color_1

    elif _today_sec > 17280 and _today_sec < 25920:
        _percent = (25920-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _color_1 = f'#{_alpha_1}{_colors[2]}'
        _color_2 = f'#{_alpha_2}{_colors[3]}'
        
    elif _today_sec == 25920:
        _x_1, _x_2 = 0.0, 1.0
        _color_1 = f'#ff{_colors[3]}'
        _color_2 = _color_1

    elif _today_sec > 25920 and _today_sec < 34560:
        _percent = (34560-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _color_1 = f'#{_alpha_1}{_colors[3]}'
        _color_2 = f'#{_alpha_2}{_colors[4]}'

    elif _today_sec == 34560:
        _x_1, _x_2 = 0.0, 1.0
        _color_1 = f'#ff{_colors[4]}'
        _color_2 = _color_1

    elif _today_sec > 34560 and _today_sec < 43200:
        _percent = (43200-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _color_1 = f'#{_alpha_1}{_colors[4]}'
        _color_2 = f'#{_alpha_2}{_colors[5]}'

    elif _today_sec == 43200:
        _x_1, _x_2 = 0.0, 1.0
        _color_1 = f'#ff{_colors[5]}'
        _color_2 = _color_1

    elif _today_sec > 43200 and _today_sec < 51840:
        _percent = (51840-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _color_1 = f'#{_alpha_1}{_colors[5]}'
        _color_2 = f'#{_alpha_2}{_colors[6]}'

    elif _today_sec == 51840:
        _x_1, _x_2 = 0.0, 1.0
        _color_1 = f'#ff{_colors[6]}'
        _color_2 = _color_1

    elif _today_sec > 51840 and _today_sec < 60480:
        _percent = (60480-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _color_1 = f'#{_alpha_1}{_colors[6]}'
        _color_2 = f'#{_alpha_2}{_colors[7]}'

    elif _today_sec == 60480:
        _x_1, _x_2 = 0.0, 1.0
        _color_1 = f'#ff{_colors[7]}'
        _color_2 = _color_1

    elif _today_sec > 60480 and _today_sec < 69120:
        _percent = (69120-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _color_1 = f'#{_alpha_1}{_colors[7]}'
        _color_2 = f'#{_alpha_2}{_colors[8]}'

    elif _today_sec == 69120:
        _x_1, _x_2 = 0.0, 1.0
        _color_1 = f'#ff{_colors[8]}'
        _color_2 = _color_1

    elif _today_sec > 69120 and _today_sec < 77760:
        _percent = (77760-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _color_1 = f'#{_alpha_1}{_colors[8]}'
        _color_2 = f'#{_alpha_2}{_colors[9]}'

    elif _today_sec == 77760:
        _x_1, _x_2 = 0.0, 1.0
        _color_1 = f'#ff{_colors[9]}'
        _color_2 = _color_1

    elif _today_sec > 77760 and _today_sec < 86400:
        _percent = (86400-_today_sec)/8640
        if _percent <= 0.5:
            _x_1 = 0.0
            _x_2 = _percent*2
            _alpha_1 = f'{int(255 *(_percent / 0.5)):02X}'
            _alpha_2 = 'ff'
        else:
            _x_1 = (_percent-0.5)*2
            _x_2 = 1.0
            _alpha_1 = 'ff'
            _alpha_2 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _color_1 = f'#{_alpha_1}{_colors[9]}'
        _color_2 = f'#{_alpha_2}{_colors[0]}'

    """ Create gradient """
    gradient = QLinearGradient()
    gradient.setStart(0, 0)
    gradient.setFinalStop(self.width(), 0)
    gradient.setColorAt(_x_1, QColor(_color_1))
    gradient.setColorAt(_x_2, QColor(_color_2))
    palette = self.palette()
    palette.setBrush(QPalette.Window, QBrush(gradient))
    self.setAutoFillBackground(True)
    self.setPalette(palette)
    #print(_x_1, _x_2, _color_1, _color_2)

