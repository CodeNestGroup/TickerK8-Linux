import pathlib # For get path to folders
import json # For json files
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
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        self.chart_data = json.load(open(self.main_path+'/CHART_DATA/AGX100_15.json', 'r')) # Get chart data 
#______________________________________________________________________________________________________________________
        self.main_scence = QGraphicsScene(self)
        



#######################################################################################################################

