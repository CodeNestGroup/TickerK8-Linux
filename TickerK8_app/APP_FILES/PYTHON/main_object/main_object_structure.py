""" Import packages """
""" Import system and operating system packages """
import pathlib # For get path to folders.
import json # For json files.
#______________________________________________________________________________________________________________________
""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QScrollArea, # Simple scroll widget.
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
        Qt # Qt.
        ) 
#______________________________________________________________________________________________________________________
""" Import main object modules """
""" Import main object ui """
from .main_object_ui import *
#______________________________________________________________________________________________________________________
""" Import main object logic """
from .main_object_logic import *
#######################################################################################################################
""" Main object widget """
class Main_object_scroll(QScrollArea):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background.
        self.setParent(parent) # Set parent.
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data.
        self.translate = json.load(open(self.main_path+'/CONFIG/main_object/translate.json', 'r')) # Get translate.
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_widget = None
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_object_ui(self)
        main_object_reload_style(self)
        setup_widget(self)
        self.setup_widget = lambda: setup_widget(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """
#######################################################################################################################
