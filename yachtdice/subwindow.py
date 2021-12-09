import sys
from PyQt5.QtWidgets import *

class subwindow(QDialog):

    def __init__(self):
        super().__init__()
        self.player = 1
        self.initUI()

    def initUI(self):

        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(self.PUSHOK)

        Number = QLabel("Number:")
        self.setPlayer = QComboBox()
        self.setPlayer.addItem('혼자서!')
        self.setPlayer.addItem('둘이서!')
        self.setPlayer.addItem('셋이서!')
        self.setPlayer.addItem('넷이서!')

        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()

        hbox.addStretch(1)
        hbox.addWidget(self.okButton)

        hbox1.addStretch(1)
        hbox1.addWidget(Number)
        hbox1.addWidget(self.setPlayer)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setGeometry(500, 500, 350, 150)
        self.setWindowTitle('플레이어 수 정하기')
        self.show()

    def PUSHOK(self):
        self.player = self.setPlayer.currentIndex() + 1
        self.accept()

    def getPlayer(self):
        return super().exec_()