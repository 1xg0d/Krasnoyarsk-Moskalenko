import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.connection = sqlite3.connect("films_db.sqlite")
        self.pushButton.clicked.connect(self.select_data)
        # По умолчанию будем выводить все данные из таблицы films
        self.params = {"Год выпуска": "year","Название": "title", "Продолжительность": "duration"}
        self.comboBox.addItems(list(self.params.keys()))

    def select_data(self):
        # Получим результат запроса, 
        # который ввели в текстовое поле
        query = f'SELECT * FROM films WHERE {self.params[self.comboBox.currentText()]} = {self.lineEdit.text()}'
        res = self.connection.cursor().execute(query).fetchone()
        self.lineEdit_2.setText(str(res[0]))
        self.lineEdit_3.setText(res[1])
        self.lineEdit_4.setText(str(res[2]))
        self.lineEdit_5.setText(str(res[3]))
        self.lineEdit_6.setText(str(res[4]))
        # Заполним размеры таблицы
        # Заполняем таблицу элементами

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение 
        # с базой данных
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())