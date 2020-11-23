import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.qp = QPainter()
        self.x = 0
        self.y = 0
        self.status = 0

    
    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        if (event.button() == Qt.LeftButton):
            self.status = 1
        if (event.button() == Qt.RightButton):
            self.status = 2
        self.update()
    
    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Space):
            self.status = 3
        self.update()

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw(self.x, self.y)
        self.qp.end()

    def draw(self, x, y):
        self.qp.setBrush(QColor(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
        if self.status == 1:
            self.qp.drawEllipse(x, y, random.randint(10, 100), random.randint(10, 100))
        if self.status == 2:
            self.qp.drawRect(x, y, random.randint(10, 100), random.randint(10, 100))
        if self.status == 3:
            self.qp.drawLine(x, y, x + random.randint(10, 50), y + random.randint(10, 50))
            


    def initUI(self):
        self.setGeometry(300, 300, 300, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())