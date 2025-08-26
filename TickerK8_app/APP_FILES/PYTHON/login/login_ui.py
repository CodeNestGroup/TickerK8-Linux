""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window.
    QLabel, # Simple label.
    QPushButton, # Simple button.
    QLineEdit, # Simple line edit.
    QGridLayout, # Grid layout.
    QSizePolicy # Size policy.
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt # Qt.
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon # Icon.
)
#######################################################################################################################
""" Login Ui """
def login_ui(self):
    """ Set object name """
    self.setObjectName('login_widget')
    self.login_login_lineedit.setObjectName('login_login_lineedit')
    self.login_password_lineedit.setObjectName('login_password_lineedit')
    self.login_login_button.setObjectName('login_login_button')
    self.login_register_button.setObjectName('login_register_button')
    self.login_welcome_label.setObjectName('login_welcome_label')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.setProperty('class', 'parent_widget')
    self.login_login_lineedit.setProperty('class', 'login_input_line')
    self.login_password_lineedit.setProperty('class', 'login_input_line')
    self.login_login_button.setProperty('class', 'login_control_button')
    self.login_register_button.setProperty('class', 'login_control_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.login_layout.addWidget(self.login_login_lineedit, 40, 5, 5, 40)
    self.login_layout.addWidget(self.login_password_lineedit, 55, 5, 5, 40)
    self.login_layout.addWidget(self.login_login_button, 70, 5, 3, 40)
    self.login_layout.addWidget(self.login_register_button, 95, 10, 3, 20)
    self.login_layout.addWidget(self.login_welcome_label, 0, 50, 100, 50)
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
    self.login_welcome_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set line edit """
    self.login_password_lineedit.setEchoMode(QLineEdit.Password)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_login_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_password_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_login_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_register_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_welcome_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Login style """
def login_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/login/'+self.global_config['__theme__']+'.css')).read())
#######################################################################################################################
""" Login retranslate"""
def login_retranslate(self):
    _t = self.login_translate # Translate texts 
    _l = self.global_config['__language__'] # Language 
    self.login_login_lineedit.setPlaceholderText(_t['login_login_lineedit'][_l])
    self.login_password_lineedit.setPlaceholderText(_t['login_password_lineedit'][_l])
    self.login_login_button.setText(_t['login_login_button'][_l])
    self.login_register_button.setText(_t['login_register_button'][_l])
    self.login_welcome_label.setText('Good morning!')
#######################################################################################################################
