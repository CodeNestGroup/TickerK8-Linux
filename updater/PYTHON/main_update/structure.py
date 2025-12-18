""" Import packages """
import pathlib 
import json
from datetime import datetime
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QProgressBar,
    QLabel,
    QGridLayout
)
from PyQt5.QtCore import (
    pyqtSignal
)
""" Import main modules """
from .ui import *
from .logic import *
#______________________________________________________________________________________________________________________

class Update_widget(QWidget):
    update_status = pyqtSignal(bool)
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        """ Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        """ Create objects """
        self.layout = QGridLayout(self)
        self.label = None
        self.dots_label = None
        self.progressbar = None
        self.timer = None
        self.text = None
        self.language = None
        """ Call functions """
        update_ui(self)
        update_reload_style(self)
        self.updated()
        """ Connect functions """
    
    def reset(self):
        if self.label:
            self.label.deleteLater()
            self.label = None
        if self.dots_label:
            self.dots_label.deleteLater()
            self.dots_label = None
        if self.progressbar:
            self.progressbar.deleteLater()
            self.progressbar = None
        if self.timer:
            self.timer.stop()
            self.timer.deleteLater()
            self.timer = None 
        if self.text:
            self.text = None
        if self.language:
            self.language = None
    
    def updated(self):
        self.reset()
        """ Create objects """
        self.label = QLabel(self)
        self.dots_label = QLabel(self)
        """ Call functions """
        updated_ui(self)
        updated_retranslate(self)
        """ Connect functions """
        loading_thread(self)

    def updating(self):
        self.reset()
        """ Create objects """
        self.progressbar = QProgressBar(self)
        self.label = QLabel(self.progressbar)
        self.dots_label = QLabel(self.progressbar)
        """ Call functions """
        updating_ui(self)
        updating_retranslate(self)
        """ Connect functions """
        loading_thread(self)
        load_text(self)
        self.controller_download = controller_download()
        self.controller_download.progress.connect(self.progress_label_handel)
        self.controller_download.progress_bar_value.connect(self.progressbar.setValue)
        self.controller_download.start()
#______________________________________________________________________________________________________________________

    def check_version(self, release_data):
        g_v = release_data[0]['published_at']
        l_v = json.load(open(self.main_path+'/CONFIG/GLOBAL/changelog.json', 'r'))['published_at']
        t = json.load(open(self.main_path+'/CONFIG/main_update/updated_translate.json', 'r'))
        l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
        g_t = datetime.fromisoformat(g_v.replace("Z", "+00:00"))
        l_t = datetime.fromisoformat(l_v.replace("Z", "+00:00"))
        if g_t == l_t:
            self.label.setText(t['label'][2][l])
            self.update_status.emit(True)
        elif g_t > l_t:
            self.label.setText(t['label'][1][l])
            self.update_status.emit(False)
        if self.dots_label:
            self.dots_label.deleteLater()
            self.dots_label = None
        if self.timer:
            self.timer.stop()
            self.timer.deleteLater()
            self.timer = None
#______________________________________________________________________________________________________________________

    def progress_label_handel(self, v):
        t = self.text
        l = self.language
        self.label.setText(t['label'][v][l])
        if v == 6:
            self.timer.stop()
            self.dots_label.setHidden(True)
#______________________________________________________________________________________________________________________