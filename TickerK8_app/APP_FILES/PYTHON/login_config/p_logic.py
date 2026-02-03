import json

def Next(self):
    if self.widget_list_index <= len(self.widget_list)-2:
        self.widget_list_index += 1
    i = self.widget_list_index
    f = self.widget_list[i]
    if f:
        self.info_label.hide()
        self.center_widget_setup()
        f()
    elif not f:
        t = json.load(open(self.main_path+'/PYTHON/login_config/j_translate.json', 'r'))
        l = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r'))['language']
        if self.center_widget:
            self.center_widget.deleteLater()
            self.center_widget = None 
        self.info_label.show()
        self.info_label.setText(t['info_label'][l][i])
    
def Previous(self):
    if self.widget_list_index >= 1:
        self.widget_list_index -= 1
    i = self.widget_list_index
    f = self.widget_list[i]
    if f:
        self.info_label.hide()
        self.center_widget_setup()
        f()
    elif not f:
        t = json.load(open(self.main_path+'/PYTHON/login_config/j_translate.json', 'r'))
        l = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r'))['language']
        if self.center_widget:
            self.center_widget.deleteLater()
            self.center_widget = None 
        self.info_label.show()
        self.info_label.setText(t['info_label'][l][i])

def ResetConfig(self):
    with json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r')) as c:
        c['language'] = 0
        c['theme'] = "vintage_elegance_dark"
        c['subscription'] = 0
        c['country'] = []
        c['market'] = []
        c['stock'] = []
        with open(self.main_path+'/PYTHON/login_config/j_config.json', 'w') as f:
            json.dump(c, f, indent=4)

def ChangeLanguage(self):
    with json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r')) as c:
        c['language'] = self.language_combobox.currentIndex()
        with open(self.main_path+'/PYTHON/login_config/j_config.json', 'w') as f:
            json.dump(c, f, indent=4)

def ChangeTheme(self):
    with open(json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r'))) as c:
        c['theme'] = self.language_combobox.currentText()
        with open(self.main_path+'/PYTHON/login_config/j_config.json', 'w') as f:
            json.dump(c, f, indent=4)

def ChangeSub(self, i:int):
    pass

def Search(self, table, ticker, name):
    pass

def Add(self):
    pass

def Delete(self):
    pass

def Reset(self):
    pass