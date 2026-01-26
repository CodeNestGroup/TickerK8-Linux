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
    QPixmap,
    QIcon,
    QPainter
)
from PyQt5.QtSvg import (
    QSvgRenderer
)

def ui(self):
    self.title_label.setObjectName('title_label')
    self.info_label.setObjectName('info_label')
    self.left_button.setObjectName('left_button')
    self.right_button.setObjectName('right_button')
    self.navi_label.setObjectName('navi_label')
    self.left_button.setProperty('class', 'navi_button')
    self.right_button.setProperty('class', 'navi_button')
    self.layout.addWidget(self.title_label, 0, 0, 10, 100)
    self.layout.addWidget(self.info_label, 15, 0, 75, 100)
    self.layout.addWidget(self.left_button, 92, 10, 6, 10)
    self.layout.addWidget(self.right_button, 92, 80, 6, 10)
    self.layout.addWidget(self.navi_label, 92, 20, 6, 60)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.layout.setRowStretch(enc, 1)
        self.layout.setColumnStretch(enc, 1)
    self.setLayout(self.layout)
    self.show()
    self.title_label.setAlignment(Qt.AlignCenter)
    self.info_label.setAlignment(Qt.AlignCenter)
    self.navi_label.setAlignment(Qt.AlignCenter)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.info_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.left_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.right_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.navi_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def reload_style(self):
    self.setStyleSheet(self.main_path+'/PYTHON/login_config/style.css')
    # Dodać ikony

def center_widget_setup(self):
    self.center_widget.setObjectName('center_widget')
    self.center_layout.setSpacing(0)
    self.center_layout.setContentsMargins(0,0,0,0)
    self.center_widget.setLayout(self.center_layout)
    self.layout.addWidget(self.center_widget, 15, 0, 75, 100)
    self.center_widget.show()
    self.center_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def app_conf_ui(self):
    self.language_subtitle_label.setObjectName('language_subtitle_label')
    self.language_combobox.setObjectName('language_combobox')
    self.theme_subtitle_label.setObjectName('theme_subtitle_label')
    self.theme_combobox.setObjectName('theme_combobox')
    self.language_subtitle_label.setProperty('class', 'subtitle')
    self.theme_subtitle_label.setProperty('class', 'subtitle')
    self.language_combobox.setProperty('class', 'list')
    self.theme_combobox.setProperty('class', 'list')
    self.center_layout.addWidget()
    self.center_layout.addWidget()
    self.center_layout.addWidget()
    self.center_layout.addWidget()
    self.center_layout.addWidget()
    self.language_subtitle_label.setAlignment(Qt.AlignCenter)
    self.theme_subtitle_label.setAlignment(Qt.AlignCenter)
    


def app_conf_reload_style(self):
    pass

def app_conf_retranslate(self):
    pass

def sub_conf_ui(self):
    pass

def sub_conf_reload_style(self):
    pass

def sub_conf_retranslate(self):
    pass

def list_conf_ui(self):
    pass

def list_conf_reload_style(self):
    pass

def list_conf_retranslate(self):
    pass

def accept_settings_ui(self):
    pass

def accept_settings_reload_style(self):
    pass

def accept_settings_retranslate(self):
    pass
