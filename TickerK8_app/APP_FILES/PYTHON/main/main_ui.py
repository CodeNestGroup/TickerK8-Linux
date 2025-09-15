import json
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
    self.main_search_button.setObjectName('main_search_button')
    self.main_objects_list_title.setObjectName('main_objects_list_title')
    self.main_objects_list_scroll.setObjectName('main_objects_list_scroll')
    self.main_type_list_button.setObjectName('main_type_list_button')
    self.main_data_list_button.setObjectName('main_data_list_button')
    self.main_settings_button.setObjectName('main_settings_button')
    self.main_logout_button.setObjectName('main_logout_button')
    #self.news_object_button.setObjectName('news_object_button')
    #self.chart_button.setObjectName('chart_button')
    #self.stats_button.setObjectName('stats_button')
    #self.news_market_button.setObjectName('news_market_button')
    #self.news_country_button.setObjectName('news_country_button')
    #self.news_world_button.setObjectName('news_world_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.main_type_list_button.setProperty('class', 'main_list_button')
    self.main_data_list_button.setProperty('class', 'main_list_button')
    self.main_settings_button.setProperty('class', 'main_bottom_button')
    self.main_logout_button.setProperty('class', 'main_bottom_button')
    #self.news_object_button.setProperty('class', 'bottom_button')
    #self.chart_button.setProperty('class', 'bottom_button')
    #self.stats_button.setProperty('class', 'bottom_button')
    #self.news_market_button.setProperty('class', 'bottom_button')
    #self.news_country_button.setProperty('class', 'bottom_button')
    #self.news_world_button.setProperty('class', 'bottom_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.main_search_button, 1, 1, 3, 11)
    self.main_layout.addWidget(self.main_objects_list_title, 8, 1, 2, 11)
    self.main_layout.addWidget(self.main_objects_list_scroll, 15, 1, 72, 11)
    self.main_layout.addWidget(self.main_type_list_button, 90, 1, 2, 5)
    self.main_layout.addWidget(self.main_data_list_button, 90, 7, 2, 5)
    self.main_layout.addWidget(self.main_settings_button, 96, 1, 2, 2)
    self.main_layout.addWidget(self.main_logout_button, 96, 4, 2, 2)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
    self.main_objects_list_scroll.setWidgetResizable(True)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.main_objects_list_title.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set button """
    #self.news_object_button.setDisabled(True)
    #self.chart_button.setDisabled(True)
    #self.stats_button.setDisabled(True)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_search_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_objects_list_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_objects_list_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_type_list_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_data_list_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_settings_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_logout_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    #self.news_object_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    #self.chart_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)#
    #self.stats_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    #self.news_market_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    #self.news_country_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    #self.news_world_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Main style """
def main_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data.
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main/'+_global_config['__theme__']+'.css')).read())
    self.main_search_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/search_'+_global_config['__theme__']+'.svg'), 256, 256)))
    self.main_search_button.setIconSize(self.main_search_button.size())
    self.main_type_list_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/list_'+_global_config['__theme__']+'.svg'), 256, 256)))
    self.main_type_list_button.setIconSize(self.main_type_list_button.size())
    self.main_data_list_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/edit_table_data_'+_global_config['__theme__']+'.svg'), 256, 256)))
    self.main_data_list_button.setIconSize(self.main_data_list_button.size())
    self.main_settings_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/settings_'+_global_config['__theme__']+'.svg'), 256, 256)))
    self.main_settings_button.setIconSize(self.main_settings_button.size())
    self.main_logout_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/exit_'+_global_config['__theme__']+'.svg'), 256, 256)))
    self.main_logout_button.setIconSize(self.main_logout_button.size())
    #self.news_object_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/news_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    #self.news_object_button.setIconSize(self.news_object_button.size())
    #self.chart_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/chart_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    #self.chart_button.setIconSize(self.chart_button.size())
    #self.stats_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/statistics_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    #self.stats_button.setIconSize(self.stats_button.size())
    #self.news_market_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/market_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    #self.news_market_button.setIconSize(self.news_market_button.size())
    #self.news_country_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/country_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    #self.news_country_button.setIconSize(self.news_country_button.size())
    #self.news_world_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/world_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    #self.news_world_button.setIconSize(self.news_world_button.size())
