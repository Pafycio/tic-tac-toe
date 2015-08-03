__author__ = 'Pawel'

import unittest
from src import O_X as OX


class TestO_X(unittest.TestCase):
    def setUp(self):
        self.game = OX.GameO_X()

    def test_start_game(self):
        self.assertTrue(isinstance(self.game, OX.GameO_X), True)

    def test_get_O(self):
        self.assertEqual(self.game.getO(), 'O')

    def test_get_X(self):
        self.assertEqual(self.game.getX(), "X")

    def test_size_of_game_array(self):
        self.assertEqual(self.game.getXSizeArray(), 3)
        self.assertEqual(self.game.getYSizeArray(), 3)

    def test_set_O_in_array(self):
        self.game.setToArrayOn(0, 0, self.game.getO())
        self.assertEqual(self.game.getArrayValue(0, 0), "O")
        self.game.printGameArray()

    def test_print_game_array(self):
        self.game.printGameArray()

    def test_round_counter(self):
        self.game.setToArrayOn(0, 0, self.game.getO())
        self.game.setToArrayOn(1, 0, self.game.getX())
        self.game.setToArrayOn(0, 1, self.game.getO())
        self.game.setToArrayOn(2, 0, self.game.getO())
        self.assertEqual(self.game.getRound(), 4)
        self.game.printGameArray()

    def test_round_counter_2(self):
        self.game.setToArrayOn(0, 0, self.game.getO())
        self.game.setToArrayOn(0, 1, self.game.getO())
        self.game.setToArrayOn(1, 0, self.game.getX())
        self.game.setToArrayOn(1, 1, self.game.getO())
        self.game.setToArrayOn(0, 2, self.game.getO())
        self.game.setToArrayOn(2, 0, self.game.getX())
        self.assertEqual(self.game.getRound(), 6)
        self.game.printGameArray()

    def test_dont_set_two_times(self):
        self.game.setToArrayOn(0, 0, self.game.getO())
        self.game.setToArrayOn(0, 0, self.game.getX())
        self.assertEqual(self.game.getRound(), 1)

    def test_check_win(self):
        self.game.setToArrayOn(0, 0, self.game.getO())
        self.game.setToArrayOn(1, 0, self.game.getX())
        self.game.setToArrayOn(0, 1, self.game.getO())
        self.game.setToArrayOn(2, 1, self.game.getX())
        self.game.setToArrayOn(0, 2, self.game.getO())
        self.assertEqual(True, self.game.checkWin())

    def test_check_win_2(self):
        self.game.setToArrayOn(0, 0, self.game.getO())
        self.game.setToArrayOn(1, 0, self.game.getX())
        self.game.setToArrayOn(0, 1, self.game.getO())
        self.game.setToArrayOn(2, 1, self.game.getX())
        self.game.setToArrayOn(2, 0, self.game.getO())
        self.game.printGameArray()
        self.assertEqual(False, self.game.checkWin())

    def test_check_win_3(self):
        self.game.setToArrayOn(0, 0, self.game.getO())
        self.game.setToArrayOn(1, 0, self.game.getX())
        self.game.setToArrayOn(1, 1, self.game.getO())
        self.game.setToArrayOn(2, 1, self.game.getX())
        self.game.setToArrayOn(2, 2, self.game.getO())
        self.game.printGameArray()
        self.assertEqual(True, self.game.checkWin())

    def test_full_map_win(self):
        self.game.setToArrayOn(0, 0, self.game.getO())
        self.game.setToArrayOn(1, 0, self.game.getX())
        self.game.setToArrayOn(2, 0, self.game.getO())
        self.game.setToArrayOn(0, 1, self.game.getX())
        self.game.setToArrayOn(1, 1, self.game.getO())
        self.game.setToArrayOn(2, 1, self.game.getX())
        self.game.setToArrayOn(0, 2, self.game.getO())
        self.game.setToArrayOn(1, 2, self.game.getX())
        self.game.setToArrayOn(2, 2, self.game.getO())
        self.game.printGameArray()
        self.assertEqual(True, self.game.checkWin())

    def test_full_map_lose(self):
        self.game.setToArrayOn(0, 0, self.game.getO())
        self.game.setToArrayOn(1, 0, self.game.getX())
        self.game.setToArrayOn(2, 0, self.game.getO())
        self.game.setToArrayOn(1, 1, self.game.getX())
        self.game.setToArrayOn(0, 1, self.game.getO())
        self.game.setToArrayOn(2, 1, self.game.getX())
        self.game.setToArrayOn(1, 2, self.game.getO())
        self.game.setToArrayOn(0, 2, self.game.getX())
        self.game.setToArrayOn(2, 2, self.game.getO())
        self.game.printGameArray()
        self.assertEqual(False, self.game.checkWin())
        self.assertEqual(True, self.game.isGameOver())
