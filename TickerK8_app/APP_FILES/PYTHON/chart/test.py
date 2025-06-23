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

    """Podstawy QGraphicsView i powiązanych klas w PyQt5
1. Dlaczego QGraphicsView?
Kiedy masz dużo elementów do wyświetlenia i chcesz je dynamicznie przesuwać, skalować, klikać, animować — klasyczne widgety (np. wiele QLabel, QWidget itd.) mogą być za wolne i nieefektywne.

QGraphicsView to specjalny framework do rysowania i zarządzania dużą liczbą elementów graficznych (wektorowych), które mogą być interaktywne i efektywnie renderowane.

2. Trzy podstawowe elementy systemu
a) QGraphicsView — Widok
To widget, który widzi i pokazuje część sceny.

Możesz go umieścić gdziekolwiek w GUI.

Odpowiada za wyświetlanie, obsługę zdarzeń (zoom, drag), transformacje (skalowanie, obrót).

b) QGraphicsScene — Scena
To miejsce, gdzie trzymasz wszystkie obiekty graficzne (QGraphicsItem).

Zarządza geometrią, kolejkowaniem rysowania, selekcją.

Jest jak "płótno" lub "świat", na którym operujesz.

c) QGraphicsItem — Element
Podstawowy element rysowany na scenie.

Możesz go dowolnie modyfikować: rysować, przesuwać, reagować na zdarzenia.

Może reprezentować np. pojedynczą świeczkę, linię, obraz, tekst itd.

3. Jak to działa w praktyce?
Tworzysz QGraphicsScene i dodajesz do niej wiele QGraphicsItem.

Tworzysz QGraphicsView i ustawiasz scenę (setScene()).

QGraphicsView pokazuje fragment sceny (możesz ją przesuwać i skalować).

Kiedy coś zmieniasz w scenie lub itemach, QGraphicsView odświeża tylko potrzebne części ekranu.

4. Rysowanie i interakcja
QGraphicsItem definiujesz przez nadpisanie metod:

boundingRect() — prostokąt zajmowany przez element (niezbędne dla optymalizacji).

paint(painter, option, widget) — tutaj rysujesz element (np. świeczkę) przy pomocy QPainter.

Możesz przechwytywać zdarzenia, np. kliknięcia, najechanie myszką:

mousePressEvent

hoverEnterEvent

hoverLeaveEvent

itp.

5. Transformacje i zoom
QGraphicsView pozwala na łatwe skalowanie widoku (scale()), obrót i przesuwanie (scroll, drag).

To działa na całą scenę i automatycznie "przesuwa" widok po elementach.

Daje to płynną i wydajną obsługę np. zoomu wykresów.

6. Zalety używania QGraphicsView
Wysoka wydajność — renderuje tylko to, co widzisz.

Elastyczność — możesz tworzyć dowolne, złożone elementy.

Wbudowana obsługa interakcji.

Skalowalność i precyzja dzięki grafice wektorowej.

Łatwe zarządzanie wieloma elementami na raz.

Mały przykład — najprostszy QGraphicsView z elementem
python
Copy
Edit
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import QRectF, Qt
import sys

class MyRectItem(QGraphicsItem):
    def boundingRect(self):
        return QRectF(0, 0, 100, 100)

    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(Qt.blue))
        painter.drawRect(0, 0, 100, 100)

app = QApplication(sys.argv)
scene = QGraphicsScene()
scene.addItem(MyRectItem())

view = QGraphicsView(scene)
view.show()
sys.exit(app.exec_())
W tym przykładzie:

Tworzymy prostokąt (MyRectItem) jako QGraphicsItem.

Dodajemy go do sceny.

Ustawiamy scenę w widoku.

Pojawia się okno z niebieskim kwadratem, który możesz przesuwać, skalować itd. (jak dodasz obsługę).

Podsumowanie i dalsze kroki
Poznaj QGraphicsItem: naucz się pisać własne elementy z metodami paint i boundingRect.

Ćwicz tworzenie scen i widoków — dodawaj wiele elementów, testuj przesuwanie i zoom.

Dodaj interakcje — obsługuj kliknięcia i hover.

Zaimplementuj wykresy — zacznij od prostych linii, potem świeczki.

"""
