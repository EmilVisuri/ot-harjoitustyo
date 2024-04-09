class SudokuGame:
    def __init__(self):
        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.game_started = False

    def start_game(self):
        self.game_started = True

    def end_game(self):
        self.game_started = False

    def is_game_started(self):
        return self.game_started

    def get_board(self):
        return self.board

    def add_number(self, row, col, number):
        if not self.game_started:
            return False
        if 0 <= row < 9 and 0 <= col < 9 and 1 <= number <= 9:
            if self.board[row][col] == 0:
                self.board[row][col] = number
                return True
        return False