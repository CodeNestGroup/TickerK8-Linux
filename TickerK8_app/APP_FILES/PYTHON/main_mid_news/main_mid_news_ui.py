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
    Qt, # Qt settings
    QSize # Szie
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon, # Icon
    QPixmap, # Graphic.
    QPainter # Painter.
) 
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
#######################################################################################################################
""" Main mid news ui """
def main_mid_news_ui(self):
    """ Set object name """
    self.setObjectName('main_mid_news')
    self.title_label.setObjectName('title_label')
    self.next_left_button.setObjectName('next_left_button')
    self.next_right_button.setObjectName('next_right_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.next_left_button.setProperty('class', 'next_buttons')
    self.next_right_button.setProperty('class', 'next_buttons')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.title_label, 0, 0, 10, 100)
    self.main_layout.addWidget(self.next_left_button, 90, 0, 10, 50)
    self.main_layout.addWidget(self.next_right_button, 90, 50, 10, 50)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.title_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.next_left_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.next_right_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Main mid news reload style """
def main_mid_news_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main_mid_news/'+self.global_config['__theme__']+'.css')).read())
    self.next_left_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/arrow_left_'+self.global_config['__theme__']+'.svg', 256, 256)))
    self.next_left_button.setIconSize(QSize(self.next_left_button.height(), self.next_left_button.height()))
    self.next_right_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/arrow_right_'+self.global_config['__theme__']+'.svg', 256, 256)))
    self.next_right_button.setIconSize(QSize(self.next_right_button.height(), self.next_right_button.height()))
#######################################################################################################################
""" Main mid news retranslate """
def main_mid_news_retranslate(self):
    _t = self.main_mid_news_translate # Translate texts 
    _l = self.global_config['__language__'] # Language
    self.title_label.setText(_t['title_label'][_l])
#######################################################################################################################
""" Load svg script """
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
