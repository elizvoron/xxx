import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow
from PyQt5.QtGui import QPixmap, QFont
import sqlite3


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(250, 200, 400, 350)
        self.setWindowTitle('Знакомство с человечком)')

        self.pixmap = QPixmap("фон1")
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(500, 450)
        self.image.setPixmap(self.pixmap)

        self.btn = QPushButton('OK', self)
        font = QFont("Times", 12, QFont.Bold)
        self.btn.setFont(font)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 300)
        self.btn.clicked.connect(self.hello)
        self.btn.clicked.connect(self.open_second_form)

        self.label = QLabel(self)
        self.label.setFont(QFont("Times", 14, QFont.Bold))
        self.label.setText("Здравствуй!")
        self.label.adjustSize()
        self.label.move(40, 20)

        self.label = QLabel(self)
        self.label.setFont(QFont("Times", 12, QFont.Bold))
        self.label.setText("Ты кто?")
        self.label.move(40, 50)

        self.name_label = QLabel(self)
        self.name_label.setFont(QFont("Times", 10, QFont.Bold))
        self.name_label.setText("Фамилия: ")
        self.name_label.move(40, 80)

        self.name_inputsn = QLineEdit(self)
        self.name_inputsn.move(150, 80)

        self.name_label = QLabel(self)
        self.name_label.setFont(QFont("Times", 10, QFont.Bold))
        self.name_label.setText("Имя: ")
        self.name_label.move(40, 110)

        self.name_inputn = QLineEdit(self)
        self.name_inputn.move(150, 110)

        self.name_label = QLabel(self)
        self.name_label.setFont(QFont("Times", 10, QFont.Bold))
        self.name_label.setText("Отчество: ")
        self.name_label.move(40, 140)

        self.name_inputfn = QLineEdit(self)
        self.name_inputfn.move(150, 140)

        self.name_label = QLabel(self)
        self.name_label.setFont(QFont("Times", 10, QFont.Bold))
        self.name_label.setText("Выбирите тест:")
        self.name_label.move(40, 210)

        self.btn1 = QPushButton('Природа', self)
        font = QFont("Times", 9, QFont.Bold)
        self.btn1.setFont(font)
        self.btn1.resize(self.btn.sizeHint())
        self.btn1.adjustSize()
        self.btn1.move(180, 180)
        self.btn1.clicked.connect(self.nach)

        self.btn2 = QPushButton('Математика', self)
        font = QFont("Times", 9, QFont.Bold)
        self.btn2.setFont(font)
        self.btn2.resize(self.btn.sizeHint())
        self.btn2.adjustSize()
        self.btn2.move(180, 210)
        self.btn2.clicked.connect(self.mat)

        self.btn3 = QPushButton('Яндекс.Лицей)', self)
        font = QFont("Times", 9, QFont.Bold)
        self.btn3.setFont(font)
        self.btn3.resize(self.btn.sizeHint())
        self.btn3.adjustSize()
        self.btn3.move(175, 240)
        self.btn3.clicked.connect(self.yan)

    def hello(self):
        self.name = self.name_inputn.text()
        self.sname = self.name_inputsn.text()
        self.fname = self.name_inputfn.text()
        self.fii = str(self.sname + ' ' + self.name + ' ' + self.fname)
        con = sqlite3.connect("names.sqlite")
        cur = con.cursor()
        cur.execute(f'INSERT INTO name(fio) VALUES("{self.fii}")')
        con.commit()
        con.close()

    def yan(self):
        self.test = str('Яндекс.Лицей')

    def mat(self):
        self.test = 'Математика'

    def nach(self):
        self.test = 'Природа'

    # def keyPressEvent(self, event):
    # if event.key() == Qt.Key_Enter:
    # self.second_form = SecondForm()
    # self.second_form.show()

    def open_second_form(self):
        ts = self.test
        fi = self.fii
        con = sqlite3.connect("names.sqlite")
        cur = con.cursor()
        cur.execute(f"INSERT INTO tests(test, fi) SELECT '{ts}', id FROM name WHERE fio = '{fi}'")
        con.commit()
        con.close()
        self.second_form = SecondForm(self.name, self.test)
        self.second_form.show()


