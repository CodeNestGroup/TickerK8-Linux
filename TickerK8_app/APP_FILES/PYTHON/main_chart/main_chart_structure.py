""" Import packages """
import pathlib
import json
import sqlite3
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem
)
from PyQt5.QtCore import Qt
""" Import main chart modules """
from .main_chart_ui import *
from .main_chart_logic import *
#______________________________________________________________________________________________________________________
""" Main mid object widget """
class Main_chart(QGraphicsView):
    def __init__(self, parent, data):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        self.chart_data = data
#______________________________________________________________________________________________________________________
        self.main_scence = QGraphicsScene(self)
#______________________________________________________________________________________________________________________
        """ Call functions """
        main_chart_ui(self)
        main_chart_reload_style(self)
        candle_chart(self)
#______________________________________________________________________________________________________________________
