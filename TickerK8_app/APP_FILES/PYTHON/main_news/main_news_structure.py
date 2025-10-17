""" Import packages """
import pathlib 
import json
#______________________________________________________________________________________________________________________
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton, 
    QComboBox,
    QGridLayout, 
    QVBoxLayout
)
from PyQt5.QtCore import (
        Qt
)
#______________________________________________________________________________________________________________________
""" Import main news packages """
from .main_news_ui import *
from .main_news_logic import *
#______________________________________________________________________________________________________________________
""" Main news widget """
class Main_news_widget(QWidget):
    def __init__(self, parent, id_news):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        self.parent = parent
        self.id_news = id_news
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.panel_widget = QWidget(self)
        self.panel_layout = QGridLayout(self.panel_widget)
        self.news_scroll = QScrollArea(self.panel_widget)
        self.panel_exit_button = QPushButton(self.panel_widget)
        """ Call functions"""
        main_news_ui(self)
        main_news_reload_style(self)
        main_news_retranslate(self)
        news_widget(self, self.id_news)
        """ Connect functions """
        self.panel_exit_button.clicked.connect(lambda: self.deleteLater())
#______________________________________________________________________________________________________________________
