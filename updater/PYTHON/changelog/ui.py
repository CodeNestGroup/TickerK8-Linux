""" Import packages """
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
)
#______________________________________________________________________________________________________________________

def changelog_ui(self):
    """ Set object name """
    self.setObjectName('changelog_widget')
    self.title_label.setObjectName('title_label')
    self.scroll.setObjectName('scroll')
    self.update_widget.setObjectName('update_widget')
    self.update_title_label.setObjectName('update_title_label')
    self.update_date_label.setObjectName('update_date_label')
    self.update_text_label.setObjectName('update_text_label')
    self.download_button.setObjectName('download_button')
    self.exit_button.setObjectName('exit_button')
    """ Set property """
    self.download_button.setProperty('class', 'buttons')
    self.exit_button.setProperty('class', 'buttons')
    """ Set layout """
    self.layout.addWidget(self.title_label, 5, 5, 10, 90)
    self.layout.addWidget(self.scroll, 20, 5, 60, 90)
    self.layout.addWidget(self.download_button, 85, 40, 4, 20)
    self.layout.addWidget(self.exit_button, 91, 40, 4, 20)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.layout.setRowStretch(enc, 1)
        self.layout.setColumnStretch(enc, 1)
    self.setLayout(self.layout)
    self.update_layout.addWidget(self.update_title_label)
    self.update_layout.addWidget(self.update_date_label)
    self.update_layout.addWidget(self.update_text_label)
    self.update_layout.setSpacing(0)
    self.update_layout.setContentsMargins(0,0,0,0)
    self.update_widget.setLayout(self.update_layout)
    """ Set widget """
    self.setHidden(False)
    self.scroll.setWidgetResizable(True)
    self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.scroll.setWidget(self.update_widget)
    """ Set label """
    self.title_label.setAlignment(Qt.AlignCenter)
    self.update_title_label.setAlignment(Qt.AlignCenter)
    self.update_date_label.setAlignment(Qt.AlignCenter)
    self.update_text_label.setWordWrap(True)
    """ Set button """
    self.download_button.setDisabled(True)
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_date_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.download_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def changelog_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/changelog/'+_global_config['theme']+'.css')).read())
#______________________________________________________________________________________________________________________

def changelog_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/changelog/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    _c = self.changelog_data
    self.title_label.setText(_t['title_label'][_l])
    self.update_title_label.setText(_c['name'])
    self.update_date_label.setText(str(_c['published_at']).replace('T', ' ').replace('Z', ''))
    self.update_text_label.setText(_c['body'])
    self.download_button.setText(_t['download_button'][_l])
    self.exit_button.setText(_t['exit_button'][_l])
#______________________________________________________________________________________________________________________    
    