#   --- Import packages ---
import json
#   --- Import PyQt5 packages ---
from PyQt5.QtWidgets import (
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
    QSize
)
from PyQt5.QtGui import (
    QIcon,
    QPixmap,
    QPainter
)
from PyQt5.QtSvg import (
    QSvgRenderer
)

def UpdateSettingsUi(self):
    self.setObjectName('SettingsW')
    self.NaviS.setObjectName('NaviS')
    self.NaviW.setObjectName('NaviW')
    self.NaviStyleB.setObjectName('NaviStyleB')
    self.NaviUpdateB.setObjectName('NaviUpdateB')
    self.NaviLanguageB.setObjectName('NaviLanguageB')
    self.NaviExitB.setObjectName('NaviExitB')
    self.NaviStyleB.setProperty('class', 'NaviB')
    self.NaviUpdateB.setProperty('class', 'NaviB')
    self.NaviLanguageB.setProperty('class', 'NaviB')
    self.NaviExitB.setProperty('class', 'NaviB')
    self.NaviL.addWidget(self.NaviStyleB)
    self.NaviL.addWidget(self.NaviUpdateB)
    self.NaviL.addWidget(self.NaviLanguageB)
    self.NaviL.setSpacing(0)
    self.NaviL.setContentsMargins(0,0,0,0)
    self.NaviW.setLayout(self.NaviL)
    self.Layout.addWidget(self.NaviS, 0, 0, 90, 20)
    self.Layout.addWidget(self.NaviExitB, 90, 0, 10, 20)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.Layout.setRowStretch(i, 1)
        self.Layout.setColumnStretch(i, 1)
    self.setLayout(self.Layout)
    self.show()
    self.NaviS.setWidgetResizable(True)
    self.NaviS.setWidget(self.NaviW)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviStyleB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviUpdateB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviLanguageB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviExitB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def UpdateSettingsReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/assets/CSS/UpdateSettingsMain.css').read()
    c = open(f'{self.Path}/assets/CSS/UpdateSettings{t}.css').read()
    self.setStyleSheet(m+c)
    self.NaviExitB.setIcon(QIcon(load_svg(f'/assets/ICON/Exit{t}.svg', 256, 256)))

def UpdareSettingsRetranslate(self):
    t = json.load(open(self.main_path+'/CONFIG/settings/menu_translate.json', 'r'))
    l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.menu_theme_button.setText(t['menu_theme_button'][l])
    self.menu_sound_button.setText(t['menu_sound_button'][l])
    self.menu_update_button.setText(t['menu_update_button'][l])
    self.menu_language_button.setText(t['menu_language_button'][l])

def theme_ui(self):
    """ Set object name """
    self.day_night_label.setObjectName('day_night_label')
    self.day_night_button.setObjectName('day_night_button')
    self.list_label.setObjectName('list_label')
    self.list_combobox.setObjectName('list_combobox')
    """ Set property """
    self.day_night_label.setProperty('class', 'name_label')
    self.day_night_button.setProperty('class', 'value_button')
    self.list_label.setProperty('class', 'name_label')
    self.list_combobox.setProperty('class', 'value_combobox')
    """ Set layout """
    self.sub_menu_layout.addWidget(self.day_night_label, 20, 0, 30, 50)
    self.sub_menu_layout.addWidget(self.day_night_button, 20, 50, 30, 50)
    self.sub_menu_layout.addWidget(self.list_label, 60, 0, 30, 50)
    self.sub_menu_layout.addWidget(self.list_combobox, 60, 50, 30, 50)
    """ Set widget """
    """ Set label """
    self.day_night_label.setAlignment(Qt.AlignCenter)
    self.list_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    """ Set size """
    self.day_night_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.day_night_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.list_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.list_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def theme_retranslate(self):
    t = json.load(open(self.main_path+'/CONFIG/settings/theme_translate.json', 'r'))
    g = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    l = g['language']
    d = g['theme_index']
    self.title_label.setText(t['title_label'][l])
    self.day_night_label.setText(t['day_night_label'][l])
    self.day_night_button.setText(t['day_night_button'][l][d])
    self.list_combobox.setCurrentIndex(d)
    self.list_label.setText(t['list_label'][l])
#______________________________________________________________________________________________________________________

def sound_ui(self):
    """ Set object name """
    self.button_label.setObjectName('button_label')
    self.button_button.setObjectName('button_button')
    """ Set property """
    self.button_label.setProperty('class', 'name_label')
    self.button_button.setProperty('class', 'value_button')
    """ Set layout """
    self.sub_menu_layout.addWidget(self.button_label, 20, 0, 15, 50)
    self.sub_menu_layout.addWidget(self.button_button, 20, 50, 15, 50)
    """ Set widget """
    """ Set label """
    self.button_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    """ Set size """
    self.button_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.button_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def sound_retranslate(self):
    t = json.load(open(self.main_path+'/CONFIG/settings/sound_translate.json', 'r'))
    g = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    l = g['language']
    s = g['sound']
    self.title_label.setText(t['title_label'][l])
    self.button_label.setText(t['button_label'][l])
    self.button_button.setText(t['button_button'][l][s['button']])
