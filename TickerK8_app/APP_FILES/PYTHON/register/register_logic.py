""" Import PyQt5 Widgets line edit """
from PyQt5.QtWidgets import QLineEdit
#######################################################################################################################
""" Show hide password """
def show_hide_password(self):
    _l = self.global_config['__language__']
    _t = self.register_translate['register_password_show_button']
    if self.register_password_lineedit.echoMode() == QLineEdit.Normal:
        self.register_password_lineedit.setEchoMode(QLineEdit.Password)
        self.register_password_show_button.setText(_t[_l][1])
    else:
        self.register_password_lineedit.setEchoMode(QLineEdit.Normal)
        self.register_password_show_button.setText(_t[_l][0])
#______________________________________________________________________________________________________________________
""" Show hide confirm password """
def show_hide_confirm_password(self):
    _l = self.global_config['__language__']
    _t = self.register_translate['register_password_confirm_show_button']
    if self.register_password_confirm_lineedit.echoMode() == QLineEdit.Normal:
        self.register_password_confirm_lineedit.setEchoMode(QLineEdit.Password)
        self.register_password_confirm_show_button.setText(_t[_l][1])
    else:
        self.register_password_confirm_lineedit.setEchoMode(QLineEdit.Normal)
        self.register_password_confirm_show_button.setText(_t[_l][0])
#######################################################################################################################
