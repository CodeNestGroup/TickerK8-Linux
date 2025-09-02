""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QSizePolicy # Size policy.
        )
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt # Qt settings.
)
#######################################################################################################################
""" Register ui """
def register_ui(self):
    """ Set object name """
    self.setObjectName('register_widget')
    self.register_name_subtitle_label.setObjectName('register_name_subtitle_label')
    self.register_name_lineedit.setObjectName('register_name_lineedit')
    self.register_name_label.setObjectName('register_name_label')
    self.register_emial_subtitle_label.setObjectName('register_emial_subtitle_label')
    self.register_emial_lineedit.setObjectName('register_emial_lineedit')
    self.register_emial_confirm_lineedit.setObjectName('register_emial_confirm_lineedit')
    self.register_email_label.setObjectName('register_email_label')
    self.register_phonenumber_subtitle_label.setObjectName('register_phonenumber_subtitle_label')
    self.register_phonenumber_combobox.setObjectName('register_phonenumber_combobox')
    self.register_phonenumber_lineedit.setObjectName('register_phonenumber_lineedit')
    self.register_country_subtitle_label.setObjectName('register_country_subtitle_label')
    self.register_country_combobox.setObjectName('register_country_combobox')
    self.register_password_subtitle_label.setObjectName('register_password_subtitle_label')
    self.register_password_lineedit.setObjectName('register_password_lineedit')
    self.register_password_requirements_label.setObjectName('register_password_requirements_label')
    self.register_password_show_button.setObjectName('register_password_show_button')
    self.register_password_confirm_lineedit.setObjectName('register_password_confirm_lineedit')
    self.register_register_button.setObjectName('register_register_button')
    self.register_exit_button.setObjectName('register_exit_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.register_name_subtitle_label.setProperty('class', 'register_sub_title')
    self.register_emial_subtitle_label.setProperty('class', 'register_sub_title')
    self.register_phonenumber_subtitle_label.setProperty('class', 'register_sub_title')
    self.register_country_subtitle_label.setProperty('class', 'register_sub_title')
    self.register_password_subtitle_label.setProperty('class', 'register_sub_title')
    self.register_name_lineedit.setProperty('class', 'register_input_line')
    self.register_emial_lineedit.setProperty('class', 'register_input_line')
    self.register_emial_confirm_lineedit.setProperty('class', 'register_input_line')
    self.register_phonenumber_lineedit.setProperty('class', 'register_input_line')
    self.register_password_lineedit.setProperty('class', 'register_input_line')
    self.register_password_confirm_lineedit.setProperty('class', 'register_input_line')
    self.register_phonenumber_combobox.setProperty('class', 'register_drop_down_list')
    self.register_name_label.setProperty('class', 'register_label')
    self.register_email_label.setProperty('class', 'register_label')
    self.register_country_combobox.setProperty('class', 'register_drop_down_list')
    self.register_password_show_button.setProperty('class', 'register_password_show_button')
    self.register_register_button.setProperty('class', 'register_button')
    self.register_exit_button.setProperty('class', 'register_button')
#______________________________________________________________________________________________________________________
    """ Set layout"""
    self.register_layout.addWidget(self.register_name_subtitle_label, 5, 5, 3, 40)
    self.register_layout.addWidget(self.register_name_lineedit, 10, 5, 2, 40)
    self.register_layout.addWidget(self.register_name_label, 14, 5, 3, 40)
    self.register_layout.addWidget(self.register_emial_subtitle_label, 5, 55, 2, 40)
    self.register_layout.addWidget(self.register_emial_lineedit, 10, 55, 2, 40)
    self.register_layout.addWidget(self.register_emial_confirm_lineedit, 14, 55, 2, 40)
    self.register_layout.addWidget(self.register_email_label, 18, 55, 2, 40)
    self.register_layout.addWidget(self.register_country_subtitle_label, 30, 5, 3, 40)
    self.register_layout.addWidget(self.register_country_combobox, 35, 5, 2, 40)
    self.register_layout.addWidget(self.register_phonenumber_subtitle_label, 30, 55, 2, 40)
    self.register_layout.addWidget(self.register_phonenumber_combobox, 35, 55, 2, 10)
    self.register_layout.addWidget(self.register_phonenumber_lineedit, 35, 65, 2, 30)
    self.register_layout.addWidget(self.register_password_subtitle_label, 60, 5, 2, 90)
    self.register_layout.addWidget(self.register_password_lineedit, 65, 5, 2, 40)
    self.register_layout.addWidget(self.register_password_requirements_label, 65, 55, 6, 20)
    self.register_layout.addWidget(self.register_password_show_button, 67, 80, 2, 10)
    self.register_layout.addWidget(self.register_password_confirm_lineedit, 69, 5, 2, 40)
    self.register_layout.addWidget(self.register_register_button, 90, 5, 5, 40)
    self.register_layout.addWidget(self.register_exit_button, 90, 55, 5, 40)
    self.register_layout.setSpacing(0)
    self.register_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.register_layout.setRowStretch(enc, 1)
        self.register_layout.setColumnStretch(enc, 1)
    self.setLayout(self.register_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
    self.register_name_label.setHidden(True)
    self.register_email_label.setHidden(True)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.register_name_subtitle_label.setAlignment(Qt.AlignCenter)
    self.register_name_label.setAlignment(Qt.AlignCenter)
    self.register_emial_subtitle_label.setAlignment(Qt.AlignCenter)
    self.register_email_label.setAlignment(Qt.AlignCenter)
    self.register_phonenumber_subtitle_label.setAlignment(Qt.AlignCenter)
    self.register_country_subtitle_label.setAlignment(Qt.AlignCenter)
    self.register_password_subtitle_label.setAlignment(Qt.AlignCenter)
    self.register_password_requirements_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set line edit """
    self.register_password_lineedit.setEchoMode(QLineEdit.Password)
    self.register_password_confirm_lineedit.setEchoMode(QLineEdit.Password)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.register_name_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_name_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_emial_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_emial_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_emial_confirm_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_email_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_phonenumber_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_phonenumber_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_phonenumber_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_country_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_country_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_requirements_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_show_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_confirm_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_register_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Combo box add item """
    self.register_phonenumber_combobox.addItems(
        [
            "+93",
            "+48"

        ]
    )
    self.register_country_combobox.addItems(
        [
            "Afganistan",
            "Polska"
        ]
    )
#######################################################################################################################
""" Register reload style """
def register_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/register/'+self.global_config['__theme__']+'.css')).read())
#######################################################################################################################
""" Register retranslate"""
def register_retranslate(self):
    _t = self.register_translate # Translate texts 
    _l = self.global_config['__language__'] # Laguage 
    self.register_name_subtitle_label.setText(_t['register_name_subtitle_label'][_l])
    self.register_name_lineedit.setPlaceholderText(_t['register_name_lineedit'][_l])
    self.register_emial_subtitle_label.setText(_t['register_emial_subtitle_label'][_l])
    self.register_emial_lineedit.setPlaceholderText(_t['register_emial_lineedit'][_l])
    self.register_emial_confirm_lineedit.setPlaceholderText(_t['register_emial_confirm_lineedit'][_l])
    self.register_phonenumber_subtitle_label.setText(_t['register_phonenumber_subtitle_label'][_l])
    self.register_phonenumber_lineedit.setPlaceholderText(_t['register_phonenumber_lineedit'][_l])
    self.register_country_subtitle_label.setText(_t['register_country_subtitle_label'][_l])
    self.register_password_subtitle_label.setText(_t['register_password_subtitle_label'][_l])
    self.register_password_requirements_label.setText(_t['register_password_requirements_label'][0][_l])
    self.register_password_show_button.setText(_t['register_password_show_button'][_l][1])
    self.register_password_lineedit.setPlaceholderText(_t['register_password_lineedit'][_l])
    self.register_password_confirm_lineedit.setPlaceholderText(_t['register_password_confirm_lineedit'][_l])
    self.register_register_button.setText(_t['register_register_button'][0][_l])
    self.register_exit_button.setText(_t['register_exit_button'][_l])
#######################################################################################################################
