from database import Check_login, Update_level_in_database, Get_user_level

class SudokuGame:
    def __init__(self):
        self.Boards = [
            [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ],
            [
                [0, 0, 0, 4, 3, 0, 0, 0, 0],
                [3, 4, 0, 0, 0, 6, 0, 1, 0],
                [0, 1, 2, 0, 0, 0, 0, 0, 3],
                [0, 0, 0, 8, 0, 0, 3, 2, 0],
                [2, 0, 0, 0, 0, 0, 0, 0, 8],
                [0, 5, 8, 0, 0, 3, 0, 0, 0],
                [5, 0, 0, 0, 0, 0, 7, 8, 0],
                [0, 7, 0, 5, 0, 0, 0, 4, 9],
                [0, 0, 0, 0, 9, 1, 0, 0, 0]
            ]
        ]
        self.Original_numbers = None
        self.Board = None
        self.Game_started = False
        self.Sudoku_solved = False
        self.Current_board_index = 0

    def Select_board(self):
        self.Original_numbers = self.Boards[self.Current_board_index]
        self.Board = [[Num for Num in Row] for Row in self.Original_numbers]

    def Start_game(self):
        self.Select_board()
        self.Game_started = True

    def End_game(self):
        self.Current_board_index += 1
        if self.Current_board_index < len(self.Boards):
            self.Start_game()
        else:
            self.Game_started = False

    def Is_game_started(self):
        return self.Game_started

    def Get_board(self):
        return self.Board

    def Add_number(self, Row, Col, Number):
        if not self.Game_started:
            return False
        if 0 <= Row < 9 and 0 <= Col < 9 and 1 <= Number <= 9:
            if self.Original_numbers[Row][Col] == 0:
                self.Board[Row][Col] = Number
                return Row, Col
            
        return False
    
    def Is_valid(self):
        for Row in self.Board:
            if not self.Is_valid_row(Row):
                return False
        
        for Col in range(9):
            Column = [self.Board[Row][Col] for Row in range(9)]
            if not self.Is_valid_row(Column):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                Square = [self.Board[row][Col] for row in range(i, i + 3) for Col in range(j, j + 3)]
                if not self.Is_valid_row(Square):
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                Square = [self.Board[row][Col] for row in range(i, i + 3) for Col in range(j, j + 3)]
                if not self.Is_valid_square(Square):
                    return False
                
        for Row in self.Board:
            for Num in Row:
                if Num == 0:
                    return False
        
        return True
    
    def Is_valid_row(self, Row):
        Seen = set()
        for Num in Row:
            if Num != 0:
                if Num in Seen:
                    return False
                Seen.add(Num)
        return True

    def Is_valid_square(self, Square):
        Seen = set()
        for Num in Square:
            if Num != 0:
                if Num in Seen:
                    return False
                Seen.add(Num)
        return True
    
    def Reset_board(self):
        for i in range(9):
            for j in range(9):
                if self.Original_numbers[i][j] == 0:
                    self.Board[i][j] = 0
                    
    def Update_level(self, username, new_level):
        if Check_login(username):
            Current_level = Get_user_level(username)
            if Current_level is not None:
                Update_level_in_database(username, new_level)
            else:
                print("Käyttäjän tasoa ei voitu hakea.")
        else:
            print("Kirjautuminen vaaditaan tason päivittämiseksi.")
 