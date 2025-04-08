""" Import """
import pathlib # For get path to folders
import json # For json files
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QLineEdit, # Simple line edit
    QGridLayout # Grid layout
)
#______________________________________________________________________________________________________________________
""" Import login ui """
from .login_ui import *
#______________________________________________________________________________________________________________________
""" Import login logic """
from .login_logic import *
#######################################################################################################################
""" Login widget """
class Login_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent) # Set parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.login_config = json.load(open(self.main_path+'/CONFIG/LOGIN/login_config.json', 'r')) # Get login config data
        self.login_translate = json.load(open(self.main_path+'/CONFIG/LOGIN/login_translate.json', 'r')) # Get login translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.login_layout = QGridLayout(self) # Creat grid layout
        self.login_title_label = QLabel(self) # Create title label
        self.login_day_night_button = QPushButton(self) # Create day night button
        self.login_login_lineedit = QLineEdit(self) # Create login input line
        self.login_password_lineedit = QLineEdit(self) # Create password input line
        self.login_login_button = QPushButton(self) # Create login button
        self.login_register_button = QPushButton(self) # Create register button 
        self.login_forgot_password_button = QPushButton(self) # Create forgot password button
#______________________________________________________________________________________________________________________
        """ Call functions """
        login_ui(self) # Call login ui function
        login_reload_style(self) # Call login style function
        login_retranslate(self) # Call login retranslte funcion 
#######################################################################################################################
