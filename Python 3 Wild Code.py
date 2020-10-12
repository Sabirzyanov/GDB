from PyQt5.QtWidgets import QApplication, \
    QWidget, \
    QTableWidget, QTableWidgetItem, QPushButton, QLabel, QLineEdit, QSpinBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sqlite3 as lite
import sqlite3 as db
import sys


class Project(QWidget):
    def __init__(self):
        # Parameters
        super().__init__()

        self.setGeometry(10, 70, 870, 600)
        self.setWindowTitle('Чтение базы')

        # Buttons
        self.open_table1 = QPushButton('Открыть', self)
        self.open_table1.move(0, 15)
        self.open_table1.clicked.connect(self.run_first_table)

        self.search = QPushButton('Поиск', self)
        self.search.move(230, 15)
        self.search.clicked.connect(self.second_window_name)

        self.open_table2 = QPushButton('Открыть вторую', self)
        self.open_table2.move(100, 15)
        self.open_table2.clicked.connect(self.open_three_window)

        self.update_button = QPushButton('Изменить', self)
        self.update_button.move(350, 15)
        self.update_button.clicked.connect(self.update_form)

        # Table
        self.table1 = QTableWidget(self)
        self.table1.setColumnCount(4)
        self.table1.setRowCount(100)
        self.table1.setMaximumWidth(530)
        self.table1.move(10, 80)
        self.table1.setFixedSize(500, 400)
        self.table1.setHorizontalHeaderLabels(["ID", "SURNAME", "NAME", "PATHRONYMIC"])

    def run_first_table(self):
        # Run table
        self.con = lite.connect('BD_ProjectY.db')
        with self.con:
            cur = self.con.cursor()
            rows = cur.execute("SELECT * FROM MAIN").fetchall()
            k = 0
            for row in rows:
                a = list(row)
                # Устанавливаем выравнивание на заголовки
                self.table1.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
                self.table1.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
                self.table1.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

                # заполняем  строки
                for i in range(len(a)):
                    if i != 0:
                        self.table1.setItem(k, i, QTableWidgetItem(a[i]))
                    else:
                        self.table1.setItem(k, i, QTableWidgetItem(str(a[i])))
                k = k + 1
                # делаем ресайз колонок по содержимому
                self.table1.resizeColumnsToContents()
                self.con.commit()
        if self.con:
            self.con.close()

    # Forms
    def second_window_name(self):
        # Open second form
        self.second_form = Second_Window(self, "Данные для второй формы")
        self.second_form.show()

    def open_three_window(self):
        self.table2 = Table_2(self)
        self.table2.show()

    def update_form(self):
        self.update_window = Update()
        self.update_window.show()


