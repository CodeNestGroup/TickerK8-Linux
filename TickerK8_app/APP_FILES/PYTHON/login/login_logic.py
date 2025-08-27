""" Import packages """
""" Import system and operating system packages """
import json # For json files.
import datetime # For get time.
import mysql  # For connect with database.
#______________________________________________________________________________________________________________________
""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window.
    )
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
""" Import PyQt5 Svg """
from PyQt5.QtSvg import (
    QSvgRenderer # Svg.
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt, # Qt.
    )
#######################################################################################################################
""" login widget background painter """
def login_widget_background_painter(self):
    """ Variables """
    """ Text """
    _language = self.global_config['__language__'] # Get langauge, local.
    _texts_title = self.login_translate['login_welcome_title_label'] # Get texts title list, local.
    _texts_sub = self.login_translate['login_welcome_sub_label'] # Get texts sub list, local.
    """ Colors """
    _colors = self.login_conf['background'] # Get colors list, local.
    _color_0 = '#000000'
    _color_1 = '#000000'
    _color_2 = '#000000'
    """ Colors alpha """
    _alpha_1 = 'ff'
    _alpha_2 = 'ff'
    """ Colors positions """
    _x_1 = 0.0
    _x_2 = 1.0 
    """ Icons """
    _icons = self.login_conf['icon'] # Get icons list, local.
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
#______________________________________________________________________________________________________________________
    """ Call text and icon change """
    if self.index_changed != _index: # Check if index changed.
        _icon = f'{self.main_path}/STYLE/IMG/icons/login/{_icons[_index]}.svg' # Get icon, local.
        change_text_icon(self, _texts_title[_index][_language], _texts_sub[_index][_language], _icon) # Call functions for change texts and icon.
        self.index_changed = _index # Update index.
#######################################################################################################################
""" Change text icon"""
def change_text_icon(self, title='', sub='', icon=''):
    """ Variables """
    _title = title # Text for title label.
    _sub = sub # Text for sub text label.
    _icon = icon # Path to icon .
#______________________________________________________________________________________________________________________
    """ Set text """
    self.login_welcome_title_label.setText(_title)
    self.login_welcome_sub_label.setText(_sub)
#______________________________________________________________________________________________________________________
    """ Set icon """
    render = QSvgRenderer(_icon) # Create Svg render.
    icon_pixmap = QPixmap(self.login_welcome_icon_label.height(), self.login_welcome_icon_label.height()) # Ceate img.
    icon_pixmap.fill(Qt.transparent) # Set transparent for background of img.
    icon_painter = QPainter(icon_pixmap) # Create painter.
    render.render(icon_painter) # Render svg graphic.
    icon_painter.end() # End painting.
    self.login_welcome_icon_label.setPixmap(QPixmap(icon_pixmap)) # Set img for icon label.
#######################################################################################################################
""" Sign in controller """
def sign_in_controller(self):
    """ Get sign in values """
    _login = self.login_login_lineedit.text()
    _password = self.login_password_lineedit.text()
#______________________________________________________________________________________________________________________
    """ Connect with database """
    connect = mysql.connector.connect(
        host = "localhost",
        user = "client",
        password = "Qwerty123456#",
        database = "TickerK8"
    )
    cursor = connect.cursor()# Creating cursor.
    cursor.execute('SELECT id FROM users WHERE name=%s and password=%s;', (_login, _password)) # Execute query.
    login_password_result = cursor.fetchone() # Fetch results.
#______________________________________________________________________________________________________________________
    """ Checking correct sign in data"""
    if login_password_result: # Check if correct login.
        self.correct_login.emit() # If correct emit signal.
    else:
        """ Reset """
        self.login_login_lineedit.clear()
        self.login_password_lineedit.clear()
#______________________________________________________________________________________________________________________
        """ Style """
        self.login_login_lineedit.setStyleSheet('border: 2px solid red;')
        self.login_password_lineedit.setStyleSheet('border: 2px solid red;')
#______________________________________________________________________________________________________________________
    """ Close connection with database """
    cursor.close()
    connect.close()
#######################################################################################################################
""" Reset style """
def reset_style(self):
    self.login_login_lineedit.setStyleSheet('border: 0;')
    self.login_password_lineedit.setStyleSheet('border: 0;')
#######################################################################################################################
