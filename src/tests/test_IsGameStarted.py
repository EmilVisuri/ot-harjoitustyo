import unittest
from game import SudokuGame
from database import Update_level_in_database, Get_user_level, Check_login
from unittest.mock import patch

class IsGameStarted(unittest.TestCase):
    def test_start_game(self):
        game = SudokuGame()
        self.assertFalse(game.Is_game_started()) 
        game.Start_game()
        self.assertTrue(game.Is_game_started()) 

    def test_add_number_to_original_square(self):
        game = SudokuGame()
        game.Start_game()
        self.assertFalse(game.Add_number(0, 0, 1))

    def test_reset_original_number(self):
        game = SudokuGame()
        game.Start_game()
        game.Add_number(0, 0, 5)
        game.Reset_board()
        self.assertEqual(game.Get_board()[0][0], 5)
        
    def test_add_number_to_non_original_square(self):
        game = SudokuGame()
        game.Start_game()
        game.Add_number(0, 0, 5)
        self.assertTrue(game.Add_number(1, 1, 3))  # Täytä ei-alkuperäinen ruutu
        self.assertEqual(game.Get_board()[1][1], 3)

    def test_check_invalid_move(self):
        game = SudokuGame()
        game.Start_game()
        self.assertFalse(game.Add_number(0, 0, 10))
        self.assertFalse(game.Add_number(10, 0, 5))
        self.assertFalse(game.Add_number(0, 0, 5))

    def test_game_winning_condition(self):
        game = SudokuGame()
        game.Start_game()
 
        solution_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        game.Board = solution_board
        self.assertTrue(game.Is_valid())
        
        
    @patch('database.sqlite3.connect')
    def test_check_login(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = ('username', 'hashed_password', 1)
        self.assertTrue(Check_login('username', 'password'))

    @patch('database.sqlite3.connect')
    def test_update_level_in_database(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        Update_level_in_database('username', 2)
        mock_cursor.execute.assert_called_once_with("UPDATE users SET level = ? WHERE username = ?", (2, 'username'))

    @patch('database.sqlite3.connect')
    def test_get_user_level(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = (1,)
        self.assertEqual(Get_user_level('username'), 1)       

    if __name__ == '__main__':
        unittest.main()
