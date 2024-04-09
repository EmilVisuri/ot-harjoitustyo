sequenceDiagram
    participant main as Main
    participant laitehallinto as HKLLaitehallinto
    participant rautatietori as Lataajalaite
    participant ratikka6 as Lukijalaite
    participant bussi244 as Lukijalaite
    participant lippu_luukku as Kioski
    participant kallen_kortti as Matkakortti

    Main ->> laitehallinto: luo laitehallinto
    Main ->> rautatietori: luo rautatietori
    Main ->> ratikka6: luo ratikka6
    Main ->> bussi244: luo bussi244
    laitehallinto ->> laitehallinto: lisää rautatietori
    laitehallinto ->> laitehallinto: lisää ratikka6
    laitehallinto ->> laitehallinto: lisää bussi244
    Main ->> lippu_luukku: luo lippu_luukku
    lippu_luukku ->> kallen_kortti: osta_matkakortti("Kalle")
    rautatietori ->> kallen_kortti: lataa_arvoa(3)
    ratikka6 ->> kallen_kortti: osta_lippu(0)
    bussi244 ->> kallen_kortti: osta_lippu(2)
