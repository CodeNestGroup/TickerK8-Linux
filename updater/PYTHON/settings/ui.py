""" Import packages """
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
    QSize
)
from PyQt5.QtGui import (
    QPixmap,
    QIcon,
    QPainter
)
from PyQt5.QtSvg import (
    QSvgRenderer
)
#______________________________________________________________________________________________________________________

def settings_ui(self):
    """ Set object name """
    self.setObjectName('settings_widget')
    self.menu_scroll.setObjectName('menu_scroll')
    self.menu_scroll_widget.setObjectName('menu_scroll_widget')
    self.menu_theme_button.setObjectName('menu_theme_button')
    self.menu_sound_button.setObjectName('menu_sound_button')
    self.menu_update_button.setObjectName('menu_update_button')
    self.menu_language_button.setObjectName('menu_language_button')
    self.menu_report_button.setObjectName('menu_report_button')
    self.exit_button.setObjectName('exit_button')
    """ Set property """
    self.menu_theme_button.setProperty('class', 'menu_buttons')
    self.menu_sound_button.setProperty('class', 'menu_buttons')
    self.menu_update_button.setProperty('class', 'menu_buttons')
    self.menu_language_button.setProperty('class', 'menu_buttons')
    self.menu_report_button.setProperty('class', 'menu_buttons')
    """ Set layout """
    self.layout.addWidget(self.menu_scroll, 0, 0, 90, 30)
    self.layout.addWidget(self.exit_button, 90, 0, 10, 30)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.layout.setRowStretch(enc, 1)
        self.layout.setColumnStretch(enc, 1)
    self.setLayout(self.layout)
    self.menu_scroll_layout.addWidget(self.menu_theme_button)
    self.menu_scroll_layout.addWidget(self.menu_sound_button)
    self.menu_scroll_layout.addWidget(self.menu_update_button)
    self.menu_scroll_layout.addWidget(self.menu_language_button)
    self.menu_scroll_layout.addWidget(self.menu_report_button)
    self.menu_scroll_layout.setSpacing(0)
    self.menu_scroll_layout.setContentsMargins(0,0,0,0)
    self.menu_scroll_widget.setLayout(self.menu_scroll_layout)
    """ Set widget """
    self.setHidden(False)
    self.menu_scroll.setWidgetResizable(True)
    self.menu_scroll.setWidget(self.menu_scroll_widget)
    self.menu_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    """ Set label """
    """ Set button """
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.menu_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.menu_theme_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.menu_sound_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.menu_update_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.menu_language_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.menu_report_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def settings_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/settings/'+_global_config['theme']+'.css')).read())
#______________________________________________________________________________________________________________________

def settings_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/settings/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.menu_theme_button.setText(_t['menu_theme_button'][_l])
    self.menu_sound_button.setText(_t['menu_sound_button'][_l])
    self.menu_update_button.setText(_t['menu_update_button'][_l])
    self.menu_language_button.setText(_t['menu_language_button'][_l])
    self.menu_report_button.setText(_t['menu_report_button'][_l])
    self.exit_button.setText(_t['exit_button'][_l])
#______________________________________________________________________________________________________________________

def theme_ui(self):
    """ Set object name """
    self.sub_menu_scroll.setObjectName('sub_menu_scroll')
    self.theme_widget.setObjectName('theme_widget')
    self.theme_title_label.setObjectName('theme_title_label')
    self.theme_d_n_label.setObjectName('theme_d_n_label')
    self.theme_d_n_button.setObjectName('theme_d_n_button')
    self.theme_list_label.setObjectName('theme_list_label')
    self.theme_list_combobox.setObjectName('theme_list_combobox')
    """ Set property """
    self.theme_widget.setProperty('class', 'sub_widgets')
    self.theme_title_label.setProperty('class', 'titles')
    self.theme_d_n_label.setProperty('class', 'sub_titles')
    self.theme_d_n_button.setProperty('class', 'sub_titles')
    self.theme_list_label.setProperty('class', 'sub_titles')
    self.theme_list_combobox.setProperty('class', 'sub_combobox')
    """ Set layout """
    self.layout.addWidget(self.sub_menu_scroll, 0, 30, 100, 70)
    self.theme_layout.addWidget(self.theme_title_label, 0, 0, 10, 100)
    self.theme_layout.addWidget(self.theme_d_n_label, 20, 0, 30, 50)
    self.theme_layout.addWidget(self.theme_d_n_button, 25, 50, 20, 50)
    self.theme_layout.addWidget(self.theme_list_label, 60, 0, 30, 50)
    self.theme_layout.addWidget(self.theme_list_combobox, 65, 50, 20, 50)
    self.theme_layout.setSpacing(0)
    self.theme_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.theme_layout.setRowStretch(enc, 1)
        self.theme_layout.setColumnStretch(enc, 1)
    self.theme_widget.setLayout(self.theme_layout)
    """ Set widget """
    self.sub_menu_scroll.setWidgetResizable(True)
    self.sub_menu_scroll.setWidget(self.theme_widget)
    self.sub_menu_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.theme_widget.setHidden(False)
    """ Set label """
    self.theme_title_label.setAlignment(Qt.AlignCenter)
    self.theme_d_n_label.setAlignment(Qt.AlignCenter)
    self.theme_list_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    """ Set size """
    self.sub_menu_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.theme_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.theme_d_n_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.theme_d_n_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.theme_list_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.theme_list_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def theme_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/settings/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.theme_title_label.setText(_t['theme_title_label'][_l])
    self.theme_d_n_label.setText(_t['theme_d_n_label'][_l])
    self.theme_d_n_button.setText(_t['theme_d_n_button'][_l][config d n ])
    self.theme_list_label.setText(_t['theme_list_label'][_l])
