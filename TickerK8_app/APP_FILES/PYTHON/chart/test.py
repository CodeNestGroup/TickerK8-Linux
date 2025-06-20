from PyQt5.QtWidgets import (
    QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QMainWindow
)
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import QRectF, Qt, QPointF
import sys


class CandlestickItem(QGraphicsItem):
    def __init__(self, data):
        super().__init__()
        self.data = data  # lista (x, open, high, low, close)

    def boundingRect(self):
        # Wyliczamy zakres wykresu dynamicznie
        if not self.data:
            return QRectF()
        x_vals = [x for x, *_ in self.data]
        low_vals = [low for *_, low, _ in self.data]
        high_vals = [high for *_, high, _, _ in self.data]
        min_x, max_x = min(x_vals), max(x_vals)
        min_y, max_y = min(low_vals), max(high_vals)
        margin = 10
        return QRectF(min_x - 5, min_y - margin, (max_x - min_x) + 10, (max_y - min_y) + 2 * margin)

    def paint(self, painter, option, widget=None):
        for (x, o, h, l, c) in self.data:
            color = Qt.green if c >= o else Qt.red
            painter.setPen(QPen(color, 1))
            # Wick
            painter.drawLine(QPointF(x, h), QPointF(x, l))
            # Body
            painter.setBrush(QBrush(color))
            rect = QRectF(x - 2, min(o, c), 4, abs(c - o))
            painter.drawRect(rect)


class CandlestickChart(QGraphicsView):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.candles = CandlestickItem(data)
        self.scene.addItem(self.candles)
        self.fitInView(self.candles.boundingRect(), Qt.KeepAspectRatio)

    def wheelEvent(self, event):
        zoom_factor = 1.15 if event.angleDelta().y() > 0 else 1 / 1.15
        self.scale(zoom_factor, zoom_factor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Wykres Świeczkowy - PyQt5")
    window.resize(1000, 600)

    sample_data = [
        (10, 100, 110, 90, 105),
        (20, 105, 115, 100, 95),
        (30, 95, 100, 90, 97),
        (40, 97, 105, 95, 100),
        (50, 100, 110, 98, 108),
        (60, 108, 112, 107, 107),
        (70, 107, 115, 100, 102),
    ]

    chart = CandlestickChart(sample_data)
    window.setCentralWidget(chart)
    window.show()
    sys.exit(app.exec_())
