import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow
from PyQt5.QtGui import QPixmap, QFont
import sqlite3


# TODO КОМЕНТАРИИ!


class FirstForm(QMainWindow):  # Первый класс, выводящий первое окно.
    def __init__(self):
        super().__init__()
        self.initUI()
        self.test = False
        self.fii = False

    def initUI(self):  # Структура первого окна.
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

    def hello(self):  # Обработка "ОК", проверка на введённые данные.
        self.name = self.name_inputn.text()
        self.sname = self.name_inputsn.text()
        self.fname = self.name_inputfn.text()
        self.fii = str(self.sname + ' ' + self.name + ' ' + self.fname)
        if self.fii:
            con = sqlite3.connect("names.sqlite")
            cur = con.cursor()
            cur.execute(f'INSERT INTO name(fio) VALUES("{self.fii}")')
            con.commit()
            con.close()

    def yan(self):  # Выбор теста
        self.test = str('Яндекс.Лицей')

    def mat(self):
        self.test = 'Математика'

    def nach(self):
        self.test = 'Природа'

    def open_second_form(self):  # Открытие второго окна и добавление информации в базу данных.
        ts = self.test
        if self.fii:
            if self.fii != '  ':
                fi = self.fii
            else:
                fi = False
        if fi and ts:
            con = sqlite3.connect("names.sqlite")
            cur = con.cursor()
            cur.execute(f"INSERT INTO tests(test, fi) SELECT '{ts}', id FROM name WHERE fio = '{fi}'")
            con.commit()
            con.close()
            self.second_form = SecondForm(self.fii, self.test)
            self.second_form.show()
            self.close()    #Закрытие первого окна.


class SecondForm(QWidget):  # Второе окно с вопросамии и вводом ответа.
    def __init__(self, a, b):
        super().__init__()
        self.initUI()
        self.fio = a
        self.tst = b
        self.num = 0
        self.answers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if b == 'Математика':  # Вывод вопросов из текстового файла.
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

    def initUI(self):  # Структура окна 2.
        self.setGeometry(600, 200, 700, 350)
        self.setWindowTitle('ТЕСТ')
        self.lbl = QLabel(self)
        self.lbl.adjustSize()

        self.pixmap = QPixmap("фон1")
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(700, 450)
        self.image.setPixmap(self.pixmap)

        self.pixmap = QPixmap("раздумья")
        self.image = QLabel(self)
        self.image.move(40, 140)
        self.image.resize(250, 150)
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

        self.pixmap1 = QPixmap("вопрос0")
        self.image = QLabel(self)
        self.image.move(300, 100)
        self.image.resize(390, 240)
        self.image.setPixmap(self.pixmap1)

        self.label3 = QLabel(self)
        self.label3.setFont(QFont("Times", 11, QFont.Bold))
        self.label3.setText("Ответ:")
        self.label3.adjustSize()
        self.label3.move(40, 100)

        self.label3 = QLabel(self)
        self.label3.setFont(QFont("Times", 10, QFont.Bold))
        self.label3.setText("Если не знаете ответ, нажмите NEXT")
        self.label3.adjustSize()
        self.label3.move(40, 120)

        self.ainput = QLineEdit(self)
        self.ainput.adjustSize()
        self.ainput.move(100, 100)

        self.btn1 = QPushButton('CLOSE', self)
        font = QFont("Times", 12, QFont.Bold)
        self.btn1.setFont(font)
        self.btn1.resize(self.btn.sizeHint())
        self.btn1.move(200, 300)
        self.btn1.clicked.connect(self.open_tr_form)

    def questh(self):  # Реагирование на нажатие кнопки, смена текста, анализ ответа, исключение ошибочного ввода.
        self.btn.setText('NEXT')
        self.btn.resize(self.btn.sizeHint())
        a = self.ainput.text()

        if not a.isdigit() and a != '':
            self.label4.setText(f"{self.quest[self.num - 1]}")
            self.label4.adjustSize()
            self.ainput.setText(f"")
            self.num += 0
        elif a == '':
            if self.num < 10:
                self.label4.setText(f"{self.quest[self.num]}")
                self.label4.adjustSize()
                self.pixmap1 = QPixmap("вопрос" + str(self.num + 1))
                self.image.setPixmap(self.pixmap1)
            else:
                self.label4.setText(f"Всё)")
                self.label4.adjustSize()
                self.pixmap1 = QPixmap("вопрос11")
                self.image.setPixmap(self.pixmap1)
            self.num += 1
            self.ainput.setText(f"")
            self.answers.append(str(0))
        else:
            if self.num < 10:
                self.label4.setText(f"{self.quest[self.num]}")
                self.label4.adjustSize()
                self.pixmap1 = QPixmap("вопрос" + str(self.num + 1))
                self.image.setPixmap(self.pixmap1)
                self.answers[self.num] = a
            else:
                self.label4.setText(f"Всё)")
                self.label4.adjustSize()
                self.pixmap1 = QPixmap("вопрос11")
                self.image.setPixmap(self.pixmap1)
            self.num += 1
            self.ainput.setText(f"")

    def keyPressEvent(self, event):    #Работа enter во время ввода ответов.
        if event.key() == 16777220:
            self.btn.setText('NEXT')
            self.btn.resize(self.btn.sizeHint())
            a = self.ainput.text()

            if not a.isdigit() and a != '':
                self.label4.setText(f"{self.quest[self.num - 1]}")
                self.label4.adjustSize()
                self.ainput.setText(f"")
                self.num += 0
            elif a == '':
                if self.num < 10:
                    self.label4.setText(f"{self.quest[self.num]}")
                    self.label4.adjustSize()
                    self.pixmap1 = QPixmap("вопрос" + str(self.num + 1))
                    self.image.setPixmap(self.pixmap1)
                else:
                    self.label4.setText(f"Всё)")
                    self.label4.adjustSize()
                    self.pixmap1 = QPixmap("вопрос11")
                    self.image.setPixmap(self.pixmap1)
                self.num += 1
                self.ainput.setText(f"")
                self.answers.append(str(0))
            else:
                if self.num < 10:
                    self.label4.setText(f"{self.quest[self.num]}")
                    self.label4.adjustSize()
                    self.pixmap1 = QPixmap("вопрос" + str(self.num + 1))
                    self.image.setPixmap(self.pixmap1)
                else:
                    self.label4.setText(f"Всё)")
                    self.label4.adjustSize()
                    self.pixmap1 = QPixmap("вопрос11")
                    self.image.setPixmap(self.pixmap1)
                self.num += 1
                self.ainput.setText(f"")
                self.answers[self.num - 1] = a

    def open_tr_form(self):    #Открытие третьего окна + закрытие второго.
        self.tr_form = TrForm(self.answers, self.answ, self.tst, self.fio)
        self.tr_form.show()
        self.close()


