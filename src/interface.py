import pygame
import sys
from game import SudokuGame

windowSize = 80
outerLines = 50
width = height = outerLines * 2 + windowSize * 9

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku")

sudoku_game = SudokuGame()

font = pygame.font.Font(None, 36)
black = pygame.Color('black')
green = pygame.Color('green')
gray = pygame.Color('gray')

clicked_row = None
clicked_col = None

def start():
    screen.fill((255, 255, 255))
    startText = font.render("Tervetuloa Sukokuun!", True, black)
    visitorButton = font.render("Vierailija", True, black)
    screen.blit(startText, (width // 2 - startText.get_width() // 2, height // 2 - 50))
    screen.blit(visitorButton, (width // 2 - visitorButton.get_width() // 2, height // 2 + 50))

# Tässä otettu mallia ChatGPT antamasta koodista
def board():
    screen.fill((255, 255, 255))
    board = sudoku_game.get_board()
    for i in range(9):
        for j in range(9):
            cell_rect = pygame.Rect(outerLines + j * windowSize, outerLines + i * windowSize, windowSize, windowSize)
            pygame.draw.rect(screen, black, cell_rect, 1)
            if board[i][j] != 0:
                numberColours = font.render(str(board[i][j]), True, green)
                screen.blit(numberColours, (outerLines + j * windowSize + windowSize // 3, outerLines + i * windowSize + windowSize // 3))
            if i == clicked_row and j == clicked_col:
                pygame.draw.rect(screen, gray, cell_rect)

    buttonBack = font.render("Takaisin", True, black)
    screen.blit(buttonBack, (outerLines, outerLines - buttonBack.get_height() - 10))

# Tässä otettu mallia ChatGPT antamasta koodista
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            if not sudoku_game.is_game_started():
                start_button_rect = pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 50)
                if start_button_rect.collidepoint(mousePosition):
                    sudoku_game.start_game()
            else:
                row = (mousePosition[1] - outerLines) // windowSize
                col = (mousePosition[0] - outerLines) // windowSize
                if 0 <= row < 9 and 0 <= col < 9:
                    clicked_row, clicked_col = row, col

                buttonBackpressed = pygame.Rect(outerLines, outerLines - font.get_height() - 10, 200, 50)
                if buttonBackpressed.collidepoint(mousePosition):
                    sudoku_game.end_game()

        elif event.type == pygame.KEYDOWN:
            if clicked_row is not None and clicked_col is not None:
                key_pressed = event.key
                if pygame.K_1 <= key_pressed <= pygame.K_9:
                    number = key_pressed - pygame.K_0
                    sudoku_game.add_number(clicked_row, clicked_col, number)
                    clicked_row, clicked_col = None, None

    if not sudoku_game.is_game_started():
        start()
    else:
        board()

    pygame.display.flip()

pygame.quit()
sys.exit()
