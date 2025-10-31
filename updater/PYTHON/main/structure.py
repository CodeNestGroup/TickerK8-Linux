""" Import packages """
import pathlib 
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QGridLayout
)
from PyQt5.QtCore import (
    Qt,
    QTimer
)
""" Import main modules """
from .ui import *
from .logic import *
""" Import application modules """
#______________________________________________________________________________________________________________________

class Main_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        """" Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        self.main_conf = json.load(open(self.main_path+'/CONFIG/main/background_conf.json', 'r'))
        """ Create objects """
        self.layout = QGridLayout(self)
        self.changelog_scroll = QScrollArea(self)
        self.logo_c_n_g_label = QLabel(self)
        self.logo_ticker_label = QLabel(self)
        self.settings_open_button
        self.settings_instagram_button
        self.settings_github_button
        self.settings_discord_button
        """ Call functions """

        """ Connect functions """

#______________________________________________________________________________________________________________________

