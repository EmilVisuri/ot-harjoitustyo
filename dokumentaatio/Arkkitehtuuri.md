### Arkkitehtuurikuvaus

## Pakkausrakenne:

Sekvenssikaavio ohjelman rakenteesta

![image](https://github.com/EmilVisuri/ot-harjoitustyo/assets/156796516/8d083854-a547-48c8-bfdf-7bb649695866)

ui: Sisältää käyttöliittymään liittyvät komponentit.

services: Tässä paketissa on sovelluslogiikasta vastaavat luokat.

repositories: Sisältää tietojen pysyväistallennuksesta vastaavat komponentit.

## Käyttöliittymä:
Käyttöliittymässä on erilliset näkymät, jotka on toteutettu omiksi luokikseen.
Näiden näkymien hallinnasta vastaa UI-luokka tai vastaava.

## Sovelluslogiikka:
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


Sovelluksen toiminnallisuudet ovat keskitetty SudokuGame-luokkaan.
Tämä luokka tarjoaa toiminnot pelin hallintaan, kuten pelin aloitus, lopetus, numeroiden lisääminen, pelitilanteen tarkistaminen jne.
Sovelluslogiikka ei suoraan käsittele tietojen tallennusta, vaan se voi kutsua tarvittaessa database-moduulin funktioita.

Tietojen pysyväistallennus:
database-moduuli vastaa tietojen tallennuksesta ja hakemisesta.
Esimerkiksi check_login, update_level_in_database, get_user_level jne. toimivat tietojen tallennuksen ja hakemisen parissa.

Ohjelman rakenteeseen jääneet heikkoudet:
Sovelluksen rakenteessa voi olla toisteisuutta tai mahdollisia parannusmahdollisuuksia, kuten yleisten komponenttien tai toistuvien toiminnallisuuksien eriyttäminen omiksi osikseen.
Tietojen pysyväistallennuksen osalta voisi harkita tietokantayhteyden hallintaa tai tallennustapojen abstrahointia, jotta muutokset tietojen tallennuksessa olisivat helpompia tehdä.

## Sekvenssikaavio käyttäjän lisäämisestä tietokantaan

participant User

participant Program

participant Database

<br>
User->>Program: Annetaan käyttäjänimi ja salasana rekisteröitymiseen

Program->>Database: Lähetetöön käyttäjän tiedot (käyttäjänimi ja salasana)

Database->>Program: Vahvistetaan, että käyttäjänimi ei ole jo käytössä


<br>
alt Käyttäjänimi on vapaa:

Program->>Database: Lisätään käyttäjä tietokantaan
    
Database->>Program: Palautetaan vahvistus rekisteröinnistä
    
Program->>User: Näytä viesti rekisteröimisen onnistumisesta
  

<br>
else Käyttäjänimi on valmiiksi käytössä:

Database->>Program: Palauta virheilmoitus
    
Program->>User: Näytä virheilmoitus käyttäjälle
     
<br>  
end
