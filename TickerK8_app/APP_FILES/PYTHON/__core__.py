""" Import packages """
import sys
import pathlib
#_______________________________________________________________________________________________________________________
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QDesktopWidget,
    QMainWindow
    )
from PyQt5.QtCore import (
    QRect
)
from PyQt5.QtGui import (
    QFontDatabase,
    QFont
    )
#______________________________________________________________________________________________________________________
""" Import application modules """
from login.login_structure import Login_widget
from register.register_structre import Register_widget
from recover_password.recover_password_structure import Recover_password_widget
from main.main_structure import Main_widget 
from settings.settings_structure import Settings_widget
from statistics.statistics_structure import Statistics_widget
from chart.chart_structure import Chart_widget
#______________________________________________________________________________________________________________________
""" App controller """
class app_controller(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('window')
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        self.login_widget = None
        self.register_widget = None
        self.recover_password_widget = None
        self.main_widget = None
        self.settings_widget = None
        self.statistics_widget = None
        self.chart_widget = None
        self.primary_screen_size = QApplication.primaryScreen().size()
        self.login_setup()
#______________________________________________________________________________________________________________________
    """ Login """
    """ Login setup """
    def login_setup(self):
        self.login_widget = Login_widget(self)
        self.layout.addWidget(self.login_widget)
        self.set_size_login()
        
        self.login_widget.correct_login.connect(self.login_to_main)
        self.login_widget.login_register_button.clicked.connect(self.login_to_register)
#______________________________________________________________________________________________________________________
    """ Set size login"""
    def set_size_login(self):
        x, y, width, height = int(self.primary_screen_size.width()//4), int(self.primary_screen_size.height()//12), int(self.primary_screen_size.width()//2), int(self.primary_screen_size.height()//1.25)
        self.setGeometry(QRect(x, y, width, height)) 
#______________________________________________________________________________________________________________________
    """ Register """
    def register_setup(self):
        self.register_widget = Register_widget(self)
        self.layout.addWidget(self.register_widget)
        self.set_size_register()
        self.register_widget.register_exit_button.clicked.connect(self.register_to_login)
#______________________________________________________________________________________________________________________
    """ Set size register """
    def set_size_register(self):
        x, y, width, height = int(self.primary_screen_size.width()//4), int(self.primary_screen_size.height()//12), int(self.primary_screen_size.width()//2), int(self.primary_screen_size.height()//1.25)
        self.setGeometry(QRect(x, y, width, height))
#______________________________________________________________________________________________________________________
    """ Recover password """
    def recover_password_setup(self):
        self.recover_password_widget = Recover_password_widget(self)
        self.layout.addWidget(self.recover_password_widget)
        self.set_size_recover_password()
        self.recover_password_widget.recover_password_exit_button.clicked.connect(self.forgot_password_to_login)
#______________________________________________________________________________________________________________________
    """ Set size recover password """
    def set_size_recover_password(self):
        x, y, width, height = int(self.primary_screen_size.width()//4), int(self.primary_screen_size.height()//12), int(self.primary_screen_size.width()//2), int(self.primary_screen_size.height()//1.25)
        self.setGeometry(QRect(x, y, width, height))
#______________________________________________________________________________________________________________________
    """ Main """
    def main_setup(self):
        self.main_widget = Main_widget(self)
        self.layout.addWidget(self.main_widget)
        self.set_size_main()
        self.main_widget.settings_button.clicked.connect(self.main_to_settings)
        self.main_widget.logout_button.clicked.connect(self.main_to_login)
#______________________________________________________________________________________________________________________
    """ Set size main """
    def set_size_main(self):
        screen = self.windowHandle().screen()
        geometry = screen.availableGeometry()
        self.showMaximized()
#______________________________________________________________________________________________________________________
    """ Settings """
    def settings_setup(self):
        self.settings_widget = Settings_widget(self)
        self.layout.addWidget(self.settings_widget)
        self.set_size_settings()
        self.settings_widget.navi_exit_button.clicked.connect(self.settings_to_main)
#______________________________________________________________________________________________________________________
    """ Set size settings """
    def set_size_settings(self):
        screen = self.windowHandle().screen()
        geometry = screen.availableGeometry()
        self.showMaximized()
#______________________________________________________________________________________________________________________
    """ Statistics """
    def statistics_setup(self):
        self.statistics_widget = Statistics_widget(self)
        self.layout.addWidget(self.statistics_widget)
        self.set_size_statistics()
        self.statistics_widget.main_exit_button.clicked.connect(self.statistics_to_main)
#______________________________________________________________________________________________________________________
    """ Set size statistics """
    def set_size_statistics(self):
        x, y, width, height = 0, 0, int(self.primary_screen_size.width()), int(self.primary_screen_size.height())
        self.setGeometry(QRect(x, y, width, height))
#______________________________________________________________________________________________________________________
    """ Chart """
    def chart_setup(self):
        self.chart_widget = Chart_widget(self)
        self.layout.addWidget(self.chart_widget)
        self.set_size_chart()
        self.chart_widget.top_exit_button.clicked.connect(self.chart_to_main)
#______________________________________________________________________________________________________________________
    """ Set size chart """
    def set_size_chart(self):
        x, y, width, height = 0, 0, int(self.primary_screen_size.width()), int(self.primary_screen_size.height()) 
        self.setGeometry(QRect(x, y, width, height))
#______________________________________________________________________________________________________________________
    """ From login to register """
    def login_to_register(self):
        self.login_widget.deleteLater()
        self.login_widget = None 
        self.register_setup()
#______________________________________________________________________________________________________________________
    """ From register to login """
    def register_to_login(self):
        self.register_widget.deleteLater()
        self.register_widget = None
        self.login_setup()
#______________________________________________________________________________________________________________________
    """ From login to forgot password """
    def login_to_forgot_password(self):
        self.login_widget.deleteLater()
        self.login_widget = None
        self.recover_password_setup()
#______________________________________________________________________________________________________________________
    """ From forgot password to login """
    def forgot_password_to_login(self):
        self.recover_password_widget.deleteLater()
        self.recover_password_widget = None
        self.login_setup()
#______________________________________________________________________________________________________________________
    """ From login to main """
    def login_to_main(self):
        self.login_widget.deleteLater()
        self.login_widget = None
        self.main_setup()
#______________________________________________________________________________________________________________________
    def main_to_login(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.login_setup()
#______________________________________________________________________________________________________________________
    """ From main to settings """
    def main_to_settings(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.settings_setup()
#______________________________________________________________________________________________________________________
    """ From settings to main """
    def settings_to_main(self):
        self.settings_widget.deleteLater()
        self.settings_widget = None
        self.main_setup()
#______________________________________________________________________________________________________________________
    """ From main to statistics """
    def main_to_statistics(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.statistics_setup()
#______________________________________________________________________________________________________________________
    """ From statistics to main """
    def statistics_to_main(self):
        self.statistics_widget.deleteLater() 
        self.statistics_widget = None
        self.main_setup()
#______________________________________________________________________________________________________________________
    """ From main to chart """
    def main_to_chart(self):
        self.main_widget.deleteLater()
        self.main_widget = None 
        self.chart_setup()
#______________________________________________________________________________________________________________________
    """ From chart to main """
    def chart_to_main(self):
        self.chart_widget.deleteLater()
        self.chart_widget = None 
        self.main_setup()
#______________________________________________________________________________________________________________________
""" Set font """
def set_font():
    font_id = QFontDatabase.addApplicationFont(str(pathlib.Path(__file__).resolve().parents[3])+'/TickerK8_app/APP_FILES/STYLE/FONTS/NotoSerif-VariableFont_wdth,wght.ttf')
    font_families = QFontDatabase.applicationFontFamilies(font_id) 
    return QFont(font_families[0])
#______________________________________________________________________________________________________________________
""" Start application """
if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setFont(set_font())
    controller = app_controller()
    controller.setHidden(False) 
    sys.exit(application.exec_())