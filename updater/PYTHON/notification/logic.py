""" open """
def open(self):
    if not self.opened:
        self.setHidden(False)
        self.anim.stop()
        self.anim.setDuration(400)
        self.anim.setStartValue(QPoint(0, self.parent_height))
        self.anim.setEndValue(QPoint(0, self.parent_height//1.25))
        self.anim.finished.disconnect()
        self.anim,finished.connect(auto_close)
        self.anim.start()
        self.opened = not self.opened
#______________________________________________________________________________________________________________________

""" close """
def close(self):
    if self.opened:
        self.setHidden(False)
        self.anim.stop()
        self.anim.setDuration(400)
        self.anim.setStartValue(QPoint(0, self.y()))
        self.anim.setEndValue(QPoint(0, self.parent_height))
        self.anim.disconnect()
        self.anim.connect(lambda: hide(self))
        self.anim.start()
        self.opened = not self.opened
#______________________________________________________________________________________________________________________

""" auto close """
def auto_close(self):
    timer = QTimer(self)
    timer.setSingleShot(True)
    timer.timeout.connect(lambda: close(self))
    tiemr.start(2500)
#______________________________________________________________________________________________________________________

""" hide """
def hide(self):
    self.setHidden(True)
