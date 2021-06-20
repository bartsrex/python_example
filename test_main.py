import unittest
from main import count_words

class TestText(unittest.TestCase):



    def test_1(self):
        text = 'Ala ma kota'
        self.assertEqual(count_words(text), 2, 'Powinno być 2')

    def test_2(self):
        text2 = 'ma ca sa'
        self.assertEqual(count_words(text2), 0, 'powinno byc 0')
		
    def test_3(self):
        text2 = 'ma ca sa'
        self.assertEqual(count_words(text2), 1, 'powinno byc 0')


if __name__ == '__main__':
    unittest.main()