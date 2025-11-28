""" Import packages """
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QPushButton
)
""" Import shadow button modules """
from .ui import *
from .logic import *
#______________________________________________________________________________________________________________________

class QPushButton_sound(QPushButton):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.clicked.connect(self.click_sound) 

    def enterEvent(self, event):
        self.enter_sound() 
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.leave_sound()
        super().leaveEvent(event) 

    def enter_sound(self):
        if self.check_config():
            print('enter')

    def leave_sound(self):
        if self.check_config(): 
            print('leave') 

    def click_sound(self):
        if self.check_config():
            print('click')

    def check_config(self):
        return json.load(open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'r'))['__sound_button__']
#______________________________________________________________________________________________________________________
