## Sovelluslogiikka

SudokuGame.py

|

|___ class SudokuGame:

|    

|___ __init__(self)

|    

|___ start_game(self)

|  

|___ end_game(self)

|    

|___ is_game_started(self)

|     

|___ get_board(self)

|    

|___ add_number(self, row, col, number)

|   

|___ is_valid(self)

|   

|___ is_valid_row(self, row)

|    

|___ is_valid_square(self, square)

|  

|___ reset_board(self)

Interface.py

|

|___ start()

|___ board()

## Sekvenssikaavio ohjelman rakenteesta
![image](https://github.com/EmilVisuri/ot-harjoitustyo/assets/156796516/8d083854-a547-48c8-bfdf-7bb649695866)


## Sekvenssikaavio käyttäjän lisäämisestä tietokantaan

participant User
participant Program
participant Database

User->>Program: Antaa käyttäjänimen ja salasanan rekisteröityäkseen
Program->>Database: Lähetä käyttäjän tiedot (käyttäjänimi, salasana)
Database->>Program: Vahvista, että käyttäjänimi ei ole jo käytössä
alt Käyttäjänimi on vapaa
    Program->>Database: Lisää käyttäjä tietokantaan
    Database->>Program: Palauta vahvistus rekisteröinnistä
    Program->>User: Näytä viesti rekisteröinnin onnistumisesta
else Käyttäjänimi on jo käytössä
    Database->>Program: Palauta virheilmoitus
    Program->>User: Näytä virheilmoitus käyttäjälle
end
