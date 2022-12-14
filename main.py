from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Кофе 800тг')
but = QPushButton('Налить')
text = QLabel('Нажми, чтобы налить кофе')
winner = QLabel('Либо без кофе :)')
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(but, alignment = Qt.AlignCenter)
main_win.setLayout(line)

def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Чашек кофе:')

but.clicked.connect(show_winner)
main_win.show()
app.exec_()