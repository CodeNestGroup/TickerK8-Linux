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

def center_widget_setup_ui(self):
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
    self.center_layout.addWidget(self.language_subtitle_label, , , , )
    self.center_layout.addWidget(self.language_combobox, , , , )
    self.center_layout.addWidget(self.theme_subtitle_label, , , , )
    self.center_layout.addWidget(self.theme_combobox, , , , )
    self.language_subtitle_label.setAlignment(Qt.AlignCenter)
    self.theme_subtitle_label.setAlignment(Qt.AlignCenter)
    self.language_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.language_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.theme_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.theme_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    
def app_conf_retranslate(self):
    t = json.load(open(self.main_path+'/PYTHON/login_config/translate.json', 'r'))
    l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.language_subtitle_label.setText(t['language_subtitle_label'][l])
    self.language_combobox.addItems()
    self.theme_subtitle_label.setText(t['theme_subtitle_label'][l])
    self.language_combobox.addItems()

def sub_conf_ui(self):
    self.left_button.setObjectName('left_button')
    self.center_button.setObjectName('center_button')
    self.right_button.setObjectName('right_button')
    self.left_button.setProperty('class', 'sub_button')
    self.center_button.setProperty('class', 'sub_button')
    self.right_button.setProperty('class', 'sub_button')
    self.center_layout.addWidget(self.left_button, , , , )
    self.center_layout.addWidget(self.center_button, , , , )
    self.center_layout.addWidget(self.right_button, , , , )
    self.left_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.center_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.right_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def sub_conf_reload_style(self):
    pass
    # Add icons 

def sub_conf_retranslate(self):
    pass
    # Add text 

def list_conf_ui(self):
    self.country_subtitle_label.setObjectName('country_subtitle_label')
    self.country_search_lineedit.setObjectName('country_search_lineedit')
    self.country_scroll.setObjectName('country_scroll')
    self.country_widget.setObjectName('country_widget')
    self.country_number_label.setObjectName('country_number_label')
    self.country_icon_label.setObjectName('country_icon_label')
    self.country_ticker_label.setObjectName('country_ticker_label')
    self.country_name_label.setObjectName('country_name_label')
    self.country_add_button.setObjectName('country_add_button')
    self.country_reset_button.setObjectName('country_reset_button')
    self.country_delete_button.setObjectName('country_delete_button')
    self.country_added_scroll.setObjectName('country_added_scroll')
    self.country_added_widget.setObjectName('country_added_widget')
    self.country_added_number_label.setObjectName('country_added_number_label')
    self.country_added_icon_label.setObjectName('country_added_icon_label')
    self.country_added_ticker_label.setObjectName('country_added_ticker_label')
    self.country_added_name_label.setObjectName('country_added_name_label')
    self.country_error_label.setObjectName('country_error_label')
    self.market_subtitle_label.setObjectName('market_subtitle_label')
    self.market_search_lineedit.setObjectName('market_search_lineedit')
    self.market_scroll.setObjectName('market_scroll')
    self.market_widget.setObjectName('market_widget')
    self.market_number_label.setObjectName('market_number_label')
    self.market_icon_label.setObjectName('market_icon_label')
    self.market_ticker_label.setObjectName('market_ticker_label')
    self.market_name_label.setObjectName('market_name_label')
    self.market_add_button.setObjectName('market_add_button')
    self.marlet_reset_button.setObjectName('marlet_reset_button')
    self.market_delete_button.setObjectName('market_delete_button')
    self.market_added_scroll.setObjectName('market_added_scroll')
    self.market_added_widget.setObjectName('market_added_widget')
    self.market_added_number_label.setObjectName('market_added_number_label')
    self.market_added_icon_label.setObjectName('market_added_icon_label')
    self.market_added_ticker_label.setObjectName('market_added_ticker_label')
    self.market_added_name_label.setObjectName('market_added_name_label')
    self.market_error_label.setObjectName('market_error_label')
    self.stock_subtitle_label.setObjectName('stock_subtitle_label')
    self.stock_search_lineedit.setObjectName('stock_search_lineedit')
    self.stock_scroll.setObjectName('stock_scroll')
    self.stock_widget.setObjectName('stock_widget')
    self.stock_number_label.setObjectName('stock_number_label')
    self.stock_icon_label.setObjectName('stock_icon_label')
    self.stock_ticker_label.setObjectName('stock_ticker_label')
    self.stock_name_label.setObjectName('stock_name_label')
    self.stock_add_button.setObjectName('stock_add_button')
    self.stock_reset_button.setObjectName('stock_reset_button')
    self.stock_delete_button.setObjectName('stock_delete_button')
    self.stock_added_scroll.setObjectName('stock_added_scroll')
    self.stock_added_widget.setObjectName('stock_added_widget')
    self.stock_added_number_label.setObjectName('stock_added_number_label')
    self.stock_added_icon_label.setObjectName('stock_added_icon_label')
    self.stock_added_ticker_label.setObjectName('stock_added_ticker_label')
    self.stock_added_name_label.setObjectName('stock_added_name_label')
    self.stock_error_label.setObjectName('stock_error_label')


    self.country_subtitle_label.setProperty('class', 'subtitle')
    self.market_subtitle_label.setProperty('class', 'subtitle')
    self.stock_subtitle_label.setProperty('class', 'subtitle')

    self.country_search_lineedit.setProperty('class', 'search')
    self.market_search_lineedit.setProperty('class', 'search')
    self.stock_search_lineedit.setProperty('class', 'search')

    self.country_scroll.setProperty('class', 'scroll')
    self.country_added_scroll.setProperty('class', 'scroll')
    self.market_scroll.setProperty('class', 'scroll')
    self.market_added_scroll.setProperty('class', 'scroll')
    self.stock_scroll.setProperty('class', 'scroll')
    self.stock_added_scroll.setProperty('class', 'scroll')

    self.country_widget
    self.country_added_widget
    self.market_widget



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