#______________________________________________________________________________________________________________________

def sound_ui(self):
    """ Set object name """
    self.sub_menu_scroll.setObjectName('sub_menu_scroll')
    self.sound_widget.setObjectName('sound_widget')
    self.sound_title_label.setObjectName('sound_title_label')
    self.sound_button_label.setObjectName('sound_button_label')
    self.sound_button_button.setObjectName('sound_button_button')
    self.sound_alert_label.setObjectName('sound_alert_label')
    self.sound_alert_button.setObjectName('sound_alert_button')
    self.sound_notification_label.setObjectName('sound_notification_label')
    self.sound_notification_button.setObjectName('sound_notification_button')
    """ Set property """
    self.sound_widget.setProperty('class', 'sub_widgets')
    self.sound_title_label.setProperty('class', 'titles')
    self.sound_button_label.setProperty('class', 'sub_titles')
    self.sound_button_button.setProperty('class', 'sub_buttons')
    self.sound_alert_label.setProperty('class', 'sub_titles')
    self.sound_alert_button.setProperty('class', 'sub_buttons')
    self.sound_notification_label.setProperty('class', 'sub_titles')
    self.sound_notification_button.setProperty('class', 'sub_buttons')
    """ Set layout """
    self.layout.addWidget(self.sub_menu_scroll, 0, 30, 100, 70)
    self.sound_layout.addWidget(self.sound_title_label, 0, 0, 1, 100)
    self.sound_layout.addWidget(self.sound_button_label, 1, 0, 1, 50)
    self.sound_layout.addWidget(self.sound_button_button, 1, 50, 1, 50)
    self.sound_layout.addWidget(self.sound_alert_label, 2, 0, 1, 50)
    self.sound_layout.addWidget(self.sound_alert_button, 2, 50, 1, 50)
    self.sound_layout.addWidget(self.sound_notification_label, 3, 0, 1, 50)
    self.sound_layout.addWidget(self.sound_notification_button, 3, 50, 1, 50)
    self.sound_layout.setSpacing(0)
    self.sound_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.sound_layout.setRowStretch(enc, 1)
    self.sound_widget.setLayout(self.sound_layout)
    """ Set widget """
    self.sub_menu_scroll.setWidgetResizable(True)
    self.sub_menu_scroll.setWidget(self.sound_widget)
    self.sub_menu_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.sound_widget.setHidden(False)
    """ Set label """
    self.sound_title_label.setAlignment(Qt.AlignCenter)
    self.sound_button_label.setAlignment(Qt.AlignCenter)
    self.sound_alert_label.setAlignment(Qt.AlignCenter)
    self.sound_notification_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    """ Set size """
    self.sub_menu_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.sound_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.sound_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.sound_button_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.sound_button_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.sound_alert_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.sound_alert_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.sound_notification_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.sound_notification_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def sound_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/settings/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.sound_title_label.setText(_t['sound_title_label'][_l])
    self.sound_button_label.setText(_t['sound_button_label'][_l])
    self.sound_button_button.setText(_t['sound_button_button'][_l][config])
    self.sound_alert_label.setText(_t['sound_alert_label'][_l])
    self.sound_alert_button.setText(_t['sound_alert_button'][_l][config])
    self.sound_notification_label.setText(_t['sound_notification_label'][_l])
    self.sound_notification_button.setText(_t['sound_notification_button'][_l][config])
