import pathlib # For get path to folders
import json # For json files
import sqlite3
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem
)
from PyQt5.QtCore import Qt
#______________________________________________________________________________________________________________________
""" Import main chart ui """
from .main_chart_ui import *
#______________________________________________________________________________________________________________________
""" Import main chart logic """
from .main_chart_logic import *
#######################################################################################################################
""" Main mid object widget """
class Main_chart(QGraphicsView):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent, data):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.chart_data = data
#______________________________________________________________________________________________________________________
        self.main_scence = QGraphicsScene(self)
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_chart_ui(self)
        main_chart_reload_style(self)
        candle_chart(self)
#######################################################################################################################
