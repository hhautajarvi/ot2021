import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.maksukortti2 = Maksukortti(10)

    #Alkuarvot:

    def test_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #Edullisesti käteisellä:

    def test_edullisesti_kateisella_kassa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_edullisesti_kateisella_maksu_oikein(self):        
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_edullisesti_kateisella_myydyt_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisesti_kateisella_kassa_ei_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisesti_kateisella_maksu_ei_tarpeeksi(self):        
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_edullisesti_kateisella_myydyt_ei_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    #Maukkaasti käteisellä:

    def test_maukkaasti_kateisella_kassa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_maukkaasti_kateisella_maksu_oikein(self):        
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_maukkaasti_kateisella_myydyt_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_kateisella_kassa_ei_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukkaasti_kateisella_maksu_ei_tarpeeksi(self):        
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_maukkaasti_kateisella_myydyt_ei_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #Edullisesti kortilla:

    def test_edullisesti_kortilla_kortti_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")

    def test_edullisesti_kortilla_palautus_oikein(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_edullisesti_kortilla_myydyt_oiken(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisesti_kortilla_kortti_ei_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)
        self.assertEqual(str(self.maksukortti2), "saldo: 0.1")

    def test_edullisesti_kortilla_palautus_ei_tarpeeksi(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2))
    
    def test_edullisesti_kortilla_myydyt_ei_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)
        self.assertEqual(self.kassapaate.edulliset, 0)

    #Maukkaasti kortilla:

    def test_maukkaasti_kortilla_kortti_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")

    def test_maukkaasti_kortilla_palautus_oikein(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_maukkaasti_kortilla_myydyt_oiken(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_kortilla_kortti_ei_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)
        self.assertEqual(str(self.maksukortti2), "saldo: 0.1")

    def test_maukkaasti_kortilla_palautus_ei_tarpeeksi(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2))
    
    def test_maukkaasti_kortilla_myydyt_ei_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)
        self.assertEqual(self.kassapaate.maukkaat, 0)   

    #Loput testit:

    def test_kassa_kortilla_edullisesti_ostettaessa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassa_kortilla_maukkaasti_ostettaessa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille_saldo_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    def test_lataa_rahaa_kortille_kassa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_lataa_rahaa_kortille_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")