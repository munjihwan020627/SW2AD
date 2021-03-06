import pickle
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import random
from RandomDice import *
from ScoreDB import *

class PersonCheck(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global sld
        okButton = QPushButton("OK")
        Number = QLabel("Number:")
        self.Nameline = QLineEdit()
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        sld.setRange(1,4)
        self.getNumber()
        lcd.display(1)
        sld.valueChanged.connect(lcd.display)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        okButton.clicked.connect(self.getNumber)
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

    def getNumber(self):
        global b
        b = sld.value()
        return b


    def PUSHOK(self):
        if b ==1:
            temp1.show()

        if b == 2:
            temp2.show()

        if b ==3:
            temp3.show()

        if b ==4:
            temp4.show()
        self.hide()

ScoreKey = ['Aces',
            'Deuces',
            'Threes',
            'Fours',
            'Fives',
            'Sixes',
            'Choice',
            '4 of a kind',
            'Full House',
            'Small Straight',
            'Large Straight',
            'Yacht',
            ]


class Yacht4(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.ResultText = QTextEdit()

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)

        v = PersonCheck.getNumber(self)
        Name1 = QLabel("Amount" + str(1) + ":")
        Nameline1 = QLineEdit()
        hbox1.addWidget(Name1)
        hbox1.addWidget(Nameline1)
        Nameline1.setReadOnly(True)
        Name2 = QLabel("Amount" + str(2) + ":")
        Nameline2 = QLineEdit()
        hbox1.addWidget(Name2)
        hbox1.addWidget(Nameline2)
        Nameline2.setReadOnly(True)
        Name3 = QLabel("Amount" + str(3) + ":")
        Nameline3 = QLineEdit()
        hbox1.addWidget(Name3)
        hbox1.addWidget(Nameline3)
        Nameline3.setReadOnly(True)
        Name4 = QLabel("Amount" + str(4) + ":")
        Nameline4 = QLineEdit()
        hbox1.addWidget(Name4)
        hbox1.addWidget(Nameline4)
        Nameline4.setReadOnly(True)


        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)

        # 5개의 주사위 표현
        Dice1 = QLabel("Dice" + str(1) + ":")
        self.DiceLine1 = QLineEdit()
        self.KeyBox1 = QComboBox()
        self.KeyBox1.addItem('again')
        self.KeyBox1.addItem('stop')

        Dice2 = QLabel("Dice" + str(2) + ":")
        self.DiceLine2 = QLineEdit()
        self.KeyBox2 = QComboBox()
        self.KeyBox2.addItem('again')
        self.KeyBox2.addItem('stop')

        Dice3 = QLabel("Dice" + str(3) + ":")
        self.DiceLine3 = QLineEdit()
        self.KeyBox3 = QComboBox()
        self.KeyBox3.addItem('again')
        self.KeyBox3.addItem('stop')

        Dice4 = QLabel("Dice" + str(4) + ":")
        self.DiceLine4 = QLineEdit()
        self.KeyBox4 = QComboBox()
        self.KeyBox4.addItem('again')
        self.KeyBox4.addItem('stop')

        Dice5 = QLabel("Dice" + str(5) + ":")
        self.DiceLine5 = QLineEdit()
        self.KeyBox5 = QComboBox()
        self.KeyBox5.addItem('again')
        self.KeyBox5.addItem('stop')





        hbox2.addWidget(Dice1)
        hbox2.addWidget(self.DiceLine1)
        hbox2.addWidget(self.KeyBox1)
        self.DiceLine1.setReadOnly(True)
        hbox2.addWidget(Dice2)
        hbox2.addWidget(self.DiceLine2)
        hbox2.addWidget(self.KeyBox2)
        self.DiceLine2.setReadOnly(True)
        hbox2.addWidget(Dice3)
        hbox2.addWidget(self.DiceLine3)
        hbox2.addWidget(self.KeyBox3)
        self.DiceLine3.setReadOnly(True)
        hbox2.addWidget(Dice4)
        hbox2.addWidget(self.DiceLine4)
        hbox2.addWidget(self.KeyBox4)
        self.DiceLine4.setReadOnly(True)
        hbox2.addWidget(Dice5)
        hbox2.addWidget(self.DiceLine5)
        hbox2.addWidget(self.KeyBox5)
        self.DiceLine5.setReadOnly(True)



        hbox4 = QHBoxLayout()
        Result = QLabel("Result:")
        rollbutton = QPushButton("roll")
        self.ResultBox = QComboBox()
        for i in ScoreKey:
            self.ResultBox.addItem(i)
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

        rollbutton.clicked.connect(self.rolldice)
        addbutton.clicked.connect(lambda :Get_score(self.ResultBox.currentIndex(),Get_Score(self.ResultBox.currentIndex(), int(self.DiceLine1.text()), int(self.DiceLine2.text()), int(self.DiceLine3.text()), int(self.DiceLine4.text()), int(self.DiceLine5.text()))))


    def rolldice(self):
        if self.KeyBox1.currentIndex() ==0:
            self.DiceLine1.setText(str(random.randint(1,6)))
        if self.KeyBox2.currentIndex() == 0:
            self.DiceLine2.setText(str(random.randint(1,6)))
        if self.KeyBox3.currentIndex() == 0:
            self.DiceLine3.setText(str(random.randint(1,6)))
        if self.KeyBox4.currentIndex() == 0:
            self.DiceLine4.setText(str(random.randint(1,6)))
        if self.KeyBox5.currentIndex() == 0:
            self.DiceLine5.setText(str(random.randint(1,6)))







