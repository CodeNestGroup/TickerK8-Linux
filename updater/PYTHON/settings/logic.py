""" Import packages"""
import json 
""" sub menu open """
def sub_menu_open(self, open_func):
    if self.sub_menu_scroll:
        self.sub_menu_scroll.deleteLater()
    """ Create objects """
    self.sub_menu_scroll = QScrollArea(self)
    self.sub_menu_widget = QWidget(self.sub_menu_scroll)
    self.sub_menu_layout = QGridLayout(self.sub_menu_widget)
    self.title_label = QLabel(self.sub_menu_widget)
    """ Call functions """
    sub_menu_ui(self)
    open_func()
#______________________________________________________________________________________________________________________

""" change language """
def change_language(self):
    _
