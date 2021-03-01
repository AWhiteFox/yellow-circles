import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.pressed.connect(self.paint)
        self.do_paint = False
        self.color = QColor('yellow')
        self.circles = []

    def paintEvent(self, event):
        if not self.do_paint:
            return

        qp = QPainter()
        qp.begin(self)
        qp.setPen(self.color)
        qp.setBrush(self.color)
        for x, y, r in self.circles:
            qp.drawEllipse(x, y, r, r)
        qp.end()

    def paint(self):
        self.do_paint = True
        self.generate_circles()
        self.repaint()

    def generate_circles(self):
        self.circles.clear()
        fw = self.size().width()
        fh = self.size().height()
        for _ in range(randint(1, 10)):
            r = randint(50, min(fw, fh) // 4)
            x = randint(0, fw - r)
            y = randint(0, fh - r)
            self.circles.append((x, y, r))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
