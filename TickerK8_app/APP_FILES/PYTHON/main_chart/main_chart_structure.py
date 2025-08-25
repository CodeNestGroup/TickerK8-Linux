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
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data
        query_set = self.global_config['mid_object']
        if query_set[0] == 'market_index':
                query = f'SELECT name FROM market_index WHERE id={query_set[1]};'
        elif query_set[0] == 'stock':
                query = f'SELECT ticker FROM stock WHERE id={query_set[1]};'
        database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
        cursor = database.cursor() # Create cursor 
        data_name = cursor.execute(query).fetchall()[0][0]
        cursor.close()
        database.close()
        self.chart_data = json.load(open(self.main_path+f'/CHART_DATA/{data_name}_15.json', 'r')) # Get chart data 
#______________________________________________________________________________________________________________________
        self.main_scence = QGraphicsScene(self)
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_chart_ui(self)
        main_chart_reload_style(self)
        candle_chart(self)
#######################################################################################################################
