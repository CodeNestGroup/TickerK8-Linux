import pathlib # For get path to folders
import json # For json files
from PyQt5.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem,
    QToolTip,
    QSizePolicy
)
from PyQt5.QtGui import QPainter, QBrush, QPen, QFont
from PyQt5.QtCore import QRectF, Qt, QPointF
#######################################################################################################################
""" Candy chart """
class Candle_chart(QGraphicsView):
    def __init__(self, data, parent=None):
        super().__init__(parent)
#______________________________________________________________________________________________________________________
        """ Get data """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json')) # Get global config.
#______________________________________________________________________________________________________________________
        """ Config Graphic View """
        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
        """ Config Graphic scene """
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
#______________________________________________________________________________________________________________________
        """ Call addCandles function """
        self.addCandles(data)
#______________________________________________________________________________________________________________________
    """ Add Candles """
    def addCandles(self, data):
        _x = 0
        for single_data in data:
            _date = single_data['d']
            _open = single_data['o']
            _high = single_data['h']
            _close = single_data['c']
            _low = single_data['l']
            _vol = single_data['v']
            candle = Candle(_x, _open, _high, _close, _low)
            _x += 3
            self.scene.addItem(candle)
        
        self.setSceneRect(rect)
        self.fitInView(rect, Qt.KeepAspectRatio)
#______________________________________________________________________________________________________________________
    """ Wheel event """
    def wheelEvent(self, event):
        zoom_factor = 1.15 if event.angleDelta().y() > 0 else 1 / 1.15
        self.scale(zoom_factor, zoom_factor)
#######################################################################################################################
""" Single Candle """
class Candle(QGraphicsItem):
    def __init__(self, x, o, h, c, l):
        super().__init__()
        self.x = x
        self.o = o 
        self.h = h
        self.c = c 
        self.l = l
        self.setAcceptHoverEvents(True)
        self.setToolTip(f'Open: {o}\nHigh: {h}\nClose: {c}\nLow: {l}')

    def boundingRect(self):
        return QRectF(self.x - 3, min(self.o, self.c), 6, abs(self.o - self.c) + abs(self.h - max(self.o, self.c)))

    def paint(self, painter, option, widget=None):
        color = Qt.green if self.c >= self.o else Qt.red
        painter.setPen(QPen(color, 1))
        # Wick
        painter.drawLine(QPointF(self.x, self.h), QPointF(self.x, self.l))
        # Body
        painter.setBrush(QBrush(color))
        painter.drawRect(QRectF(self.x - 2, min(self.o, self.c), 4, abs(self.c - self.o)))

    def hoverEnterEvent(self, event):
        # Podświetlenie na hover
        QToolTip.showText(event.screenPos(), self.toolTip())
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        QToolTip.hideText()
        super().hoverLeaveEvent(event)
#######################################################################################################################