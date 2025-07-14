import pathlib # For get path to folders
import json # For json files
from PyQt5.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem,
    QToolTip,
    QSizePolicy
)
from PyQt5.QtGui import QPainter, QBrush, QPen, QFont, QColor
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
        """ Set dafoult """
        self.max_price = None
        self.min_price = None
        self.max_min_difference = None
        self.scale = None 
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
        self.scene.setObjectName('main_chart_graphics_scene')
        self.setScene(self.scene)
#______________________________________________________________________________________________________________________
        """ Call set scale function """
        self.set_scale(data, parent)
#______________________________________________________________________________________________________________________
        """ Call add Candles function """
        self.add_Candles(data)
#______________________________________________________________________________________________________________________
    """ Set scale """
    def set_scale(self, data, parent):
        for single_data in data:
            if not self.max_price:
                self.max_price = single_data['h']
            elif single_data['h'] >= self.max_price:
                self.max_price = single_data['h']

            if not self.min_price:
                self.min_price = single_data['l']
            elif single_data['l'] <= self.min_price:
                self.min_price = single_data['l']
        self.max_min_difference = self.max_price-self.min_price
        self.scale = None 
#______________________________________________________________________________________________________________________
    """ Add Candles """
    def add_Candles(self, data):
        _x = 0
        _space_between = self.global_config['charts_config'][0]['space_between']
        for single_data in data:
            _date = single_data['d']
            _open = single_data['o']
            _high = single_data['h']
            _close = single_data['c']
            _low = single_data['l']
            _vol = single_data['v']
            _color_wick = QColor(self.global_config['charts_config'][0]['+_border']) if _close >= _open else QColor(self.global_config['charts_config'][0]['-_border'])
            _color_body = QColor(self.global_config['charts_config'][0]['+_body']) if _close >= _open else QColor(self.global_config['charts_config'][0]['-_body'])
            candle = Candle(_x, _open, _high, _close, _low, _color_wick, _color_body)
            _x += _space_between
            self.scene.addItem(candle)
        rect = QRectF(0, self.global_config['charts_config'][0]['y_margin'], _x+self.global_config['charts_config'][0]['x_margin'], 600-self.global_config['charts_config'][0]['y_margin'])
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
    def __init__(self, x, o, h, c, l, color_wick, color_body):
        super().__init__()
        self.x = x # X axis start
        self.o = o # Open pirce
        self.h = h # High price
        self.c = c # Close price
        self.l = l # Low price
        self.color_wick = color_wick # Color wick
        self.color_body = color_body # Color body 
        self.setAcceptHoverEvents(True)
        self.setToolTip(f'Open: {o}\nHigh: {h}\nClose: {c}\nLow: {l}')

    def boundingRect(self):
        return QRectF(self.x, self.h, 4, abs(self.h-self.l))

    def paint(self, painter, option, widget=None):
        painter.setPen(QPen(self.color_wick, 1))
        # Wick
        painter.drawLine(QPointF(self.x+2, self.h), QPointF(self.x+2, self.l))
        # Body
        painter.setBrush(QBrush(self.color_body))
        painter.drawRect(QRectF(self.x, max(self.o, self.c), 4, abs(self.o-self.c)))

    def hoverEnterEvent(self, event):
        # Podświetlenie na hover
        QToolTip.showText(event.screenPos(), self.toolTip())
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        QToolTip.hideText()
        super().hoverLeaveEvent(event)
#######################################################################################################################