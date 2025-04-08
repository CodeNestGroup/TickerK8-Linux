""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QLineEdit, # Simple line edit
    QGridLayout, # Grid layout
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt # Qt settings
)
#######################################################################################################################
""" Login Ui """
def login_ui(self):
    """ Set object name """
    self.setObjectName('login_widget')
    self.login_title_label.setObjectName('login_title_label')
    self.login_login_lineedit.setObjectName('login_login_lineedit')
    self.login_password_lineedit.setObjectName('login_password_lineedit')
    self.login_login_button.setObjectName('login_login_button')
    self.login_register_button.setObjectName('login_register_button')
    self.login_forgot_password_button.setObjectName('login_forgot_password_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.setProperty('class', 'parent_widget')
    self.login_login_lineedit.setProperty('class', 'login_input_line')
    self.login_password_lineedit.setProperty('class', 'login_input_line')
    self.login_login_button.setProperty('class', 'login_control_button')
    self.login_register_button.setProperty('class', 'login_control_button')
    self.login_forgot_password_button.setProperty('class', 'login_control_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.login_layout.addWidget(self.login_title_label, 5, 0, 5, 100)
    self.login_layout.addWidget(self.login_login_lineedit, 40, 10, 5, 80)
    self.login_layout.addWidget(self.login_password_lineedit, 55, 10, 5, 80)
    self.login_layout.addWidget(self.login_login_button, 80, 40, 5, 20)
    self.login_layout.addWidget(self.login_register_button, 90, 25, 5, 20)
    self.login_layout.addWidget(self.login_forgot_password_button, 90, 55, 5, 20)
    self.login_layout.setSpacing(0)
    self.login_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.login_layout.setRowStretch(enc, 1)
        self.login_layout.setColumnStretch(enc, 1)
    self.setLayout(self.login_layout)
#______________________________________________________________________________________________________________________
    """ Set widget"""
    self.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.login_title_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set line edit """
    self.login_password_lineedit.setEchoMode(QLineEdit.Password)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expandig)
    self.login_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expandig)
    self.login_login_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expandig)
    self.login_password_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expandig)
    self.login_login_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expandig)
    self.login_register_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expandig)
    self.login_forgot_password_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expandig)
#######################################################################################################################

