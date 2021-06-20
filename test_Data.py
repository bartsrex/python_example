import unittest
import Data


class TestData(unittest.TestCase):

    """Klasa implementująca testy."""

    def test_init_Stan(self):
        """Test jednostkowy."""
        try:
            test_obj = Data.Stan()
        except:
            self.fail("Nie powinno byc bledu")
        else:
            self.assertIsInstance(test_obj, Data.Stan, "text")

    def test_dodaj_do_stanu(self):
        """Test jednostkowy i integracyjny (z klasą Ksiazka)."""
        try:
            test_obj = Data.Stan()
        except:
            self.fail("Nie powinno byc bledu")

        res = Data.Stan.dodaj_do_stanu(test_obj, '002')
        self.assertEquals(res, True)

    def test_dodaj_do_stanu2(self):
        """Test jednostkowy i integracyjny (z klasą Ksiazka)."""
        try:
            test_obj = Data.Stan()
        except:
            self.fail("Nie powinno byc bledu")

        res = Data.Stan.dodaj_do_stanu(test_obj, '003')
        self.assertEquals(res, True)
        res = Data.Stan.dodaj_do_stanu(test_obj, '003')
        self.assertEquals(res, False)

#Manualnie inne testy integracyjne, funkcjonalne
#Manualnie testy akceptacyjne


if __name__ == "__main__":
    unittest.main()
