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
""" Main Ui """
def main_ui(self):
    """ Set object name """
    self.setObjectName('main_widget')
    self.top_widget.setObjectName('top_widget')
    self.top_exit_button.setObjectName('top_exit_button')
    self.top_window_button.setObjectName('top_window_button')
    self.top_minimize_button.setObjectName('top_minimize_button')
    self.top_search_button.setObjectName('top_search_button')
    self.top_settings_button.setObjectName('top_settings_button')
    self.mid_widget.setObjectName('mid_widget')
    self.mid_object_scroll.setObjectName('mid_object_scroll')
    self.bottom_widget.setObjectName('bottom_widget')
    self.bottom_left_news_button.setObjectName('bottom_left_news_button')
    self.bottom_left_chart_button.setObjectName('bottom_left_chart_button')
    self.bottom_left_stats_button.setObjectName('bottom_left_stats_button')
    self.botom_center_add_button.setObjectName('botom_center_add_button')
    self.bottom_right_market_button.setObjectName('bottom_right_market_button')
    self.bottom_right_country_button.setObjectName('bottom_right_country_button')
    self.bottom_right_world_button.setObjectName('bottom_right_world_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.top_exit_button.setProperty('class', 'top_button')
    self.top_window_button.setProperty('class', 'top_button')
    self.top_minimize_button.setProperty('class', 'top_button')
    self.top_settings_button.setProperty('class', 'top_button')
    self.bottom_left_news_button.setProperty('class', 'bottom_button')
    self.bottom_left_chart_button.setProperty('class', 'bottom_button')
    self.bottom_left_stats_button.setProperty('class', 'bottom_button')
    self.botom_center_add_button.setProperty('class', 'bottom_button')
    self.bottom_right_market_button.setProperty('class', 'bottom_button')
    self.bottom_right_country_button.setProperty('class', 'bottom_button')
    self.bottom_right_world_button.setProperty('class', 'bottom_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.top_widget, 0, 0, 15, 100)
    self.main_layout.addWidget(self.mid_widget, 15, 0, 70, 100)
    self.main_layout.addWidget(self.bottom_widget, 85, 0, 15, 100)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
    self.top_widget_layout.addWidget(self.top_exit_button, 15, 2, 25, 3)
    self.top_widget_layout.addWidget(self.top_window_button, 15, 6, 25, 3)
    self.top_widget_layout.addWidget(self.top_minimize_button, 15, 10, 25, 3)
    self.top_widget_layout.addWidget(self.top_search_button, 30, 40, 40, 20)
    self.top_widget_layout.addWidget(self.top_settings_button, 35, 90, 30, 3)
    self.top_widget_layout.setSpacing(0)
    self.top_widget_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.top_widget_layout.setRowStretch(enc, 1)
        self.top_widget_layout.setColumnStretch(enc, 1)
    self.top_widget.setLayout(self.top_widget_layout)
    self.mid_widget_layout.addWidget(self.mid_object_scroll, 0, 0, 100, 30)
    self.mid_widget_layout.addWidget(self.mid_object_list_widget, 0, 30, 100, 40)
    self.mid_widget_layout.addWidget(self.mid_news_widget, 0, 70, 100, 30)
    self.mid_widget_layout.setSpacing(0)
    self.mid_widget_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.mid_widget_layout.setRowStretch(enc, 1)
        self.mid_widget_layout.setColumnStretch(enc, 1)
    self.mid_widget.setLayout(self.mid_widget_layout)
    self.bottom_widget_layout.addWidget(self.bottom_left_news_button, 0, 0, 100, 10)
    self.bottom_widget_layout.addWidget(self.bottom_left_chart_button, 0, 10, 100, 10)
    self.bottom_widget_layout.addWidget(self.bottom_left_stats_button, 0, 20, 100, 10)
    self.bottom_widget_layout.addWidget(self.botom_center_add_button, 0, 30, 100, 40)
    self.bottom_widget_layout.addWidget(self.bottom_right_market_button, 0, 70, 100, 10)
    self.bottom_widget_layout.addWidget(self.bottom_right_country_button, 0, 80, 100, 10)
    self.bottom_widget_layout.addWidget(self.bottom_right_world_button, 0, 90, 100, 10)
    self.bottom_widget_layout.setSpacing(0)
    self.bottom_widget_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.bottom_widget_layout.setRowStretch(enc, 1)
        self.bottom_widget_layout.setColumnStretch(enc, 1)
    self.bottom_widget.setLayout(self.bottom_widget_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
    self.mid_object_scroll.setWidgetResizable(True)
    self.mid_object_scroll.setWidget(self.mid_object_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
#______________________________________________________________________________________________________________________
    """ Set line edit """
#______________________________________________________________________________________________________________________
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_window_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_minimize_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_search_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_settings_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.mid_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.mid_object_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.mid_object_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.mid_object_list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.mid_news_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_left_news_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_left_chart_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_left_stats_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.botom_center_add_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_right_market_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_right_country_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_right_world_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Main style """
def main_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main/'+self.global_config['__theme__']+'.css')).read())
#######################################################################################################################
""" Main retranslate """
def main_retranslate(self):
    _t = self.main_translate # Translate texts 
    _l = self.global_config['__language__'] # Language
    self.top_exit_button.setText(_t['top_exit_button'][_l])
    self.top_window_button.setText(_t['top_window_button'][_l])
    self.top_minimize_button.setText(_t['top_minimize_button'][_l])
    self.top_search_button.setText(_t['top_search_button'][_l])
    self.top_settings_button.setText(_t['top_settings_button'][_l])
    self.bottom_left_news_button.setText(_t['bottom_left_news_button'][_l])
    self.bottom_left_chart_button.setText(_t['bottom_left_chart_button'][_l])
    self.bottom_left_stats_button.setText(_t['bottom_left_stats_button'][_l])
    self.botom_center_add_button.setText(_t['botom_center_add_button'][_l])
    self.bottom_right_market_button.setText(_t['bottom_right_market_button'][_l])
    self.bottom_right_country_button.setText(_t['bottom_right_country_button'][_l])
    self.bottom_right_world_button.setText(_t['bottom_right_world_button'][_l])
#######################################################################################################################
#  