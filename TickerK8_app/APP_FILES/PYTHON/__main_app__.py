""" Import sys """
import sys
import pathlib
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import QApplication
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import QFontDatabase, QFont
#______________________________________________________________________________________________________________________
""" Import core of application """
from core.__main_app_core__ import app_controller
#######################################################################################################################
""" Set font """
def set_font():
    font_id = QFontDatabase.addApplicationFont(str(pathlib.Path(__file__).resolve().parents[3])+'/TickerK8_updater/APP_FILES/FONTS/Montserrat-Regular.ttf') # Get font.
    font_families = QFontDatabase.applicationFontFamilies(font_id) # Set font family.
    return QFont(font_families[0]) # Return new font.
#######################################################################################################################
""" Main """
def main():
    application = QApplication(sys.argv)
    application.setFont(set_font())
    controller = app_controller()
    controller.setHidden(False) 
    sys.exit(application.exec_())
#######################################################################################################################
""" Start application """
if __name__ == '__main__':
    main()
 