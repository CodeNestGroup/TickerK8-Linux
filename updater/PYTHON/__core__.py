""" Import packages """
import sys
import pathlib
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QDesktopWidget,
    QMainWindow
    )
from PyQt5.QtCore import (
    QRect
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

    def settings_setup(self):
        self.settings_widget = Settings_widget(self)
        self.layout.addWidget(self.settings_widget)
        pos_x = int(self.geometry.width()//4)
        pos_y = int(self.geometry.height()//4)
        width = int(self.geometry.width()//2)
        height = int(self.geometry.height()//2)
        self.setGeometry(QRect(pos_x, pos_y, width, height))
    
    def changelog_setup(self):
        self.changelog_widget = Changelog_widget(self)
        self.layout.addWidget(self.changelog_widget)
        pos_x = int(self.geometry.width()//4)
        pos_y = int(self.geometry.height()//4)
        width = int(self.geometry.width()//2)
        height = int(self.geometry.height()//2)
        self.setGeometry(QRect(pos_x, pos_y, width, height))

    def report_setup(self):
        self.report_widget = Report_widget(self)
        self.layout.addWidget(self.report_widget)
        pos_x = int(self.geometry.width()//4)
        pos_y = int(self.geometry.height()//4)
        width = int(self.geometry.width()//2)
        height = int(self.geometry.height()//2)
        self.setGeometry(QRect(pos_x, pos_y, width, height))
#______________________________________________________________________________________________________________________

    def main_to_settings(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.settings_setup()

    def settings_to_main(self):
        self.settings_widget.deleteLater()
        self.settings_widget = None
        self.main_setup()

    def main_to_changelog(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.changelog_setup()
    
    def changelog_to_main(self):
        self.changelog_widget.deleteLater()
        self.changelog_widget = None
        self.main_setup()
    
    def settings_to_changelog(self):
        self.settings_widget.deleteLater()
        self.settings_widget = None
        self.changelog_setup()
    
    def changelog_to_settings(self):
        self.changelog_widget.deleteLater()
        self.changelog_widget = None
        self.settings_setup()
    
    def settings_to_report(self):
        self.settings_widget.deleteLater()
        self.settings_widget = None
        self.report_setup()

    def report_to_settings(self):
        self.report_widget.deleteLater()
        self.report_widget = None
        self.settings_setup()

#______________________________________________________________________________________________________________________

def set_font():
    font_id = QFontDatabase.addApplicationFont(str(pathlib.Path(__file__).resolve().parents[3])+'/updater/STYLE/FONTS/NotoSerif-VariableFont_wdth,wght.ttf')
    font_families = QFontDatabase.applicationFontFamilies(font_id) 
    return QFont(font_families[0])
#______________________________________________________________________________________________________________________

if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setFont(set_font())
    controller = app_controller()
    controller.setHidden(False)
    sys.exit(app.exec_())
