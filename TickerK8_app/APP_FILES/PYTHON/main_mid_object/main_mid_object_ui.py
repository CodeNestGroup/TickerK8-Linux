""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QPushButton, # Simple button
    QGridLayout, # Grid layout
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt # Qt settings
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon # Icon
)
#######################################################################################################################
""" Main mid object Ui """
def main_mid_object_ui(self):
    """ Set object name """
    self.setObjectName('main_mid_object')
    self.object_widget.setObjectName('object_widget')
    self.next_left.setObjectName('next_left')
    self.next_right.setObjectName('next_right')
#_______________________________________________________________________________________________________________________

