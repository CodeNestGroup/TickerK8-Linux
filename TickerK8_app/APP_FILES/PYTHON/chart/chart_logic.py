""" Import """
import pathlib # For get path to folders
import json # For json files
from PyQt5.QtWidgets import QLabel, QSizePolicy, QApplication
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QPixmap, QPainter, QPen
#######################################################################################################################
""" Create chart """
def create_chart(self, value):
    """ Get data """
    chart_object = self.global_config['mid_object']
    chart_data = json.load(open(self.main_path+'/test_chart_data/AGX100/agx100_5min.json', 'r'))
#______________________________________________________________________________________________________________________
    """ Set chart """
    """ Create main chart label"""
    self.main_chart_label = QLabel(self)
    """ Set object name """
    self.main_chart_label.setObjectName('main_chart_label')
    """ Set main chart label to main layout """
    self.main_layout.addWidget(self.main_chart_label, 10, 0, 80, 100)
    """ Set alignemnt """
    self.main_chart_label.setAlignment(Qt.AlignCenter)
    """ Set size """
    self.main_chart_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Create chart img """
    self.main_chart_label.setScaledContents(True)
    self.main_chart_label.setPixmap(create_line_chart(chart_data, self.main_chart_label.size()))
    """ Set char title """
    self.top_title_label.setText('AGX100')

#######################################################################################################################
""" Create line chart """
def create_line_chart(d, s: QSize):
    """ Setup data """
    chart_data = d # Set data 
    size = s
    print(size)
    pixmap = QPixmap(size)
    pixmap.fill(Qt.black)
    return pixmap
















