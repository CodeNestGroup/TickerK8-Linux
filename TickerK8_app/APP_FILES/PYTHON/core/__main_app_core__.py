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
        self.main_widget = None # Set default

        self.primary_screen_size = QApplication.primaryScreen().size() # Get screen size
        self.login_setup() # Set on start of application
#______________________________________________________________________________________________________________________
    """ Login """
    def login_setup(self):
        self.login_widget = Login_widget(self) # Creat login widget
        self.layout.addWidget(self.login_widget) # Add login widget to main layoyt
        self.set_size_login() # Set size of main window for login setup
        self.login_widget.login_register_button.clicked.connect(self.login_to_register) # Connect function
#______________________________________________________________________________________________________________________
    """ Set size login"""
    def set_size_login(self):
        x, y, width, height = int(self.primary_screen_size.width()//4), int(self.primary_screen_size.height()//12), int(self.primary_screen_size.width()//2), int(self.primary_screen_size.height()//1.25) # Set size
        self.setGeometry(QRect(x, y, width, height)) # Set geometry 
#______________________________________________________________________________________________________________________
    """ Register """
    def register_setup(self):
        self.register_widget = Register_widget(self) # Creat register widget
        self.layout.addWidget(self.register_widget) # Add register widget to main layout
        self.set_size_register() # Set size of main window for register setup
        self.register_widget.register_exit_button.clicked.connect(self.register_to_login) # Connect function
#______________________________________________________________________________________________________________________
    def set_size_register(self):
        x, y, width, height = int(self.primary_screen_size.width()//4), int(self.primary_screen_size.height()//12), int(self.primary_screen_size.width()//2), int(self.primary_screen_size.height()//1.25) # Set size
        self.setGeometry(QRect(x, y, width, height)) # Set geometry
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
        pass
#______________________________________________________________________________________________________________________
    """ From forgot password to login """
    def forgot_password_to_login(self):
        pass
#######################################################################################################################
    