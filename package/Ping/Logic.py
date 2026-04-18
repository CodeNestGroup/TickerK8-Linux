#   --- Import PySide6 ---
from PySide6.QtCore import (
    QObject,
    QTimer,
    Signal,
    Slot
)

#   --- PingO ---

class PingO(QObject):
    Status = Signal(bool)
    def __init__(self):
        self.Timer = QTimer()
        self.Timer.timeout.connect(self.Check)
        self.Timer.start(5000)

    @Slot()
    def Check(self):
        try:
            r = requests.get('https://api.github.com', timeout=3)
            self.Status.emit(True)
        except Exception as e:
            self.Status.emit(False)
