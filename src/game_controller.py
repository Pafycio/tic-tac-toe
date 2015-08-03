__author__ = 'Pawel'

import tkinter as tk
from src import O_X as ox


class Game(object):
    def __init__(self):
        self.root = tk.Tk()
        self.game = ox.GameO_X()
        self.cursor_x, self.cursor_y = 0, 0
        self.old_cursor_x, self.old_cursor_y = 0, 0
        self.old_value = " "
        self.currPlayer = 0
        self.introduction()
        self.setRound()

    def introduction(self):
        print("GAME O and X\nMoving WSAD Place Spacebar \nFirst Player is O\nSecound Player is X\nHave Fun! !")

    def gameLoop(self):
        while not self.game.isGameOver():
            self.root.bind_all('<Key>', self.keyPress)
            self.root.withdraw()
            self.root.mainloop()
        print("END GAME")

    def setRound(self):
        self.old_value = self.game.getArrayValue(0, 0)
        self.set_new_position()
        self.moveCursor()

    def moveCursor(self):
        self.clean_old_cursor()
        self.move_cursor()
        self.game.printGameArray(self.currPlayer)

    def clean_old_cursor(self):
        self.game.setToArrayOn(self.old_cursor_y, self.old_cursor_x, self.old_value, "move")

    def move_cursor(self):
        self.old_value = self.game.getArrayValue(self.cursor_y, self.cursor_x)
        self.game.setToArrayOn(self.cursor_y, self.cursor_x, "_", "move")

    def set_old_position(self):
        self.old_cursor_y = self.cursor_y
        self.old_cursor_x = self.cursor_x

    def set_new_position(self):
        self.cursor_x = self.cursor_y = 0
        self.old_cursor_x = self.old_cursor_y = 0

    def place_value(self):
        self.game.setToArrayOn(self.cursor_y, self.cursor_x, self.currPlayer, "place")
        self.check_end_game()
        self.currPlayer = (self.currPlayer+1) % 2

    def check_end_game(self):
        if self.game.checkWin() == 1:
            self.game.printGameArray(self.currPlayer)
            print("WIN PLAYER " + str(self.currPlayer))
            self.root.destroy()
        elif self.game.checkWin() == -1:
            self.game.printGameArray(self.currPlayer)
            print("REMIS")
            self.root.destroy()

    def keyPress(self, event):
        self.set_old_position()
        x = event.char
        move = True
        if event.keysym == 'Escape':
            self.game.gameOver = True
            self.root.destroy()
        elif event.keysym == 'space' and self.old_value == " ":
            move = False
            self.place_value()
        elif x == "w":
            if self.cursor_y - 1 >= 0:
                self.cursor_y -= 1
        elif x == "a":
            if self.cursor_x - 1 >= 0:
                self.cursor_x -= 1
        elif x == "s":
            if self.cursor_y + 1 < 3:
                self.cursor_y += 1
        elif x == "d":
            if self.cursor_x + 1 < 3:
                self.cursor_x += 1

        if move and not self.game.gameOver:
            self.moveCursor()
        elif not self.game.gameOver:
            self.setRound()


if __name__ == '__main__':
    game = Game()
    game.gameLoop()