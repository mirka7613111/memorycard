from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGroupBox, QPushButton,
    QRadioButton, QLabel, QVBoxLayout, QHBoxLayout,
    QButtonGroup, QMessageBox
)
import random


class Question:
    def __init__(self, text, right_answer, wrong1, wrong2, wrong3):
        self.text = text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions = [
    Question('когда вышла 1 серия шкибиди туалетов?', 'давно', 'вчера', 'сегодня', 'завтра'),
    Question('где я родился"?', 'Россия', 'Юпитер', 'Луна', 'Австралия'),
    Question('В каком году родился христос?', 'я не знаю', '-1', '10', '1945'),
    Question('Какой человек умнее?', 'самый умный', 'глупый', 'умный', 'абоба'),
    Question('Какой океан является самым большим по площади?', 'Тихий океан', 'Атлантический океан', 'Индийский океан', 'Северный Ледовитый океан'),
    Question('Какая страна является родиной демократии?', 'Греция', 'Италия', 'Англия', 'Аргентина'),
    Question('Какой цвет на красном плакате?', 'красный', 'зеленый', 'мммсиний', 'я не знаю'),
    Question('кто предаель?', 'импостэээр', 'красный', 'желтый', 'я')
]


def is_checked():
    for rbtn in answers_btn:
        if rbtn.isChecked():
            return True
    return False


def show_result():
    if not is_checked():
        return
    
    btn.setText('Следующий вопрос')  # смена надписи на кнопке
    for rbtn in answers_btn:  # цикл для перебора радио-кнопок
        rbtn.setDisabled(True)
        if rbtn.isChecked():  # проверка каждой кнопки на "выбрана ли она"
            if rbtn.text() == answers_btn[0].text():  # проверяем верный ли ответ
                rbtn.setStyleSheet('color: green;')  # поменяем цвет выбранного ответа на зеленый
                main_win.score += 1
            else:
                rbtn.setStyleSheet('color: red;')  # поменяем цвет выбранного ответа на красный
                answers_btn[0].setStyleSheet('color: green;')  # поменяем цвет правильного ответа на зеленый



def show_question():
    next_question()
    btn.setText('Ответить')  # смена надписи на кнопке
    button_group.setExclusive(False)  # убираем взаимосвязь между кнопками
    for rbtn in answers_btn:  # цикл для перебора радио-кнопок
        rbtn.setDisabled(False)
        rbtn.setChecked(False)  # убираем нажатие на кнопки
        rbtn.setStyleSheet('')  # убираем выделение цветов правильного и/или неправильного ответа
    button_group.setExclusive(True)  # вовзращаем взаимосвязь между кнопками


def start_test():
    if btn.text() == 'Ответить':  # если на кнопке надпись "Ответить"
        show_result()  # то запустить функцию show_result()
    else:  # иначе
        show_question()  # запускаем функцию show_question()


def ask(q: Question):
    question_text.setText(q.text)  # устаналиваем новый вопрос в виджет QLabel
    random.shuffle(answers_btn)  # перемешиваем список с нашими кнопками
    answers_btn[0].setText(q.right_answer)  # устанавливаем правильный ответ на первую в списке радио-кнопку
    answers_btn[1].setText(q.wrong1)  # устанавливаем неправильный ответ №1 на вторую в списке радио-кнопку
    answers_btn[2].setText(q.wrong2)  # устанавливаем неправильный ответ №2 на третью в списке радио-кнопку
    answers_btn[3].setText(q.wrong3)  # устанавливаем неправильный ответ №3 на четвертую в списке радио-кнопку


def next_question():
    if main_win.q_index == len(questions) - 1:
        main_win.q_index = -1
        random.shuffle(questions)
        show_score()
        main_win.score = 0
    
    main_win.q_index += 1
    q = questions[main_win.q_index]
    ask(q)

def show_score():
    percent = main_win.score / main_win.total * 100
    percent = round(percent, 2)
    text = ' уважаемый пользователь!\n'
    text += ' Вы ответили правильно на ' + str(main_win.score) + ' из ' + str(main_win.total) + ' вопросов.\n'
    text += ' процент правильных ответов: ' + str(percent) + ' % '

    msg = QMessageBox()
    msg.setWindowTitle('Результат тестирования')
    msg.setText(text)
    msg.exec()


# настройка окна
app = QApplication([])  # создание экземпляра приложения
main_win = QWidget()  # создание окна
main_win.setWindowTitle('MemoryCard')  # заголовок для окна
main_win.resize(640, 480)  # изменение размера окна
main_win.q_index = -1  # счетчик вопросов
main_win.score = 0
main_win.total = len(questions)
# настройка окна

# создание виджетов
question_text = QLabel('Тут будет вопрос?')  # создание виджета для текста вопроса
grp_box = QGroupBox('Варианты ответов')  # создание виджета для группировки вариантов ответов
radio1 = QRadioButton('Нет')  # первый вариант (кнопка-переключатель)
radio2 = QRadioButton('Да')  # второй вариант (кнопка-переключатель)
radio3 = QRadioButton('Что')  # третий вариант (кнопка-переключатель)
radio4 = QRadioButton('Зачем?')  # четвертый вариант (кнопка-переключатель)
btn = QPushButton('Ответить')  # виджет кнопки "Ответить"
# создание виджетов

# создания списка с кнопками
answers_btn = [radio1, radio2, radio3, radio4]
# создания списка с кнопками

# создание и установка группы кнопок
button_group = QButtonGroup()
button_group.addButton(radio1)
button_group.addButton(radio2)
button_group.addButton(radio3)
button_group.addButton(radio4)
# создание и установка группы кнопок

# создание направляющих
main_layout = QVBoxLayout()  # создание вертикальной направляющей для главного окна
main_h1 = QHBoxLayout()  # создание 1ой горизонтальной направляющей
main_h2 = QHBoxLayout()  # создание 2ой горизонтальной направляющей
main_h3 = QHBoxLayout()  # создание 3ой горизонтальной направляющей
grp_layout = QHBoxLayout()  # создание главной горизонтальной направляющей для QGroupBox'a
grp_v1 = QVBoxLayout()  # создание 1ой вертикальной направляющей для вариантов ответа
grp_v2 = QVBoxLayout()  # создание 2ой вертикальной направляющей для вариантов ответа
# создание направляющих

# установка виджетов на направляющие
main_h1.addWidget(question_text, alignment=Qt.AlignCenter)  # добавление на направляющую виджета с вопросом
main_h2.addWidget(grp_box)  # добавление на направляющую
main_h3.addStretch(1)
main_h3.addWidget(btn, stretch=3)
main_h3.addStretch(1)
main_layout.addLayout(main_h1)
main_layout.addLayout(main_h2)
main_layout.addLayout(main_h3)
grp_v1.addWidget(radio1)
grp_v1.addWidget(radio2)
grp_v2.addWidget(radio3)
grp_v2.addWidget(radio4)
grp_layout.addLayout(grp_v1)
grp_layout.addLayout(grp_v2)
grp_box.setLayout(grp_layout)
main_win.setLayout(main_layout)
# установка виджетов на направляющие

btn.clicked.connect(start_test)  # соединение кнопки с функцией

# тестовый запуск функции ask
random.shuffle(questions)
next_question()

main_win.show()
app.exec()
