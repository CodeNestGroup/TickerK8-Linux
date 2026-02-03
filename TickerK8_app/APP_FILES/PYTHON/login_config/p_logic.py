import json

def next(self):
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
    
def previous(self):
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