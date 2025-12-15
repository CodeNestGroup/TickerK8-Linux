""" Import packages """
import json 
import sys
import subprocess
""" Import PyQT5 packages """
from PyQt5.QtCore import (
    QUrl
)
from PyQt5.QtGui import (
    QDesktopServices
)
#______________________________________________________________________________________________________________________

""" Open discord """
def open_discord():
    url = QUrl("https://discord.gg/twZ3SNcC")
    try:
        QDesktopServices.openUrl(url)
        # Notification 
    except:
        print('does not open discord ')
        # Notification 
#______________________________________________________________________________________________________________________

""" Open instagram """
def open_instagram():
    url = QUrl("https://www.instagram.com/codenestgroup/")
    try:
        QDesktopServices.openUrl(url)
        # Notification 
    except:
        print('does not open ig ')
        # Notification 
#______________________________________________________________________________________________________________________

""" Open github """
def open_github():
    url = QUrl("https://github.com/CodeNestGroup")
    try:
        QDesktopServices.openUrl(url)
        # Notification 
    except:
        print('does not open github ')
        # Notification 
#______________________________________________________________________________________________________________________

""" Open main app """
def open_main_app(self):
    subprocess.Popen(['/bin/bash', self.main_path+'/TickerK8.sh'])
    sys.exit(0)
#______________________________________________________________________________________________________________________
