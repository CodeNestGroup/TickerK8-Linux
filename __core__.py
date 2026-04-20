#   --- Import ---
import sys
import pathlib
import json

#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QMainWindow
    )
from PySide6.QtCore import (
    QRect,
    QThread
    )
from PySide6.QtGui import (
    QGuiApplication,
    QFontDatabase,
    QFont
    )
#   --- Import __core__ modules ---
from package.Update.Structure import UpdateW
from package.UpdateSettings.Structure import UpdateSettingsW
from package.Login.Structure import LoginW
from package.Register.Structure import RegisterW
from package.LoginConfig.Structure import LoginConfigurationW

#   --- Import backend
from package.Db.Connection import Database
from package.Ping.Logic import PingO


#   --- AppWindow ---

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
#           --- AppWindowUi ---
        self.OpenedW = None
        self.setObjectName('AppWindow')
        self.Layout = QVBoxLayout(self)
        self.Layout.setSpacing(0)
        self.Layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.Layout)
#           --- Get app data ---
        self.Path = str(pathlib.Path(__file__).resolve().parents[0])
        self.ConfigOffline = json.load(open(f'{self.Path}/assets/JSON/ConfigOffline.json', 'r', encoding='utf-8'))
        self.Screen = QGuiApplication.primaryScreen()
        self.Geometry = self.Screen.availableGeometry()
#           --- App functions  ---
        self.Database = Database()
        self.PingO = PingO()

#   --- Func for opens windows ---

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
        self.ConfigOffline = json.load(open(f'{self.Path}/assets/JSON/ConfigOffline.json', 'r', encoding='utf-8'))

    def UpdateSettingsOpen(self):
        self.Reset()
        self.OpenedW = UpdateSettingsW(self)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//4, self.Geometry.width()//2, self.Geometry.height()//2
        self.setGeometry(x, y, w, h)

    def UpdateChangelogOpen(self, d):
        self.Reset()
        self.OpenedW = UpdateChangelogW(self, d)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//4, self.Geometry.width()//2, self.Geometry.height()//2
        self.setGeometry(x, y, w, h)

    def LoginOpen(self):
        self.LoggedUserId = None
        self.OpenW = LoginW(self)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//12, self.Geometry.width()//2, self.Geometry.height()//1.25
        self.setGeometry(x, y, w, h)

    def RegisterOpen(self):
        self.OpenW = RegisterW(self)
        self.Layout.addWidget(self.OpenW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//12, self.Geometry.width()//2, self.Geometry.height()//1.25
        self.setGeometry(x, y, w, h)
        
    def LoginConfigurationOpen(self):
        self.OpenedW = LoginConfigurationW(self)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//12, self.Geometry.width()//2, self.Geometry.height()//1.25
        self.setGeometry(x, y, w, h)



        self.login_configuration_widget.accept_button.clicked.connect(self.login_configuration_controller)
        
    def MainOpen(self):
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

    def SetLoggedUserId(self, i):
        self.LoggedUserId = i
    
    def login_configuration_controller(self):
        self.database.LoginConfiguration(self.logged_user_id)
        self.login_configuration_to_login()
            
def SetFont():
    font_id = QFontDatabase.addApplicationFont(str(pathlib.Path(__file__).resolve().parents[0])+'/assets/FONTS/NotoSerif-VariableFont_wdth,wght.ttf')
    font_families = QFontDatabase.applicationFontFamilies(font_id) 
    return QFont(font_families[0])

if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setFont(SetFont())
    AppW = AppWindow()
    AppW.show()
    AppW.UpdateOpen()
    sys.exit(application.exec())
    