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
        self.data = data
#______________________________________________________________________________________________________________________
        """ Set dafoult """
        self.max_price = None
        self.min_price = None
        self.max_min_difference = None
        self.resized_value = None 
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
    """ Set scale """
    def set_scale(self):
        for single_data in self.data:
            if not self.max_price:
                self.max_price = single_data['h']
            elif single_data['h'] >= self.max_price:
                self.max_price = single_data['h']
            if not self.min_price:
                self.min_price = single_data['l']
            elif single_data['l'] <= self.min_price:
                self.min_price = single_data['l']
        self.max_min_difference = self.max_price-self.min_price
        return ((self.height()-(self.global_config['charts_config'][0]['y_margin']*2))/self.max_min_difference)/10**len(str(self.max_price).split('.')[-1] if '.' in str(self.max_price) else 1)
#______________________________________________________________________________________________________________________
    """ Add Candles """
    def add_Candles(self):
        _x = 0
        _space_between = self.global_config['charts_config'][0]['space_between']
        _scale = self.set_scale()
        for single_data in self.data:
            _date = single_data['d'] # Get candle date
            _open = single_data['o'] # Get candle open price
            _high = single_data['h'] # Get candle highest price
            _close = single_data['c'] # Get candle close price
            _low = single_data['l'] # Get candle lowest price
            _vol = single_data['v'] # Get candle volume value
            _color_wick = QColor(self.global_config['charts_config'][0]['+_border']) if _close >= _open else QColor(self.global_config['charts_config'][0]['-_border'])
            _color_body = QColor(self.global_config['charts_config'][0]['+_body']) if _close >= _open else QColor(self.global_config['charts_config'][0]['-_body'])
            candle = Candle(_x, _scale, _open, _high, _close, _low, _color_wick, _color_body)
            _x += _space_between
            self.scene.addItem(candle)
        rect = QRectF(0, self.global_config['charts_config'][0]['y_margin'], _x+self.global_config['charts_config'][0]['x_margin'], int(self.height()-(self.global_config['charts_config'][0]['y_margin']*2)))
        self.setSceneRect(rect)
        self.fitInView(QRectF(_x-200, self.global_config['charts_config'][0]['y_margin'], self.width(), int(self.height()-(self.global_config['charts_config'][0]['y_margin']*2))), Qt.KeepAspectRatio)
#______________________________________________________________________________________________________________________
    """ Wheel event """
    def wheelEvent(self, event):
        zoom_factor = 1.15 if event.angleDelta().y() > 0 else 1 / 1.15
        self.scale(zoom_factor, zoom_factor)
#______________________________________________________________________________________________________________________
    """ Reszie event """
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if not self.resized_value:
            """ Call add Candles function """
            self.add_Candles()
            self.resized_value = True

#######################################################################################################################
""" Single Candle """
class Candle(QGraphicsItem):
    def __init__(self, x, scale, o, h, c, l, color_wick, color_body):
        super().__init__()
        self.x = x # X axis start
        self.scale = scale # Scale 
        self.o = o # Open pirce
        self.h = h # High price
        self.c = c # Close price
        self.l = l # Low price
        self.color_wick = color_wick # Color wick
        self.color_body = color_body # Color body 
        self.setAcceptHoverEvents(True)
        self.setToolTip(f'Open: {o}\nHigh: {h}\nClose: {c}\nLow: {l}')

    def boundingRect(self):
        print(self.scale, self.o, self.h, self.c, self.l, '\n', self.o*self.scale, int(self.o*self.scale))
        return QRectF(self.x, int(self.h*self.scale), 4, int(abs(self.h-self.l)*self.scale))

    def paint(self, painter, option, widget=None):
        painter.setPen(QPen(self.color_wick, 1))
        # Wick
        painter.drawLine(QPointF(self.x+2, int(self.h*self.scale)), QPointF(self.x+2, int(self.l*self.scale)))
        # Body
        painter.setBrush(QBrush(self.color_body))
        painter.drawRect(QRectF(self.x, int(max(self.o, self.c)*self.scale), 4, int(abs(self.o-self.c)*self.scale)))

    def hoverEnterEvent(self, event):
        # Podświetlenie na hover
        QToolTip.showText(event.screenPos(), self.toolTip())
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        QToolTip.hideText()
        super().hoverLeaveEvent(event)
#######################################################################################################################