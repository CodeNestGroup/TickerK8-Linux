""" Import packages """
import json
import sys
import pathlib
import urllib.request
import socket
import time
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QDesktopWidget,
    QMainWindow
    )
from PyQt5.QtCore import (
    QRect,
    QThread,
    pyqtSignal
    )
from PyQt5.QtGui import (
    QFontDatabase,
    QFont
    )
""" Import application modules """
from main.structure import Main_widget
from settings.structure import Settings_widget
from changelog.structure import Changelog_widget
from report.structure import Report_widget
#______________________________________________________________________________________________________________________

class app_controller(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('window')
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        self.main_widget = None
        self.settings_widget = None
        self.changelog_widget = None
        self.report_widget = None 
        self.screen = QApplication.primaryScreen()
        self.geometry = self.screen.availableGeometry()
        self.ping_thread = self.controller_ping()
        self.ping_thread.start()
        self.main_setup()
#______________________________________________________________________________________________________________________

    def main_setup(self):
        self.main_widget = Main_widget(self)
        self.layout.addWidget(self.main_widget)
        pos_x = int(self.geometry.width()//4)
        pos_y = int(self.geometry.height()//4)
        width = int(self.geometry.width()//2)
        height = int(self.geometry.height()//2)
        self.setGeometry(QRect(pos_x, pos_y, width, height))
        self.ping_thread.signal.connect(self.main_widget.main_connect_controller)
        self.main_widget.changelog_widget.open.connect(self.main_to_changelog)
        self.main_widget.settings_button.clicked.connect(self.main_to_settings)

    def settings_setup(self):
        self.settings_widget = Settings_widget(self)
        self.layout.addWidget(self.settings_widget)
        pos_x = int(self.geometry.width()//4)
        pos_y = int(self.geometry.height()//4)
        width = int(self.geometry.width()//2)
        height = int(self.geometry.height()//2)
        self.setGeometry(QRect(pos_x, pos_y, width, height))
        self.settings_widget.exit_button.clicked.connect(self.settings_to_main)
    
    def changelog_setup(self, data):
        self.changelog_widget = Changelog_widget(self, data)
        self.layout.addWidget(self.changelog_widget)
        pos_x = int(self.geometry.width()//4)
        pos_y = int(self.geometry.height()//4)
        width = int(self.geometry.width()//2)
        height = int(self.geometry.height()//2)
        self.setGeometry(QRect(pos_x, pos_y, width, height))
        # Dodanie, że albo z settings albo z main 

    def report_setup(self):
        self.report_widget = Report_widget(self)
        self.layout.addWidget(self.report_widget)
        pos_x = int(self.geometry.width()//4)
        pos_y = int(self.geometry.height()//4)
        width = int(self.geometry.width()//2)
        height = int(self.geometry.height()//2)
        self.setGeometry(QRect(pos_x, pos_y, width, height))
        self.report_widget.exit_button.clicked.connect(self.report_to_settings)
#______________________________________________________________________________________________________________________

    def main_to_settings(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.settings_setup()
        self.ping_thread.signal.disconnect()

    def settings_to_main(self):
        self.settings_widget.deleteLater()
        self.settings_widget = None
        self.main_setup()
        self.ping_thread.signal.disconnect()

    def main_to_changelog(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.changelog_setup(data)
        self.ping_thread.signal.disconnect()
    
    def changelog_to_main(self):
        self.changelog_widget.deleteLater()
        self.changelog_widget = None
        self.main_setup()
        self.ping_thread.signal.disconnect()
    
    def settings_to_changelog(self):
        self.settings_widget.deleteLater()
        self.settings_widget = None
        self.changelog_setup()
        self.ping_thread.signal.disconnect()
    
    def changelog_to_settings(self):
        self.changelog_widget.deleteLater()
        self.changelog_widget = None
        self.settings_setup()
        self.ping_thread.signal.disconnect()
    
    def settings_to_report(self):
        self.settings_widget.deleteLater()
        self.settings_widget = None
        self.report_setup()
        self.ping_thread.signal.disconnect()

    def report_to_settings(self):
        self.report_widget.deleteLater()
        self.report_widget = None
        self.settings_setup()
        self.ping_thread.signal.disconnect()
#______________________________________________________________________________________________________________________

    class controller_ping(QThread):
        signal = pyqtSignal(bool)
        def __init__(self):
            super().__init__()
            self.is_connect = None

        def run(self):
            while True:
                self.single_ping()
                time.sleep(5)

        def single_ping(self):
            try:
                socket.setdefaulttimeout(3)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
                if self.is_connect == False or self.is_connect == None:
                    self.is_connect = True
                    self.signal.emit(self.is_connect)
            except socket.error:
                if self.is_connect == True or self.is_connect == None:
                    self.is_connect = False
                    self.signal.emit(self.is_connect)
#______________________________________________________________________________________________________________________

def set_font():
    font_id = QFontDatabase.addApplicationFont(str(pathlib.Path(__file__).resolve().parents[2])+'/updater/STYLE/FONTS/NotoSerif-VariableFont_wdth,wght.ttf')
    font_families = QFontDatabase.applicationFontFamilies(font_id) 
    return QFont(font_families[0])
#______________________________________________________________________________________________________________________

if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setFont(set_font())
    controller = app_controller()
    controller.setHidden(False)
    sys.exit(application.exec_())
#______________________________________________________________________________________________________________________
