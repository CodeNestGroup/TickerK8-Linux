""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QGraphicsItem,
)
from PyQt5.QtCore import (
    QRectF,
    QPointF
)
""" Import from QtGui """
from PyQt5.QtGui import (
    QPainter, # Painter, tool that create/paint item
    QBrush, # Brush 
    QPen, # Pen for single line 
    QColor # For set color 
)
#######################################################################################################################
""" Candle chart """
def candle_chart(self):
    local_list = [] # Create local variable
    for s in self.chart_data: local_list += [s['h'], s['l']]# Loop for data, serch highest and lowest price
    max_price, min_price = max(local_list), min(local_list) # Get highest, lowest price 
    _space_between = 0
    _view_height = self.height()
    _scale = (max_price-min_price)*_view_height
    for single_data in self.chart_data:
        _space_between += 5
        _open = ((max_price-single_data['o'])/_scale)*100000
        _high = ((max_price-single_data['h'])/_scale)*100000
        _close = ((max_price-single_data['c'])/_scale)*100000
        _low = ((max_price-single_data['l'])/_scale)*100000
        self.main_scence.addItem(Candle(_space_between, _open, _high, _close, _low))
#######################################################################################################################
""" Candle """
class Candle(QGraphicsItem):
    """ __init__ """
    def __init__(self, x=int, o=int, h=int, c=int, l=int):
        super().__init__()
        self.x = x
        self.o = o
        self.h = h
        self.c = c
        self.l = l
        self.color_wick = QColor('#000000')
        self.color_body = QColor('#ff0000') if self.o < self.c else QColor('#00ff00')
        print(self.x, self.o, self.h, self.c, self.l)
#______________________________________________________________________________________________________________________
    """ boundig rect """
    def boundingRect(self):
        return QRectF(self.x, self.h, 4, int(self.l-self.h))
#______________________________________________________________________________________________________________________
    """ paint """
    def paint(self, painter, option, widget=None):
        painter.setPen(QPen(self.color_wick, 1)) # Set pen color, size to create high, low price line
        painter.drawLine(QPointF(self.x+2, self.h), QPointF(self.x+2, self.l)) # Draw line
        painter.setBrush(QBrush(self.color_body)) # Set brush color to create body 
        painter.drawRect(QRectF(self.x, min(self.o, self.c), 4, abs(self.o-self.c))) # Create body 
#######################################################################################################################