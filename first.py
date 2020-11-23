import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.qp = QPainter()
        self.status = 0
        self.setMouseTracking(True)
        self.btn = QPushButton('haha', self)
        self.btn.clicked.connect(self.haha)

    def haha(self):
        self.status = 1
        self.update()

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw()
        self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(random.randint(0, 255),
                                random.randint(0, 255), random.randint(0, 255)))
        if self.status == 1:
            self.qp.drawEllipse(random.randint(10, 200), random.randint(
                10, 200), random.randint(10, 200), random.randint(10, 200))
        self.status = 0

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
