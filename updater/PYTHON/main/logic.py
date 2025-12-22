""" Import packages """
import json 
import sys
import subprocess
import urllib
""" Import PyQT5 packages """
from PyQt5.QtCore import (
    QUrl,
    QThread,
    pyqtSignal
)
from PyQt5.QtGui import (
    QDesktopServices
)
#______________________________________________________________________________________________________________________

def open_link(u):
    try:
        QDesktopServices.openUrl(u)
    except:
        pass
        # Sygnał do reportu

def open_main_app(self):
    try:
        subprocess.Popen(['/bin/bash', self.main_path+'/TickerK8.sh'])
        sys.exit(0)
    except:
        pass
        # Sygnał do reportu
#______________________________________________________________________________________________________________________

def main_no_connect(self):
    t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r'))
    l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    
    self.changelog_widget.no_connection()
    self.update_widget.info()
    self.instagram_button.setDisabled(True)
    self.github_button.setDisabled(True)
    self.discord_button.setDisabled(True)
    self.start_button.setDisabled(True)
    self.start_button.disconnect()
    self.start_button.setText(t['start_button'][0][l])

def main_connect(self):
    self.get_releases_thread = get_releases()
    self.get_releases_thread.finished.connect(self.changelog_widget.connection)
    self.get_releases_thread.finished.connect(self.update_widget.check_version)
    self.get_releases_thread.finished.connect(lambda: self.get_releases_thread.quit())
    self.get_releases_thread.finished.connect(lambda: self.get_releases_thread.wait())
    self.get_releases_thread.finished.connect(lambda: self.get_releases_thread.deleteLater())
    self.get_releases_thread.start()
    self.instagram_button.setDisabled(False)
    self.github_button.setDisabled(False)
    self.discord_button.setDisabled(False)
    self.start_button.setDisabled(True)
#______________________________________________________________________________________________________________________

class get_releases(QThread):
        finished = pyqtSignal(list)
        def __init__(self):
            super().__init__()
            self.start()

        def run(self):
            release = urllib.request.urlopen('https://api.github.com/repos/CodeNestGroup/TickerK8-Linux/releases')
            self.finished.emit(json.loads(release.read().decode()))
#______________________________________________________________________________________________________________________

def update_status_controller(self, b):
    t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r'))
    l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    if b:
        text = t['start_button'][2][l]
        self.start_button.clicked.connect(lambda: open_main_app(self))
    elif not b:
        text = t['start_button'][1][l]
        self.start_button.clicked.connect(self.update_widget.updating)
        self.start_button.clicked.connect(lambda: self.start_button.setDisabled(True))
    self.start_button.setText(text)
    self.start_button.setDisabled(False)
#______________________________________________________________________________________________________________________
