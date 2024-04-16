from game import SudokuGame
from pygame import Color, font, display
import pygame
import sys

WindowSize = 80
OuterLines = 70
Width = Height = OuterLines * 2 + WindowSize * 9

pygame.init()
Screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Sudoku")

sudoku_game = SudokuGame()

font = pygame.font.Font(None, 36)
Black = pygame.Color('black')
Red = pygame.Color('red')
Gray = pygame.Color('gray')
Green = pygame.Color('green')

Clicked_row = None
Clicked_col = None

def start():
    Screen.fill((255, 255, 255))
    startText = font.render("Tervetuloa Sukokuun!", True, Black)
    visitorButton = font.render("Vierailija", True, Black)
    Screen.blit(startText, (Width // 2 - startText.get_width() // 2, Height // 2 - 50))
    Screen.blit(visitorButton, (Width // 2 - visitorButton.get_width() // 2, Height // 2 + 50))

# Tässä otettu mallia ChatGPT antamasta koodista
def board():
    Screen.fill((255, 255, 255))
    board = sudoku_game.get_board()
    for i in range(9):
        for j in range(9):
            cell_rect = pygame.Rect(OuterLines + j * WindowSize, OuterLines + i * WindowSize, WindowSize, WindowSize)
            pygame.draw.rect(Screen, Black, cell_rect, 1)
            if board[i][j] != 0:
                if board[i][j] == -1:
                    numberColor = font.render(str(board[i][j]), True, (255, 0, 0))
                else:
                    numberColor = font.render(str(board[i][j]), True, Black)
                Screen.blit(numberColor, (OuterLines + j * WindowSize + WindowSize // 3, OuterLines + i * WindowSize + WindowSize // 3))
            if i == Clicked_row and j == Clicked_col:
                pygame.draw.rect(Screen, Gray, cell_rect)

    buttonBack = font.render("Takaisin", True, Black)
    Screen.blit(buttonBack, (OuterLines, OuterLines - buttonBack.get_height() - 10))
    
    buttonCheck = font.render("Tarkasta", True, Black)
    buttonCheck_rect = buttonCheck.get_rect(topleft=(Width - OuterLines - buttonCheck.get_width(), Height - OuterLines - buttonCheck.get_height() - 10 + 35))
    Screen.blit(buttonCheck, buttonCheck_rect)
    
    buttonReset = font.render("Nollaa", True, Black)
    buttonReset_rect = buttonReset.get_rect(topleft=(Width - OuterLines - buttonReset.get_width(), OuterLines - buttonReset.get_height() - 10))
    Screen.blit(buttonReset, buttonReset_rect)
    
buttonReset = font.render("Nollaa", True, Black)
buttonReset_rect = buttonReset.get_rect(topleft=(Width - OuterLines - buttonReset.get_width(), OuterLines - buttonReset.get_height() - 10))
Screen.blit(buttonReset, buttonReset_rect)
    
buttonCheck = font.render("Tarkasta", True, Black)
buttonCheck_rect = buttonCheck.get_rect(topleft=(Width - OuterLines - buttonCheck.get_width(), Height - OuterLines - buttonCheck.get_height() - 10 + 35))
Screen.blit(buttonCheck, buttonCheck_rect)

sudoku_solved_message_time = 0
running = True
sudoku_checked = False
sudoku_solved_message_shown = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            if not sudoku_game.is_game_started():
                start_button_rect = pygame.Rect(Width // 2 - 100, Height // 2 + 50, 200, 50)
                if start_button_rect.collidepoint(mousePosition):
                    sudoku_game.start_game()
            else:
                row = (mousePosition[1] - OuterLines) // WindowSize
                col = (mousePosition[0] - OuterLines) // WindowSize
                if 0 <= row < 9 and 0 <= col < 9:
                    Clicked_row, Clicked_col = row, col

                buttonBackpressed = pygame.Rect(OuterLines, OuterLines - font.get_height() - 10, 200, 50)
                if buttonBackpressed.collidepoint(mousePosition):
                    sudoku_game.end_game()

                if buttonCheck_rect.collidepoint(mousePosition):
                    if sudoku_game.is_game_started():
                        if sudoku_game.is_valid():
                            print("Sudoku on ratkaistu oikein!")
                        else:
                            print("Sudoku on ratkaistu väärin!")
                        sudoku_checked = True
                        sudoku_solved_message_shown = True
                        sudoku_solved_message_time = pygame.time.get_ticks()
                    
                if buttonReset_rect.collidepoint(mousePosition):
                    sudoku_game.reset_board()
                    Clicked_row, Clicked_col = None, None

        elif event.type == pygame.KEYDOWN:
            if Clicked_row is not None and Clicked_col is not None:
                key_pressed = event.key
                if pygame.K_1 <= key_pressed <= pygame.K_9:
                    number = key_pressed - pygame.K_0
                    sudoku_game.add_number(Clicked_row, Clicked_col, number)
                    Clicked_row, Clicked_col = None, None
                    
    #Tähän loppuu ChatGPT antaman koodin malli

    if not sudoku_game.is_game_started():
        start()
    else:
        board()

    if sudoku_checked and (not sudoku_solved_message_shown or pygame.time.get_ticks() - sudoku_solved_message_time < 3):
        if sudoku_game.is_valid():
            sudoku_solved_message = font.render("Sudoku on ratkaistu oikein!", True, Green)
            Screen.blit(sudoku_solved_message, (OuterLines + 220, Height // 18 - sudoku_solved_message.get_height() // 2))
        else:
            sudoku_solved_message = font.render("Sudoku on ratkaistu väärin!", True, Red)
            Screen.blit(sudoku_solved_message, (OuterLines + 220, Height // 18 - sudoku_solved_message.get_height() // 2))
    else:
        sudoku_solved_message_shown = False

    if sudoku_checked and pygame.time.get_ticks() - sudoku_solved_message_time >= 3000:
        sudoku_solved_message_shown = True

    pygame.display.flip()

pygame.quit()
sys.exit()