#######################################################################################################################
""" Main retranslate """
def main_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r')) # Translate texts.
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['__language__'] # Language.
    self.main_search_button.setText(_t['main_search_button'][_l])
    #self.news_object_button.setText(_t['news_object_button'][_l])
    #self.chart_button.setText(_t['chart_button'][_l])
    #self.stats_button.setText(_t['stats_button'][_l])
    self.main_type_list_button.setText(_t['main_type_list_button'][_l])
    self.main_data_list_button.setText(_t['main_data_list_button'][_l])
    #self.news_market_button.setText(_t['news_market_button'][_l])
    #self.news_country_button.setText(_t['news_country_button'][_l])
    #self.news_world_button.setText(_t['news_world_button'][_l])
#######################################################################################################################
""" main_object_list_lists_ui"""
def main_object_list_lists_ui(self):
    """ Set object name """
    self.main_objects_list_lists_title_label.setObjectName('main_objects_list_lists_title_label')
    self.main_objects_list_lists_scroll.setObjectName('main_objects_list_lists_scroll')
    self.main_objects_list_lists_scroll_widget.setObjectName('main_objects_list_lists_widget')
    self.main_objects_list_lists_exit_button.setObjectName('main_objects_list_lists_exit_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.main_objects_list_lists_title_label, 8, 1, 2, 11)
    self.main_layout.addWidget(self.main_objects_list_lists_scroll, 15, 1, 72, 11)
    self.main_layout.addWidget(self.main_objects_list_lists_exit_button, 90, 1, 2, 11)
    self.main_objects_list_lists_layout.setSpacing(0)
    self.main_objects_list_lists_layout.setContentsMargins(0,0,0,0)
    self.main_objects_list_lists_widget.setLayout(self.main_objects_list_lists_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.main_objects_list_lists_scroll.setWidgetResizable(True)
    self.main_objects_list_lists_scroll.setWidget(self.main_objects_list_lists_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.main_objects_list_lists_title_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.main_objects_list_lists_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_objects_list_lists_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_objects_list_lists_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_objects_list_lists_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" main object list lists reload style """
def main_object_list_lists_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Get global config data.
    self.main_objects_list_lists_exit_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/exit_'+_global_config['__theme__']+'.svg', 256, 256)))
    self.main_objects_list_lists_exit_button.setIconSize(self.main_objects_list_lists_exit_button.size())
#######################################################################################################################
""" main object list lists retranslate """
def main_object_list_lists_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r')) # Translate texts.
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['__language__'] # Language.
    self.main_objects_list_lists_title_label.setText(_t['main_objects_list_lists_title_label'][_l])
#######################################################################################################################
""" main object list edit ui """
def main_object_list_edit_ui(self):
    """ Set object name """
    self.main_object_list_edit_title_label.setObjectName('main_object_list_edit_title_label')
    self.main_object_list_edit_scroll.setObjectName('main_object_list_edit_scroll')
    self.main_object_list_edit_widget.setObjectName('main_object_list_edit_widget')
    self.main_object_list_edit_icon_button.setObjectName('main_object_list_edit_icon_button')
    self.main_object_list_edit_ticker_button.setObjectName('main_object_list_edit_ticker_button')
    self.main_object_list_edit_pe_ratio_button.setObjectName('main_object_list_edit_pe_ratio_button')
    self.main_object_list_edit_eps_button.setObjectName('main_object_list_edit_eps_button')
    self.main_object_list_edit_dividend_yield_button.setObjectName('main_object_list_edit_dividend_yield_button')
    self.main_object_list_edit_capitalization_button.setObjectName('main_object_list_edit_capitalization_button')
    self.main_object_list_edit_capital_button.setObjectName('main_object_list_edit_capital_button')
    self.main_object_list_edit_exit_button.setObjectName('main_object_list_edit_exit_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.main_object_list_edit_icon_button.setProperty('class', 'main_object_list_edit_data_button')
    self.main_object_list_edit_ticker_button.setProperty('class', 'main_object_list_edit_data_button')
    self.main_object_list_edit_pe_ratio_button.setProperty('class', 'main_object_list_edit_data_button')
    self.main_object_list_edit_eps_button.setProperty('class', 'main_object_list_edit_data_button')
    self.main_object_list_edit_dividend_yield_button.setProperty('class', 'main_object_list_edit_data_button')
    self.main_object_list_edit_capitalization_button.setProperty('class', 'main_object_list_edit_data_button')
    self.main_object_list_edit_capital_button.setProperty('class', 'main_object_list_edit_data_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.main_object_list_edit_title_label, 8, 1, 2, 11)
    self.main_layout.addWidget(self.main_object_list_edit_scroll, 15, 1, 72, 11)
    self.main_layout.addWidget(self.main_object_list_edit_exit_button, 90, 1, 2, 11)
    self.main_object_list_edit_layout.addWidget(self.main_object_list_edit_icon_button,0,0)
    self.main_object_list_edit_layout.addWidget(self.main_object_list_edit_ticker_button,0,1)
    self.main_object_list_edit_layout.addWidget(self.main_object_list_edit_pe_ratio_button,1,0)
    self.main_object_list_edit_layout.addWidget(self.main_object_list_edit_eps_button,1,1)
    self.main_object_list_edit_layout.addWidget(self.main_object_list_edit_dividend_yield_button,2,0)
    self.main_object_list_edit_layout.addWidget(self.main_object_list_edit_capitalization_button,2,1)
    self.main_object_list_edit_layout.addWidget(self.main_object_list_edit_capital_button,3,0)
    self.main_object_list_edit_layout.setSpacing(0)
    self.main_object_list_edit_layout.setContentsMargins(0,0,0,0)
    self.main_object_list_edit_widget.setLayout(self.main_object_list_edit_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.main_object_list_edit_scroll.setWidgetResizable(True)
    self.main_object_list_edit_scroll.setWidget(self.main_object_list_edit_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.main_object_list_edit_title_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.main_object_list_edit_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_object_list_edit_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_object_list_edit_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_object_list_edit_icon_button.setFixedHeight(self.main_object_list_edit_scroll.height()//2)
    self.main_object_list_edit_icon_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_object_list_edit_ticker_button.setFixedHeight(self.main_object_list_edit_scroll.height()//2)
    self.main_object_list_edit_ticker_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_object_list_edit_pe_ratio_button.setFixedHeight(self.main_object_list_edit_scroll.height()//2)
    self.main_object_list_edit_pe_ratio_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_object_list_edit_eps_button.setFixedHeight(self.main_object_list_edit_scroll.height()//2)
    self.main_object_list_edit_eps_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_object_list_edit_dividend_yield_button.setFixedHeight(self.main_object_list_edit_scroll.height()//2)
    self.main_object_list_edit_dividend_yield_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_object_list_edit_capitalization_button.setFixedHeight(self.main_object_list_edit_scroll.height()//2)
    self.main_object_list_edit_capitalization_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_object_list_edit_capital_button.setFixedHeight(self.main_object_list_edit_scroll.height()//2)
    self.main_object_list_edit_capital_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_object_list_edit_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" main object list edit reload style """
def main_object_list_edit_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    self.main_object_list_edit_exit_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/exit_'+_global_config['__theme__']+'.svg', 256, 256)))
    self.main_object_list_edit_exit_button.setIconSize(self.main_object_list_edit_exit_button.size())
#######################################################################################################################
""" main object list edit retranslate """
def main_object_list_edit_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r')) # Translate texts.
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['__language__'] # Language.
    self.main_object_list_edit_title_label.setText(_t['main_object_list_edit_title_label'][_l])
    self.main_object_list_edit_icon_button.setText(_t['main_object_list_edit_icon_button'][_l])
    self.main_object_list_edit_ticker_button.setText(_t['main_object_list_edit_ticker_button'][_l])
    self.main_object_list_edit_pe_ratio_button.setText(_t['main_object_list_edit_pe_ratio_button'][_l])
    self.main_object_list_edit_eps_button.setText(_t['main_object_list_edit_eps_button'][_l])
    self.main_object_list_edit_dividend_yield_button.setText(_t['main_object_list_edit_dividend_yield_button'][_l])
    self.main_object_list_edit_capitalization_button.setText(_t['main_object_list_edit_capitalization_button'][_l])
    self.main_object_list_edit_capital_button.setText(_t['main_object_list_edit_capital_button'][_l])
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