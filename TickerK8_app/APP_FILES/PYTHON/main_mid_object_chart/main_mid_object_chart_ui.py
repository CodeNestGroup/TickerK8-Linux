""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt, # Qt settings
    QSize # Size
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon # Icon
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (QPixmap, # Graphic.
                         QPainter) # Painter.
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
#######################################################################################################################
""" Main mid object chart Ui """
def main_mid_object_chart_ui(self):
    """ Set object name """
    self.setObjectName('main_mid_object_chart')
    self.current_price_line_label.setObjectName('current_price_line_label')
    self.type_chart_button.setObjectName('type_chart_button')
    self.time_widget.setObjectName('time_widget')
    self.time_day_button.setObjectName('time_day_button')
    self.time_five_day_button.setObjectName('time_five_day_button')
    self.time_one_month_button.setObjectName('time_one_month_button')
    self.time_three_month_button.setObjectName('time_three_month_button')
    self.time_six_month_button.setObjectName('time_six_month_button')
    self.time_one_year_button.setObjectName('time_one_year_button')
    self.time_five_year_button.setObjectName('time_five_year_button')
    self.time_all_button.setObjectName('time_all_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.time_day_button.setProperty('class', 'time_button')
    self.time_five_day_button.setProperty('class', 'time_button')
    self.time_one_month_button.setProperty('class', 'time_button')
    self.time_three_month_button.setProperty('class', 'time_button')
    self.time_one_year_button.setProperty('class', 'time_button')
    self.time_five_year_button.setProperty('class', 'time_button')
    self.time_all_button.setProperty('class', 'time_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.time_widget, 90, 0, 10, 80)
    self.main_layout.addWidget(self.type_chart_button, 92, 85, 6, 10)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
    self.time_layout.addWidget(self.time_day_button, 10, 10, 80, 8)
    self.time_layout.addWidget(self.time_five_day_button, 10, 20, 80, 8)
    self.time_layout.addWidget(self.time_one_month_button, 10, 30, 80, 8)
    self.time_layout.addWidget(self.time_three_month_button, 10, 40, 80, 8)
    self.time_layout.addWidget(self.time_six_month_button, 10, 50, 80, 8)
    self.time_layout.addWidget(self.time_one_year_button, 10, 60, 80, 8)
    self.time_layout.addWidget(self.time_five_year_button, 10, 70, 80, 8)
    self.time_layout.addWidget(self.time_all_button, 10, 80, 80, 8)
    self.time_layout.setSpacing(0)
    self.time_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.time_layout.setRowStretch(enc, 1)
        self.time_layout.setColumnStretch(enc, 1)
    self.time_widget.setLayout(self.time_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Set label """
#______________________________________________________________________________________________________________________
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.current_price_line_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.type_chart_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.time_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.time_day_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.time_five_day_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.time_one_month_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.time_three_month_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.time_six_month_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.time_one_year_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.time_five_year_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.time_all_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Main mid object chart reload style """
def main_mid_object_chart_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main_mid_object_chart/'+self.global_config['__theme__']+'.css')).read())
#######################################################################################################################
""" Main settings retranslate """
def main_mid_object_chart_retranslate(self):
    _t = self.main_translate
    _l = self.global_config['__language__']
    self.time_day_button.setText(_t['time_day_button'][_l])
    self.time_five_day_button.setText(_t['time_five_day_button'][_l])
    self.time_one_month_button.setText(_t['time_one_month_button'][_l])
    self.time_three_month_button.setText(_t['time_three_month_button'][_l])
    self.time_six_month_button.setText(_t['time_six_month_button'][_l])
    self.time_one_year_button.setText(_t['time_one_year_button'][_l])
    self.time_five_year_button.setText(_t['time_five_year_button'][_l])
    self.time_all_button.setText(_t['time_all_button'][_l])
#######################################################################################################################
""" Load svg """
def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) # Render svg
    pixmap = QPixmap(width, height) # Create pixmap
    pixmap.fill(Qt.transparent) # Transparent
    painter = QPainter(pixmap) # Render graphic 
    renderer.render(painter) # Render graphic
    painter.end() # Render graphic
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation) # Scal pixmap
    return scaled_pixmap
#######################################################################################################################
