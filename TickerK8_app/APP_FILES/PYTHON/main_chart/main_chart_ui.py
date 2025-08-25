import pathlib # For get path to folders
import json # For json files
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem,
    QSizePolicy
)
from PyQt5.QtCore import Qt
#______________________________________________________________________________________________________________________
#######################################################################################################################
""" Main chart ui """
def main_chart_ui(self):
    """ Set object name """
    self.setObjectName('main_chart_graphic')
    self.main_scence.setObjectName('main_scence')
#______________________________________________________________________________________________________________________
    """ Set property """
#______________________________________________________________________________________________________________________
    """ Set layout """
#______________________________________________________________________________________________________________________
    """ Set widget """
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.setScene(self.main_scence)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_scence.setSceneRect(0, 0, self.width(), self.height())
#######################################################################################################################
""" Main chart style """
def main_chart_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main_chart/'+self.global_config['__theme__']+'.css')).read())
