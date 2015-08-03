__author__ = 'Pawel'


class GameO_X(object):
    def __init__(self):
        self.gameOver = False
        self.gameArray = [[" " for j in range(3)] for i in range(3)]
        self.round = 1

    def getO(self):
        return "O"

    def getX(self):
        return "X"

    def nextRound(self):
        self.round += 1

    def getXSizeArray(self):
        return 3

    def getYSizeArray(self):
        return 3

    def setToArrayOn(self, x, y, value, action):
        if action == "move":
            self.gameArray[x][y] = value
        elif action == "place":
            if value == 0:
                self.gameArray[x][y] = "O"
            elif value == 1:
                self.gameArray[x][y] = "X"
            self.nextRound()

    def getArrayValue(self, x, y):
        return self.gameArray[x][y]

    def printGameArray(self, player):
        tmp = " "
        if player == 0:
            tmp = "O"
        elif player == 1:
            tmp = "X"
        print("="*15)
        print("Round : " + str(self.getRound()) + " Player "+ tmp)
        print("="*15)
        for i in self.gameArray:
            print(str(i))

    def getRound(self):
        return self.round

    def checkRow(self, i):
        if self.gameArray[i][0] == self.gameArray[i][1] == self.gameArray[i][2] != ' ':
            return True
        return False

    def checkColumn(self, i):
        if self.gameArray[0][i] == self.gameArray[1][i] == self.gameArray[2][i] != ' ':
            return True
        return False

    def checkCross(self):
        if self.gameArray[0][0] == self.gameArray[1][1] == self.gameArray[2][2] != ' ':
            return True
        elif self.gameArray[2][0] == self.gameArray[1][1] == self.gameArray[0][2] != ' ':
            return True
        return False

    def checkAllRowColumn(self):
        for i in range(3):
            if self.checkRow(i):
                return True
            elif self.checkColumn(i):
                return True

    def checkWin(self):
        if self.checkCross() or self.checkAllRowColumn():
            self.gameOver = True
            return 1
        if self.getRound() == 10:
            self.gameOver = True
            return -1
        return 0

    def isGameOver(self):
        return self.gameOver
