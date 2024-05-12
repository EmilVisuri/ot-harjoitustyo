from database import check_login, update_level_in_database, get_user_level

class SudokuGame:
    def __init__(self):
        """
        Initializes the SudokuGame object.
        
        """
        self.boards = [
            [
                [5, 0, 4, 6, 7, 0, 9, 1, 2],
                [6, 7, 0, 1, 0, 5, 3, 0, 8],
                [1, 0, 8, 3, 0, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 0, 3],
                [4, 0, 6, 8, 5, 0, 7, 9, 1],
                [7, 1, 0, 9, 0, 4, 8, 0, 6],
                [0, 6, 0, 5, 3, 0, 2, 0, 4],
                [0, 8, 0, 4, 1, 9, 0, 3, 5],
                [3, 4, 5, 2, 0, 6, 1, 7, 0]
            ],
            [
                [0, 1, 6, 0, 0, 2, 5, 0, 4],
                [0, 0, 8, 9, 6, 4, 0, 0, 2],
                [0, 0, 0, 0, 5, 8, 9, 7, 0],
                [8, 0, 9, 0, 0, 0, 6, 0, 1],
                [1, 0, 3, 0, 8, 0, 0, 0, 7],
                [0, 4, 0, 0, 0, 3, 0, 0, 0],
                [0, 8, 0, 4, 0, 0, 7, 2, 3],
                [0, 0, 0, 0, 2, 6, 4, 0, 9],
                [4, 9, 2, 7, 0, 0, 0, 0, 0]
            ],
            [
                [1, 4, 7, 0, 0, 0, 0, 5, 3],
                [0, 9, 8, 7, 0, 0, 0, 2, 0],
                [0, 0, 0, 0, 0, 0, 7, 8, 4],
                [0, 7, 0, 0, 0, 6, 0, 0, 0],
                [0, 8, 0, 9, 0, 0, 4, 0, 0],
                [4, 3, 0, 0, 0, 8, 0, 9, 0],
                [0, 5, 4, 8, 1, 0, 0, 0, 6],
                [0, 0, 0, 0, 3, 0, 2, 1, 8],
                [0, 0, 3, 2, 6, 7, 5, 4, 0]
            ],
            [
                [6, 0, 9, 4, 0, 8, 5, 2, 0],
                [2, 4, 0, 5, 1, 0, 3, 7, 9],
                [0, 0, 0, 2, 7, 0, 6, 8, 0],
                [5, 0, 6, 0, 2, 1, 4, 3, 0],
                [0, 3, 0, 6, 9, 0, 2, 0, 0],
                [8, 0, 2, 7, 4, 0, 0, 0, 5],
                [0, 0, 5, 0, 0, 7, 0, 4, 2],
                [0, 0, 1, 0, 0, 0, 7, 5, 6],
                [0, 6, 0, 1, 5, 2, 8, 9, 3]
            ],
            [
                [0, 0, 0, 7, 0, 0, 1, 2, 4],
                [4, 0, 1, 0, 2, 8, 9, 5, 0],
                [0, 0, 0, 1, 0, 4, 0, 6, 3],
                [8, 1, 0, 2, 0, 0, 3, 0, 0],
                [5, 0, 4, 0, 1, 3, 0, 0, 6],
                [7, 9, 0, 0, 4, 5, 0, 1, 8],
                [6, 0, 0, 4, 0, 0, 0, 0, 0],
                [0, 4, 2, 0, 8, 0, 6, 0, 0],
                [3, 5, 7, 9, 6, 0, 4, 0, 1]
            ]
        ]
        self.original_numbers = None
        self.board = None
        self.game_started = False
        self.sudoku_solved = False
        self.current_board_index = 0

    def select_board(self):
        """
        Selects a board from the 'boards' list and initializes the game board.
        
        """
        self.original_numbers = self.boards[self.current_board_index]
        self.board = [[Num for Num in Row] for Row in self.original_numbers]

    def start_game(self):
        """
        Starts the Sudoku game by selecting the first board.
        
        """
        self.select_board()
        self.game_started = True
        self.numbers_placed = 0

    def end_game(self):
        """
        Ends the current game and selects the next board.
        
        """
        self.current_board_index += 1
        if self.current_board_index < len(self.boards):
            self.start_game()
        else:
            print("Kaikki sudokut on ratkaistu!")
            self.current_board_index = 0  # Aseta indeksi takaisin nollaan
            self.game_started = False

    def is_game_started(self):
        """
        Returns True if the game has started, False otherwise.
        
        """
        return self.game_started

    def get_board(self):
        """
        Returns the current state of the Sudoku board.
        
        """
        return self.board

    def add_number(self, row, col, number):
        """
        Adds a number to the Sudoku board.

        Args:
        - row: The row index of the cell.
        - col: The column index of the cell.
        - number: The number to be added.

        Returns:
        - Tuple (row, col) if the number is added successfully, False otherwise.
        
        """
        if not self.game_started:
            return False
        if 0 <= row < 9 and 0 <= col < 9 and 1 <= number <= 9:
            if self.original_numbers[row][col] == 0:
                self.board[row][col] = number
                return row, col
        return False

    def is_valid(self):
        """
        Checks if the current state of the Sudoku board is valid.

        Returns:
        - True if the board is valid, False otherwise.
        
        """
        for row in self.board:
            if not self.is_valid_row(row):
                return False

        for col in range(9):
            column = [self.board[row][col] for row in range(9)]
            if not self.is_valid_row(column):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [self.board[row][col] for row in range(i, i + 3)
                          for col in range(j, j + 3)]
                if not self.is_valid_row(square):
                    return False

        for row in self.board:
            for num in row:
                if num == 0:
                    return False
        return True

    def is_valid_row(self, row):
        """
        Checks if a row in the Sudoku board is valid.

        Args:
        - row: The row to be checked.

        Returns:
        - True if the row is valid, False otherwise.
        
        """
        seen = set()
        for num in row:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True

    def is_valid_square(self, square):
        """
        Checks if a 3x3 square in the Sudoku board is valid.

        Args:
        - square: The 3x3 square to be checked.

        Returns:
        - True if the square is valid, False otherwise.
        
        """
        seen = set()
        for num in square:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True

    def reset_board(self):
        """
        Resets the non-original numbers on the Sudoku board.
        
        """
        for i in range(9):
            for j in range(9):
                if self.original_numbers[i][j] == 0:
                    self.board[i][j] = 0

    def update_level(self, username, new_level):
        """
        Updates the user's level in the database.

        Args:
        - username: The username of the user.
        - new_level: The new level to be updated.

        """
        if check_login(username):
            current_level = get_user_level(username)
            if current_level is not None:
                update_level_in_database(username, new_level)
            else:
                print("Käyttäjän tasoa ei voitu hakea.")
        else:
            print("Kirjautuminen vaaditaan tason päivittämiseksi.")
 