#______________________________________________________________________________________________________________________

def update_ui(self):
    """ Set object name """
    self.sub_menu_scroll.setObjectName('sub_menu_scroll')
    self.update_widget.setObjectName('update_widget')
    self.update_title_label.setObjectName('update_title_label')
    self.update_version_subtitle_label.setObjectName('update_version_subtitle_label')
    self.update_version_desc_title_label.setObjectName('update_version_desc_title_label')
    self.update_version_desc_label.setObjectName('update_version_desc_label')
    self.update_version_changelog_title_label.setObjectName('update_version_changelog_title_label')
    self.update_version_changelog_button.setObjectName('update_version_changelog_button')
    self.update_option_subtitle_label.setObjectName('update_option_subtitle_label')
    self.update_option_autoupdate_title_label.setObjectName('update_option_autoupdate_title_label')
    self.update_option_autoupdate_button.setObjectName('update_option_autoupdate_button')
    self.update_option_check_title_label.setObjectName('update_option_check_title_label')
    self.update_option_check_button.setObjectName('update_option_check_button')
    self.update_advanced_subtitle_label.setObjectName('update_advanced_subtitle_label')
    self.update_advanced_capacity_title_label.setObjectName('update_advanced_capacity_title_label')
    self.update_advanced_capacity_combobox.setObjectName('update_advanced_capacity_combobox')
    self.update_advanced_verification_title_label.setObjectName('update_advanced_verification_title_label')
    self.update_advanced_verification_button.setObjectName('update_advanced_verification_button')
    """ Set property """
    self.update_widget.setProperty('class', 'sub_widgets')
    self.update_title_label.setProperty('class', 'titles')
    self.update_version_subtitle_label.setProperty('class', 'sub_titles')
    self.update_version_desc_title_label.setProperty('class', '')
    self.update_version_desc_label.setProperty('class', '')
    self.update_version_changelog_title_label.setProperty('class', '')
    self.update_version_changelog_button.setProperty('class', '')
    self.update_option_subtitle_label.setProperty('class', 'sub_titles')
    self.update_option_autoupdate_title_label.setProperty('class', '')
    self.update_option_autoupdate_button.setProperty('class', '')
    self.update_option_check_title_label.setProperty('class', '')
    self.update_option_check_button.setProperty('class', '')
    self.update_advanced_subtitle_label.setProperty('class', 'sub_titles')
    self.update_advanced_capacity_title_label.setProperty('class', '')
    self.update_advanced_capacity_combobox.setProperty('class', '')
    self.update_advanced_verification_title_label.setProperty('class', '')
    self.update_advanced_verification_button.setProperty('class', '')
    """ Set layout """
    self.layout.addWidget(self.sub_menu_scroll, 0, 30, 100, 70)
    self.update_layout.addWidget(self.update_title_label, 0, 0, 1, 100)
    self.update_layout.addWidget(self.update_version_subtitle_label, 1, 0, 1, 100)
    self.update_layout.addWidget(self.update_version_desc_title_label, 2, 0, 1, 50)
    self.update_layout.addWidget(self.update_version_desc_label, 2, 50, 1, 50)
    self.update_layout.addWidget(self.update_version_changelog_title_label, 3, 0, 1, 50)
    self.update_layout.addWidget(self.update_version_changelog_button, 3, 50, 1, 50)
    self.update_layout.addWidget(self.update_option_subtitle_label, 4, 0, 1, 100)
    self.update_layout.addWidget(self.update_option_autoupdate_title_label, 5, 0, 1, 50)
    self.update_layout.addWidget(self.update_option_autoupdate_button, 5, 50, 1, 50)
    self.update_layout.addWidget(self.update_option_check_title_label, 6, 0, 1, 50)
    self.update_layout.addWidget(self.update_option_check_button, 6, 50, 1, 50)
    self.update_layout.addWidget(self.update_advanced_subtitle_label, 7, 0, 1, 100)
    self.update_layout.addWidget(self.update_advanced_capacity_title_label, 8, 0, 1, 50)
    self.update_layout.addWidget(self.update_advanced_capacity_combobox, 8, 50, 1, 50)
    self.update_layout.addWidget(self.update_advanced_verification_title_label, 9, 0, 1, 50)
    self.update_layout.addWidget(self.update_advanced_verification_button, 9, 50, 1, 50)
    self.update_layout.setSpacing(0)
    self.update_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.update_layout.setColumnStretch(enc, 1)
    self.update_widget.setLayout(self.update_layout)
    """ Set widget """
    self.sub_menu_scroll.setWidgetResizable(True)
    self.sub_menu_scroll.setWidget(self.update_widget)
    self.sub_menu_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.update_widget.setHidden(False)
    """ Set label """
    self.update_title_label.setAlignment(Qt.AlignCenter)
    self.update_version_subtitle_label.setAlignment(Qt.AlignCenter)
    self.update_version_desc_title_label.setAlignment(Qt.AlignCenter)
    self.update_version_desc_label.setAlignment(Qt.AlignCenter)
    self.update_version_desc_label.setWordWrap(True)
    self.update_version_changelog_title_label.setAlignment(Qt.AlignCenter)
    self.update_option_subtitle_label.setAlignment(Qt.AlignCenter)
    self.update_option_autoupdate_title_label.setAlignment(Qt.AlignCenter)
    self.update_option_check_title_label.setAlignment(Qt.AlignCenter)
    self.update_advanced_subtitle_label.setAlignment(Qt.AlignCenter)
    self.update_advanced_capacity_title_label.setAlignment(Qt.AlignCenter)
    self.update_advanced_verification_title_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    self.update_option_check_button.setDisabled(True)
    """ Set size """
    self.sub_menu_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_version_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_version_desc_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_version_desc_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_version_changelog_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_version_changelog_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_option_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_option_autoupdate_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_option_autoupdate_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_option_check_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_option_check_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_advanced_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_advanced_capacity_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_advanced_capacity_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_advanced_verification_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_advanced_verification_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def update_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/settings/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.update_title_label.setText(_t['update_title_label'][_l])
    self.update_version_subtitle_label.setText(_t['update_version_subtitle_label'][_l])
    self.update_version_desc_title_label.setText(_t['update_version_desc_title_label'][_l])
    self.update_version_desc_label.setText(_t['update_version_desc_label'][_l])
    self.update_version_changelog_title_label.setText(_t['update_version_changelog_title_label'][_l])
    self.update_version_changelog_button.setText(_t['update_version_changelog_button'][_l])
    self.update_option_subtitle_label.setText(_t['update_option_subtitle_label'][_l])
    self.update_option_autoupdate_title_label.setText(_t['update_option_autoupdate_title_label'][_l])
    self.update_option_autoupdate_button.setText(_t['update_option_autoupdate_button'][_l][config])
    self.update_option_check_title_label.setText(_t['update_option_check_title_label'][_l])
    self.update_option_check_button.setText(_t['update_option_check_button'][_l])
    self.update_advanced_subtitle_label.setText(_t['update_advanced_subtitle_label'][_l])
    self.update_advanced_capacity_title_label.setText(_t['update_advanced_capacity_title_label'][_l])
    self.update_advanced_capacity_combobox.setCurrentIndex(config)
    self.update_advanced_verification_title_label.setText(_t['update_advanced_verification_title_label'][_l])
    self.update_advanced_verification_button.setText(_t['update_advanced_verification_button'][_l])
