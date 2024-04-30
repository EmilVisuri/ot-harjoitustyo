import unittest
from unittest.mock import patch
import os
import sys
import sqlite3
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

from game import SudokuGame
from database import update_level_in_database, get_user_level, check_login, add_user

class IsGameStarted(unittest.TestCase):
    def test_start_game(self):
        sudoku_game = SudokuGame()
        self.assertFalse(sudoku_game.is_game_started()) 
        sudoku_game.start_game()
        self.assertTrue(sudoku_game.is_game_started()) 

    def test_add_number_to_original_square(self):
        sudoku_game = SudokuGame()
        sudoku_game.start_game()
        self.assertFalse(sudoku_game.add_number(0, 0, 1))

    def test_reset_original_number(self):
        sudoku_game = SudokuGame()
        sudoku_game.start_game()
        sudoku_game.add_number(0, 0, 5)
        sudoku_game.reset_board()
        self.assertEqual(sudoku_game.get_board()[0][0], 5)
        
    def test_add_number_to_non_original_square(self):
        sudoku_game = SudokuGame()
        sudoku_game.start_game()
        sudoku_game.add_number(0, 0, 5)
        self.assertTrue(sudoku_game.add_number(8, 8, 3))  # Täytä ei-alkuperäinen ruutu
        self.assertEqual(sudoku_game.get_board()[8][8], 3)

    def test_check_invalid_move(self):
        sudoku_game = SudokuGame()
        sudoku_game.start_game()
        self.assertFalse(sudoku_game.add_number(0, 0, 10))
        self.assertFalse(sudoku_game.add_number(10, 0, 5))
        self.assertFalse(sudoku_game.add_number(0, 0, 5))

    def test_game_winning_condition(self):
        sudoku_game = SudokuGame()
        sudoku_game.start_game()
 
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
        sudoku_game.board = solution_board
        self.assertTrue(sudoku_game.is_valid())
    
    def setUp(self):
        self.game = SudokuGame()
    
    def test_valid_row(self):
        row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(self.game.is_valid_row(row))

    def test_invalid_row_duplicate(self):
        row = [1, 2, 3, 4, 5, 6, 7, 8, 1]
        self.assertFalse(self.game.is_valid_row(row))

        
    @patch('database.sqlite3.connect')
    def test_check_login(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = ('username', 'hashed_password', 1)
        self.assertTrue(check_login('username', 'password'))

    @patch('database.sqlite3.connect')
    def test_update_level_in_database(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        update_level_in_database('username', 2)
        mock_cursor.execute.assert_called_once_with("UPDATE users SET level = ? WHERE username = ?", (2, 'username'))

    @patch('database.sqlite3.connect')
    def test_get_user_level(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = (1,)
        self.assertEqual(get_user_level('username'), 1)
        
    @patch('builtins.print')  # Mock print function
    def test_add_user_duplicate_username(self, mock_print):
        # Mock SQLite connection and cursor
        conn = sqlite3.connect(':memory:')  # Use in-memory database for testing
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT, level INTEGER)")
        cursor.execute("INSERT INTO users VALUES ('existing_user', 'password', 3)")
        conn.commit()

        # Test add_user function with duplicate username
        add_user('existing_user', 'new_password', 1)

        # Check if print was called with appropriate message
        mock_print.assert_called_with("Käyttäjätunnus on jo käytössä.")

        cursor.close()
        conn.close()

    if __name__ == '__main__':
        unittest.main()
