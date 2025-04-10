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
    QComboBox, # Drop down list
    QGridLayout # Grid layout
)
from PyQt5.QtCore import Qt
#______________________________________________________________________________________________________________________
""" Import register ui """
from .register_ui import *
#______________________________________________________________________________________________________________________
""" Import register logic """
from .register_logic import *
#######################################################################################################################
""" Login widget """
class Register_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent 
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.register_translate = json.load(open(self.main_path+'/CONFIG/register/register_translate.json', 'r')) # Get global translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.register_layout = QGridLayout(self) # Create layout
        self.register_title_label = QLabel(self) # Create title label 
        self.register_name_subtitle_label = QLabel(self) # Create name sub title label
        self.register_name_lineedit = QLineEdit(self) # Create name input line
        self.register_name_combobox = QComboBox(self) # Create name drop donw list of sugessted names
        self.register_emial_subtitle_label = QLabel(self) # Create email sub title label
        self.register_emial_lineedit = QLineEdit(self) # Create emial input line
        self.register_emial_confirm_lineedit = QLineEdit(self) # Create emial confirm input line
        self.register_phonenumber_subtitle_label = QLabel(self) # Create phone number sub title label
        self.register_phonenumber_combobox = QComboBox(self) # Create phone number drop down list of prefix phone +48
        self.register_phonenumber_lineedit = QLineEdit(self) # Create phone number input line edit
        self.register_country_subtitle_label = QLabel(self) # Create country sub title label 
        self.register_country_combobox = QComboBox(self) # Create country drop down list
        self.register_password_subtitle_label = QLabel(self) # Create password sub title label 
        self.register_password_lineedit = QLineEdit(self) # Create password input line
        self.register_password_requirements_label = QLabel(self) # Create password requirments label 
        self.register_password_show_button = QPushButton(self) # Create password show button
        self.register_password_confirm_lineedit = QLineEdit(self) # Create password confirm input line 
        self.register_password_confirm_show_button = QPushButton(self) # Create password confirm show button
        self.register_register_button = QPushButton(self) # Create register button
        self.register_exit_button = QPushButton(self) # Create exit button
#______________________________________________________________________________________________________________________
        """ Call functions """
        register_ui(self)
        register_reload_style(self)
        register_retranslate(self)
#______________________________________________________________________________________________________________________
        """ Connect local functions """
        self.register_password_show_button.clicked.connect(lambda: show_hide_password(self))
        self.register_password_confirm_show_button.clicked.connect(lambda: show_hide_confirm_password(self))
#######################################################################################################################