class Yacht3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.ResultText = QTextEdit()

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)

        v = PersonCheck.getNumber(self)
        Name1 = QLabel("Amount" + str(1) + ":")
        Nameline1 = QLineEdit()
        hbox1.addWidget(Name1)
        hbox1.addWidget(Nameline1)
        Nameline1.setReadOnly(True)
        Name2 = QLabel("Amount" + str(2) + ":")
        Nameline2 = QLineEdit()
        hbox1.addWidget(Name2)
        hbox1.addWidget(Nameline2)
        Nameline2.setReadOnly(True)
        Name3 = QLabel("Amount" + str(3) + ":")
        Nameline3 = QLineEdit()
        hbox1.addWidget(Name3)
        hbox1.addWidget(Nameline3)
        Nameline3.setReadOnly(True)
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)

        # 5개의 주사위 표현
        Dice1 = QLabel("Dice" + str(1) + ":")
        self.DiceLine1 = QLineEdit()
        self.KeyBox1 = QComboBox()
        self.KeyBox1.addItem('again')
        self.KeyBox1.addItem('stop')

        Dice2 = QLabel("Dice" + str(2) + ":")
        self.DiceLine2 = QLineEdit()
        self.KeyBox2 = QComboBox()
        self.KeyBox2.addItem('again')
        self.KeyBox2.addItem('stop')

        Dice3 = QLabel("Dice" + str(3) + ":")
        self.DiceLine3 = QLineEdit()
        self.KeyBox3 = QComboBox()
        self.KeyBox3.addItem('again')
        self.KeyBox3.addItem('stop')

        Dice4 = QLabel("Dice" + str(4) + ":")
        self.DiceLine4 = QLineEdit()
        self.KeyBox4 = QComboBox()
        self.KeyBox4.addItem('again')
        self.KeyBox4.addItem('stop')

        Dice5 = QLabel("Dice" + str(5) + ":")
        self.DiceLine5 = QLineEdit()
        self.KeyBox5 = QComboBox()
        self.KeyBox5.addItem('again')
        self.KeyBox5.addItem('stop')





        hbox2.addWidget(Dice1)
        hbox2.addWidget(self.DiceLine1)
        hbox2.addWidget(self.KeyBox1)
        self.DiceLine1.setReadOnly(True)
        hbox2.addWidget(Dice2)
        hbox2.addWidget(self.DiceLine2)
        hbox2.addWidget(self.KeyBox2)
        self.DiceLine2.setReadOnly(True)
        hbox2.addWidget(Dice3)
        hbox2.addWidget(self.DiceLine3)
        hbox2.addWidget(self.KeyBox3)
        self.DiceLine3.setReadOnly(True)
        hbox2.addWidget(Dice4)
        hbox2.addWidget(self.DiceLine4)
        hbox2.addWidget(self.KeyBox4)
        self.DiceLine4.setReadOnly(True)
        hbox2.addWidget(Dice5)
        hbox2.addWidget(self.DiceLine5)
        hbox2.addWidget(self.KeyBox5)
        self.DiceLine5.setReadOnly(True)



        hbox4 = QHBoxLayout()
        Result = QLabel("Result:")
        rollbutton = QPushButton("roll")
        self.ResultBox = QComboBox()
        for i in ScoreKey:
            self.ResultBox.addItem(i)
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

        rollbutton.clicked.connect(self.rolldice)
        addbutton.clicked.connect(lambda :Get_score(self.ResultBox.currentIndex(),Get_Score(self.ResultBox.currentIndex(), int(self.DiceLine1.text()), int(self.DiceLine2.text()), int(self.DiceLine3.text()), int(self.DiceLine4.text()), int(self.DiceLine5.text()))))


    def rolldice(self):
        if self.KeyBox1.currentIndex() ==0:
            self.DiceLine1.setText(str(random.randint(1,6)))
        if self.KeyBox2.currentIndex() == 0:
            self.DiceLine2.setText(str(random.randint(1,6)))
        if self.KeyBox3.currentIndex() == 0:
            self.DiceLine3.setText(str(random.randint(1,6)))
        if self.KeyBox4.currentIndex() == 0:
            self.DiceLine4.setText(str(random.randint(1,6)))
        if self.KeyBox5.currentIndex() == 0:
            self.DiceLine5.setText(str(random.randint(1,6)))


