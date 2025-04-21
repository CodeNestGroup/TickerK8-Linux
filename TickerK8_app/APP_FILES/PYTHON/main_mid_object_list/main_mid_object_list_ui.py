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
""" Main mid object list Ui """
def main_mid_object_list_ui(self):
    """ Set object name """
    self.setObjectName('main_mid_object_list')
    self.title_label.setObjectName('title_label')
    self.tag_widget.setObjectName('tag_widget')
    self.list_scroll.setObjectName('list_scroll')
    self.type_list_button.setObjectName('type_list_button')
    self.data_list_button.setObjectName('data_list_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.type_list_button.setProperty('class', 'controll_button')
    self.data_list_button.setProperty('class', 'controll_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.title_label, 0, 0, 10, 100)
    self.main_layout.addWidget(self.tag_widget, 10, 0, 5, 100)
    self.main_layout.addWidget(self.list_scroll, 15, 0, 77, 100)
    self.main_layout.addWidget(self.type_list_button, 92, 0, 8, 50)
    self.main_layout.addWidget(self.data_list_button, 92, 50, 8, 50)
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
    self.type_list_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.data_list_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Main mid object list tyle """
def main_mid_object_list_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main_mid_object_list/'+self.global_config['__theme__']+'.css')).read())
    self.type_list_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/list_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.type_list_button.setIconSize(self.type_list_button.size())
    self.data_list_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/edit_table_data_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.data_list_button.setIconSize(self.data_list_button.size())
#######################################################################################################################
""" Main settings retranslate """
def main_mid_object_list_retranslate(self):
    _t = self.main_mid_object_list_translate # Translate texts
    _l = self.global_config['__language__'] # Language
    self.type_list_button.setText(_t['type_list_button'][_l])
    self.data_list_button.setText(_t['data_list_button'][_l])
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
