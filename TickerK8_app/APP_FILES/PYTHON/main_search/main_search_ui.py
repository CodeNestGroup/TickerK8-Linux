""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QPushButton, # Simple button
    QGridLayout, # Grid layout
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt # Qt settings
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon # Icon
)
#######################################################################################################################
""" Main search Ui """
def main_search_ui(self):
    """ Set object name """
    self.setObjectName('main_search_widget')
    self.panel_widget.setObjectName('panel_widget')
    self.panel_search_icon_label.setObjectName('panel_search_icon_label')
    self.panel_search_lineedit.setObjectName('panel_search_lineedit')
    self.panel_type_stock_button.setObjectName('panel_type_stock_button')
    self.panel_type_etf_button.setObjectName('panel_type_etf_button')
    self.panel_type_forex_button.setObjectName('panel_type_forex_button')
    self.panel_type_index_button.setObjectName('panel_type_index_button')
    self.panel_type_market_button.setObjectName('panel_type_market_button')
    self.panel_type_country_button.setObjectName('panel_type_country_button')
    self.panel_sort_id_button.setObjectName('panel_sort_id_button')
    self.panel_logo_label.setObjectName('panel_logo_label')
    self.panel_sort_name_button.setObjectName('panel_sort_name_button')
    self.panel_scroll.setObjectName('panel_scroll')
    self.panel_exit_button.setObjectName('panel_exit_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.panel_type_stock_button.setProperty('class', 'panel_type_buttons')
    self.panel_type_etf_button.setProperty('class', 'panel_type_buttons')
    self.panel_type_forex_button.setProperty('class', 'panel_type_buttons')
    self.panel_type_index_button.setProperty('class', 'panel_type_buttons')
    self.panel_type_market_button.setProperty('class', 'panel_type_buttons')
    self.panel_type_country_button.setProperty('class', 'panel_type_buttons')
    self.panel_sort_id_button.setProperty('class', 'panel_sort_buttons')
    self.panel_sort_name_button.setProperty('class', 'panel_sort_buttons')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.panel_widget, 10, 20, 80, 60)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
    self.panel_layout.addWidget(self.panel_search_icon_label, 5, 35, 5, 5)
    self.panel_layout.addWidget(self.panel_search_lineedit, 5, 40, 5, 20)
    self.panel_layout.addWidget(self.panel_type_stock_button, 15, 5, 3, 14)
    self.panel_layout.addWidget(self.panel_type_etf_button, 15, 21, 3, 14)
    self.panel_layout.addWidget(self.panel_type_forex_button, 15, 37, 3, 14)
    self.panel_layout.addWidget(self.panel_type_index_button, 15, 53, 3, 14)
    self.panel_layout.addWidget(self.panel_type_market_button, 15, 69, 3, 14)
    self.panel_layout.addWidget(self.panel_type_country_button, 15, 85, 3, 14)
    self.panel_layout.addWidget(self.panel_sort_id_button, 20, 5, 3, 5)
    self.panel_layout.addWidget(self.panel_logo_label, 20, 10, 3, 5)
    self.panel_layout.addWidget(self.panel_sort_name_button, 20, 15, 3, 5)
    self.panel_layout.addWidget(self.panel_scroll, 23, 5, 67, 90)
    self.panel_layout.addWidget(self.panel_exit_button, 93, 40, 4, 20)
    self.panel_layout.setSpacing(0)
    self.panel_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.panel_layout.setRowStretch(enc, 1)
        self.panel_layout.setColumnStretch(enc, 1)
    self.panel_widget.setLayout(self.panel_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.panel_search_icon_label.setAlignment(Qt.AlignCenter)
    self.panel_logo_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set line edit """
#______________________________________________________________________________________________________________________
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_search_icon_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_search_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_type_stock_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_type_etf_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_type_forex_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_type_index_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_type_market_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_type_country_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_sort_id_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_logo_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_sort_name_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Main search style """
def main_search_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/MAIN_SEARCH/'+self.global_config['__theme__']+'.css')).read())
#######################################################################################################################
""" Main search retranslate """
def main_search_retranslate(self):
    _t = self.main_search_translate # Translate texts 
    _l = self.global_config['__language__'] # Language
    self.panel_search_lineedit.setPlaceholderText(_t['panel_search_lineedit'][_l])
    self.panel_type_stock_button.setText(_t['panel_type_stock_button'][_l])
    self.panel_type_etf_button.setText(_t['panel_type_etf_button'][_l])
    self.panel_type_forex_button.setText(_t['panel_type_forex_button'][_l])
    self.panel_type_index_button.setText(_t['panel_type_index_button'][_l])
    self.panel_type_market_button.setText(_t['panel_type_index_button'][_l])
    self.panel_type_country_button.setText(_t['panel_type_country_button'][_l])
    self.panel_sort_id_button.setText(_t['panel_sort_id_button'][_l])
    self.panel_logo_label.setText(_t['panel_logo_label'][_l])
    self.panel_sort_name_button.setText(_t['panel_sort_name_button'][_l])
    self.panel_exit_button.setText(_t['panel_exit_button'][_l])
#######################################################################################################################
