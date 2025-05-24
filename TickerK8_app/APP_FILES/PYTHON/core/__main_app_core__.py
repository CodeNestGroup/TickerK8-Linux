""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import QRect
#______________________________________________________________________________________________________________________
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
""" Import statistics widget """
from statistics.statistics_structure import Statistics_widget
#######################################################################################################################
""" App controller """
class app_controller(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('window')
        self.layout = QVBoxLayout(self) # Create layout for responsiwe design
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout) # Set layout 
        
        self.login_widget = None # Set default
        self.register_widget = None # Set default
        self.recover_password_widget = None # Set default
        self.main_widget = None # Set default

        self.primary_screen_size = QApplication.primaryScreen().size() # Get screen size
        self.login_setup() # Set on start of application
#______________________________________________________________________________________________________________________
    """ Login """
    def login_setup(self):
        self.login_widget = Login_widget(self) # Creat login widget
        self.layout.addWidget(self.login_widget) # Add login widget to main layoyt
        self.set_size_login() # Set size of main window for login setup
        self.login_widget.login_login_button.clicked.connect(self.login_correct_controller) # Connect function 
        self.login_widget.login_register_button.clicked.connect(self.login_to_register) # Connect function
        self.login_widget.login_forgot_password_button.clicked.connect(self.login_to_forgot_password) # Conenct exit function
#______________________________________________________________________________________________________________________
    """ Set size login"""
    def set_size_login(self):
        x, y, width, height = int(self.primary_screen_size.width()//4), int(self.primary_screen_size.height()//12), int(self.primary_screen_size.width()//2), int(self.primary_screen_size.height()//1.25) # Set size
        self.setGeometry(QRect(x, y, width, height)) # Set geometry 
#______________________________________________________________________________________________________________________
    """ Login correct controller """
    def login_correct_controller(self):
        if self.login_correct():
            self.login_to_main()
        else:
            self.login_widget.login_login_lineedit.setStyleSheet("border: 2px solid red;")
            self.login_widget.login_password_lineedit.setStyleSheet("border: 2px solid red;")
#______________________________________________________________________________________________________________________
    """ Login correct """
    def login_correct(self):
        if self.login_widget.login_login_lineedit.text() == 'x' and self.login_widget.login_password_lineedit.text() == 'x':
            return True
        else:
            return False
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
        self.main_widget.bottom_left_stats_button.clicked.connect(self.main_to_statistics) # Connect open statistics widget
#______________________________________________________________________________________________________________________
    """ Set size main """
    def set_size_main(self):
        x, y, width, height = 0, 0, int(self.primary_screen_size.width()), int(self.primary_screen_size.height()) # Set size
        self.setGeometry(QRect(x, y, width, height)) # Set geometry
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
    """ From main to statistics """
    def main_to_statistics(self):
        self.main_widget.deleteLater() # Delete main widget
        self.main_widget = None # Set dafault
        self.statistics_setup() # Call statistics setup function
#______________________________________________________________________________________________________________________
    """ From statistics to main """
    def statistics_to_main(self):
        self.statistics_widget.deleteLater() # Delte statistics widget
        self.statistics_widget = None # Set dafault
        self.main_setup() # Call main setup function 
#######################################################################################################################
    