import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):

    def test_kortin_saldo_oikein_alussa(self):
        kortti = Maksukortti(1000)
        self.assertEqual(str(kortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortille_lataaminen_toimii_oikein(self):
        kortti = Maksukortti(1000)
        kortti.lataa_rahaa(500)
        self.assertEqual(str(kortti), "Kortilla on rahaa 15.00 euroa")

    def test_rahan_ottaminen_toimii_oikein(self):
        kortti = Maksukortti(1000)
        self.assertTrue(kortti.ota_rahaa(500))
        self.assertEqual(str(kortti), "Kortilla on rahaa 5.00 euroa")

    def test_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(100)
        self.assertFalse(kortti.ota_rahaa(200))
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")

if __name__ == '__main__':
    unittest.main()