# Second Form
class Second_Window(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        # Parameters
        self.setGeometry(20, 80, 1000, 600)
        self.setWindowTitle('Поиск')

        # Labels
        self.Label_N = QLabel(self)
        self.Label_N.move(15, 15)
        self.Label_N.setText('Name: ')
        self.Label_N.setFont(QFont('Ariel', 17))

        self.Label_S = QLabel(self)
        self.Label_S.move(15, 120)
        self.Label_S.setText('Surname: ')
        self.Label_S.setFont(QFont('Ariel', 17))

        self.Label_P = QLabel(self)
        self.Label_P.move(15, 240)
        self.Label_P.setText('Pathronymic: ')
        self.Label_P.setFont(QFont('Ariel', 17))

        # LineEdit's
        self.Name_Edit = QLineEdit(self)
        self.Name_Edit.move(15, 50)
        self.Name_Edit.setFont(QFont('Ariel', 14))
        self.Name_Edit.resize(450, 40)

        self.Surname_Edit = QLineEdit(self)
        self.Surname_Edit.move(15, 155)
        self.Surname_Edit.setFont(QFont('Ariel', 14))
        self.Surname_Edit.resize(450, 40)

        self.Pathronymic_Edit = QLineEdit(self)
        self.Pathronymic_Edit.move(15, 280)
        self.Pathronymic_Edit.setFont(QFont('Ariel', 14))
        self.Pathronymic_Edit.resize(450, 40)

        # Table
        self.table_search_name = QTableWidget(self)
        self.table_search_name.move(510, 15)
        self.table_search_name.setColumnCount(4)
        self.table_search_name.setRowCount(100)
        self.table_search_name.setMaximumWidth(530)
        self.table_search_name.resize(450, 500)
        self.table_search_name.setHorizontalHeaderLabels(["ID", "SURNAME", "NAME", "PATHRONYMIC"])

        # Buttons
        self.search_button_name = QPushButton('Поиск', self)
        self.search_button_name.move(100, 15)
        self.search_button_name.setFont(QFont('Ariel', 14))
        self.search_button_name.clicked.connect(self.run_table_name)

        self.search_button_surname = QPushButton('Поиск', self)
        self.search_button_surname.move(125, 120)
        self.search_button_surname.setFont(QFont('Ariel', 14))
        self.search_button_surname.clicked.connect(self.run_table_surname)

        self.search_button_pathronymic = QPushButton('Поиск', self)
        self.search_button_pathronymic.move(155, 240)
        self.search_button_pathronymic.setFont(QFont('Ariel', 14))
        self.search_button_pathronymic.clicked.connect(self.run_table_pathronymic)

    def run_table_name(self):
        # Run table
        self.con = lite.connect('BD_ProjectY.db')
        with self.con:
            cur = self.con.cursor()
            rows = cur.execute("SELECT * from MAIN WHERE NAME = ?",
                               (self.Name_Edit.text(), )).fetchall()
            k = 0
            for row in rows:
                a = list(row)
                # Устанавливаем выравнивание на заголовки
                self.table_search_name.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
                self.table_search_name.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
                self.table_search_name.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

                # заполняем  строки
                for i in range(len(a)):
                    if i != 0:
                        self.table_search_name.setItem(k, i, QTableWidgetItem(a[i]))
                    else:
                        self.table_search_name.setItem(k, i, QTableWidgetItem(str(a[i])))
                k = k + 1
                # делаем ресайз колонок по содержимому
                self.table_search_name.resizeColumnsToContents()
        if self.con:
            self.con.close()

    def run_table_surname(self):
        # Run table
        self.con = lite.connect('BD_ProjectY.db')
        with self.con:
            cur = self.con.cursor()
            rows = cur.execute("SELECT * from MAIN WHERE SURNAME = ?",
                               (self.Surname_Edit.text(), )).fetchall()
            k = 0
            for row in rows:
                a = list(row)
                # Устанавливаем выравнивание на заголовки
                self.table_search_name.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
                self.table_search_name.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
                self.table_search_name.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

                # заполняем  строки
                for i in range(len(a)):
                    if i != 0:
                        self.table_search_name.setItem(k, i, QTableWidgetItem(a[i]))
                    else:
                        self.table_search_name.setItem(k, i, QTableWidgetItem(str(a[i])))
                k = k + 1
                # делаем ресайз колонок по содержимому
                self.table_search_name.resizeColumnsToContents()
        if self.con:
            # self.cur.close()
            self.con.close()

    def run_table_pathronymic(self):
        # Run table
        self.con = lite.connect('BD_ProjectY.db')
        with self.con:
            cur = self.con.cursor()
            rows = cur.execute("SELECT * from MAIN WHERE PATHRONYMIC = ?",
                               (self.Pathronymic_Edit.text(), )).fetchall()
            k = 0
            for row in rows:
                a = list(row)
                # Устанавливаем выравнивание на заголовки
                self.table_search_name.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
                self.table_search_name.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
                self.table_search_name.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

                # заполняем  строки
                for i in range(len(a)):
                    if i != 0:
                        self.table_search_name.setItem(k, i, QTableWidgetItem(a[i]))
                    else:
                        self.table_search_name.setItem(k, i, QTableWidgetItem(str(a[i])))
                k = k + 1
                # делаем ресайз колонок по содержимому
                self.table_search_name.resizeColumnsToContents()
        if self.con:
            self.con.close()


class Update(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(20, 80, 870, 600)
        self.setWindowTitle('Изменение')

        self.ID = QLabel(self)
        self.ID.move(15, 20)
        self.ID.setText('ID: ')
        self.ID.setFont(QFont('Ariel', 17))

        self.update_box = QSpinBox(self)
        self.update_box.move(50, 20)
        self.update_box.resize(800, 30)
        self.update_box.setFont(QFont('Ariel', 17))

        # Buttons
        self.download_button = QPushButton('Загрузить', self)
        self.download_button.move(15, 60)
        self.download_button.resize(850, 40)
        self.download_button.clicked.connect(self.update_result)

        self.save_button = QPushButton('Сохранить', self)
        self.save_button.move(15, 120)
        self.save_button.resize(850, 40)
        self.save_button.clicked.connect(self.save_results)

        # Table
        self.table = QTableWidget(self)
        self.table.move(15, 180)
        self.table.setColumnCount(4)
        self.table.setRowCount(100)
        self.table.setMaximumWidth(530)
        self.table.resize(900, 300)
        self.table.setHorizontalHeaderLabels(["ID", "SURNAME", "NAME", "PATHRONYMIC"])
        self.table.itemChanged.connect(self.item_changed)

        self.con = lite.connect('BD_ProjectY.db')

        self.modified = {}
        self.titles = None

    def update_result(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("Select * from MAIN WHERE ID=?",
                             (self.update_box.text(),)).fetchall()
        # Заполнили размеры таблицы
        self.table.setRowCount(len(result))
        self.table.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        # Если значение в ячейке было изменено,
        # то в словарь записывается пара: название поля, новое значение
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE MAIN SET\n"
            for key in self.modified.keys():
                que += "{}='{}'\n".format(key, self.modified.get(key))
            que += "WHERE ID = ?"
            cur.execute(que, (self.update_box.text(),))
            self.con.commit()


class Table_2(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(20, 80, 870, 600)
        self.setWindowTitle('Вторая таблица')

        # Buttons
        self.open_table = QPushButton('Открыть', self)
        self.open_table.move(0, 15)
        self.open_table.clicked.connect(self.run_second_table)

        self.update_button = QPushButton('Изменить', self)
        self.update_button.move(125, 15)
        self.update_button.clicked.connect(self.update_table_2)

        # Table
        self.table1 = QTableWidget(self)
        self.table1.setColumnCount(4)
        self.table1.setRowCount(100)
        self.table1.setMaximumWidth(530)
        self.table1.move(10, 80)
        self.table1.setFixedSize(500, 400)
        self.table1.setHorizontalHeaderLabels(["ID", "BIRTHDAY", "PROFESSION", "ADRESS"])

    def run_second_table(self):
        # Run table
        self.con = lite.connect('BD_ProjectY.db')
        with self.con:
            cur = self.con.cursor()
            rows = cur.execute("SELECT * FROM Table2").fetchall()
            k = 0
            for row in rows:
                a = list(row)
                # Устанавливаем выравнивание на заголовки
                self.table1.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
                self.table1.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
                self.table1.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

                # заполняем  строки
                for i in range(len(a)):
                    if i != 0:
                        self.table1.setItem(k, i, QTableWidgetItem(a[i]))
                    else:
                        self.table1.setItem(k, i, QTableWidgetItem(str(a[i])))
                k = k + 1
                # делаем ресайз колонок по содержимому
                self.table1.resizeColumnsToContents()
                self.con.commit()
        if self.con:
            self.con.close()

    def update_table_2(self):
        self.update_table = Update_Table2()
        self.update_table.show()


class Update_Table2(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(20, 80, 870, 600)
        self.setWindowTitle('Изменение')

        self.ID = QLabel(self)
        self.ID.move(15, 20)
        self.ID.setText('ID: ')
        self.ID.setFont(QFont('Ariel', 17))

        self.update_box = QSpinBox(self)
        self.update_box.move(50, 20)
        self.update_box.resize(800, 30)
        self.update_box.setFont(QFont('Ariel', 17))

        # Buttons
        self.download_button = QPushButton('Загрузить', self)
        self.download_button.move(15, 60)
        self.download_button.resize(850, 40)
        self.download_button.clicked.connect(self.update_result)

        self.save_button = QPushButton('Сохранить', self)
        self.save_button.move(15, 120)
        self.save_button.resize(850, 40)
        self.save_button.clicked.connect(self.save_results)

        # Table
        self.table = QTableWidget(self)
        self.table.move(15, 180)
        self.table.setColumnCount(4)
        self.table.setRowCount(100)
        self.table.setMaximumWidth(530)
        self.table.resize(900, 300)
        self.table.setHorizontalHeaderLabels(["ID", "BIRTHDAY", "PROFESSION", "ADRESS"])
        self.table.itemChanged.connect(self.item_changed)

        self.con = lite.connect('BD_ProjectY.db')

        self.modified = {}
        self.titles = None

    def update_result(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("Select * from Table2 WHERE ID=?",
                             (self.update_box.text(),)).fetchall()
        # Заполнили размеры таблицы
        self.table.setRowCount(len(result))
        self.table.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        # Если значение в ячейке было изменено,
        # то в словарь записывается пара: название поля, новое значение
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE Table2 SET\n"
            for key in self.modified.keys():
                que += "{}='{}'\n".format(key, self.modified.get(key))
            que += "WHERE ID = ?"
            cur.execute(que, (self.update_box.text(),))
            self.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    project = Project()
    project.show()
    sys.exit(app.exec())
