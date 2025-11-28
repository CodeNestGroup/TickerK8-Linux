""" Import packages """
import pathlib 
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QScrollArea,
    QGridLayout
)
from PyQt5.QtCore import (
    QPropertyAnimation
)
""" Import main modules """
from .ui import *
from .logic import *
""" Import button modules """
from shadowbutton.structure import QPushButton_sound
#______________________________________________________________________________________________________________________

class Notification_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        """" Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        self.message_index = 0
        """ Create objects """
        self.background_layout = QGridLayout(self)
        self.widget = QWidget(self)
        self.layout = QGridLayout(self.widget)
        self.text_label = QLabel(self.widget)
        self.exit_button = QPushButton_sound(self.widget)
        self.anim = QPropertyAnimation(self, b'pos')
        """ Call functions """
        notification_ui(self)
        notification_reload_style(self)
        notification_retranslate(self)
        """ Connect functions """
#______________________________________________________________________________________________________________________
