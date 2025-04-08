""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import QRect
#______________________________________________________________________________________________________________________
""" Import login widget """
from login.login_structure import Login_widget
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
        self.login_widget = Login_widget(self) # Creat logim widget
        self.layout.addWidget(self.login_widget) # Add login widget to main layoyt
        self.set_size_login() # Set size of main window for login setup
#______________________________________________________________________________________________________________________
    """ Set size login"""
    def set_size_login(self):
        x, y, width, height = int(self.primary_screen_size.width()//3), int(self.primary_screen_size.height()//4), int(self.primary_screen_size.width()//3), int(self.primary_screen_size.height()//2) # Set size
        self.setGeometry(QRect(x, y, width, height)) # Set geometry 
#######################################################################################################################
    