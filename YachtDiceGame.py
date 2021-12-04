import pickle
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt



class PersonCheck(QWidget):
    global temp
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        Number = QLabel("Number:")
        self.Nameline = QLineEdit()
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        sld.setRange(1,4)
        lcd.display(1)
        sld.valueChanged.connect(lcd.display)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        okButton.clicked.connect(self.PUSHOK)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(Number)
        hbox1.addWidget(lcd)
        hbox1.addStretch(1)
        hbox1.addWidget(sld)
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


class Yacht(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        Result = QLabel("Result:")
        self.ResultText = QTextEdit()

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        for i in range(1, 4):  # 이 부분 인원수로 표현해야함
            Name = QLabel("Amount" + str(i) + ":")
            self.Nameline = QLineEdit()
            hbox1.addWidget(Name)
            hbox1.addWidget(self.Nameline)
            self.Nameline.setReadOnly(True)

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
        hbox4.addWidget(Result)
        hbox4.addStretch(1)
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