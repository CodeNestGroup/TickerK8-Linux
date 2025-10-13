""" Import packages """
""" Import system and operating system packages """
import sys # Sys package, access to system func.
import pathlib # Pathlib package, for get path to application.
#_______________________________________________________________________________________________________________________
""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QApplication, # Application, define application.
    QWidget, # Widget, simple widget.
    QVBoxLayout, # Vertical Layout.
    QDesktopWidget,
    QMainWindow
    )
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    QRect
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QFontDatabase, # Font database for add new font to app.
    QFont # Font for add new font to app.
    )
#______________________________________________________________________________________________________________________
""" Import application modules """
""" Import login widget """
from login.login_structure import Login_widget
#______________________________________________________________________________________________________________________
""" Import register widget """
from register.register_structre import Register_widget
#______________________________________________________________________________________________________________________
""" Import recover password widget """
from recover_password.recover_password_structure import Recover_password_widget
#______________________________________________________________________________________________________________________
""" Import main widget """
from main.main_structure import Main_widget 
#______________________________________________________________________________________________________________________
""" Import settings widget """
from settings.settings_structure import Settings_widget
#______________________________________________________________________________________________________________________
""" Import statistics widget """
from statistics.statistics_structure import Statistics_widget
#______________________________________________________________________________________________________________________
""" Import chart widget """
from chart.chart_structure import Chart_widget
#######################################################################################################################
""" App controller """
class app_controller(QWidget):
    """ Init """
    def __init__(self):
        super().__init__()
        self.setObjectName('window')
        self.layout = QVBoxLayout(self) # Create layout for responsiwe design.
        self.layout.setSpacing(0) # Set spacing.
        self.layout.setContentsMargins(0,0,0,0) # Set contents marigns.
        self.setLayout(self.layout) # Set layout.
        self.login_widget = None # Set default.
        self.register_widget = None # Set default.
        self.recover_password_widget = None # Set default.
        self.main_widget = None # Set default.
        self.settings_widget = None # Set default.
        self.statistics_widget = None # Set default.
        self.chart_widget = None # Set default.
        self.primary_screen_size = QApplication.primaryScreen().size() # Get screen size.
        self.login_setup() # Set on start of application.
#______________________________________________________________________________________________________________________
    """ Login """
    """ Login setup """
    def login_setup(self):
        self.login_widget = Login_widget(self) # Creat login widget.
        self.layout.addWidget(self.login_widget) # Add login widget to main layoyt.
        self.set_size_login() # Set size of main window for login setup.
        self.login_widget.correct_login.connect(self.login_to_main) # Call function when correct login.
        self.login_widget.login_register_button.clicked.connect(self.login_to_register) # Connect function.