class Yacht2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.ResultText = QTextEdit()

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)

        v = PersonCheck.getNumber(self)
        Name1 = QLabel("Amount" + str(1) + ":")
        Nameline1 = QLineEdit()
        hbox1.addWidget(Name1)
        hbox1.addWidget(Nameline1)
        Nameline1.setReadOnly(True)
        Name2 = QLabel("Amount" + str(2) + ":")
        Nameline2 = QLineEdit()
        hbox1.addWidget(Name2)
        hbox1.addWidget(Nameline2)
        Nameline2.setReadOnly(True)
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)

        # 5개의 주사위 표현
        Dice1 = QLabel("Dice" + str(1) + ":")
        self.DiceLine1 = QLineEdit()
        self.KeyBox1 = QComboBox()
        self.KeyBox1.addItem('again')
        self.KeyBox1.addItem('stop')

        Dice2 = QLabel("Dice" + str(2) + ":")
        self.DiceLine2 = QLineEdit()
        self.KeyBox2 = QComboBox()
        self.KeyBox2.addItem('again')
        self.KeyBox2.addItem('stop')

        Dice3 = QLabel("Dice" + str(3) + ":")
        self.DiceLine3 = QLineEdit()
        self.KeyBox3 = QComboBox()
        self.KeyBox3.addItem('again')
        self.KeyBox3.addItem('stop')

        Dice4 = QLabel("Dice" + str(4) + ":")
        self.DiceLine4 = QLineEdit()
        self.KeyBox4 = QComboBox()
        self.KeyBox4.addItem('again')
        self.KeyBox4.addItem('stop')

        Dice5 = QLabel("Dice" + str(5) + ":")
        self.DiceLine5 = QLineEdit()
        self.KeyBox5 = QComboBox()
        self.KeyBox5.addItem('again')
        self.KeyBox5.addItem('stop')





        hbox2.addWidget(Dice1)
        hbox2.addWidget(self.DiceLine1)
        hbox2.addWidget(self.KeyBox1)
        self.DiceLine1.setReadOnly(True)
        hbox2.addWidget(Dice2)
        hbox2.addWidget(self.DiceLine2)
        hbox2.addWidget(self.KeyBox2)
        self.DiceLine2.setReadOnly(True)
        hbox2.addWidget(Dice3)
        hbox2.addWidget(self.DiceLine3)
        hbox2.addWidget(self.KeyBox3)
        self.DiceLine3.setReadOnly(True)
        hbox2.addWidget(Dice4)
        hbox2.addWidget(self.DiceLine4)
        hbox2.addWidget(self.KeyBox4)
        self.DiceLine4.setReadOnly(True)
        hbox2.addWidget(Dice5)
        hbox2.addWidget(self.DiceLine5)
        hbox2.addWidget(self.KeyBox5)
        self.DiceLine5.setReadOnly(True)



        hbox4 = QHBoxLayout()
        Result = QLabel("Result:")
        rollbutton = QPushButton("roll")
        self.ResultBox = QComboBox()
        for i in ScoreKey:
            self.ResultBox.addItem(i)
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

        rollbutton.clicked.connect(self.rolldice)
        addbutton.clicked.connect(lambda :Get_score(self.ResultBox.currentIndex(),Get_Score(self.ResultBox.currentIndex(), int(self.DiceLine1.text()), int(self.DiceLine2.text()), int(self.DiceLine3.text()), int(self.DiceLine4.text()), int(self.DiceLine5.text()))))


    def rolldice(self):
        if self.KeyBox1.currentIndex() ==0:
            self.DiceLine1.setText(str(random.randint(1,6)))
        if self.KeyBox2.currentIndex() == 0:
            self.DiceLine2.setText(str(random.randint(1,6)))
        if self.KeyBox3.currentIndex() == 0:
            self.DiceLine3.setText(str(random.randint(1,6)))
        if self.KeyBox4.currentIndex() == 0:
            self.DiceLine4.setText(str(random.randint(1,6)))
        if self.KeyBox5.currentIndex() == 0:
            self.DiceLine5.setText(str(random.randint(1,6)))