class SecondForm(QWidget):
    def __init__(self, a, b):
        super().__init__()
        self.initUI()
        self.n = a
        self.t = b
        self.num = 0
        self.answers = []
        if b == 'Математика':
            ts = open('ts_math.txt', encoding="utf8", mode='r').read().split('\n')
            self.quest = []
            self.answ = []
            for i in range(10):
                a = ts[i].split('$')
                self.quest.append(a[0])
                self.answ.append(a[-1])
        if b == 'Природа':
            ts = open('ts_nachh.txt', encoding="utf8", mode='r').read().split('\n')
            self.quest = []
            self.answ = []
            for i in range(10):
                a = ts[i].split('$')
                self.quest.append(a[0])
                self.answ.append(a[-1])
        if b == 'Яндекс.Лицей':
            ts = open('ts_yand.txt', encoding="utf8", mode='r').read().split('\n')
            self.quest = []
            self.answ = []
            for i in range(10):
                a = ts[i].split('$')
                self.quest.append(a[0])
                self.answ.append(a[-1])

    def initUI(self):
        self.setGeometry(600, 200, 700, 350)
        self.setWindowTitle('ТЕСТ')
        self.lbl = QLabel(self)
        self.lbl.adjustSize()

        self.pixmap = QPixmap("фон1")
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(700, 450)
        self.image.setPixmap(self.pixmap)

        self.label1 = QLabel(self)
        self.label1.setFont(QFont("Times", 14, QFont.Bold))
        self.label1.setText('И снова здравствуй!')
        self.label1.adjustSize()
        self.label1.move(40, 20)

        self.label2 = QLabel(self)
        self.label2.setFont(QFont("Times", 10, QFont.Bold))
        self.label2.setText(f"Ты проходишь тест )")
        self.label2.adjustSize()
        self.label2.move(40, 40)

        self.label3 = QLabel(self)
        self.label3.setFont(QFont("Times", 10, QFont.Bold))
        self.label3.setText("На все вопросы отвечай одним числом!")
        self.label3.adjustSize()
        self.label3.move(40, 60)

        self.btn = QPushButton('Начать!', self)
        font = QFont("Times", 12, QFont.Bold)
        self.btn.setFont(font)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(40, 300)
        self.btn.clicked.connect(self.questh)

        self.label4 = QLabel(self)
        self.label4.setFont(QFont("Times", 12, QFont.Bold))
        self.label4.setText('Вопросы:')
        self.label4.adjustSize()
        self.label4.move(40, 80)

        self.label3 = QLabel(self)
        self.label3.setFont(QFont("Times", 11, QFont.Bold))
        self.label3.setText("Ответ:")
        self.label3.adjustSize()
        self.label3.move(40, 100)

        self.ainput = QLineEdit(self)
        self.ainput.adjustSize()
        self.ainput.move(100, 100)

        self.btn1 = QPushButton('CLOSE', self)
        font = QFont("Times", 12, QFont.Bold)
        self.btn1.setFont(font)
        self.btn1.resize(self.btn.sizeHint())
        self.btn1.move(200, 300)
        self.btn1.clicked.connect(self.open_tr_form)

    def questh(self):
        self.btn.setText('NEXT')
        self.btn.resize(self.btn.sizeHint())
        a = self.ainput.text()
        if not a.isdigit() and a != '':
            raise ValueError
        try:
            if self.num < 10:
                self.label4.setText(f"{self.quest[self.num]}")
                self.label4.adjustSize()
            else:
                self.label4.setText(f"Всё)")
                self.label4.adjustSize()
            self.num += 1
            self.ainput.setText(f"")
            self.answers.append(a)
        except ValueError:
            self.label4.setText(f"{self.quest[self.num]}")
            self.label4.adjustSize()
            self.ainput.setText(f"")

    def open_tr_form(self):
        self.tr_form = TrForm(self.answers, self.answ)
        self.tr_form.show()


class TrForm(QWidget):
    def __init__(self, a, b):
        super().__init__()
        self.initUI()
        self.answw = b
        self.itt = a
        self.n = 0

    def initUI(self):
        self.setGeometry(600, 200, 400, 350)
        self.setWindowTitle('ИТОГ')
        self.lbl = QLabel(self)
        self.lbl.adjustSize()

        self.pixmap = QPixmap("фон1")
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(700, 450)
        self.image.setPixmap(self.pixmap)

        self.label1 = QLabel(self)
        self.label1.setFont(QFont("Times", 14, QFont.Bold))
        self.label1.setText('Привет)')
        self.label1.adjustSize()
        self.label1.move(40, 20)

        self.label2 = QLabel(self)
        self.label2.setFont(QFont("Times", 12, QFont.Bold))
        self.label2.setText(f"Твой результат:")
        self.label2.adjustSize()
        self.label2.move(40, 40)

        self.btn = QPushButton('Посмотреть>', self)
        font = QFont("Times", 10, QFont.Bold)
        self.btn.setFont(font)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(40, 60)
        self.btn.clicked.connect(self.itg)

        self.label2 = QLabel(self)
        self.label2.setFont(QFont("Times", 15, QFont.Bold))
        self.label2.setText(f" ")
        self.label2.adjustSize()
        self.label2.move(40, 100)

    def itg(self):
        for i in range(len(self.answw)):
            if int(self.answw[i]) == int(self.itt[i]):
                self.n += 1
        self.n *= 10
        vv = str(self.n) + '%'
        self.label2.setText(f"{vv}")
        self.label2.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
