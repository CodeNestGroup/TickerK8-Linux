#   --- Import ---
import sys
import pathlib
import json

#   --- Import PySide2 ---
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QDesktopWidget,
    QMainWindow
    )
from PySide2.QtCore import (
    QRect
    )
from PySide2.QtGui import (
    QFontDatabase,
    QFont
    )
#   --- Import main modules ---
from .package.Update.Structure import UpdateW
from .package.UpdateSettings.Structure import UpdateSettingsW




from login.structure import Login_widget
from register.structure import Register_widget
from login_config.p_structure import Login_configuration_widget
from recover_password.structure import Recover_password_widget
from Main.AStructure import MainW 
from Settings.AStructure import SettingsW
from statistics.structure import Statistics_widget
from chart.structure import Chart_widget
#   --- Import backend
from db.connection import database


#   --- AppWindow ---

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
#           --- AppWindow Ui ---
        self.setObjectName('AppWindow')
        self.Layout = QVBoxLayout(self)
        self.Layout.setSpacing(0)
        self.Layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.Layout)
        self.OpenedW = None
#           --- App default varaibles ---
        self.Path = str(pathlib.Path(__file__).resolve().parents[2])
        self.LoggedUserId = None
        self.Screen = QApplication.screen()
        self.Geometry = self.Screen.availableGeometry()
#           --- Database Class  ---
        self.Database = Database()
#       --- Func for opens windows ---

    def Reset(self):
        if self.OpenedW:
            self.OpenedW.deleteLater()
            self.OpenedW = None

    def UpdateOpen(self):
        self.Reset()
        self.OpenedW = UpdateW(self)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//4, self.Geometry.width()//2, self.Geometry.height()//2
        self.setGeometry(x, y, w, h)

    def UpdateSettingsOpen(self):
        self.Reset()
        self.OpenedW = UpdateSettingsW(self)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//4, self.Geometry.width()//2, self.Geometry.height()//2
        self.setGeometry(x, y, w, h)
        self.OpenedW.ExitB.clicked.connect(self.UpdateOpen)

    def UpdateChangelogOpen(self):
        self.Reset()
        self.OpenedW = UpdateChangelogW(self)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//4, self.Geometry.width()//2, self.Geometry.height()//2
        self.setGeometry(x, y, w, h)
        self.OpenedW.ExitB.clicked.connect(self.UpdateOpen)


    def LoginOpen(self):
        self.logged_user_id = None

        self.login_widget = Login_widget(self)
        self.layout.addWidget(self.login_widget)
        self.setGeometry(QRect(self.pos_x, self.pos_y, self.width, self.height))
        self.login_widget.login_login_button.clicked.connect(self.login_controller)
        self.login_widget.login_register_button.clicked.connect(self.login_to_register)
    
    def register_setup(self):
        self.register_widget = Register_widget(self)
        self.layout.addWidget(self.register_widget)
        self.setGeometry(QRect(self.pos_x, self.pos_y, self.width, self.height))
        self.register_add_country()
        self.register_add_prefix()
        self.register_widget.correct_data.connect(self.register_user)
        self.register_widget.register_exit_button.clicked.connect(self.register_to_login)
    
    def login_configuration_setup(self):
        self.login_configuration_widget = Login_configuration_widget(self)
        self.layout.addWidget(self.login_configuration_widget)
        self.setGeometry(QRect(self.pos_x, self.pos_y, self.width, self.height))
        self.login_configuration_widget.accept_button.clicked.connect(self.login_configuration_controller)
        self.login_configuration_widget.exit_button.clicked.connect(self.login_configuration_to_login)
    
    def main_setup(self):
        self.main_widget = MainW(self)
        self.layout.addWidget(self.main_widget)
        self.setGeometry(self.geometry)
        self.showMaximized()
        self.main_widget.NavSettingsB.clicked.connect(self.main_to_settings)
        self.main_widget.NavLogoutB.clicked.connect(self.main_to_login)

    def settings_setup(self):
        self.settings_widget = SettingsW(self)
        self.layout.addWidget(self.settings_widget)
        self.setGeometry(self.geometry)
        self.showMaximized()
        self.settings_widget.NaviExitB.clicked.connect(self.settings_to_main)
    
    def login_to_register(self):
        self.login_widget.deleteLater()
        self.login_widget = None 
        self.register_setup()

    def register_to_login(self):
        self.register_widget.deleteLater()
        self.register_widget = None
        self.login_setup()

    def login_to_login_configuration(self):
        self.login_widget.deleteLater()
        self.login_widget = None 
        self.login_configuration_setup()
    
    def login_configuration_to_login(self):
        self.login_configuration_widget.deleteLater()
        self.login_configuration_widget = None
        self.login_setup()

    def forgot_password_to_login(self):
        self.recover_password_widget.deleteLater()
        self.recover_password_widget = None
        self.login_setup()

    def login_to_main(self):
        self.login_widget.deleteLater()
        self.login_widget = None
        self.main_setup()

    def main_to_login(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.login_setup()

    def main_to_settings(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.settings_setup()

    def settings_to_main(self):
        self.database.SaveSettings(self.logged_user_id, self.settings_widget.Config['theme'], self.settings_widget.Config['language'])
        self.settings_widget.deleteLater()
        self.settings_widget = None
        self.main_setup()


#   --- Modules functions  ---

    def login_controller(self):
        d = self.database.LoginByName(str(self.login_widget.login_login_lineedit.text()))
        if d[1] == self.login_widget.login_password_lineedit.text():
            if d[2]:
                pass # Dopisać kiedyś notyfikacje że ktoś inny jest już zalogowany
            else:
                self.logged_user_id = d[0]
                if not d[3]:
                    self.login_to_login_configuration()
                else:
                    self.database.UpdateLastLogin(d[0])
                    self.login_to_main()
        else:
            self.login_widget.login_login_lineedit.clear()
            self.login_widget.login_password_lineedit.clear()
            self.login_widget.login_login_lineedit.setStyleSheet('border: 2px solid red;')
            self.login_widget.login_password_lineedit.setStyleSheet('border: 2px solid red;')
    
    def register_add_country(self):
        r = self.database.GetCountries()
        self.register_widget.register_country_combobox.addItems(r)
    
    def register_add_prefix(self):
        r = self.database.GetPhonePrefix()
        self.register_widget.register_phonenumber_combobox.addItems(r)

    def register_user(self, user_data: tuple):
        try:
            err = self.database.RegisterUser(user_data)
            if not err:
                self.register_to_login()
            else:
                for e in err:
                    if e == 'USER_EXISTS':
                        self.register_widget.user_exists()
                    elif e == 'EMAIL_EXISTS':
                        self.register_widget.email_exists()
                    elif e == 'PHONE_EXISTS_IN_PREFIX':
                        self.register_widget.phone_exists()
                    else:
                        raise Exception
        except Exception as e:
            print(e) # Dopisz do logi
    
    def login_configuration_controller(self):
        self.database.LoginConfiguration(self.logged_user_id)
        self.login_configuration_to_login()
            

def set_font():
    font_id = QFontDatabase.addApplicationFont(str(pathlib.Path(__file__).resolve().parents[3])+'/TickerK8_app/APP_FILES/STYLE/FONTS/NotoSerif-VariableFont_wdth,wght.ttf')
    font_families = QFontDatabase.applicationFontFamilies(font_id) 
    return QFont(font_families[0])

if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setFont(set_font())
    AppW = AppWindow()
    AppW.show()
    AppW.UpdateOpen()
    sys.exit(application.exec())
    