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
""" nav object list ui """
def nav_object_list_ui(self):
    """ Set object name """
    self.setObjectName('nav_object_list')
    self.title_label.setObjectName('title_label')
    self.tag_widget.setObjectName('tag_widget')
    self.list_scroll.setObjectName('list_scroll')
#______________________________________________________________________________________________________________________
    """ Set property """
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.title_label, 0, 0, 10, 100)
    self.main_layout.addWidget(self.tag_widget, 10, 0, 5, 100)
    self.main_layout.addWidget(self.list_scroll, 15, 0, 85, 100)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
    self.tag_layout.setSpacing(0)
    self.tag_layout.setContentsMargins(0,0,0,0)
    self.tag_widget.setLayout(self.tag_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
    self.list_scroll.setWidgetResizable(True)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.title_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.tag_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.list_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" nav object list tyle """
def nav_object_list_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/nav_object_list/'+self.global_config['__theme__']+'.css')).read())
#######################################################################################################################
""" nav object list retranslate """
def nav_object_list_retranslate(self):
    _t = self.nav_object_list_translate # Translate texts
    _l = self.global_config['__language__'] # Language
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