class Yacht1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.ResultText = QTextEdit()

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)

        Name1 = QLabel("Amount" + str(1) + ":")
        Nameline1 = QLineEdit()
        hbox1.addWidget(Name1)
        hbox1.addWidget(Nameline1)
        Nameline1.setReadOnly(True)
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)

        # 5개의 주사위 표현
        Dice1 = QLabel("Dice" + str(1) + ":")
        self.DiceLine1 = QLineEdit()
        self.KeyBox1 = QComboBox()
        self.KeyBox1.addItem('again')
        self.KeyBox1.addItem('stop')

        Dice2 = QLabel("Dice" + str(2) + ":")
        self.DiceLine2 = QLineEdit()
        self.KeyBox2 = QComboBox()
        self.KeyBox2.addItem('again')
        self.KeyBox2.addItem('stop')

        Dice3 = QLabel("Dice" + str(3) + ":")
        self.DiceLine3 = QLineEdit()
        self.KeyBox3 = QComboBox()
        self.KeyBox3.addItem('again')
        self.KeyBox3.addItem('stop')

        Dice4 = QLabel("Dice" + str(4) + ":")
        self.DiceLine4 = QLineEdit()
        self.KeyBox4 = QComboBox()
        self.KeyBox4.addItem('again')
        self.KeyBox4.addItem('stop')

        Dice5 = QLabel("Dice" + str(5) + ":")
        self.DiceLine5 = QLineEdit()
        self.KeyBox5 = QComboBox()
        self.KeyBox5.addItem('again')
        self.KeyBox5.addItem('stop')





        hbox2.addWidget(Dice1)
        hbox2.addWidget(self.DiceLine1)
        hbox2.addWidget(self.KeyBox1)
        self.DiceLine1.setReadOnly(True)
        hbox2.addWidget(Dice2)
        hbox2.addWidget(self.DiceLine2)
        hbox2.addWidget(self.KeyBox2)
        self.DiceLine2.setReadOnly(True)
        hbox2.addWidget(Dice3)
        hbox2.addWidget(self.DiceLine3)
        hbox2.addWidget(self.KeyBox3)
        self.DiceLine3.setReadOnly(True)
        hbox2.addWidget(Dice4)
        hbox2.addWidget(self.DiceLine4)
        hbox2.addWidget(self.KeyBox4)
        self.DiceLine4.setReadOnly(True)
        hbox2.addWidget(Dice5)
        hbox2.addWidget(self.DiceLine5)
        hbox2.addWidget(self.KeyBox5)
        self.DiceLine5.setReadOnly(True)



        hbox4 = QHBoxLayout()
        Result = QLabel("Result:")
        rollbutton = QPushButton("roll")
        self.ResultBox = QComboBox()
        for i in ScoreKey:
            self.ResultBox.addItem(i)
        addbutton = QPushButton("Add")
        hbox4.addWidget(Result)
        hbox4.addStretch(1)
        hbox4.addWidget(rollbutton)
        hbox4.addStretch(1)
        hbox4.addWidget(self.ResultBox)
        hbox4.addStretch(1)
        hbox4.addWidget(addbutton)

        hbox5 = QHBoxLayout()
        ScoreList = QTableWidget()
        hbox5.addWidget(ScoreList)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addStretch(1)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Yacht Game')


        rollbutton.clicked.connect(self.rolldice)
        addbutton.clicked.connect(lambda :Get_score(self.ResultBox.currentIndex(),Get_Score(self.ResultBox.currentIndex(), int(self.DiceLine1.text()), int(self.DiceLine2.text()), int(self.DiceLine3.text()), int(self.DiceLine4.text()), int(self.DiceLine5.text()))))



    def rolldice(self):
        if self.KeyBox1.currentIndex() ==0:
            self.DiceLine1.setText(str(random.randint(1,6)))
        if self.KeyBox2.currentIndex() == 0:
            self.DiceLine2.setText(str(random.randint(1,6)))
        if self.KeyBox3.currentIndex() == 0:
            self.DiceLine3.setText(str(random.randint(1,6)))
        if self.KeyBox4.currentIndex() == 0:
            self.DiceLine4.setText(str(random.randint(1,6)))
        if self.KeyBox5.currentIndex() == 0:
            self.DiceLine5.setText(str(random.randint(1,6)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PersonCheck()
    temp1 = Yacht1()
    temp2 = Yacht2()
    temp3 = Yacht3()
    temp4 = Yacht4()
    sys.exit(app.exec_())