#______________________________________________________________________________________________________________________

def update_ui(self):
    """ Set object name """
    self.version_heading1_label.setObjectName('version_heading1_label')
    self.version_desc_label.setObjectName('version_desc_label')
    self.version_desc_value_label.setObjectName('version_desc_label')
    self.version_changelog_label.setObjectName('version_changelog_label')
    self.version_changelog_button.setObjectName('version_changelog_button')
    self.advanced_heading1_label.setObjectName('advanced_heading1_label')
    self.advanced_capacity_label.setObjectName('advanced_capacity_label')
    self.advanced_capacity_combobox.setObjectName('advanced_capacity_combobox')
    """ Set property """
    self.version_heading1_label.setProperty('class', 'heading1')
    self.version_desc_label.setProperty('class', 'name_label')
    self.version_desc_value_label.setProperty('class', 'value_label')
    self.version_changelog_label.setProperty('class', 'name_label')
    self.version_changelog_button.setProperty('class', 'value_button')
    self.advanced_heading1_label.setProperty('class', 'heading1')
    self.advanced_capacity_label.setProperty('class', 'name_label')
    self.advanced_capacity_combobox.setProperty('class', 'value_combobox')
    """ Set layout """
    self.sub_menu_layout.addWidget(self.version_heading1_label, 20, 0, 10, 100)
    self.sub_menu_layout.addWidget(self.version_desc_label, 35, 0, 5, 50)
    self.sub_menu_layout.addWidget(self.version_desc_value_label, 35, 50, 5, 50)
    self.sub_menu_layout.addWidget(self.version_changelog_label, 45, 0, 5, 50)
    self.sub_menu_layout.addWidget(self.version_changelog_button, 45, 50, 5, 50)
    self.sub_menu_layout.addWidget(self.advanced_heading1_label, 90, 0, 10, 100)
    self.sub_menu_layout.addWidget(self.advanced_capacity_label, 105, 0, 5, 50)
    self.sub_menu_layout.addWidget(self.advanced_capacity_combobox, 105, 50, 5, 50)
    """ Set widget """
    """ Set label """
    self.version_heading1_label.setAlignment(Qt.AlignCenter)
    self.version_desc_label.setAlignment(Qt.AlignCenter)
    self.version_desc_label.setWordWrap(True)
    self.version_desc_value_label.setAlignment(Qt.AlignCenter)
    self.version_desc_value_label.setWordWrap(True)
    self.version_changelog_label.setAlignment(Qt.AlignCenter)
    self.version_changelog_label.setWordWrap(True)
    self.advanced_heading1_label.setAlignment(Qt.AlignCenter)
    self.advanced_capacity_label.setAlignment(Qt.AlignCenter)
    self.advanced_capacity_label.setWordWrap(True)
    """ Set button """
    """ Set size """
    self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.version_heading1_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.version_desc_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.version_desc_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.version_changelog_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.version_changelog_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.advanced_heading1_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.advanced_capacity_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.advanced_capacity_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def update_retranslate(self):
    t = json.load(open(self.main_path+'/CONFIG/settings/update_translate.json', 'r'))
    g = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    d = json.load(open(self.main_path+'/CONFIG/GLOBAL/changelog.json', 'r'))['name']
    l = g['language']
    c = g['capacity']
    self.title_label.setText(t['title_label'][l])
    self.version_heading1_label.setText(t['version_heading1_label'][l])
    self.version_desc_label.setText(t['version_desc_label'][l])
    self.version_desc_value_label.setText(d)
    self.version_changelog_label.setText(t['version_changelog_label'][l])
    self.version_changelog_button.setText(t['version_changelog_button'][l])
    self.advanced_heading1_label.setText(t['advanced_heading1_label'][l])
    self.advanced_capacity_label.setText(t['advanced_capacity_label'][l])
    self.advanced_capacity_combobox.setCurrentIndex(c)
#______________________________________________________________________________________________________________________

def language_ui(self):
    """ Set object name """
    self.type_label.setObjectName('type_label')
    self.type_combobox.setObjectName('type_combobox')
    """ Set property """
    self.type_label.setProperty('class', 'name_label')
    self.type_combobox.setProperty('class', 'value_combobox')
    """ Set layout """
    self.sub_menu_layout.addWidget(self.type_label, 35, 0, 5, 50)
    self.sub_menu_layout.addWidget(self.type_combobox, 35, 50, 5, 50)
    """ Set widget """
    """ Set label """
    self.type_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    """ Set size """
    self.type_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.type_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def language_retranslate(self):
    t = json.load(open(self.main_path+'/CONFIG/settings/language_translate.json', 'r'))
    l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.title_label.setText(t['title_label'][l])
    self.type_label.setText(t['type_label'][l])
    self.type_combobox.setCurrentIndex(l)

def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) 
    pixmap = QPixmap(width, height) 
    pixmap.fill(Qt.transparent) 
    painter = QPainter(pixmap) 
    renderer.render(painter)
    painter.end()
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return scaled_pixmap
#______________________________________________________________________________________________________________________
