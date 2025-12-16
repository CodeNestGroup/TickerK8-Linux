""" Import packages """
import json 
import sys
import subprocess
import urllib.request
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

def open_discord():
    url = QUrl("https://discord.gg/twZ3SNcC")
    try:
        QDesktopServices.openUrl(url)
        # Notification 
    except:
        print('does not open discord ')
        # Notification 

def open_instagram():
    url = QUrl("https://www.instagram.com/codenestgroup/")
    try:
        QDesktopServices.openUrl(url)
        # Notification 
    except:
        print('does not open ig ')
        # Notification 

def open_github():
    url = QUrl("https://github.com/CodeNestGroup")
    try:
        QDesktopServices.openUrl(url)
        # Notification 
    except:
        print('does not open github ')
        # Notification 

def open_main_app(self):
    subprocess.Popen(['/bin/bash', self.main_path+'/TickerK8.sh'])
    sys.exit(0)
#______________________________________________________________________________________________________________________

def main_no_connect(self):
    self.changelog_widget.no_connection()
    self.instagram_button.setDisabled(True)
    self.github_button.setDisabled(True)
    self.discord_button.setDisabled(True)
    self.start_button.setDisabled(True)

def main_connect(self):
    self.get_releases_thread = get_releases()
    self.get_releases_thread.finished.connect(self.changelog_widget.connection)
    self.get_releases_thread.finished.connect(lambda: self.get_releases_thread.quit())
    self.get_releases_thread.finished.connect(lambda: self.get_releases_thread.wait())
    self.get_releases_thread.finished.connect(lambda: self.get_releases_thread.deleteLater())
    self.get_releases_thread.start()
    self.instagram_button.setDisabled(False)
    self.github_button.setDisabled(False)
    self.discord_button.setDisabled(False)
    self.start_button.setDisabled(False)
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
