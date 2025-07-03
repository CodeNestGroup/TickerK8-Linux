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
    """ Set chart title """
    self.top_title_label.setText('AGX100')
#______________________________________________________________________________________________________________________
    """ Set chart """
    """ Create main chart graphics view """
    """ Set object name """
    """ Set main chart graphics view to main layout """
    """ Set alignemnt """
    """ Set size """
    """ Set char title """
    self.top_title_label.setText('AGX100')
#######################################################################################################################
