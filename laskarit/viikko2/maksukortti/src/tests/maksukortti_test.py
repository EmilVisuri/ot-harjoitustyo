import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.kortti.lataa_rahaa(500)
        self.assertEqual(self.kortti.saldo_euroina(), 15.00)

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(self.kortti.saldo_euroina(), 7.5)

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        kortti = Maksukortti(200)
        kortti.syo_maukkaasti()
        self.assertEqual(kortti.saldo_euroina(), 2.0)

    def test_syo_edullisesti_palauttaa_true_jos_rahat_riittavat(self):
        self.assertTrue(self.kortti.syo_edullisesti())

    def test_syo_edullisesti_palauttaa_false_jos_rahat_ei_riita(self):
        kortti = Maksukortti(200)
        self.assertFalse(kortti.syo_edullisesti())

    def test_syo_maukkaasti_palauttaa_true_jos_rahat_riittavat(self):
        self.assertTrue(self.kortti.syo_maukkaasti())

    def test_syo_maukkaasti_palauttaa_false_jos_rahat_ei_riita(self):
        kortti = Maksukortti(200)
        self.assertFalse(kortti.syo_maukkaasti())

if __name__ == '__main__':
    unittest.main()
