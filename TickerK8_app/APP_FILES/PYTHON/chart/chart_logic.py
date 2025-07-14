""" Import """
import pathlib # For get path to folders
import json # For json files
import sqlite3 # For database data 
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem,
    QMainWindow,
    QToolTip,
    QSizePolicy
)
from PyQt5.QtGui import QPainter, QBrush, QPen, QFont
from PyQt5.QtCore import QRectF, Qt, QPointF
#______________________________________________________________________________________________________________________
""" Charts types import """
from .candle_chart import Candle_chart
#######################################################################################################################
""" Create chart """
def create_chart(self, value):
    """ Get data """
    chart_object = self.global_config['mid_object']
    chart_type = self.global_config['chart_type']
    chart_data = json.load(open(self.main_path+'/test_chart_data/AGX100/agx100_5min.json', 'r'))
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
    cursor = database.cursor() # Create cursor 
    object_data = cursor.execute(f'SELECT name FROM {chart_object[0]} WHERE id={chart_object[1]};').fetchall()[0] # Get data 
    cursor.close() # Close cursor connection  
    database.close() # Close database connection
#______________________________________________________________________________________________________________________
    """ Set chart """
    if self.main_chart_graphics_view:
        self.main_chart_graphics_view.deleteLater()
        self.main_chart_graphics_view = None 
    if chart_type == 0:
        self.main_chart_graphics_view = Candle_chart(chart_data, self)
        self.main_chart_graphics_view.setObjectName('main_chart_graphics_view')
    self.main_layout.addWidget(self.main_chart_graphics_view, 10, 0, 80, 100)
#______________________________________________________________________________________________________________________
    """ Create main chart graphics view """
#______________________________________________________________________________________________________________________
    """ Set object name """
#______________________________________________________________________________________________________________________
    """ Set main chart graphics view to main layout """
#______________________________________________________________________________________________________________________
    """ Set alignemnt """
#______________________________________________________________________________________________________________________
    """ Set size """
#______________________________________________________________________________________________________________________
    """ Set char title """
    self.top_title_label.setText(f'{object_data[0]}')
#######################################################################################################################