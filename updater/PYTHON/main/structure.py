""" Import packages """
import pathlib 
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QScrollArea,
    QGridLayout
)
""" Import main modules """
from .ui import *
from .logic import *
""" Import button modules """
from shadowbutton.structure import QPushButton_shadow
#______________________________________________________________________________________________________________________

class Main_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        """" Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        """ Create objects """
        self.layout = QGridLayout(self)
        # Custo widget który przyjmuje tylko instrukcje co ma robic
        # Dorobić ping, który sprawdza połączenie 
        #self.changelog_error_widget = Changelog_error_widget(self)
        #self.changelog_scroll = QScrollArea(self)
        #self.update_progressbar = QProgressBar(self)
        self.update_label = QLabel(self)
        self.logo_c_n_g_label = QLabel(self)
        self.logo_ticker_label = QLabel(self)
        self.settings_button = QPushButton_shadow(self)
        self.instagram_button = QPushButton_shadow(self)
        self.github_button = QPushButton_shadow(self)
        self.discord_button = QPushButton_shadow(self)
        self.start_button = QPushButton_shadow(self)
        """ Call functions """
        main_ui(self)
        main_reload_style(self)
        main_retranslate(self)
        """ Connect functions """
        self.instagram_button.clicked.connect(open_instagram)
        self.github_button.clicked.connect(open_github)
        self.discord_button.clicked.connect(open_discord)
        self.start_button.clicked.connect(lambda: open_main_app(self))
#______________________________________________________________________________________________________________________