#______________________________________________________________________________________________________________________
    """ Set size login"""
    def set_size_login(self):
        x, y, width, height = int(self.primary_screen_size.width()//4), int(self.primary_screen_size.height()//12), int(self.primary_screen_size.width()//2), int(self.primary_screen_size.height()//1.25) # Set size.
        self.setGeometry(QRect(x, y, width, height)) # Set geometry.
#______________________________________________________________________________________________________________________
    """ Register """
    def register_setup(self):
        self.register_widget = Register_widget(self) # Creat register widget
        self.layout.addWidget(self.register_widget) # Add register widget to main layout
        self.set_size_register() # Set size of main window for register setup
        self.register_widget.register_exit_button.clicked.connect(self.register_to_login) # Connect exit function
#______________________________________________________________________________________________________________________
    """ Set size register """
    def set_size_register(self):
        x, y, width, height = int(self.primary_screen_size.width()//4), int(self.primary_screen_size.height()//12), int(self.primary_screen_size.width()//2), int(self.primary_screen_size.height()//1.25) # Set size
        self.setGeometry(QRect(x, y, width, height)) # Set geometry
#______________________________________________________________________________________________________________________
    """ Recover password """
    def recover_password_setup(self):
        self.recover_password_widget = Recover_password_widget(self) # Creat recover password widget
        self.layout.addWidget(self.recover_password_widget) # Add recover password widget to main layout
        self.set_size_recover_password() # Set size of main window for recover password widget 
        self.recover_password_widget.recover_password_exit_button.clicked.connect(self.forgot_password_to_login) # Connect exit function 
#______________________________________________________________________________________________________________________
    """ Set size recover password """
    def set_size_recover_password(self):
        x, y, width, height = int(self.primary_screen_size.width()//4), int(self.primary_screen_size.height()//12), int(self.primary_screen_size.width()//2), int(self.primary_screen_size.height()//1.25) # Set size
        self.setGeometry(QRect(x, y, width, height)) # Set geometry
#______________________________________________________________________________________________________________________
    """ Main """
    def main_setup(self):
        self.main_widget = Main_widget(self) # Creat main widget
        self.layout.addWidget(self.main_widget) # Add main widget to main layout 
        self.set_size_main() # Set size if main window fir main widget
        self.main_widget.settings_button.clicked.connect(self.main_to_settings)
#______________________________________________________________________________________________________________________
    """ Set size main """
    def set_size_main(self):
        screen = self.windowHandle().screen()
        geometry = screen.availableGeometry()
        #self.setGeometry(geometry)
        self.showMaximized()
#______________________________________________________________________________________________________________________
    """ Settings """
    def settings_setup(self):
        self.settings_widget = Settings_widget(self) # Create settings widget
        self.layout.addWidget(self.settings_widget) # Add settings widget to main layout
        self.set_size_settings() # Set size
        self.settings_widget.navi_exit_button.clicked.connect(self.settings_to_main) # Connect exit function 
#______________________________________________________________________________________________________________________
    """ Set size settings """
    def set_size_settings(self):
        screen = self.windowHandle().screen()
        geometry = screen.availableGeometry()
        #self.setGeometry(geometry)
        self.showMaximized()
#______________________________________________________________________________________________________________________
    """ Statistics """
    def statistics_setup(self):
        self.statistics_widget = Statistics_widget(self) # Create statistics widget
        self.layout.addWidget(self.statistics_widget) # Add statistics widget to main layout
        self.set_size_statistics() # Set size 
        self.statistics_widget.main_exit_button.clicked.connect(self.statistics_to_main) # Connect exit function
#______________________________________________________________________________________________________________________
    """ Set size statistics """
    def set_size_statistics(self):
        x, y, width, height = 0, 0, int(self.primary_screen_size.width()), int(self.primary_screen_size.height()) # Set size
        self.setGeometry(QRect(x, y, width, height)) # Set geometry
#______________________________________________________________________________________________________________________
    """ Chart """
    def chart_setup(self):
        self.chart_widget = Chart_widget(self) # Create chart widget
        self.layout.addWidget(self.chart_widget) # Add chart widget to main layout 
        self.set_size_chart() # Set size 
        self.chart_widget.top_exit_button.clicked.connect(self.chart_to_main) # Connect exit function
#______________________________________________________________________________________________________________________
    """ Set size chart """
    def set_size_chart(self):
        x, y, width, height = 0, 0, int(self.primary_screen_size.width()), int(self.primary_screen_size.height()) # Set size
        self.setGeometry(QRect(x, y, width, height)) # Set geometry
#______________________________________________________________________________________________________________________
    """ From login to register """
    def login_to_register(self):
        self.login_widget.deleteLater() # Delete login widget 
        self.login_widget = None  # Set default
        self.register_setup() # Call register setup function 
#______________________________________________________________________________________________________________________
    """ From register to login """
    def register_to_login(self):
        self.register_widget.deleteLater() # Delete register widget
        self.register_widget = None # Set default 
        self.login_setup() # Call login setup function 
#______________________________________________________________________________________________________________________
    """ From login to forgot password """
    def login_to_forgot_password(self):
        self.login_widget.deleteLater() # Delete login widget
        self.login_widget = None # Set default 
        self.recover_password_setup() # Call recover password setup function 
#______________________________________________________________________________________________________________________
    """ From forgot password to login """
    def forgot_password_to_login(self):
        self.recover_password_widget.deleteLater() # Delete login widget
        self.recover_password_widget = None # Set default 
        self.login_setup() # Call recover password setup function 
#______________________________________________________________________________________________________________________
    """ From login to main """
    def login_to_main(self):
        self.login_widget.deleteLater() # Delete login widget
        self.login_widget = None # Set default  
        self.main_setup() # Call main setup function
#______________________________________________________________________________________________________________________
    """ From main to settings """
    def main_to_settings(self):
        self.main_widget.deleteLater() # Delete main widget
        self.main_widget = None # Set dafault 
        self.settings_setup() # Call settings_setup function
#______________________________________________________________________________________________________________________
    """ From settings to main """
    def settings_to_main(self):
        self.settings_widget.deleteLater() # Delete settings widget
        self.settings_widget = None # Set dafault 
        self.main_setup() # Call main setup function
#______________________________________________________________________________________________________________________
    """ From main to statistics """
    def main_to_statistics(self):
        self.main_widget.deleteLater() # Delete main widget
        self.main_widget = None # Set dafault
        self.statistics_setup() # Call statistics setup function
#______________________________________________________________________________________________________________________
    """ From statistics to main """
    def statistics_to_main(self):
        self.statistics_widget.deleteLater() # Delete statistics widget
        self.statistics_widget = None # Set dafault
        self.main_setup() # Call main setup function 
#______________________________________________________________________________________________________________________
    """ From main to chart """
    def main_to_chart(self):
        self.main_widget.deleteLater() # Delete main widget
        self.main_widget = None # Set dafault
        self.chart_setup() # Call chart setup fucntion 
#______________________________________________________________________________________________________________________
    """ From chart to main """
    def chart_to_main(self):
        self.chart_widget.deleteLater() # Delete chart widget 
        self.chart_widget = None # Set dafault
        self.main_setup() # Call main setup function 
#######################################################################################################################
""" Set font """
def set_font():
    font_id = QFontDatabase.addApplicationFont(str(pathlib.Path(__file__).resolve().parents[3])+'/TickerK8_app/APP_FILES/STYLE/FONTS/NotoSerif-VariableFont_wdth,wght.ttf') # Get font.
    font_families = QFontDatabase.applicationFontFamilies(font_id) # Set font family.
    return QFont(font_families[0]) # Return new font.
#######################################################################################################################
""" Start application """
if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setFont(set_font())
    controller = app_controller()
    controller.setHidden(False) 
    sys.exit(application.exec_())