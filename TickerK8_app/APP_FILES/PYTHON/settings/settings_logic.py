import json
""" open sub widget """
def open_sub_widget(self, to_open):
    if self.opened_sub_widget != to_open: 
        if not self.opened_sub_widget:
            to_open.setHidden(False)
            self.opened_sub_widget = to_open
        else:
            self.opened_sub_widget.setHidden(True)
            to_open.setHidden(False)
        self.opened_sub_widget = to_open
    elif self.opened_sub_widget == to_open:
        to_open.setHidden(True)
        self.opened_sub_widget = None
#######################################################################################################################
""" change day night """
def change_day_night(self):
    _index = self.style_theme_themes_content_combobox.currentIndex()
    if _index%2:
        self.style_theme_themes_content_combobox.setCurrentIndex(int(_index-1)) 
    else:
        self.style_theme_themes_content_combobox.setCurrentIndex(int(_index+1))
#_______________________________________________________________________________________________________________________
""" change theme"""
def change_theme(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    _global_config['__theme__'] = int(self.style_theme_themes_content_combobox.currentIndex())
    json.dump(_global_config, open(self.main_self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    self.settings_reload_style()
#______________________________________________________________________________________________________________________
""" Set sound disabled and enabled """
def set_sound_d_e(self, _type):
    
    self.main_self.settings_config_file[_type] = not self.main_self.settings_config_file[_type] # Change config
    json.dump(self.main_self.settings_config_file, open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'w'), indent=4) # Save config
    self.main_self.settings_config_file = json.load(open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'r')) # Reload settings config file
    button = None # Set deafoult
    if _type == '__sound_button__':
        button = self.main_self.settings_sound_button_button
    elif _type == '__sound_alert__':
        button = self.main_self.settings_sound_alert_button
    elif _type == '__sound_notification__':
        button = self.main_self.settings_sound_notification_button
    if button:
        button.setText(self.main_self.settings_translate_file[f'settings{_type[1:-1]}button'][self.main_self.settings_config_file['__language__']][self.main_self.settings_config_file[_type]]) # Change text of button
    self.main_self.notification_background_widget.setHidden(False) # Show notification widget
    self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][4]) # Set text
    self.main_self.controller_notification.open() # Open notification
#_______________________________________________________________________________________________________________________
""" Change language """
def change_language(self):
    """ Get data """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    _global_config['__language__'] = int(self.language_langauge_content_combobox.currentIndex())  
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    self.settings_retranslate()
#######################################################################################################################