class TrForm(QWidget):  #Третье окно.
    def __init__(self, a, b, tst, fio):
        super().__init__()
        self.initUI()
        self.answw = b
        self.itt = a
        self.n = 0
        self.fio = fio
        self.tst = tst
        for i in range(len(self.answw)):
            if int(self.answw[i]) == int(self.itt[i + 1]):
                self.n += 1
            else:
                self.n = self.n
        self.n *= 10
        self.n = str(self.n)

        ts = self.tst
        fi = self.fio
        con = sqlite3.connect("names.sqlite")
        cur = con.cursor()
        cur.execute(
            f"UPDATE tests SET ress = {self.n} WHERE test = '{ts}' AND fi = (SELECT id FROM name WHERE fio = '{fi}')")
        con.commit()
        con.close()
            #Занос результатов в базу данных.
        fi = self.fio
        con = sqlite3.connect("names.sqlite")
        cur = con.cursor()
        result = cur.execute(
            f"SELECT test, ress FROM tests WHERE fi = (SELECT id FROM name WHERE fio = '{fi}')").fetchall()
        llis = []   #Создание строки для вывода результата.
        llis1 = []
        for i in set(result):
            llis.append(list(i)[0])
            llis1.append(list(i)[-1])
        self.aaaa = ''
        self.bbbb = ''
        for i in llis:
            self.aaaa += i
            self.aaaa += '\n'
        for i in llis1:
            self.bbbb += i
            self.bbbb += '\n'

    def initUI(self):   #Структура окна три.
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
        self.label2.move(40, 90)

        self.label3 = QLabel(self)
        self.label3.setFont(QFont("Times", 10, QFont.Bold))
        self.label3.setText(f" ")
        self.label3.adjustSize()
        self.label3.move(40, 120)

        self.label4 = QLabel(self)
        self.label4.setFont(QFont("Times", 10, QFont.Bold))
        self.label4.setText(f" ")
        self.label4.adjustSize()
        self.label4.move(40, 140)

        self.btn = QPushButton('Все результаты>', self)
        font = QFont("Times", 10, QFont.Bold)
        self.btn.setFont(font)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 60)
        self.btn.clicked.connect(self.all)

        self.label5 = QLabel(self)
        self.label5.setFont(QFont("Times", 10, QFont.Bold))
        self.label5.setText(f" ")
        self.label5.adjustSize()
        self.label5.move(200, 100)

        self.label6 = QLabel(self)
        self.label6.setFont(QFont("Times", 10, QFont.Bold))
        self.label6.setText(f" ")
        self.label6.adjustSize()
        self.label6.move(320, 100)

        self.pixmap1 = QPixmap("Поздравление")
        self.image = QLabel(self)
        self.image.move(150, 150)
        self.image.resize(250, 200)
        self.image.setPixmap(self.pixmap1)

        self.btn1 = QPushButton('Остальные\nучастники', self)
        font = QFont("Times", 10, QFont.Bold)
        self.btn1.setFont(font)
        self.btn1.resize(self.btn.sizeHint())
        self.btn1.adjustSize()
        self.btn1.move(40, 300)
        self.btn1.clicked.connect(self.open_qtr_form)

    def itg(self):  #Вывод окончательных итогов решения теста.
        vv = str(self.n) + '%'
        self.label2.setText(f"{vv}")
        self.label2.adjustSize()

        self.label3.setText(f"Правильно/ответ")
        self.label3.adjustSize()

        innnn = ''
        for i in range(len(self.answw)):
            innnn += f'{self.answw[i]}\t{self.itt[i + 1]}\n'
        self.label4.setText(f"{innnn}")
        self.label4.adjustSize()

    def all(self):  #Вывод общей статистики по используемому ФИО.
        self.label5.setText(f"{self.aaaa}")
        self.label5.adjustSize()

        self.label6.setText(f"{self.bbbb}")
        self.label6.adjustSize()

    def open_qtr_form(self):    #Открытие четвёртого окна.
        self.qtr_form = QtrForm()
        self.qtr_form.show()


