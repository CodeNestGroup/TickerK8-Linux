""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QScrollArea, # Simple scroll widget
    QLabel, # Simple label
    QPushButton, # Simple button
    QComboBox, # Drop down list
    QGridLayout, # Grid layout
    QVBoxLayout # Vertical layout 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 QtCore """
from PyQt5.QtCore import Qt
#######################################################################################################################
""" Create list"""
def create_list(self):
    if self.global_config['__object_list__'] == 'fav':
        main_mid_object_list_favourite()
    elif self.global_config['__object_list__'] == 'hot':
        main_mid_object_list_hot()
#######################################################################################################################
""" Main mid object list favourite """
def main_mid_object_list_favourite(self):
    """ Set variables """
    object_list = list(self.global_config['__favourite_objects__']) # Create object list
#______________________________________________________________________________________________________________________
    """ Check if list widget exists"""
    if self.list_widget:
        self.list_widget.deleteLater()
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.list_widget = QWidget(self.list_scroll)
    self.list_layout = QGridLayout(self.list_widget)
    self.list_tag_index_label
    self.list_tag_logo_label
    self.list_tag_name_label 
#______________________________________________________________________________________________________________________
    """ Set object name"""
    self.list_widget.setObjectName('list_widget')
#______________________________________________________________________________________________________________________
    """ Set Layout """
    self.list_layout.setSpacing(0)
    self.list_layout.setContentsMargins(0,0,0,0)
    self.list_widget.setLayout(self.list_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.list_scroll.setWidget(self.list_widget)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)



#######################################################################################################################
""" Main mid object list hot """
def main_mid_object_list_hot(self):
    pass
#######################################################################################################################