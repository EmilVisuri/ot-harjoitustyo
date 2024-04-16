import unittest
from game import SudokuGame

class IsGameStarted(unittest.TestCase):
    def test_start_game(self):
        game = SudokuGame()
        self.assertFalse(game.is_game_started()) 
        game.start_game()
        self.assertTrue(game.is_game_started()) 

    def test_add_number_to_original_square(self):
        game = SudokuGame()
        game.start_game()
        self.assertFalse(game.add_number(0, 0, 1))

    def test_reset_original_number(self):
        game = SudokuGame()
        game.start_game()
        game.add_number(0, 0, 5)
        game.reset_board()
        self.assertEqual(game.get_board()[0][0], 5)

if __name__ == '__main__':
    unittest.main()
