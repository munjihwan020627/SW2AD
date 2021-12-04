import pickle
import sys
from PyQt5.QtWidgets import *
import random

from PyQt5.QtCore import Qt


class PersonCheck(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton("OK")
        Number = QLabel("Number:")
        numberLine = QLineEdit()
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        okButton.clicked.connect(self.PUSHOK)
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(Number)
        hbox1.addStretch(1)
        hbox1.addWidget(numberLine)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('인원 수 정하기')
        self.show()
    def PUSHOK(self):
        self.close()
        temp.show()




def AddingHbox(n,hbox):
    for i in range(1,n+1):
        Name = QLabel("Amount" + str(i) + ":")
        Nameline = QLineEdit()
        hbox.addWidget(Name)
        hbox.addWidget(Nameline)
        Nameline.setReadOnly(True)


class Yacht(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.ResultText = QTextEdit()

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        a = random.randint(1,4) # 현재 인자를 받는데에 오류가 발생하므로 랜덤으로 인원수를 전달받음
        AddingHbox(a,hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        for i in range(1, 6):  # 5개의 주사위 표현
            Dice = QLabel("Dice" + str(i) + ":")
            self.DiceLine = QLineEdit()
            self.KeyBox = QComboBox()
            self.KeyBox.addItem('stop')
            self.KeyBox.addItem('again')
            hbox2.addWidget(Dice)
            hbox2.addWidget(self.DiceLine)
            hbox2.addWidget(self.KeyBox)
            self.DiceLine.setReadOnly(True)

        hbox4 = QHBoxLayout()
        Result = QLabel("Result:")
        rollbutton = QPushButton("roll")
        self.ResultBox = QComboBox()
        self.ResultBox.addItem('Aces')
        self.ResultBox.addItem('Deuces')
        self.ResultBox.addItem('Threes')
        self.ResultBox.addItem('Fours')
        self.ResultBox.addItem('Fives')
        self.ResultBox.addItem('Sixes')
        self.ResultBox.addItem('Choice')
        self.ResultBox.addItem('4 of a kind')
        self.ResultBox.addItem('Small Straight')
        self.ResultBox.addItem('Large Straight')
        self.ResultBox.addItem('Yacht')
        addbutton = QPushButton("Add")
        hbox4.addWidget(Result)
        hbox4.addStretch(1)
        hbox4.addWidget(rollbutton)
        hbox4.addStretch(1)
        hbox4.addWidget(self.ResultBox)
        hbox4.addStretch(1)
        hbox4.addWidget(addbutton)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.ResultText)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addStretch(1)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Yacht Game')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PersonCheck()
    temp = Yacht()

    sys.exit(app.exec_())
