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
        self.original_numbers = [[num for num in row] for row in self.board] 
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
            if self.original_numbers[row][col] == 0: 
                self.board[row][col] = number
                return row, col
            
        return False
    
    def is_valid(self):
        for row in self.board:
            if not self.is_valid_row(row):
                return False

        for col in range(9):
            column = [self.board[row][col] for row in range(9)]
            if not self.is_valid_row(column):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [self.board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
                if not self.is_valid_row(square):
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [self.board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
                if not self.is_valid_square(square):
                    return False
                
        for row in self.board:
            for num in row:
                if num == 0:
                    return False
        
        return True
    
    def is_valid_row(self, row):
        seen = set()
        for num in row:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True

    def is_valid_square(self, square):
        seen = set()
        for num in square:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True
    
    def reset_board(self):
        for i in range(9):
            for j in range(9):
                if self.original_numbers[i][j] == 0:
                    self.board[i][j] = 0
                    