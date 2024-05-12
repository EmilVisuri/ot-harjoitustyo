# Ohjelmistotekniikka, harjoitustyö
Tarkoituksena olisi luoda **sudoku** peli, jossa käyttäjä voi *kirjautua sisään/luoda tunnuksen*, jolloin pelissä eteneminen **tallennetaan tietokantaan**. 


Pelissä pystyy tällä hetkellä pääsemään peliin vierailijana. Itse pelissä voi laittaa tyhjään ruutuun valitsemansa numeron 0-9 välillä ja päästä takaisin alkuvalikkoon "takaisin" napista.

## Dokumentaatio
Arkkitehtuuri: https://github.com/EmilVisuri/ot-harjoitustyo/blob/master/dokumentaatio/Arkkitehtuuri.md

Changelog: https://github.com/EmilVisuri/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md

käyttöohje: https://github.com/EmilVisuri/ot-harjoitustyo/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md

Työaikakirjanpito: https://github.com/EmilVisuri/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md

Vaatimusmäärittely: https://github.com/EmilVisuri/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md


## Sovelluksen testaaminen
1. Sovellus käyttää SQLite tietokantaa. Jos sinulla ei ole sitä valmiiksi, niin voit ladata sen täältä: https://www.sqlite.org/download.html

2. Lataa sovellus release kohdasta: [https://github.com/EmilVisuri/ot-harjoitustyo/releases](https://github.com/EmilVisuri/ot-harjoitustyo/releases/tag/Loppupalautus) ja pura ZIP-tiedosto haluamaasi paikkaan.

3. Avaa purettu sovellus ja navigoi ohjelman juurikansioon ja avaa se terminaalissa.

4. Kun terminaali on avattu, kirjoita ensin poetry shell, sitten poetry install ja viimeiseksi poetry run invoke start.

5. Testit voi suorittaa komennolla poetry run invoke coverage-report

6. Pylint-tarkastukset voi suorittaa komennolla pylint src
