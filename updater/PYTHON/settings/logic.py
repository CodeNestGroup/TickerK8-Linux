""" Import packages"""
import json 
import hashlib
import pathlib
import urllib.request
""" Import PyQt5 packages """
from PyQt5.QtCore import (
    QThread,
    pyqtSignal
)
""" Import settings modules"""
from .ui import (
    settings_reload_style,
    settings_retranslate,
    theme_retranslate,
    sound_retranslate,
    update_retranslate,
    language_retranslate,
    report_retranslate
    )
#______________________________________________________________________________________________________________________

def change_d_n(self):
    """ Change config """
    c = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    t = c['theme'][:-1]
    i = c['theme_index']
    if i%2:
        t += 'l'
        i -= 1
    else:
        t += 'd'
        i += 1
    c['theme'] = t
    c['theme_index'] = i
    json.dump(c, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    """ Reload """
    settings_reload_style(self)
    theme_retranslate(self)
    self.list_combobox.setCurrentIndex(i)
#______________________________________________________________________________________________________________________

def change_theme(self):
    c = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    i = int(self.list_combobox.currentIndex())
    if i == 0:
        t = 'vintage_elegance_l'
    elif i == 1:
        t = 'vintage_elegance_d'
    c['theme'] = t
    c['theme_index'] = i
    json.dump(c, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    """ Reload """
    settings_reload_style(self)
    theme_retranslate(self)
#______________________________________________________________________________________________________________________

def change_sound_d_e(self, t):
    c = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    c['sound'][t] = not c['sound'][t]
    json.dump(c, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    """ Reload """
    sound_retranslate(self)
#______________________________________________________________________________________________________________________

def change_auto_update(self):
    c = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    c['auto_update'] = not c['auto_update']
    json.dump(c, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    """ Reload """
    update_retranslate(self)
#______________________________________________________________________________________________________________________

def get_releases_file(self):
    self.get_releases_thread = get_releases()
    self.get_releases_thread.finished.connect()
    self.get_releases_thread.finished.connect(lambda: self.get_releases_thread.quit())
    self.get_releases_thread.finished.connect(lambda: self.get_releases_thread.wait())
    self.get_releases_thread.finished.connect(lambda: self.get_releases_thread.deleteLater())
#______________________________________________________________________________________________________________________

class check_releases(QThread):
        finished = pyqtSignal(list)
        def __init__(self):
            super().__init__()
            self.start()

        def run(self):
            release = urllib.request.urlopen('https://api.github.com/repos/CodeNestGroup/TickerK8-Linux/releases')
            self.finished.emit(json.loads(release.read().decode()))
#______________________________________________________________________________________________________________________

""" change capacity """
def change_capacity(self):
    c = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    c['capacity'] = self.advanced_capacity_combobox.currentIndex()
    json.dump(c, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
#______________________________________________________________________________________________________________________

"""" check compatibility """
def check_compatibility(self):
    p = str(pathlib.Path(__file__).resolve().parents[3])
    f = json.load(open(self.main_path+'/CONFIG/GLOBAL/app_file_list.json', 'r'))
    compatibility = False
    for file, value in f.items():
        if value == 'config':
            continue
        elif value != check_sum_control(p+file):
            print(file, check_sum_control(p+file))
            compatibility = False
        if compatibility:
            # Dodać że notyfikacja
            pass
        else:
            # Dodać że alert
            pass
#______________________________________________________________________________________________________________________

""" check sum control """
def check_sum_control(file):
    sha256 = hashlib.sha256()  
    f = open(file, "rb")
    while chunk := f.read(4096):
        sha256.update(chunk)
    return sha256.hexdigest()
#______________________________________________________________________________________________________________________

""" change language """
def change_language(self):
    c = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    c['language'] = self.type_combobox.currentIndex()
    json.dump(c, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    """ Reload """
    settings_retranslate(self)
    language_retranslate(self)
#______________________________________________________________________________________________________________________

""" change auto report """
def change_auto_report(self):
    c = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    c['auto_report'] = not c['auto_report']
    json.dump(c, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    """ Reload """
    report_retranslate(self)
#______________________________________________________________________________________________________________________
