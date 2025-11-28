""" Import packages """
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QPushButton
)
""" Import shadow button modules """
from .ui import *
from .logic import *

#______________________________________________________________________________________________________________________

class QPushButton_shadow(QPushButton):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setPalette
        self.initShadow()
        self.initAnimation()
        self.clicked.connect(self.click_sound)
   
    def initShadow(self):
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 240))
        self.setGraphicsEffect(self.shadow)
    
    def initAnimation(self):
        self.anim = QPropertyAnimation(self, b"shadowColor")
        self.anim.setDuration(400)
#_______________________________________________________________________________________________________________________
    
    @pyqtProperty(QColor)
    def shadowColor(self):
        return self.shadow.color()
   
    @shadowColor.setter
    def shadowColor(self, color):
        self.shadow.setColor(color)
#_______________________________________________________________________________________________________________________
    
    def enterEvent(self, event):
        self.enter_sound()
        self.anim.stop()
        self.anim.setStartValue(self.shadow.color())
        self.anim.setEndValue(QColor(0, 0, 0, 130))
        self.anim.start()
        self.shadow.setBlurRadius(50)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.leave_sound()
        self.anim.stop()
        self.anim.setStartValue(self.shadow.color())
        self.anim.setEndValue(QColor(0, 0, 0, 240))
        self.anim.start()
        self.shadow.setBlurRadius(10)
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
        return json.load(open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'r'))['__sound_button__'] # Returning config
#______________________________________________________________________________________________________________________
