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
    if self.register_password_lineedit.echoMode() == QLineEdit.Normal: # Check if normal.
        self.register_password_lineedit.setEchoMode(QLineEdit.Password) # Set Password mode.
        self.register_password_show_button.setText(_t[_l][1])
    else:
        self.register_password_lineedit.setEchoMode(QLineEdit.Normal) # Set Normal mode.
        self.register_password_show_button.setText(_t[_l][0])
#######################################################################################################################
""" Register controller """
def register_controller(self):
    """ Variables """
    """ Texts """
    _t = self.register_translate # Get translate, local.
    _l = self.global_config['__language__'] # Get language, local.
    """ Style """
    _wrong_data = 'border: 2px solid #c01414;'
    """ Data to insert """
    c_n = None # Correct name.
    c_e = None # Correct email.
    c_p = None # Correct phone number.
    c_c = None # Correct country.
    c_pass = None # Correct password.
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
    if self.register_name_lineedit.text() != '': # Check if name line is not empty.
        _name_line = self.register_name_lineedit.text() # Get text from line.
        cursor.execute('SELECT id FROM users WHERE name=%s;', (_name_line,)) # Send request.
        c_n_e = cursor.fetchall() # Get data.
        if c_n_e == []: # Check if name exists in database.
            c_n = _name_line # Set correct name.
        else:
            c_n = None # Set none for name.
            self.register_name_label.setHidden(False) # Show error name label.
            self.register_name_label.setText(f'{_t['register_name_label'][1][_l]}')
            self.register_name_lineedit.setStyleSheet(_wrong_data)
    else:
        c_n = None # Set none for name.
        self.register_name_label.setHidden(False) # Show error name label.
        self.register_name_label.setText(f'{_t['register_name_label'][0][_l]}')
        self.register_name_lineedit.setStyleSheet(_wrong_data)
#______________________________________________________________________________________________________________________
    """ Check if emial exists"""
    if self.register_emial_lineedit.text() != '': # Check if emial line is not empty.
        _email_line = self.register_emial_lineedit.text() # Get text from line.
        cursor.execute('SELECT id FROM users WHERE emial=%s;', (_email_line,)) # Send request.
        c_e_e = cursor.fetchall() # Get data.
        if c_e_e == []: # Check if emial exists in database.
            if self.register_emial_confirm_lineedit.text() == _email_line: # Check if confirm line is same as first line.
                c_e = _email_line # Set correct email.
            else:
                c_e = None # Set none for email.
                self.register_email_label.setHidden(False) # Show error email label.
                self.register_email_label.setText(f'{_t['register_email_label'][2][_l]}')
                self.register_emial_confirm_lineedit.setStyleSheet(_wrong_data)
        else:
            c_e = None # Set none for email.
            self.register_email_label.setHidden(False) # Show error email label.
            self.register_email_label.setText(f'{_t['register_email_label'][1][_l]}')
            self.register_emial_lineedit.setStyleSheet(_wrong_data)
            self.register_emial_confirm_lineedit.setStyleSheet(_wrong_data)
    else:
        c_e = None # Set none for email.
        self.register_email_label.setHidden(False) # Show error emial label.
        self.register_email_label.setText(f'{_t['register_email_label'][0][_l]}')
        self.register_emial_lineedit.setStyleSheet(_wrong_data)
        self.register_emial_confirm_lineedit.setStyleSheet(_wrong_data)
#______________________________________________________________________________________________________________________
    """ Check if phone correct """
    try: # Checking if phone number is int.
        if self.register_phonenumber_lineedit.text() != '': # Check if emial line is not empty.
            int_nunber = int(self.register_phonenumber_lineedit.text()) # Get text from line and convert to intiger.
            c_p = f'{self.register_phonenumber_combobox.currentText()}{int_nunber}' # Set correct phone number.
    except:
        c_p = None# Set none for phone number.
        self.register_phonenumber_lineedit.setText(f'{_t['register_phonenumber_lineedit_error'][_l]}')
        self.register_phonenumber_lineedit.setStyleSheet(_wrong_data)
#______________________________________________________________________________________________________________________
    """ Country set """
    c_c = self.register_country_combobox.currentText() # Set correct country.
