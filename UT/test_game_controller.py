__author__ = 'Pawel'

import unittest
from src import game_controller as gc
from src import O_X as ox
import tkinter as tk


class TestGameController(unittest.TestCase):
    def setUp(self):
        pass

    def Test_Create_Game(self):
        gameObj = gc.Game()
        self.assertEqual(True, isinstance(gameObj.game, ox))
        self.assertEqual(True, isinstance(gameObj.root, tk))