class QtrForm(QWidget): #Четвёртое окно.
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):   #Общая структура окна четыре.
        self.setGeometry(600, 200, 400, 350)
        self.setWindowTitle('Все участники:')
        self.lbl = QLabel(self)
        self.lbl.adjustSize()

        self.pixmap = QPixmap("фон1")
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(700, 450)
        self.image.setPixmap(self.pixmap)

        self.label = QLabel(self)
        self.label.setFont(QFont("Times", 14, QFont.Bold))
        self.label.setText("Приветитки)")
        self.label.adjustSize()
        self.label.move(40, 20)

        self.label = QLabel(self)
        self.label.setFont(QFont("Times", 12, QFont.Bold))
        self.label.setText("О ком хочешь узнать?")
        self.label.adjustSize()
        self.label.move(40, 50)

        self.name_label = QLabel(self)
        self.name_label.setFont(QFont("Times", 10, QFont.Bold))
        self.name_label.setText("Фамилия: ")
        self.name_label.adjustSize()
        self.name_label.move(40, 80)

        self.name_inputsn = QLineEdit(self)
        self.name_inputsn.move(150, 80)

        self.name_label = QLabel(self)
        self.name_label.setFont(QFont("Times", 10, QFont.Bold))
        self.name_label.setText("Имя: ")
        self.name_label.adjustSize()
        self.name_label.move(40, 110)

        self.name_inputn = QLineEdit(self)
        self.name_inputn.move(150, 110)

        self.name_label = QLabel(self)
        self.name_label.setFont(QFont("Times", 10, QFont.Bold))
        self.name_label.setText("Отчество: ")
        self.name_label.adjustSize()
        self.name_label.move(40, 140)

        self.name_inputfn = QLineEdit(self)
        self.name_inputfn.move(150, 140)

        self.btn = QPushButton('Лицезреть>', self)
        font = QFont("Times", 10, QFont.Bold)
        self.btn.setFont(font)
        self.btn.resize(self.btn.sizeHint())
        self.btn.adjustSize()
        self.btn.move(40, 170)
        self.btn.clicked.connect(self.infa)

        self.name_label5 = QLabel(self)
        self.name_label5.setFont(QFont("Times", 12, QFont.Bold))
        self.name_label5.setText(" ")
        self.name_label5.adjustSize()
        self.name_label5.move(40, 200)

        self.label6 = QLabel(self)
        self.label6.setFont(QFont("Times", 12, QFont.Bold))
        self.label6.setText(f" ")
        self.label6.adjustSize()
        self.label6.move(200, 200)

    def infa(self): #Вывод статистики по введённому ФИО.
        self.name = self.name_inputn.text()
        self.sname = self.name_inputsn.text()
        self.fname = self.name_inputfn.text()
        self.fii = str(self.sname + ' ' + self.name + ' ' + self.fname)
        fi = self.fii
        if fi:
            con = sqlite3.connect("names.sqlite")
            cur = con.cursor()
            result = cur.execute(
                f"SELECT test, ress FROM tests WHERE fi = (SELECT id FROM name WHERE fio = '{fi}')").fetchall()
            llis = []
            llis1 = []
            for i in set(result):
                llis.append(list(i)[0])
                llis1.append(list(i)[-1])
            self.aaaa = ''
            self.bbbb = ''
            for i in llis:
                self.aaaa += i
                self.aaaa += '\n'
            for i in llis1:
                self.bbbb += i
                self.bbbb += '\n'

            self.name_label5.setText(f"{self.aaaa}")
            self.name_label5.adjustSize()

            self.label6.setText(f"{self.bbbb}")
            self.label6.adjustSize()

        if not fi or fi == '  ':
            self.name_label5.setText(f"Введите информацию")
            self.name_label5.adjustSize()

    def keyPressEvent(self, event): #Работа клавиши enter.
        if event.key() == 16777220:
            self.infa()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
