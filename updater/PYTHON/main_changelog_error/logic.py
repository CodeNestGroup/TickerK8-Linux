""" Import packages """
""" Import PyQT5 packages """
from PyQt5.QtCore import (
    QThread,
    pyqtSignal
)
#______________________________________________________________________________________________________________________

def controller_error(self):
        try:
            self.animation.stop()
            self.animation.quit()
            self.animation.wait()
            self.animation.deleteLater()
        except:
            pass
        self.loading_message_label.setText(self.main_self.settings_translate_file['main_changelog_error_widget'][0][self.main_self.settings_config_file['__language__']]) # Set text of message 
        self.loading_message_label.setHidden(False)
#______________________________________________________________________________________________________________________
    
def controller_loading(self):
        try:
            self.animation.stop()
            self.animation.quit()
            self.animation.wait()
            self.animation.deleteLater()
        except:
            pass
        self.animation = self.animation_thread()
        self.animation.update_text.connect(self.setup_text)
        self.animation.start()
        self.loading_message_label.setHidden(False)
    
def setup_text(self, dots):
        self.loading_message_label.setText(self.main_self.settings_translate_file['main_changelog_error_widget'][1][self.main_self.settings_config_file['__language__']]+dots) # Set text
#______________________________________________________________________________________________________________________

class animation_thread(QThread):
    update_text = pyqtSignal(str)
    stop_signal = False
    def run(self):
        dots = ""
        while not self.stop_signal:
            dots = "." * ((len(dots) + 1) % 4)
            self.update_text.emit(dots)
            time.sleep(0.5)
    def stop(self):
        self.stop_signal = True
#______________________________________________________________________________________________________________________
