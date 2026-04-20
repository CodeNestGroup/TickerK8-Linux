#   --- Import ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QSizePolicy
)
from PySide6.QtCore import (
    Qt,
    QSize
)
from PySide6.QtGui import (
    QPixmap,
    QIcon,
    QPainter
)
from PySide6.QtSvg import (
    QSvgRenderer
)

def LoginConfigurationUi(self):
    self.setObjectName('LoginConfigurationW')
    self.TitleL.setObjectName('TitleL')
    self.InfoL.setObjectName('InfoL')
    self.LeftB.setObjectName('LeftB')
    self.ExitB.setObjectName('ExitB')
    self.RightB.setObjectName('RightB')
    self.AcceptB.setObjectName('AcceptB')
    self.NaviL.setObjectName('NaviL')
    self.LeftB.setProperty('class', 'NaviButton')
    self.ExitB.setProperty('class', 'NaviButton')
    self.RightB.setProperty('class', 'NaviButton')
    self.AcceptB.setProperty('class', 'NaviButton')
    self.Layout.addWidget(self.TitleL, 0, 0, 10, 100)
    self.Layout.addWidget(self.InfoL, 15, 0, 75, 100)
    self.Layout.addWidget(self.LeftB, 92, 10, 3, 10)
    self.Layout.addWidget(self.ExitB, 97, 10, 3, 10)
    self.Layout.addWidget(self.RightB, 92, 80, 3, 10)
    self.Layout.addWidget(self.AcceptB, 97, 80, 3, 10)
    self.Layout.addWidget(self.NaviL, 92, 20, 6, 60)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.Layout.setRowStretch(enc, 1)
        self.Layout.setColumnStretch(enc, 1)
    self.setLayout(self.Layout)
    self.show()
    self.AcceptB.hide()
    self.TitleL.setAlignment(Qt.AlignCenter)
    self.InfoL.setAlignment(Qt.AlignCenter)
    self.NaviL.setAlignment(Qt.AlignCenter)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.TitleL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.InfoL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.LeftB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ExitB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.RightB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.AcceptB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def LoginConfigurationReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/assets/CSS/LoginConfigurationMain.css').read()
    c = open(f'{self.Path}/assets/CSS/LoginConfiguration{t}.css').read()
    self.setStyleSheet(m+c)

def LoginConfigurationRetranslate(self):
    l = self.Language
    t = json.load(open(f'{self.Path}/assets/JSON/LoginConfigurationTranslate.json', 'r', encoding='utf-8'))
    self.TitleL.setText(t['TitleL'][l])
    self.InfoL.setText(t['InfoL'][l][0])
    self.LeftB.setText(t['LeftB'][l])
    self.ExitB.setText(t['ExitB'][l])
    self.RightB.setText(t['RightB'][l])
    self.AcceptB.setText(t['AcceptB'][l])

def AppConfUi(self):
    self.CenterW.setObjectName('CenterW')



    
    self.language_subtitle_label.setObjectName('language_subtitle_label')
    self.language_combobox.setObjectName('language_combobox')
    self.theme_subtitle_label.setObjectName('theme_subtitle_label')
    self.theme_combobox.setObjectName('theme_combobox')
    self.language_subtitle_label.setProperty('class', 'subtitle')
    self.theme_subtitle_label.setProperty('class', 'subtitle')
    self.language_combobox.setProperty('class', 'list')
    self.theme_combobox.setProperty('class', 'list')
    self.center_layout.addWidget(self.language_subtitle_label, 0, 0, 10, 50)
    self.center_layout.addWidget(self.language_combobox, 20, 20, 80, 20)
    self.center_layout.addWidget(self.theme_subtitle_label, 0, 50, 10, 50)
    self.center_layout.addWidget(self.theme_combobox, 20, 60, 80, 20)

    self.layout.addWidget(self.center_widget, 15, 0, 75, 100)


    self.language_subtitle_label.setAlignment(Qt.AlignCenter)
    self.theme_subtitle_label.setAlignment(Qt.AlignCenter)
    self.accept_button.hide()
    self.language_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.language_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.theme_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.theme_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    
def AppConfRetranslate(self):
    t = json.load(open(self.main_path+'/PYTHON/login_config/j_app_conf_translate.json', 'r'))
    l = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r'))['language']
    self.language_subtitle_label.setText(t['language_subtitle_label'][l])
    self.language_combobox.addItems(t['language_combobox'])
    self.language_combobox.setCurrentIndex(l)
    self.theme_subtitle_label.setText(t['theme_subtitle_label'][l])
    self.theme_combobox.addItems(t['theme_combobox'])

def sub_conf_ui(self):
    self.left_button.setObjectName('left_button')
    self.center_button.setObjectName('center_button')
    self.right_button.setObjectName('right_button')
    self.left_button.setProperty('class', 'sub_button')
    self.center_button.setProperty('class', 'sub_button')
    self.right_button.setProperty('class', 'sub_button')
    self.center_layout.addWidget(self.left_button, 0, 10, 100, 15)
    self.center_layout.addWidget(self.center_button, 0, 30, 100, 40)
    self.center_layout.addWidget(self.right_button, 0, 75, 100, 15)
    self.accept_button.hide()
    self.left_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.center_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.right_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def sub_conf_reload_style(self):
    s = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r'))['subscription']
    l = [self.center_button, self.right_button, self.left_button]
    self.checked_button = l[s-1]
    self.checked_button.setStyleSheet('border: 2px solid green;')


def sub_conf_retranslate(self):
    t = json.load(open(self.main_path+'/PYTHON/login_config/j_sub_translate.json', 'r'))
    l = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r'))['language']
    self.left_button.setText(t['left_button'][l])
    self.center_button.setText(t['center_button'][l])
    self.right_button.setText(t['right_button'][l])

def accept_settings_ui(self):
    self.regulations_scroll.setObjectName('regulations_scroll')
    self.regulations_widget.setObjectName('regulations_widget')
    self.regulations_label.setObjectName('regulations_label')
    self.center_layout.addWidget(self.regulations_scroll, 0, 20, 100, 60)
    self.regulations_layout.addWidget(self.regulations_label, 0, 0)
    self.regulations_layout.setSpacing(0)
    self.regulations_layout.setContentsMargins(0,0,0,0)
    self.regulations_widget.setLayout(self.regulations_layout)
    self.accept_button.show()
    self.regulations_scroll.setWidget(self.regulations_widget)
    self.regulations_scroll.setWidgetResizable(True)
    self.regulations_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.regulations_label.setAlignment(Qt.AlignCenter)
    self.regulations_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.regulations_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.regulations_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def accept_settings_reload_style(self):
    pass

def accept_settings_retranslate(self):
    t = json.load(open(self.main_path+'/PYTHON/login_config/j_accept_settings_translate.json', 'r'))
    l = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r'))['language']
    self.regulations_label.setText(t['regulations_label'][l])
