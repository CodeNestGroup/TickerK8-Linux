def main_changelog_error_ui(self):
    """ Set Object Name """
    self.setObjectName('main_changelog_error_widget')
    self.icon_label.setObjectName('icon_label')
    self.loading_message_label.setObjectName('loading_message_label')
    """ Set property """
    """ Set Layout """
    self.layout.addWidget(self.icon_label, 30, 0, 30, 100)
    self.layout.addWidget(self.loading_message_label, 62, 0, 10, 100)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.layout.setRowStretch(enc, 1)
        self.layout.setColumnStretch(enc, 1)
    self.setLayout(self.layout)
    """ Set Widget """
    self.loading_message_label.setHidden(True)
    """ Set label """
    self.icon_label.setAlignment(Qt.AlignCenter)
    self.loading_message_label.setAlignment(Qt.AlignCenter)
    """ Set Size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.icon_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.loading_message_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def main_changelog_error_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main_changelog_error/'+_global_config['theme']+'.css')).read())
#______________________________________________________________________________________________________________________
