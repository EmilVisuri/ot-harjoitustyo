classDiagram
    class Monopolipeli {
        +Noppa[] nopat
        +Pelilauta pelilauta
        +Ruutu aloitusruutu
        +Ruutu vankila
        +Ruutu[] sattuma_ja_yhteismaa
        +Ruutu[] asemat_ja_laitokset
        +Ruutu[] kadut
        +void pelaaja_liikkuu(Pelaaja pelaaja, int nopan_silmäluku)
        +void suorita_ruudun_toiminto(Ruutu ruutu, Pelaaja pelaaja)
    }

    class Noppa {
        +int heita()
    }

    class Pelilauta {
        +Ruutu[] ruudut
        +Ruutu aloitusruutu
        +Ruutu vankila
    }

    class Ruutu {
        +Ruutu seuraava
        +Toiminto toiminto
        +String[] omistajat
        +int[] talot
        +int hotelli
        +String tyyppi
        +String nimi
    }

    class Pelaaja {
        +String nimi
        +int rahaa
    }

    class Toiminto {
        +void suorita_toiminto(Pelaaja pelaaja)
    }

    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "1" Ruutu : aloitusruutu
    Monopolipeli "1" -- "1" Ruutu : vankila
    Monopolipeli "1" -- "*" Ruutu : sattuma_ja_yhteismaa
    Monopolipeli "1" -- "*" Ruutu : asemat_ja_laitokset
    Monopolipeli "1" -- "*" Ruutu : kadut
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Ruutu "1" -- "1" Toiminto
    Pelaaja "2..8" -- "1" Monopolipeli
