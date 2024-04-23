from game import SudokuGame
from pygame import Color, font, display
import pygame
import sqlite3
from database import Add_user, Check_login, Get_level, Get_username
import sys

WindowSize = 80
OuterLines = 70
Width = Height = OuterLines * 2 + WindowSize * 9

pygame.init()
Screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Sudoku")
Sudoku_game = SudokuGame()

font = pygame.font.Font(None, 36)
Black = pygame.Color('black')
Red = pygame.Color('red')
Gray = pygame.Color('gray')
Green = pygame.Color('green')
White = pygame.Color('White')

Clicked_row = None
Clicked_col = None

# Tässä otettu mallia ChatGPT antamasta koodista
def Login():
    pygame.init()
    Width = 857
    Height = 850
    Screen = pygame.display.set_mode((Width, Height))
    font = pygame.font.Font(None, 36)
    Black = pygame.Color('black')

    Username_rect = pygame.Rect(Width // 2 - 100, Height // 2, 200, 40)
    Password_rect = pygame.Rect(Width // 2 - 100, Height // 2 + 50, 200, 40)
    Back_rect = pygame.Rect(OuterLines, OuterLines - font.get_height() - 10, 200, 50)
    Send_rect = pygame.Rect(Width // 2 - 50, Height // 2 + 120, 100, 50)

    Username_text = ''
    Password_text = ''

    Is_typing_username = False
    Is_typing_password = False

    Sudoku_game = SudokuGame()
    Login_successful = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Username_rect.collidepoint(event.pos):
                    Is_typing_username = True
                    Is_typing_password = False
                elif Password_rect.collidepoint(event.pos):
                    Is_typing_password = True
                    Is_typing_username = False
                else:
                    Is_typing_username = False
                    Is_typing_password = False
                if Back_rect.collidepoint(event.pos):
                    return
                if Send_rect.collidepoint(event.pos):
                    Login_successful = Check_login(Username_text, Password_text)
                    if Login_successful:
                        print("Kirjautuminen onnistui!")
                        Current_level = Get_level(Username_text)
                        print(Current_level)
                        if Current_level is not None:
                            Sudoku_game.current_board_index = Current_level - 1
                            Sudoku_game.Select_board()
                            Sudoku_game.Start_game()
                        else:
                            print("Käyttäjän tasoa ei voitu hakea.")
                    else:
                        print("Kirjautuminen epäonnistui. Tarkista käyttäjätunnus ja salasana.")
                    break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Login_successful = Check_login(Username_text, Password_text)
                    if Login_successful:
                        print("Kirjautuminen onnistui!")
                        Current_level = Get_level(Username_text)
                        if Current_level is not None:
                            Sudoku_game.current_board_index = Current_level - 1
                            Sudoku_game.Select_board()
                            Sudoku_game.Start_game()
                            return
                        else:
                            print("Käyttäjän tasoa ei voitu hakea.")
                    else:
                        print("Kirjautuminen epäonnistui. Tarkista käyttäjätunnus ja salasana.")
                elif event.key == pygame.K_BACKSPACE:
                    if Is_typing_username:
                        Username_text = Username_text[:-1]
                    elif Is_typing_password:
                        Password_text = Password_text[:-1]
                else:
                    if Is_typing_username:
                        Username_text += event.unicode
                    elif Is_typing_password:
                        Password_text += event.unicode

        Screen.fill((255, 255, 255))

        LoginText = font.render("Kirjaudu sisään", True, Black)
        Screen.blit(LoginText, (330, 360))
        Username_label = font.render("Käyttäjänimi:", True, Black)
        Screen.blit(Username_label, (147, 433))
        Password_label = font.render("Salasana:", True, Black)
        Screen.blit(Password_label, (180, 480))

        Username_surface = font.render(Username_text, True, Black)
        pygame.draw.rect(Screen, Black, Username_rect, 2)
        Screen.blit(Username_surface, (Username_rect.x + 5, Username_rect.y + 5))

        Password_surface = font.render('*' * len(Password_text), True, Black)
        pygame.draw.rect(Screen, Black, Password_rect, 2)
        Screen.blit(Password_surface, (Password_rect.x + 5, Password_rect.y + 5))

        Back_button = font.render("Takaisin", True, Black)
        Screen.blit(Back_button, (50, 50))

        Send_button = font.render("Lähetä", True, Black)
        Screen.blit(Send_button, (Width // 2 - Send_button.get_width() // 2, Height // 2 + 125))

        pygame.display.flip()
        
        
def Register():
    pygame.init()
    Width = 857
    Height = 850
    Screen = pygame.display.set_mode((Width, Height))
    font = pygame.font.Font(None, 36)
    Black = pygame.Color('black')

    Username_rect = pygame.Rect(Width // 2 - 100, Height // 2, 200, 40)
    Password_rect = pygame.Rect(Width // 2 - 100, Height // 2 + 50, 200, 40)
    Back_rect = pygame.Rect(OuterLines, OuterLines - font.get_height() - 10, 200, 50)
    Send_rect = pygame.Rect(Width // 2 - 50, Height // 2 + 120, 100, 50)

    Username_text = ''
    Password_text = ''

    Conn = sqlite3.connect('users.db')
    Cursor = Conn.cursor()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Username_rect.collidepoint(event.pos):
                    Is_typing_username = True
                    Is_typing_password = False
                elif Password_rect.collidepoint(event.pos):
                    Is_typing_password = True
                    Is_typing_username = False
                else:
                    Is_typing_username = False
                    Is_typing_password = False
                if Back_rect.collidepoint(event.pos):
                    Cursor.close()
                    Conn.close()
                    return
                if Send_rect.collidepoint(event.pos):
                    if Username_text and Password_text:  
                        Add_user(Username_text, Password_text, 1) 
                        print("Käyttäjä lisätty tietokantaan!")
                    else:
                        print("Anna käyttäjätunnus ja salasana.")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    if Is_typing_username:
                        Username_text = Username_text[:-1]
                    elif Is_typing_password:
                        Password_text = Password_text[:-1]
                else:
                    if Is_typing_username:
                        Username_text += event.unicode
                    elif Is_typing_password:
                        Password_text += event.unicode

        Screen.fill((255, 255, 255))

        LoginText = font.render("Rekisteröidy:", True, Black)
        Screen.blit(LoginText, (330, 360))
        Username_label = font.render("Käyttäjänimi:", True, Black)
        Screen.blit(Username_label, (147, 433))
        Password_label = font.render("Salasana:", True, Black)
        Screen.blit(Password_label, (180, 480))

        Username_surface = font.render(Username_text, True, Black)
        pygame.draw.rect(Screen, Black, Username_rect, 2)
        Screen.blit(Username_surface, (Username_rect.x + 5, Username_rect.y + 5))

        Password_surface = font.render('*' * len(Password_text), True, Black)
        pygame.draw.rect(Screen, Black, Password_rect, 2)
        Screen.blit(Password_surface, (Password_rect.x + 5, Password_rect.y + 5))

        Back_button = font.render("Takaisin", True, Black)
        Screen.blit(Back_button, (50, 50))

        Send_button = font.render("Lähetä", True, Black)
        Screen.blit(Send_button, (Width // 2 - Send_button.get_width() // 2, Height // 2 + 125))

        pygame.display.flip()       
    # Tähän loppuu ChatGPT antaman koodin malli
        
def Start():
    Screen.fill((255, 255, 255))
    StartText = font.render("Tervetuloa Sukokuun!", True, Black)
    VisitorButton = font.render("Vierailija", True, Black)
    LoginButton = font.render("Kirjaudu", True, Black)
    RegisterButton = font.render("Rekisteröidy", True, Black)
    Screen.blit(StartText, (Width // 2 - StartText.get_width() // 2, Height // 2 - 50))
    Screen.blit(VisitorButton, (Width // 2 - VisitorButton.get_width() // 2, Height // 2 + 55))
    Screen.blit(LoginButton, (Width // 2 - LoginButton.get_width() // 2, Height // 2 + 10))
    Screen.blit(RegisterButton, (Width // 2 - RegisterButton.get_width() // 2, Height // 2 + 100))

# Tässä otettu mallia ChatGPT antamasta koodista
def Board():
    global Clicked_row, Clicked_col
    Screen.fill((255, 255, 255))
    if Sudoku_game.Is_game_started():
        board = Sudoku_game.Get_board()
    for i in range(9):
        for j in range(9):
            Cell_rect = pygame.Rect(OuterLines + j * WindowSize, OuterLines + i * WindowSize, WindowSize, WindowSize)
            pygame.draw.rect(Screen, Black, Cell_rect, 1)
            if board[i][j] != 0:
                if board[i][j] == -1:
                    NumberColor = font.render(str(board[i][j]), True, (255, 0, 0))
                else:
                    NumberColor = font.render(str(board[i][j]), True, Black)
                Screen.blit(NumberColor, (OuterLines + j * WindowSize + WindowSize // 3, OuterLines + i * WindowSize + WindowSize // 3))
            if i == Clicked_row and j == Clicked_col:
                pygame.draw.rect(Screen, Gray, Cell_rect)

    ButtonBack = font.render("Takaisin", True, Black)
    Screen.blit(ButtonBack, (OuterLines, OuterLines - ButtonBack.get_height() - 10))
    
    ButtonCheck = font.render("Tarkasta", True, Black)
    ButtonCheck_rect = ButtonCheck.get_rect(topleft=(Width - OuterLines - ButtonCheck.get_width(), Height - OuterLines - ButtonCheck.get_height() - 10 + 35))
    Screen.blit(ButtonCheck, ButtonCheck_rect)
    
    ButtonReset = font.render("Nollaa", True, Black)
    ButtonReset_rect = ButtonReset.get_rect(topleft=(Width - OuterLines - ButtonReset.get_width(), OuterLines - ButtonReset.get_height() - 10))
    Screen.blit(ButtonReset, ButtonReset_rect)
    
    if Sudoku_game.Is_valid() and Sudoku_game.Is_game_started():
        Next_button_rect = pygame.Rect(490, 800 - 10, 200, 50)
        if Next_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Screen, Green, Next_button_rect)
            if pygame.mouse.get_pressed()[0]:
                Username = Get_username() 
                if Check_login(Username, ""):
                    Current_level = Get_level(Username)
                    New_level = Current_level + 1
                    Sudoku_game.Update_level(Username, New_level)
                Sudoku_game.second_sudoku_solved = False
                Sudoku_game.Reset_board()
                Clicked_row, Clicked_col = None, None
                Sudoku_game.End_game()
        else:
            pygame.draw.rect(Screen, White, Next_button_rect)
            
        Next_button_text = font.render("Seuraava", True, Black)
        Screen.blit(Next_button_text, (530, 792))


    
ButtonReset = font.render("Nollaa", True, Black)
ButtonReset_rect = ButtonReset.get_rect(topleft=(Width - OuterLines - ButtonReset.get_width(), OuterLines - ButtonReset.get_height() - 10))
Screen.blit(ButtonReset, ButtonReset_rect)
    
ButtonCheck = font.render("Tarkasta", True, Black)
ButtonCheck_rect = ButtonCheck.get_rect(topleft=(Width - OuterLines - ButtonCheck.get_width(), Height - OuterLines - ButtonCheck.get_height() - 10 + 35))
Screen.blit(ButtonCheck, ButtonCheck_rect)

ButtonLogin = font.render("Kirjaudu", True, Black)
ButtonLogin_rect = ButtonLogin.get_rect(topleft=(Width // 2 - ButtonLogin.get_width() // 2, Height // 2 + 10))
Screen.blit(ButtonLogin, ButtonLogin_rect)

ButtonRegister = font.render("Rekisteröidy", True, Black)
ButtonRegister_rect = ButtonRegister.get_rect(topleft=(Width // 2 - ButtonRegister.get_width() // 2, Height // 2 + 95))
Screen.blit(ButtonRegister, ButtonRegister_rect)

Sudoku_solved_message_time = 0
Running = True
Sudoku_checked = False
Sudoku_solved_message_shown = False

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            MousePosition = pygame.mouse.get_pos()
            if not Sudoku_game.Is_game_started():
                Start_button_rect = pygame.Rect(Width // 2 - 100, Height // 2 + 50, 200, 50)
                if Start_button_rect.collidepoint(MousePosition):
                    Sudoku_game.Start_game()
                elif ButtonRegister_rect.collidepoint(MousePosition):  
                    Register() 
                elif ButtonLogin_rect.collidepoint(MousePosition):
                    Login() 
            else:
                Row = (MousePosition[1] - OuterLines) // WindowSize
                Col = (MousePosition[0] - OuterLines) // WindowSize
                if 0 <= Row < 9 and 0 <= Col < 9:
                    Clicked_row, Clicked_col = Row, Col
                                       
                def Back_to_menu():
                    global Sudoku_game
                    Sudoku_game = SudokuGame()        

                ButtonBackpressed = pygame.Rect(OuterLines, OuterLines - font.get_height() - 10, 200, 50)
                if ButtonBackpressed.collidepoint(MousePosition):
                    Back_to_menu()

                if ButtonCheck_rect.collidepoint(MousePosition):
                    if Sudoku_game.Is_game_started():
                        if Sudoku_game.Is_valid():
                            print("Sudoku on ratkaistu oikein!")
                        else:
                            print("Sudoku on ratkaistu väärin!")
                        Sudoku_checked = True
                        Sudoku_solved_message_shown = True
                        Sudoku_solved_message_time = pygame.time.get_ticks()
                    
                if ButtonReset_rect.collidepoint(MousePosition):
                    Sudoku_game.Reset_board()
                    Clicked_row, Clicked_col = None, None

        elif event.type == pygame.KEYDOWN:
            if Clicked_row is not None and Clicked_col is not None:
                Key_pressed = event.key
                if pygame.K_1 <= Key_pressed <= pygame.K_9:
                    Number = Key_pressed - pygame.K_0
                    Sudoku_game.Add_number(Clicked_row, Clicked_col, Number)
                    Clicked_row, Clicked_col = None, None                 
    # Tähän loppuu ChatGPT antaman koodin malli
    
    if not Sudoku_game.Is_game_started():
        Start()
    else:
        Board()

    if Sudoku_checked and (not Sudoku_solved_message_shown or pygame.time.get_ticks() - Sudoku_solved_message_time < 3000):
        if Sudoku_game.Is_valid():
            Sudoku_solved_message = font.render("Sudoku on ratkaistu oikein!", True, Green)
            Screen.blit(Sudoku_solved_message, (OuterLines + 220, Height // 18 - Sudoku_solved_message.get_height() // 2))
        else:
            Sudoku_solved_message = font.render("Sudoku on ratkaistu väärin!", True, Red)
            Screen.blit(Sudoku_solved_message, (OuterLines + 220, Height // 18 - Sudoku_solved_message.get_height() // 2))
    else:
        Sudoku_solved_message = False

    if Sudoku_checked and pygame.time.get_ticks() - Sudoku_solved_message_time >= 3000:
        Sudoku_solved_message = True

    pygame.display.flip()

pygame.quit()
sys.exit()
 