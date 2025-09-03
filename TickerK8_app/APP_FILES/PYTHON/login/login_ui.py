""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QLineEdit, # Simple line edit.
    QSizePolicy # Size policy.
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt # Qt.
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
    self.login_welcome_title_label.setObjectName('login_welcome_title_label')
    self.login_welcome_sub_label.setObjectName('login_welcome_sub_label')
    self.login_welcome_icon_label.setObjectName('login_welcome_icon_label')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.login_login_lineedit.setProperty('class', 'login_input_line')
    self.login_password_lineedit.setProperty('class', 'login_input_line')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.login_layout.addWidget(self.login_login_lineedit, 42, 4, 4, 42)
    self.login_layout.addWidget(self.login_password_lineedit, 48, 4, 4, 42)
    self.login_layout.addWidget(self.login_login_button, 56, 12, 2, 26)
    self.login_layout.addWidget(self.login_register_button, 97, 15, 1, 20)
    self.login_layout.addWidget(self.login_welcome_title_label, 30, 50, 15, 50)
    self.login_layout.addWidget(self.login_welcome_sub_label, 45, 50, 10, 50)
    self.login_layout.addWidget(self.login_welcome_icon_label, 55, 50, 10, 50)
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
    self.login_welcome_title_label.setAlignment(Qt.AlignCenter)
    self.login_welcome_sub_label.setAlignment(Qt.AlignCenter)
    self.login_welcome_icon_label.setAlignment(Qt.AlignCenter)
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
    self.login_welcome_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_welcome_sub_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_welcome_icon_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Login style """
def login_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/login/vintage_elegance_dark.css')).read())
#######################################################################################################################
""" Login retranslate"""
def login_retranslate(self):
    _t = self.login_translate # Translate texts.
    _l = self.global_config['__language__'] # Language.
    self.login_login_lineedit.setPlaceholderText(_t['login_login_lineedit'][_l])
    self.login_password_lineedit.setPlaceholderText(_t['login_password_lineedit'][_l])
    self.login_login_button.setText(_t['login_login_button'][_l])
    self.login_register_button.setText(_t['login_register_button'][_l])
#######################################################################################################################
