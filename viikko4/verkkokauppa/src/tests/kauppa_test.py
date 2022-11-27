import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 20
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "vegejuusto", 3)
            if tuote_id == 3:
                return Tuote(3, "kissanruoka", 2)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # aloita asiointi
        self.kauppa.aloita_asiointi()

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostosten_paatyttya_pankin_metodin_tilisiirto_parametrien_arvot_ovat_oikein(self):

        # tehdään ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # tarkistetaan, että ensimmäisen ja kolman parametrin arvo on oikein
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, ANY)

    def test_pankin_metodi_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinro_summa(self):

        # tehdään ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("erno", "77899")

        self.pankki_mock.tilisiirto.assert_called_with("erno", ANY, "77899", ANY, 8)

    def test_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinro_summa_kaksi_samaa(self):

        # tehdään ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "77899")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "77899", ANY, 10)

    def test_tuotetta_tarpeeksi_ja_ei_tarpeeksi(self):

        # tehdään ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_aloita_asiointi_nollaa_ostokset(self):

        # tehdään ostokset
        self.kauppa.lisaa_koriin(1)

        # aloita asiointi
        self.kauppa.aloita_asiointi()

        # tehdään uudet ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # tarkistetaan ettei toista ostosta näy
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):

        # määritellään että metodi palauttaa ensimmäisellä kutsulla 42 ja toisella 43
        self.viitegeneraattori_mock.uusi.side_effect = [42, 43]

        # tehdään uudet ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # tarkistaa, viitenumeron oikeellisuuden
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)

        # aloita asiointi
        self.kauppa.aloita_asiointi()

        # tehdään uudet ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # tarkistetaan ettei toista ostosta näy
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 43, "12345", ANY, 5)

    def test_poista_korista(self):

        # lisätään koriin
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)

        # poistetaan korista
        self.kauppa.poista_korista(2)

        # maksetaan ostos
        self.kauppa.tilimaksu("pekka", "12345")

        # tarkistetaan ettei toista ostosta näy
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)


