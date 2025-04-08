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
from .login_ui import login_ui
#______________________________________________________________________________________________________________________
""" Import login logic """
from .login_logic import login_logic
#######################################################################################################################
""" Login widget """
class Login_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent) # Set parent
        self.login_layout = QGridLayout(self) # Creat grid layout
        self.login_title_label = QLabel(self) # Create title label
        self.login_login_lineedit = QLineEdit(self) # Create login input line
        self.login_password_lineedit = QLineEdit(self) # Create password input line
        self.login_login_button = QPushButton(self) # Create login button
        self.login_register_button = QPushButton(self) # Create register button 
        self.login_forgot_password_button = QPushButton(self) # Create forgot password button
#______________________________________________________________________________________________________________________
        login_ui(self) # Call login ui function
        login_logic(self) # Call login logic function
#######################################################################################################################
