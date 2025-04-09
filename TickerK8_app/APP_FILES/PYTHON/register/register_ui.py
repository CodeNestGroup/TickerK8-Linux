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
""" Register ui """
def register_ui(self):
    """ Set object name """
    self.setObjectName('register_widget')
    self.register_title_label.setObjectName('register_title_label')
    self.register_name_subtitle_label.setObjectName('register_name_subtitle_label')
    self.register_name_lineedit.setObjectName('register_name_lineedit')
    self.register_name_combobox.setObjectName('register_name_combobox')
    self.register_emial_subtitle_label.setObjectName('register_emial_subtitle_label')
    self.register_emial_lineedit.setObjectName('register_emial_lineedit')
    self.register_emial_confirm_lineedit.setObjectName('register_emial_confirm_lineedit')
    self.register_phonenumber_subtitle_label.setObjectName('register_phonenumber_subtitle_label')
    self.register_phonenumber_combobox.setObjectName('register_phonenumber_combobox')
    self.register_phonenumber_lineedit.setObjectName('register_phonenumber_lineedit')
    self.register_country_subtitle_label.setObjectName('register_country_subtitle_label')
    self.register_country_combobox.setObjectName('register_country_combobox')
    self.register_password_subtitle_label.setObjectName('register_password_subtitle_label')
    self.register_password_lineedit.setObjectName('register_password_lineedit')
    self.register_password_show_button.setObjectName('register_password_show_button')
    self.register_password_confirm_lineedit.setObjectName('register_password_confirm_lineedit')
    self.register_password_confirm_show_button.setObjectName('register_password_confirm_show_button')
    self.register_register_button.setObjectName('register_register_button')
    self.register_exit_button.setObjectName('register_exit_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.register_name_subtitle_label.setProperty('class', 'register_sub_title')
    self.register_emial_subtitle_label.setProperty('class', 'register_sub_title')
    self.register_phonenumber_subtitle_label.setProperty('class', 'register_sub_title')
    self.register_country_subtitle_label.setProperty('class', 'register_sub_title')
    self.register_password_subtitle_label.setProperty('class', 'register_sub_title')
    self.register_password_show_button.setProperty('class', 'register_password_show_button')
    self.register_password_confirm_show_button.setProperty('class', 'register_password_show_button')
    self.register_register_button.setProperty('class', 'register_button')
    self.register_exit_button.setProperty('class', 'register_button')
#______________________________________________________________________________________________________________________
    """ Set layout"""
    self.register_layout.addWidget(self.register_title_label, 5, 0, 5, 100)
    self.register_layout.addWidget(self.register_name_subtitle_label, 13, 0, 2, 100)
    self.register_layout.addWidget(self.register_name_lineedit, 15, 5, 2, 40)
    self.register_layout.addWidget(self.register_name_combobox, 15, 55, 2, 40)
    self.register_layout.addWidget(self.register_emial_subtitle_label, 20, 0, 2, 100)
    self.register_layout.addWidget(self.register_emial_lineedit, 22, 5, 2, 90)
    self.register_layout.addWidget(self.register_emial_confirm_lineedit, 25, 5, 2, 90)
    self.register_layout.addWidget(self.register_phonenumber_subtitle_label, 30, 0, 2, 100)
    self.register_layout.addWidget(self.register_phonenumber_combobox, 32, 5, 2, 20)
    self.register_layout.addWidget(self.register_phonenumber_lineedit, 32, 25, 2, 65)
    self.register_layout.addWidget(self.register_country_subtitle_label, 37, 0, 2, 100)
    self.register_layout.addWidget(self.register_country_combobox, 39, 5, 2, 90)
    self.register_layout.addWidget(self.register_password_subtitle_label, 44, 0, 2, 100)
    self.register_layout.addWidget(self.register_password_lineedit, 46, 5, 2, 70)
    self.register_layout.addWidget(self.register_password_show_button, 46, 80, 2, 15)
    self.register_layout.addWidget(self.register_password_confirm_lineedit, 49, 5, 2, 70)
    self.register_layout.addWidget(self.register_password_confirm_show_button, 49, 80, 2, 15)
    self.register_layout.addWidget(self.register_register_button, 85, 28, 5, 20)
    self.register_layout.addWidget(self.register_exit_button, 85, 52, 5, 20)
    self.register_layout.setSpacing(0)
    self.register_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.register_layout.setRowStretch(enc, 1)
        self.register_layout.setColumnStretch(enc, 1)
    self.setLayout(self.register_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.register_title_label.setAlignment(Qt.AlignCenter)
    self.register_name_subtitle_label.setAlignment(Qt.AlignCenter)
    self.register_emial_subtitle_label.setAlignment(Qt.AlignCenter)
    self.register_phonenumber_subtitle_label.setAlignment(Qt.AlignCenter)
    self.register_country_subtitle_label.setAlignment(Qt.AlignCenter)
    self.register_password_subtitle_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set line edit """
    self.register_password_lineedit.setEchoMode(QLineEdit.Password)
    self.register_password_confirm_lineedit.setEchoMode(QLineEdit.Password)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.register_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_name_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_name_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_name_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_emial_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_emial_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_emial_confirm_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_phonenumber_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_phonenumber_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_phonenumber_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_country_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_country_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_show_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_confirm_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_confirm_show_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_register_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Register reload style """
def register_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/REGISTER/'+self.global_config['__theme__']+'.css')).read())
#######################################################################################################################
""" Logi retranslate"""
def login_retranslate(self):
    _t = self.register_translate # Translate texts 
    _l = self.global_config['__language__'] # Laguage 
    self.register_title_label.setText(_t['register_title_label'][_l])
    self.register_name_subtitle_label.setText(_t['register_name_subtitle_label'][_l])
    self.register_name_lineedit.setPlaceholderText(_t['register_name_lineedit'][_l])
    self.register_emial_subtitle_label.setText(_t['register_emial_subtitle_label'][_l])
    self.register_emial_lineedit.setPlaceholderText(_t['register_emial_lineedit'][_l])
    self.register_emial_confirm_lineedit.setPlaceholderText(_t['register_emial_confirm_lineedit'][_l])
    self.register_phonenumber_subtitle_label.setText(_t['register_phonenumber_subtitle_label'][_l])
    self.register_phonenumber_lineedit.setPlaceholderText(_t['register_phonenumber_lineedit'][_l])
    self.register_country_subtitle_label.setText(_t['register_country_subtitle_label'][_l])
    self.register_password_subtitle_label.setText(_t['register_password_subtitle_label'][_l])
    self.register_password_lineedit.setPlaceholderText(_t['register_password_lineedit'][_l])
    self.register_password_confirm_lineedit.setPlaceholderText(_t['register_password_confirm_lineedit'][_l])
    self.register_register_button.setText(_t['register_register_button'][_l])
    self.register_exit_button.setText(_t['register_exit_button'][_l])
#######################################################################################################################
