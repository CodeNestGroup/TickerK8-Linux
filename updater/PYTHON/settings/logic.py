""" Import packages"""
import json 
""" sub menu open """
def sub_menu_open(self, open_func):
    if self.sub_menu_scroll:
        self.sub_menu_scroll.deleteLater()
    """ Create objects """
    self.sub_menu_scroll = QScrollArea(self)
    self.sub_menu_widget = QWidget(self.sub_menu_scroll)
    self.sub_menu_layout = QGridLayout(self.sub_menu_widget)
    self.title_label = QLabel(self.sub_menu_widget)
    """ Call functions """
    sub_menu_ui(self)
    open_func()
#______________________________________________________________________________________________________________________
""" change day night """
def change_d_n(self):
    c = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r'))
    i = c['theme']
    n = None
    if i%2:
        n -=1
    else:
        n += 1
    if n:   
        c['theme'] = n
    json.dump(c, open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'w', indent=4))
#______________________________________________________________________________________________________________________

""" change theme """
def change_theme(self):
    c = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r'))
    c['theme'] = int(self.list_combobox.currentIndex())
    json.dump(c, open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'w', indent=4))
#______________________________________________________________________________________________________________________

""" change sound disabled, enabled """
def change_sound_d_e(self, t):
    c = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r'))
    c['sound'][t] = not c['sound'][t]
    json.dump(c, open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'w', indent=4))
#______________________________________________________________________________________________________________________

""" change auto update """
def change_auto_update(self):
    c = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r'))
    c['auto_update'] = not c['auto_update']
    json.dump(c, open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'w', indent=4))
#______________________________________________________________________________________________________________________

""" check updates """
def check_updates(self):
    pass
#______________________________________________________________________________________________________________________

""" change capacity """
def change_capacity(self):
    c = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r'))
    c['capacity'] = self.advanced_capacity_combobox.currentIndex()
    json.dump(c, open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'w', indent=4))
#______________________________________________________________________________________________________________________

"""" check compatibility """
def check_compatibility(self):
    f = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/app_file_list.json', 'r'))
    compatibility = False
    for file, value in f.items():
        if value == 'config':
            continue
        elif value != calculate_sha256(self.main_self.main_path+file):
        #   print(file, calculate_sha256(self.main_self.main_path+file))
            compatibility = False # Set not compatibility in files
        if compatibility:
            # Dodać że notyfikacja
            pass
        else:
            # Dodać że alert
            pass
#______________________________________________________________________________________________________________________

""" check sum control """
def check_sum_control():
    sha256 = hashlib.sha256()  
    f = open(file, "rb")
    while chunk := f.read(4096):
        sha256.update(chunk)
    return sha256.hexdigest()
#______________________________________________________________________________________________________________________

""" change language """
def change_language(self):
    c = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r'))
    c['language'] = self.type_combobox.currentIndex()
    json.dump(c, open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'w', indent=4))
#______________________________________________________________________________________________________________________

""" change auto report """
def change_auto_report(self):
    c = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r'))
    c['auto_report'] = not c['auto_report']
    json.dump(c, open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'w', indent=4))
#______________________________________________________________________________________________________________________