#______________________________________________________________________________________________________________________

def language_ui(self):
    """ Set object name """
    self.sub_menu_scroll.setObjectName('sub_menu_scroll')
    self.language_widget.setObjectName('language_widget')
    self.language_title_label.setObjectName('language_title_label')
    self.language_type_label.setObjectName('language_type_label')
    self.language_type_combobox.setObjectName('language_type_combobox')
    """ Set property """
    self.language_widget.setProperty('class', 'sub_widgets')
    self.language_title_label.setProperty('class', 'titles')
    self.language_type_label.setProperty('class', 'sub_titles')
    self.language_type_combobox.setProperty('class', '')
    """ Set layout """
    self.layout.addWidget(self.sub_menu_scroll, 0, 30, 100, 70)
    self.language_layout.addWidget(self.language_title_label, 0, 0, 1, 100)
    self.language_layout.addWidget(self.language_type_label, 1, 0, 1, 50)
    self.language_layout.addWidget(self.language_type_combobox, 1, 50, 1, 50)
    self.language_layout.setSpacing(0)
    self.language_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.language_layout.setColumnStretch(enc, 1)
    self.language_widget.setLayout(self.language_layout)
    """ Set widget """
    self.sub_menu_scroll.setWidgetResizable(True)
    self.sub_menu_scroll.setWidget(self.language_widget)
    self.sub_menu_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.language_widget.setHidden(False)
    """ Set label """
    self.language_title_label.setAlignment(Qt.AlignCenter)
    self.language_type_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    """ Set size """
    self.sub_menu_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.language_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.language_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.language_type_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.language_type_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

