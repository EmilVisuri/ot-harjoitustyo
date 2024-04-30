""" 
  Modules:
- sqlite3: for working with SQLite database
- sys: for system-specific parameters and functions
- pygame: for building the graphical user interface
- sudoku: contains the SudokuGame class for managing Sudoku puzzles
- database: contains functions for working with user data in a SQLite database

  Classes:
- SudokuGame: manages the state and logic of the Sudoku game
"""

import sqlite3
import sys
import pygame
from game import SudokuGame
from database import add_user, check_login, get_level, get_username
# pylint: disable=no-member

# Constantssrc/interface.py:6:0: E0401: Unable to import 'database' (import-error)
WINDOW_SIZE = 80
OUTER_LINES = 70
WIDTH = HEIGHT = OUTER_LINES * 2 + WINDOW_SIZE * 9

# Initialize Pygame
pygame.init()
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
Sudoku_game = SudokuGame()

# Colors
font = pygame.font.Font(None, 36)
BLACK = pygame.Color('black')
RED = pygame.Color('red')
GRAY = pygame.Color('gray')
GREEN = pygame.Color('green')
WHITE = pygame.Color('White')

CLICKED_ROW = None
CLICKED_COL = None


# Tässä otettu mallia ChatGPT antamasta koodista
def login():
    """
    Handles the login functionality. 
    Provides a graphical interface for users to enter their username and password. 
    Returns None.
    
    """
    pygame.init()
    width = 857
    height = 850
    login_screen = pygame.display.set_mode((width, height))
    font = pygame.font.Font(None, 36)

    username_rect = pygame.Rect(width // 2 - 100, height // 2, 200, 40)
    password_rect = pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 40)
    back_rect = pygame.Rect(OUTER_LINES, OUTER_LINES - font.get_height() - 10, 200, 50)
    send_rect = pygame.Rect(width // 2 - 50, height // 2 + 120, 100, 50)

    username_text = ''
    password_text = ''

    is_typing_username = False
    is_typing_password = False

    sudoku_game = SudokuGame()
    login_successful = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if username_rect.collidepoint(event.pos):
                    is_typing_username = True
                    is_typing_password = False
                elif password_rect.collidepoint(event.pos):
                    is_typing_password = True
                    is_typing_username = False
                else:
                    is_typing_username = False
                    is_typing_password = False
                if back_rect.collidepoint(event.pos):
                    return
                if send_rect.collidepoint(event.pos):
                    login_successful = check_login(username_text, password_text)
                    if login_successful:
                        print("Kirjautuminen onnistui!")
                        current_level = get_level(username_text)
                        print(current_level)
                        if current_level is not None:
                            sudoku_game.current_board_index = current_level - 1
                            sudoku_game.select_board()
                            sudoku_game.start_game()
                        else:
                            print("Käyttäjän tasoa ei voitu hakea.")
                    else:
                        print("Kirjautuminen epäonnistui. Tarkista käyttäjätunnus ja salasana.")
                    break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    login_successful = check_login(username_text, password_text)
                    if login_successful:
                        print("Kirjautuminen onnistui!")
                        current_level = get_level(username_text)
                        if current_level is not None:
                            sudoku_game.current_board_index = current_level - 1
                            sudoku_game.select_board()
                            sudoku_game.start_game()
                            return
                        else:
                            print("Käyttäjän tasoa ei voitu hakea.")
                    else:
                        print("Kirjautuminen epäonnistui. Tarkista käyttäjätunnus ja salasana.")
                elif event.key == pygame.K_BACKSPACE:
                    if is_typing_username:
                        username_text = username_text[:-1]
                    elif is_typing_password:
                        password_text = password_text[:-1]
                else:
                    if is_typing_username:
                        username_text += event.unicode
                    elif is_typing_password:
                        password_text += event.unicode

        login_screen.fill((255, 255, 255))

        login_text = font.render("Kirjaudu sisään", True, BLACK)
        login_screen.blit(login_text, (330, 360))
        username_label = font.render("Käyttäjänimi:", True, BLACK)
        login_screen.blit(username_label, (147, 433))
        password_label = font.render("Salasana:", True, BLACK)
        login_screen.blit(password_label, (180, 480))

        username_surface = font.render(username_text, True, BLACK)
        pygame.draw.rect(login_screen, BLACK, username_rect, 2)
        login_screen.blit(username_surface, (username_rect.x + 5, username_rect.y + 5))

        password_surface = font.render('*' * len(password_text), True, BLACK)
        pygame.draw.rect(login_screen, BLACK, password_rect, 2)
        login_screen.blit(password_surface, (password_rect.x + 5, password_rect.y + 5))

        back_button = font.render("Takaisin", True, BLACK)
        login_screen.blit(back_button, (50, 50))

        send_button = font.render("Lähetä", True, BLACK)
        login_screen.blit(send_button, (width // 2 - send_button.get_width() //
                                        2, height // 2 + 125))

        pygame.display.flip()

def register():
    """"
    Handles the registration functionality.
    Allows new users to create accounts by providing a username and password.
    Returns None.
    
    """
    pygame.init()
    width = 857
    height = 850
    register_screen = pygame.display.set_mode((width, height))
    font = pygame.font.Font(None, 36)

    username_rect = pygame.Rect(width // 2 - 100, height // 2, 200, 40)
    password_rect = pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 40)
    back_rect = pygame.Rect(OUTER_LINES, OUTER_LINES - font.get_height() - 10, 200, 50)
    send_rect = pygame.Rect(width // 2 - 50, height // 2 + 120, 100, 50)

    username_text = ''
    password_text = ''

    conn = sqlite3.connect('users.db')
    Cursor = conn.cursor()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if username_rect.collidepoint(event.pos):
                    is_typing_username = True
                    is_typing_password = False
                elif password_rect.collidepoint(event.pos):
                    is_typing_password = True
                    is_typing_username = False
                else:
                    is_typing_username = False
                    is_typing_password = False
                if back_rect.collidepoint(event.pos):
                    Cursor.close()
                    conn.close()
                    return
                if send_rect.collidepoint(event.pos):
                    if username_text and password_text:
                        add_user(username_text, password_text, 1)
                        print("Käyttäjä lisätty tietokantaan!")
                    else:
                        print("Anna käyttäjätunnus ja salasana.")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    if is_typing_username:
                        username_text = username_text[:-1]
                    elif is_typing_password:
                        password_text = password_text[:-1]
                else:
                    if is_typing_username:
                        username_text += event.unicode
                    elif is_typing_password:
                        password_text += event.unicode

        register_screen.fill((255, 255, 255))

        loginText = font.render("Rekisteröidy:", True, BLACK)
        register_screen.blit(loginText, (330, 360))
        username_label = font.render("Käyttäjänimi:", True, BLACK)
        register_screen.blit(username_label, (147, 433))
        password_label = font.render("Salasana:", True, BLACK)
        register_screen.blit(password_label, (180, 480))

        username_surface = font.render(username_text, True, BLACK)
        pygame.draw.rect(register_screen, BLACK, username_rect, 2)
        register_screen.blit(username_surface, (username_rect.x + 5, username_rect.y + 5))

        password_surface = font.render('*' * len(password_text), True, BLACK)
        pygame.draw.rect(register_screen, BLACK, password_rect, 2)
        register_screen.blit(password_surface, (password_rect.x + 5, password_rect.y + 5))

        back_button = font.render("Takaisin", True, BLACK)
        register_screen.blit(back_button, (50, 50))

        send_button = font.render("Lähetä", True, BLACK)
        register_screen.blit(send_button, (width // 2 - send_button.get_width() // 2, height
                                           // 2 + 125))

        pygame.display.flip()
    # Tähän loppuu ChatGPT antaman koodin malli

def start():
    """"
    Displays the starting screen of the game with options to play as a guest, log in, or register.
    Returns None.
    
    """
    Screen.fill((255, 255, 255))
    start_text = font.render("Tervetuloa Sukokuun!", True, BLACK)
    visitor_button = font.render("Vierailija", True, BLACK)
    login_button = font.render("Kirjaudu", True, BLACK)
    register_button = font.render("Rekisteröidy", True, BLACK)
    Screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - 50))
    Screen.blit(visitor_button, (WIDTH // 2 - visitor_button.get_width() // 2, HEIGHT // 2 + 55))
    Screen.blit(login_button, (WIDTH // 2 - login_button.get_width() // 2, HEIGHT // 2 + 10))
    Screen.blit(register_button, (WIDTH // 2 - register_button.get_width() // 2,
                                  HEIGHT // 2 + 100))

# Tässä otettu mallia ChatGPT antamasta koodista
def board():
    """
    Displays the Sudoku game board and handles user interactions during gameplay,
    such as selecting cells, adding numbers, checking the solution, and resetting the board.
    Returns None.
    
    """
    global CLICKED_ROW, CLICKED_COL
    Screen.fill((255, 255, 255))
    if Sudoku_game.is_game_started():
        board = Sudoku_game.get_board()
    for i in range(9):
        for j in range(9):
            cell_rect = pygame.Rect(OUTER_LINES + j * WINDOW_SIZE, OUTER_LINES + i *
                                    WINDOW_SIZE, WINDOW_SIZE, WINDOW_SIZE)
            pygame.draw.rect(Screen, BLACK, cell_rect, 1)
            if board[i][j] != 0:
                if board[i][j] == -1:
                    number_color = font.render(str(board[i][j]), True, (255, 0, 0))
                else:
                    number_color = font.render(str(board[i][j]), True, BLACK)
                Screen.blit(number_color, (OUTER_LINES + j * WINDOW_SIZE + WINDOW_SIZE // 3,
                                          OUTER_LINES + i * WINDOW_SIZE + WINDOW_SIZE // 3))
            if i == CLICKED_ROW and j == CLICKED_COL:
                pygame.draw.rect(Screen, GRAY, cell_rect)

    button_back = font.render("Takaisin", True, BLACK)
    Screen.blit(button_back, (OUTER_LINES, OUTER_LINES - button_back.get_height() - 10))

    button_check = font.render("Tarkasta", True, BLACK)
    button_check_rect = button_check.get_rect(topleft=(WIDTH - OUTER_LINES -
                                                       button_check.get_width(),
                                                       HEIGHT - OUTER_LINES -
                                                       button_check.get_height()- 10 + 35))
    Screen.blit(button_check, button_check_rect)

    button_reset = font.render("Nollaa", True, BLACK)
    button_reset_rect = button_reset.get_rect(topleft=(WIDTH - OUTER_LINES -
                                                       button_reset.get_width(),
                                                       OUTER_LINES -
                                                       button_reset.get_height() - 10))
    Screen.blit(button_reset, button_reset_rect)

    if Sudoku_game.is_valid() and Sudoku_game.is_game_started():
        next_button_rect = pygame.Rect(490, 800 - 10, 200, 50)
        if next_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Screen, GREEN, next_button_rect)
            if pygame.mouse.get_pressed()[0]:
                username = get_username()
                if check_login(username, ""):
                    current_level = get_level(username)
                    new_level = current_level + 1
                    Sudoku_game.update_level(username, new_level)
                Sudoku_game.second_sudoku_solved = False
                Sudoku_game.reset_board()
                CLICKED_ROW, CLICKED_COL = None, None
                Sudoku_game.end_game()
        else:
            pygame.draw.rect(Screen, WHITE, next_button_rect)

        next_button_text = font.render("Seuraava", True, BLACK)
        Screen.blit(next_button_text, (530, 792))



button_reset = font.render("Nollaa", True, BLACK)
button_reset_rect = button_reset.get_rect(topleft=(WIDTH - OUTER_LINES -
                                                 button_reset.get_width(), OUTER_LINES -
                                                 button_reset.get_height() - 10))
Screen.blit(button_reset, button_reset_rect)

button_check = font.render("Tarkasta", True, BLACK)
button_check_rect = button_check.get_rect(topleft=(WIDTH - OUTER_LINES -
                                                 button_check.get_width(), HEIGHT -
                                                 OUTER_LINES - button_check.get_height()
                                                 - 10 + 35))
Screen.blit(button_check, button_check_rect)

button_login = font.render("Kirjaudu", True, BLACK)
button_login_rect = button_login.get_rect(topleft=(WIDTH // 2 - button_login.get_width()
                                                 // 2, HEIGHT // 2 + 10))
Screen.blit(button_login, button_login_rect)

button_register = font.render("Rekisteröidy", True, BLACK)
button_register_rect = button_register.get_rect(topleft=(WIDTH // 2 - button_register.get_width()
                                                       // 2, HEIGHT // 2 + 95))
Screen.blit(button_register, button_register_rect)

SUDOKU_SOLVED_MESSAGE_TIME = 0
RUNNING = True
SUDOKU_CHECKED = False
SUDOKU_SOLVED_MESSAGE_SHOWN = False

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if not Sudoku_game.is_game_started():
                start_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
                if start_button_rect.collidepoint(mouse_position):
                    Sudoku_game.start_game()
                elif button_register_rect.collidepoint(mouse_position):
                    register()
                elif button_login_rect.collidepoint(mouse_position):
                    login()
            else:
                row = (mouse_position[1] - OUTER_LINES) // WINDOW_SIZE
                col = (mouse_position[0] - OUTER_LINES) // WINDOW_SIZE
                if 0 <= row < 9 and 0 <= col < 9:
                    CLICKED_ROW, CLICKED_COL = row, col

                def back_to_menu():
                    """
                    Gets the user to menu, if button back is pressed
                    
                    """
                    global Sudoku_game
                    Sudoku_game = SudokuGame()

                button_back_pressed = pygame.Rect(OUTER_LINES, OUTER_LINES -
                                                font.get_height() - 10, 200, 50)
                if button_back_pressed.collidepoint(mouse_position):
                    back_to_menu()

                if button_check_rect.collidepoint(mouse_position):
                    if Sudoku_game.is_game_started():
                        if Sudoku_game.is_valid():
                            print("Sudoku on ratkaistu oikein!")
                        else:
                            print("Sudoku on ratkaistu väärin!")
                        SUDOKU_CHECKED = True
                        SUDOKU_SOLVED_MESSAGE_SHOWN = True
                        SUDOKU_SOLVED_MESSAGE_TIME = pygame.time.get_ticks()

                if button_reset_rect.collidepoint(mouse_position):
                    Sudoku_game.reset_board()
                    CLICKED_ROW, CLICKED_COL = None, None

        elif event.type == pygame.KEYDOWN:
            if CLICKED_ROW is not None and CLICKED_COL is not None:
                key_pressed = event.key
                if pygame.K_1 <= key_pressed <= pygame.K_9:
                    number = key_pressed - pygame.K_0
                    Sudoku_game.add_number(CLICKED_ROW, CLICKED_COL, number)
                    CLICKED_ROW, CLICKED_COL = None, None
    # Tähän loppuu ChatGPT antaman koodin malli

    if not Sudoku_game.is_game_started():
        start()
    else:
        board()

    if SUDOKU_CHECKED and (not SUDOKU_SOLVED_MESSAGE_SHOWN or pygame.time.get_ticks() -
                           SUDOKU_SOLVED_MESSAGE_TIME < 3000):
        if Sudoku_game.is_valid():
            SUDOKU_SOLVED_MESSAGE = font.render("Sudoku on ratkaistu oikein!", True, GREEN)
            Screen.blit(SUDOKU_SOLVED_MESSAGE, (OUTER_LINES + 220, HEIGHT // 18 -
                                                SUDOKU_SOLVED_MESSAGE.get_height() // 2))
        else:
            SUDOKU_SOLVED_MESSAGE = font.render("Sudoku on ratkaistu väärin!", True, RED)
            Screen.blit(SUDOKU_SOLVED_MESSAGE, (OUTER_LINES + 220, HEIGHT // 18 -
                                                SUDOKU_SOLVED_MESSAGE.get_height() // 2))
    else:
        SUDOKU_SOLVED_MESSAGE = False

    if SUDOKU_CHECKED and pygame.time.get_ticks() - SUDOKU_SOLVED_MESSAGE_TIME >= 3000:
        SUDOKU_SOLVED_MESSAGE = True

    pygame.display.flip()

pygame.quit()
sys.exit()
