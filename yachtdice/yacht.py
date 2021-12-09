import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from subwindow import subwindow
from table import table
from scorecalc import scorecalc


class Yacht(QWidget):
    def __init__(self):
        super().__init__()
        self.player = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Yacht Game')
        self.setGeometry(300, 100, 500, 800)

        self.turn = 1
        self.currPlayer = 1
        self.rollChance = 3

        self.playerScore = [[-1 for i in range(16)] for j in range(5)]

        self.showRollChance = QLabel("Roll Chance : " + str(self.rollChance))
        self.showRollChance.setMaximumHeight(80)

        font1 = self.showRollChance.font()
        font1.setPointSize(15)
        font1.setFamily("Arial")
        font1.setBold(True)
        self.showRollChance.setFont(font1)

        self.scoreTable = QTableWidget()



        self.getPlayer()
        self.setScoreTable()

        self.diceEye = [1, 1, 1, 1, 1]
        self.dice = [QLabel() for i in range(5)]
        self.diceState = [0 for i in range(5)]
        self.lockButton = [QPushButton("Lock") for i in range(5)]
        for i in range(5):
            self.dice[i].resize(100, 100)
        self.rollDice = QPushButton("Roll")

        font2 = self.rollDice.font()
        font2.setPointSize(15)
        font2.setFamily("Arial")
        font2.setBold(True)
        self.rollDice.setFont(font2)

        self.rollDice.clicked.connect(self.roll)
        self.rollDice.setMaximumHeight(80)

        self.setGeometry(300, 100, 130 + self.player * 80 + 800, 754)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.scoreTable)

        vbox2 = QVBoxLayout()

        hbox0 = QHBoxLayout()
        hbox0.addStretch(1)
        hbox0.addWidget(self.showRollChance)
        hbox0.addStretch(1)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        for i in range(5):
            hbox1.addStretch(1)
            hbox1.addWidget(self.dice[i])
        hbox1.addStretch(2)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        for i in range(5):
            hbox2.addStretch(1)
            hbox2.addWidget(self.lockButton[i])
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.rollDice)
        hbox3.addStretch(1)

        vbox2.addLayout(hbox0)
        vbox2.addStretch(1)
        vbox2.addLayout(hbox1)
        vbox2.addStretch(1)
        vbox2.addLayout(hbox2)
        vbox2.addStretch(1)
        vbox2.addLayout(hbox3)

        HBOX = QHBoxLayout()
        HBOX.addLayout(vbox1)
        HBOX.addLayout(vbox2)

        self.setLayout(HBOX)


    def getPlayer(self):
        sub = subwindow()
        fine = sub.getPlayer()
        if fine:
            self.player = sub.player
        else:
            exit()


    def setScoreTable(self):
        self.scoreTable.setRowCount(16)
        self.scoreTable.setColumnCount(self.player + 1)
        self.scoreTable.setMaximumWidth(130 + 80 * self.player + 2)

        self.scoreTable.verticalHeader().setVisible(False)
        self.scoreTable.horizontalHeader().setVisible(False)
        self.scoreTable.verticalScrollBar().setVisible(False)
        self.scoreTable.horizontalScrollBar().setVisible(False)

        self.scoreTable.setSelectionMode(QAbstractItemView.NoSelection)
        self.scoreTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.scoreTable.font().setBold(True)
        self.scoreTable.setColumnWidth(0, 130)
        self.scoreTable.cellClicked.connect(self.scoreSelect)

        for row in range(16):
            self.scoreTable.setItem(row, 0, QTableWidgetItem(table[row]))
            self.scoreTable.item(row, 0).setBackground(QColor(153, 255, 255))

        for i in range(1, self.player + 1):
            self.scoreTable.setColumnWidth(i, 80)
            self.scoreTable.setItem(0, i, QTableWidgetItem("Player " + str(i)))
            self.scoreTable.setItem(7, i, QTableWidgetItem("0"))
            self.scoreTable.setItem(8, i, QTableWidgetItem("0"))
            self.scoreTable.setItem(15, i, QTableWidgetItem("0"))


    def roll(self):
        if self.rollChance > 0:
            for i in range(5):
                self.diceEye[i] = random.randrange(1, 7)
            self.diceEye.sort()
            self.setScore()
            self.setImage()
            self.rollChance -= 1
            self.showRollChance.setText("Roll Chance : " + str(self.rollChance))

    def setImage(self):
        for i in range(5):
            pixmap = QPixmap("dice"+str(self.diceEye[i])+".png")
            pixmap = pixmap.scaledToWidth(100)
            self.dice[i].setPixmap(QPixmap(pixmap))

    def setScore(self):
        for i in range(1, 16):
            if self.playerScore[self.currPlayer][i] == -1:
                if not(i in [7, 8, 15]):
                    self.scoreTable.setItem(i, self.currPlayer, QTableWidgetItem(str(scorecalc(self.diceEye, self.scoreTable.item(i, 0).text()))))
                    self.scoreTable.item(i, self.currPlayer).setForeground(QColor(180, 180, 180))

    def scoreSelect(self):
        if self.rollChance < 3:
            column = self.scoreTable.currentColumn()
            if not(column == self.currPlayer):
                return
            row = self.scoreTable.currentRow()
            if row in [0, 7, 8, 15]:
                return
            self.playerScore[column][row] = int(self.scoreTable.item(row, column).text())
            self.scoreTable.item(row, column).setForeground(QColor(0, 0, 0))
            self.turnFine()

    def turnFine(self):
        self.rollChance = 3
        self.showRollChance.setText("Roll Chance : " + str(self.rollChance))

        self.playerScore[self.currPlayer][7] = 0
        self.playerScore[self.currPlayer][15] = 0

        for i in range(1, 7):
            self.playerScore[self.currPlayer][7] += max(0, self.playerScore[self.currPlayer][i])

        if self.playerScore[self.currPlayer][7] >= 63:
            self.playerScore[self.currPlayer][8] = 35
        else:
            self.playerScore[self.currPlayer][8] = 0

        for i in range(7,15):
            self.playerScore[self.currPlayer][15] += max(0, self.playerScore[self.currPlayer][i])

        self.scoreTable.setItem(7, self.currPlayer, QTableWidgetItem(str(self.playerScore[self.currPlayer][7])))
        self.scoreTable.setItem(8, self.currPlayer, QTableWidgetItem(str(self.playerScore[self.currPlayer][8])))
        self.scoreTable.setItem(15, self.currPlayer, QTableWidgetItem(str(self.playerScore[self.currPlayer][15])))

        for i in range(1, 16):
            if self.playerScore[self.currPlayer][i] == -1:
                self.scoreTable.setItem(i, self.currPlayer, QTableWidgetItem(""))

        for i in range(5):
            pixmap = QPixmap("")
            self.dice[i].setPixmap(QPixmap(pixmap))

        if self.currPlayer == self.player:
            self.turn += 1
            self.scoreTable.setItem(0,0,QTableWidgetItem("Turn : " + str(self.turn) + " / 12"))
            self.scoreTable.item(0, 0).setBackground(QColor(153, 255, 255))
            self.currPlayer = 1
        else:
            self.currPlayer += 1

        if self.turn == 13:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    temp = Yacht()
    temp.show()
    sys.exit(app.exec_())