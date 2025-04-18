""" Import PyQt5 Gui """
from PyQt5.QtGui import (QPixmap, # Graphic.
                         QPainter) # Painter.
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
#######################################################################################################################
""" Setup widget """
def setup_widget(self):
    """ Get data """
    connect = sqlite3.connect(self.local_database) # Create connect 
    cursor = connect.cursor() # Create cursor 
    query = f'SELECT id, logo, name, ticker FROM INDEXES WHERE id=={self.main_mid_object_config['__id__']};' # Query 
    cursor.execute(query, object_list) # Execute 
    result = cursor.fetchall() # Get result
#______________________________________________________________________________________________________________________
    self.icon_label.setPixmap(load_svg(self.main_path+result[1], 128, 128))
    self.ticker_label.setText(result[3])
    self.name_label.setText(result[2])
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
