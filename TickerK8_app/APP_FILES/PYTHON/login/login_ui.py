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
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon # Icon
)
#######################################################################################################################
""" Login Ui """
def login_ui(self):
    """ Set object name """
    self.setObjectName('login_widget')
    self.login_title_label.setObjectName('login_title_label')
    self.login_day_night_button.setObjectName('login_day_night_button')
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
    self.login_layout.addWidget(self.login_day_night_button, 15, 45, 15, 10)
    self.login_layout.addWidget(self.login_login_lineedit, 40, 10, 5, 80)
    self.login_layout.addWidget(self.login_password_lineedit, 55, 10, 5, 80)
    self.login_layout.addWidget(self.login_login_button, 70, 30, 3, 40)
    self.login_layout.addWidget(self.login_register_button, 87, 15, 3, 30)
    self.login_layout.addWidget(self.login_forgot_password_button, 87, 55, 3, 30)
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
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_day_night_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_login_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_password_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_login_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_register_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_forgot_password_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Login style """
def login_reload_style(self):
    #self.login_day_night_button.setIcon(QIcon(self.main_path+'/STYLE/IMG/ICONS/'+))
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/login/'+self.global_config['__theme__']+'.css')).read())

#######################################################################################################################
""" Login retranslate"""
def login_retranslate(self):
    _t = self.login_translate # Translate texts 
    _l = self.global_config['__language__'] # Language 
    self.login_title_label.setText(_t['login_title_label'][_l])
    self.login_login_lineedit.setPlaceholderText(_t['login_login_lineedit'][_l])
    self.login_password_lineedit.setPlaceholderText(_t['login_password_lineedit'][_l])
    self.login_login_button.setText(_t['login_login_button'][_l])
    self.login_register_button.setText(_t['login_register_button'][_l])
    self.login_forgot_password_button.setText(_t['login_forgot_password_button'][_l])
#######################################################################################################################
