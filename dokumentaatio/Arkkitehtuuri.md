# Arkkitehtuurikuvaus

## Pakkausrakenne:

Sekvenssikaavio ohjelman rakenteesta

![Screenshot from 2024-04-30 03-42-37](https://github.com/EmilVisuri/ot-harjoitustyo/assets/156796516/6ce8269b-e762-4ae1-a1de-f43685656b8a)



## Käyttöliittymä:
Käyttöliittymässä on näkymät kirjautumiselle, rekisteröinnille ja itse pelille.

Käyttöliittymän näkymät on toteuttu kaikki samassa interface.py tiedostossa

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

Tämä luokka tarjoaa toiminnot pelin hallintaan, kuten pelin aloitus, lopetus, numeroiden lisääminen, pelitilanteen tarkistaminen yms.

Sovelluslogiikka ei suoraan käsittele tietojen tallennusta, vaan se voi kutsua tarvittaessa database-moduulin funktioita.

**Tietojen pysyväistallennus:**

database-moduuli vastaa tietojen tallennuksesta ja hakemisesta.

Esimerkiksi check_login, update_level_in_database, get_user_level yms. toimivat tietojen tallennuksen ja hakemisen parissa.

## Päätoiminnallisuudet
**Sekvenssikaavio käyttäjän lisäämisestä tietokantaan**

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

**sekvenssikaavio käyttäjän rekisteröitymisestä**

 *pitää vielä tehdä*
 
**sekvenssikaavio pelin toiminnasta**

*pitää vielä tehdä*

## Ohjelman rakenteeseen jääneet heikkoudet:
Sovelluksen rakenteessa voi olla toisteisuutta ja mahdollisia parannusmahdollisuuksia olisikin yleisten komponenttien tai toistuvien toiminnallisuuksien eriyttäminen omiksi osikseen.
Myös sovelluksen eri osat voisi littää omiin tiedostoihinsa.
