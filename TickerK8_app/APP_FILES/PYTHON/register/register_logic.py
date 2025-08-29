""" Import packages """
import string # For strings.
import mysql # For connect with database.
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets line edit """
from PyQt5.QtWidgets import QLineEdit
#######################################################################################################################
""" Show hide password """
def show_hide_password(self):
    """ Variables """
    _l = self.global_config['__language__'] # Get language, local.
    _t = self.register_translate['register_password_show_button'] # Get translate, local.
    """ Set hide or show """
    if self.register_password_lineedit.echoMode() == QLineEdit.Normal:
        self.register_password_lineedit.setEchoMode(QLineEdit.Password)
        self.register_password_show_button.setText(_t[_l][1])
    else:
        self.register_password_lineedit.setEchoMode(QLineEdit.Normal)
        self.register_password_show_button.setText(_t[_l][0])
#######################################################################################################################
""" Register controller """
def register_controller(self):
    """ Variables """
    _t = self.register_translate
    _l = self.global_config['__language__']
    c_n = None
    c_e = None
    c_p = None
    c_c = None
    c_pass = None
#______________________________________________________________________________________________________________________
    """ Database """
    connect = mysql.connector.connect( # Connect to database.
        host = "localhost",
        user = "register_user",
        password = "Qwerty123456#",
        database = "TickerK8"
    )
    cursor = connect.cursor()# Creating cursor.
#______________________________________________________________________________________________________________________
    """ Check if name exists """
    cursor.execute('SELECT id FROM WHERE name=%s;', (self.register_name_lineedit.text()))
    c_n_e = cursor.fetchone()
    if not c_n_e:
        c_n = self.register_name_lineedit.text()
    else:
        c_n = None
        self.register_name_label.setHidden(False)
        self.register_name_label.setText(f'{_t['register_name_label'][_l]}')
        self.register_name_lineedit.clear()
        self.register_name_lineedit.setStyleSheet('border: 2px solid red;')
#______________________________________________________________________________________________________________________
    """ Check if emial exists"""
    cursor.execute('SELECT id FROM WHERE name=%s;', (self.register_emial_lineedit.text()))
    if not c_e_e and self.register_emial_confirm_lineedit.text() == self.register_emial_lineedit.text():
        c_e = self.register_emial_confirm_lineedit.text() # Set correct email
    else:
        c_e = None
        self.register_email_label.setHidden(False)
        self.register_email_label.setText(f'{_t['register_email_label'][_l]}')
        self.register_emial_confirm_lineedit.clear()
        self.register_emial_confirm_lineedit.setStyleSheet('border: 2px solid red;')
#______________________________________________________________________________________________________________________
    """ Check if phone correct """
    try:
        if self.register_phonenumber_combobox.text() != '':
            int(self.register_phonenumber_lineedit.text())
            c_p = f'{self.register_phonenumber_combobox.currentText()}{self.register_phonenumber_lineedit.text()}'
    except:
        c_p = None
        self.register_phonenumber_lineedit.clear()
        self.register_phonenumber_lineedit.setText(f'{_t['register_phonenumber_lineedit_error'][_l]}')
        self.register_phonenumber_lineedit.setStyleSheet('border: 2px solid red;')
#______________________________________________________________________________________________________________________
    """ Country set """
    c_c = self.register_country_combobox.currentText()
#______________________________________________________________________________________________________________________
    """ Check if password correct"""
    _password_confirm = self.register_password_confirm_lineedit.text()
    if len(_password_confirm) >= 8 and any(h.isupper() for h in _password_confirm) and any(h.isdigit() for h in _password_confirm) and any(h in string.punctuation for h in _password_confirm):
        if self.register_password_lineedit.text() == _password_confirm:
            c_pass = _password_confirm
        else:
            c_pass = None
            self.register_password_lineedit.clear()
            self.register_password_lineedit.setStyleSheet('border: 2px solid red;')
            self.register_password_lineedit.setText(f'{_t['register_password_lineedit_error'][0][_l]}')
            self.register_password_confirm_lineedit.clear()
            self.register_password_confirm_lineedit.setStyleSheet('border: 2px solid red;')
    else:
        c_pass = None
        self.register_password_lineedit.clear()
        self.register_password_lineedit.setStyleSheet('border: 2px solid red;')
        self.register_password_lineedit.setText(f'{_t['register_password_lineedit'][1][_l]}')
        self.register_password_confirm_lineedit.clear()
        self.register_password_confirm_lineedit.setStyleSheet('border: 2px solid red;')
#______________________________________________________________________________________________________________________
    """ Correct register call function """
    if c_n and c_e and c_p and c_c and c_pass:
        correct_register(self, c_n, c_e, c_p, c_c, c_pass)
#______________________________________________________________________________________________________________________
    """ Close connection """
    cursor.close()
    connect.close()
#######################################################################################################################
""" Correct register """
def correct_register(self, name, email, phone, country, password):
    """ Variables """
    _name = name
    _emial = email
    _phone = phone
    _country = country
    _password = password
#______________________________________________________________________________________________________________________
    """ Database """
    connect = mysql.connector.connect( # Connect to database.
        host = "localhost",
        user = "register_user",
        password = "Qwerty123456#",
        database = "TickerK8"
    )
    cursor = connect.cursor()# Creating cursor.
    cursor.execute('INSERT INTO users (name, emial, phone, country, password) values(%s, %s, %s, %s, %s);', (_name, _emial, _phone, _country, _password)) # Execute query.
    connect.commit() # Commit changes.
    cursor.close() # Close connection.
    connect.close()
#######################################################################################################################
""" Reset name """
def reset_name(self):
    pass
#######################################################################################################################
""" Reset email """
def reset_email(self):
    pass
#######################################################################################################################
""" Reset phone """
def reset_phone(self):
    pass
#######################################################################################################################
""" Reset password """
def reset_password(self):
    pass
#######################################################################################################################
