""" Import sys """
import sys
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import QApplication
#______________________________________________________________________________________________________________________
""" Import core of application """
from core.__main_app_core__ import app_controller
#######################################################################################################################
""" Main """
def main():
    application = QApplication(sys.argv)
    controller = app_controller()
    controller.setHidden(False)
    sys.exit(application.exec_())
#######################################################################################################################
""" Start application """
if __name__ == '__main__':
    main()
 