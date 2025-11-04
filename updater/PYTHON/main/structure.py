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
        self.update_progressbar = QProgressBar(self)
        self.update_label = QLabel(self)
        self.logo_c_n_g_label = QLabel(self)
        self.logo_ticker_label = QLabel(self)
        self.settings_button = ShadowButton(self, self)
        self.instagram_button = ShadowButton(self, self)
        self.github_button = ShadowButton(self, self)
        self.discord_button = ShadowButton(self, self)
        self.start_button = ShadowButton(self, self)
        """ Call functions """
        main_ui(self)
        main_reload_style(self)
        main_retranslate(self)
        """ Connect functions """
        self.settings_button.clicked.connect(lambda: )
        self.instagram_button.clicked.connect(lambda: )
        self.github_button.clicked.connect(lambda: )
        self.discord_button.clicked.connect(lambda: )
        self.start_button.clicked.connect(lambda: )

#______________________________________________________________________________________________________________________

