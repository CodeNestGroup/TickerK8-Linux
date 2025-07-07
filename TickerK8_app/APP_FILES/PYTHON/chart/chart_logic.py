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
    QToolTip
)
from PyQt5.QtGui import QPainter, QBrush, QPen, QFont
from PyQt5.QtCore import QRectF, Qt, QPointF
#######################################################################################################################
""" Create chart """
def create_chart(self, value):
    """ Get data """
    chart_object = self.global_config['mid_object']
    chart_data = json.load(open(self.main_path+'/test_chart_data/AGX100/agx100_5min.json', 'r'))
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
    cursor = database.cursor() # Create cursor 
    object_data = cursor.execute(f'SELECT name FROM {chart_object[0]} WHERE id={chart_object[1]};').fetchall()[0] # Get data 
    cursor.close() # Close cursor connection  
    database.close() # Close database connection
#______________________________________________________________________________________________________________________
    """ Set chart """
    self.main_chart_graphics_view
#______________________________________________________________________________________________________________________
    """ Create main chart graphics view """
    self.main_chart_graphics_scene.addItem(MyRectItem())
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
""" Candy chart """
class Candy_chart(QGraphicsScene):
    def __init__(self, o, h, c, l):
        pass
#######################################################################################################################
class Candy(QGraphicsItem):
    def boundingRect(self):
        return QRectF(0, 0, 100, 100)

    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(Qt.blue))
        painter.drawRect(0, 0, 100, 100)

#######################################################################################################################