""" Import PyQt5 packages """
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QSizePolicy # Size policy.
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt, # Qt settings.
    QSize # Size.
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon # Icon.
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (QPixmap, # Graphic.
                         QPainter) # Painter.
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
#######################################################################################################################
""" Main Ui """
def main_ui(self):
    """ Set object name """
    self.setObjectName('main_widget')
    self.top_widget.setObjectName('top_widget')
    self.top_search_button.setObjectName('top_search_button')
    self.top_settings_button.setObjectName('top_settings_button')
    self.mid_widget.setObjectName('mid_widget')
    self.bottom_widget.setObjectName('bottom_widget')
    self.bottom_left_news_button.setObjectName('bottom_left_news_button')
    self.bottom_left_chart_button.setObjectName('bottom_left_chart_button')
    self.bottom_left_stats_button.setObjectName('bottom_left_stats_button')
    self.bottom_mid_type_list_button.setObjectName('bottom_mid_type_list_button')
    self.bottom_mid_data_list_button.setObjectName('bottom_mid_data_list_button')
    self.bottom_right_market_button.setObjectName('bottom_right_market_button')
    self.bottom_right_country_button.setObjectName('bottom_right_country_button')
    self.bottom_right_world_button.setObjectName('bottom_right_world_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.top_settings_button.setProperty('class', 'top_button')
    self.bottom_left_news_button.setProperty('class', 'bottom_button')
    self.bottom_left_chart_button.setProperty('class', 'bottom_button')
    self.bottom_left_stats_button.setProperty('class', 'bottom_button')
    self.bottom_mid_type_list_button.setProperty('class', 'bottom_button')
    self.bottom_mid_data_list_button.setProperty('class', 'bottom_button')
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
    self.top_widget_layout.addWidget(self.top_search_button, 30, 40, 40, 20)
    self.top_widget_layout.addWidget(self.top_settings_button, 15, 95, 25, 3)
    self.top_widget_layout.setSpacing(0)
    self.top_widget_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.top_widget_layout.setRowStretch(enc, 1)
        self.top_widget_layout.setColumnStretch(enc, 1)
    self.top_widget.setLayout(self.top_widget_layout)
    self.mid_widget_layout.addWidget(self.mid_object_scroll, 0, 0, 100, 27)
    self.mid_widget_layout.addWidget(self.mid_object_list_widget, 0, 30, 100, 40)
    self.mid_widget_layout.addWidget(self.mid_news_widget, 0, 73, 100, 27)
    self.mid_widget_layout.setSpacing(0)
    self.mid_widget_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.mid_widget_layout.setRowStretch(enc, 1)
        self.mid_widget_layout.setColumnStretch(enc, 1)
    self.mid_widget.setLayout(self.mid_widget_layout)
    self.bottom_widget_layout.addWidget(self.bottom_left_news_button, 0, 0, 100, 9)
    self.bottom_widget_layout.addWidget(self.bottom_left_chart_button, 0, 9, 100, 9)
    self.bottom_widget_layout.addWidget(self.bottom_left_stats_button, 0, 18, 100, 9)
    self.bottom_widget_layout.addWidget(self.bottom_mid_type_list_button, 0, 30, 100, 20)
    self.bottom_widget_layout.addWidget(self.bottom_mid_data_list_button, 0, 50, 100, 20)
    self.bottom_widget_layout.addWidget(self.bottom_right_market_button, 0, 73, 100, 9)
    self.bottom_widget_layout.addWidget(self.bottom_right_country_button, 0, 82, 100, 9)
    self.bottom_widget_layout.addWidget(self.bottom_right_world_button, 0, 91, 100, 9)
    self.bottom_widget_layout.setSpacing(0)
    self.bottom_widget_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.bottom_widget_layout.setRowStretch(enc, 1)
        self.bottom_widget_layout.setColumnStretch(enc, 1)
    self.bottom_widget.setLayout(self.bottom_widget_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Set label """
#______________________________________________________________________________________________________________________
    """ Set button """
    self.bottom_left_news_button.setDisabled(True)
    self.bottom_left_chart_button.setDisabled(True)
    self.bottom_left_stats_button.setDisabled(True)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_search_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_settings_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.mid_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.mid_object_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.mid_object_list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.mid_news_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_left_news_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_left_chart_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_left_stats_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_mid_type_list_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_mid_data_list_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_right_market_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_right_country_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_right_world_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Main style """
def main_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main/'+self.global_config['__theme__']+'.css')).read())
    self.top_search_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/search_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.top_search_button.setIconSize(self.top_settings_button.size())
    self.top_settings_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/settings_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.top_settings_button.setIconSize(self.top_settings_button.size())
    self.bottom_left_news_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/news_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.bottom_left_news_button.setIconSize(self.bottom_left_news_button.size())
    self.bottom_left_chart_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/chart_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.bottom_left_chart_button.setIconSize(self.bottom_left_chart_button.size())
    self.bottom_left_stats_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/statistics_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.bottom_left_stats_button.setIconSize(self.bottom_left_stats_button.size())
    self.bottom_mid_type_list_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/list_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.bottom_mid_type_list_button.setIconSize(self.bottom_mid_type_list_button.size())
    self.bottom_mid_data_list_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/edit_table_data_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.bottom_mid_data_list_button.setIconSize(self.bottom_mid_data_list_button.size())
    self.bottom_right_market_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/market_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.bottom_right_market_button.setIconSize(self.bottom_right_market_button.size())
    self.bottom_right_country_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/country_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.bottom_right_country_button.setIconSize(self.bottom_right_country_button.size())
    self.bottom_right_world_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/world_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.bottom_right_world_button.setIconSize(self.bottom_right_world_button.size())

#######################################################################################################################
""" Main retranslate """
def main_retranslate(self):
    _t = self.main_translate # Translate texts.
    _l = self.global_config['__language__'] # Language.
    self.top_search_button.setText(_t['top_search_button'][_l])
    self.bottom_left_news_button.setText(_t['bottom_left_news_button'][_l])
    self.bottom_left_chart_button.setText(_t['bottom_left_chart_button'][_l])
    self.bottom_left_stats_button.setText(_t['bottom_left_stats_button'][_l])
    self.bottom_mid_type_list_button.setText(_t['bottom_mid_type_list_button'][_l])
    self.bottom_mid_data_list_button.setText(_t['bottom_mid_data_list_button'][_l])
    self.bottom_right_market_button.setText(_t['bottom_right_market_button'][_l])
    self.bottom_right_country_button.setText(_t['bottom_right_country_button'][_l])
    self.bottom_right_world_button.setText(_t['bottom_right_world_button'][_l])
#######################################################################################################################
""" Load svg script """
def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) # Render svg.
    pixmap = QPixmap(width, height) # Create pixmap.
    pixmap.fill(Qt.transparent) # Transparent.
    painter = QPainter(pixmap) # Render graphic .
    renderer.render(painter) # Render graphic.
    painter.end() # Render graphic.
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation) # Scal pixmap.
    return scaled_pixmap
#######################################################################################################################