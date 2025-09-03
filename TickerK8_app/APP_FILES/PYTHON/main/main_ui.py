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
    self.nav_widget.setObjectName('nav_widget')
    self.nav_search_button.setObjectName('nav_search_button')
    self.nav_object_list_widget.setObjectName('nav_object_list_widget')
    self.nav_type_list_button.setObjectName('nav_type_list_button')
    self.nav_data_list_button.setObjectName('nav_data_list_button')
    self.nav_settings_button.setObjectName('nav_settings_button')
    self.nav_logout_button.setObjectName('nav_logout_button')
    self.news_object_button.setObjectName('news_object_button')
    self.chart_button.setObjectName('chart_button')
    self.stats_button.setObjectName('stats_button')
    self.news_market_button.setObjectName('news_market_button')
    self.news_country_button.setObjectName('news_country_button')
    self.news_world_button.setObjectName('news_world_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.nav_type_list_button.setProperty('class', 'nav_list_button')
    self.nav_data_list_button.setProperty('class', 'nav_list_button')
    self.nav_settings_button.setProperty('class', 'nav_bottom_button')
    self.nav_logout_button.setProperty('class', 'nav_bottom_button')
    self.news_object_button.setProperty('class', 'bottom_button')
    self.chart_button.setProperty('class', 'bottom_button')
    self.stats_button.setProperty('class', 'bottom_button')
    self.news_market_button.setProperty('class', 'bottom_button')
    self.news_country_button.setProperty('class', 'bottom_button')
    self.news_world_button.setProperty('class', 'bottom_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.nav_widget, 0, 0, 100, 15)
    self.main_layout.addWidget(self.object_scroll, 0, 20, 90, 35)
    self.main_layout.addWidget(self.news_object_button, 90, 20, 10, 10)
    self.main_layout.addWidget(self.chart_button, 90, 30, 10, 10)
    self.main_layout.addWidget(self.stats_button, 90, 40, 10, 10)
    self.main_layout.addWidget(self.news_widget, 0, 60, 90, 35)
    self.main_layout.addWidget(self.news_market_button, 90, 60, 10, 10)
    self.main_layout.addWidget(self.news_country_button, 90, 70, 10, 10)
    self.main_layout.addWidget(self.news_world_button, 90, 80, 10, 10)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
    self.nav_layout.addWidget(self.nav_search_button, 5, 5, 15, 90)
    self.nav_layout.addWidget(self.nav_object_list_widget, 20, 0, 60, 100)
    self.nav_layout.addWidget(self.nav_type_list_button, 80, 0, 5, 50)
    self.nav_layout.addWidget(self.nav_data_list_button, 80, 50, 5, 50)
    self.nav_layout.addWidget(self.nav_settings_button, 90, 25, 5, 15)
    self.nav_layout.addWidget(self.nav_logout_button, 90, 60, 6, 15)
    for enc in range(15):
        self.nav_layout.setRowStretch(enc, 1)
        self.nav_layout.setColumnStretch(enc, 1)
    self.nav_widget.setLayout(self.nav_layout)  
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Set label """
#______________________________________________________________________________________________________________________
    """ Set button """
    self.news_object_button.setDisabled(True)
    self.chart_button.setDisabled(True)
    self.stats_button.setDisabled(True)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.nav_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.nav_search_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.nav_object_list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.nav_type_list_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.nav_data_list_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.nav_settings_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.nav_logout_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_object_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.chart_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.stats_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_market_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_country_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_world_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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