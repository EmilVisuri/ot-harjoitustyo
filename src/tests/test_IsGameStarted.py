import unittest
from game import SudokuGame

class IsGameStarted(unittest.TestCase):
    def test_start_game(self):
        game = SudokuGame()
        self.assertFalse(game.is_game_started())  # Pelin pitäisi aluksi olla aloittamaton
        game.start_game()
        self.assertTrue(game.is_game_started())   # Pelin pitäisi olla käynnissä

if __name__ == '__main__':
    unittest.main()