#______________________________________________________________________________________________________________________
    """ Check if password correct"""
    _password_confirm = self.register_password_confirm_lineedit.text() # Get text from line.
    if len(_password_confirm) >= 8 and any(h.isupper() for h in _password_confirm) and any(h.isdigit() for h in _password_confirm) and any(h in string.punctuation for h in _password_confirm): # Check if password pass requirments.
        if self.register_password_lineedit.text() == _password_confirm: # Check if confirm same as first line.
            c_pass = _password_confirm # Set correct password.
        else:
            c_pass = None # Set none for password.
            self.register_password_requirements_label.setText(f'{_t['register_password_requirements_label'][1][_l]}')
            self.register_password_confirm_lineedit.setStyleSheet(_wrong_data)
    else:
        c_pass = None # Set none for password.
        self.register_password_lineedit.setStyleSheet('border: 2px solid #c01414;')
        self.register_password_requirements_label.setText(f'{_t['register_password_requirements_label'][2][_l]}')
#______________________________________________________________________________________________________________________
    """ Correct register call function """
    if c_n and c_e and c_p and c_c and c_pass: # Check if all varriables are good.
        correct_register(self, c_n, c_e, c_p, c_c, c_pass) # Call correct register function.
#______________________________________________________________________________________________________________________
    """ Close connection """
    cursor.close()
    connect.close()
#######################################################################################################################
""" Correct register """# 
def correct_register(self, name, email, phone, country, password):
    """ Variables """
    _name = name # Set name, local.
    _emial = email # Set email, local.
    _phone = phone # Set phone number, local.
    _country = country # Set country, local.
    _password = password # Set password, local.
    _t = self.register_translate # Get translate, local.
    _l = self.global_config['__language__'] # Get language, local.
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
#______________________________________________________________________________________________________________________
    """ Confirm cuccess"""
    self.register_name_lineedit.setDisabled(True)
    self.register_emial_lineedit.setDisabled(True)
    self.register_emial_confirm_lineedit.setDisabled(True)
    self.register_phonenumber_combobox.setDisabled(True)
    self.register_phonenumber_lineedit.setDisabled(True)
    self.register_country_combobox.setDisabled(True)
    self.register_password_lineedit.setDisabled(True)
    self.register_password_confirm_lineedit.setDisabled(True)
    self.register_register_button.setDisabled(True)
    self.register_register_button.setText(_t['register_register_button'][1][_l])
    self.register_register_button.setStyleSheet('background-color: #2e8317;')
#######################################################################################################################
""" Reset name """
def reset_name(self):
    self.register_name_label.setHidden(True) # Hide error label.
    self.register_name_lineedit.setStyleSheet('border: 0;') # reset line edit.
#######################################################################################################################
""" Reset email """
def reset_email(self):
    self.register_email_label.setHidden(True) # Hide error label.
    self.register_emial_lineedit.setStyleSheet('border: 0;')
    self.register_emial_confirm_lineedit.setStyleSheet('border: 0;')
#######################################################################################################################
""" Reset confirm email """
def reset_confirm_email(self):
    self.register_email_label.setHidden(True) # Hide error label.
    self.register_emial_confirm_lineedit.setStyleSheet('border: 0;')
#######################################################################################################################
""" Reset phone """
def reset_phone(self):
    self.register_phonenumber_lineedit.setStyleSheet('border: 0;')
#######################################################################################################################
""" Reset password """
def reset_password(self):
    _t = self.register_translate # Get translate, local.
    _l = self.global_config['__language__'] # Get language, local.
    self.register_password_requirements_label.setText(f'{_t['register_password_requirements_label'][0][_l]}')
    self.register_password_lineedit.setStyleSheet('border: 0;')
#######################################################################################################################
""" Reset confirm password """
def reset_confirm_password(self):
    _t = self.register_translate # Get translate, local.
    _l = self.global_config['__language__'] # Get language, local.
    self.register_password_requirements_label.setText(f'{_t['register_password_requirements_label'][0][_l]}')
    self.register_password_confirm_lineedit.setStyleSheet('border: 0;')
#######################################################################################################################
