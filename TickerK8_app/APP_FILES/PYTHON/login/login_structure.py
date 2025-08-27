""" Import packages """
""" Import system and operating system packages """
import pathlib # For get path to folders.
import json # For json files.
#______________________________________________________________________________________________________________________
""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window.
    QLabel, # Simple label.
    QPushButton, # Simple button.
    QLineEdit, # Simple line edit.
    QGridLayout # Grid layout.
        )
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
        Qt, # Qt.
        QTimer, # Timer
        pyqtSignal # Signal 
        )
#______________________________________________________________________________________________________________________
""" Import login modules """
""" Import login ui """
from .login_ui import *
#______________________________________________________________________________________________________________________
""" Import login logic """
from .login_logic import *
#######################################################################################################################
""" Login widget """
class Login_widget(QWidget):
    correct_login = pyqtSignal() # Create signal for correct login.
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background.
        self.setParent(parent) # Set parent.
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data.
        self.login_translate = json.load(open(self.main_path+'/CONFIG/login/translate.json', 'r')) # Get global translate data.
        self.login_conf = json.load(open(self.main_path+'/CONFIG/login/conf.json', 'r')) # Get config.
        self.index_changed = -10
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.login_layout = QGridLayout(self) # Creat grid layout.
        self.login_login_lineedit = QLineEdit(self) # Create login input line.
        self.login_password_lineedit = QLineEdit(self) # Create password input line.
        self.login_login_button = QPushButton(self) # Create login button.
        self.login_register_button = QPushButton(self) # Create register button.
        self.login_welcome_title_label = QLabel(self) # Create welcome label.
        self.login_welcome_sub_label = QLabel(self) # Create welcome sub label.
        self.login_welcome_icon_label = QLabel(self) # Create welcome icon label.
        self.timer = QTimer(self) # Create timer.
#______________________________________________________________________________________________________________________
        """ Call functions """
        login_ui(self) # Call login ui function.
        login_reload_style(self) # Call login style function.
        login_retranslate(self) # Call login retranslte funcion.
        login_widget_background_painter(self)
        self.login_widget_background = lambda: login_widget_background_painter(self) # Function for background.
        self.timer.timeout.connect(self.login_widget_background) # Connect.
        self.timer.start(1) # Start timer.
#______________________________________________________________________________________________________________________
        """ Connect functions """
        self.login_login_button.clicked.connect(lambda: sign_in_controller(self))
        self.login_login_lineedit.textChanged.connect(lambda: reset_style(self))
        self.login_password_lineedit.textChanged.connect(lambda: reset_style(self))
#######################################################################################################################
