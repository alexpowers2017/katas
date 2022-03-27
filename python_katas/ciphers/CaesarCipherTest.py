import unittest
from ciphers.CaesarCipher import CaesarCipher


class CaesarCipherEncode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cipher = CaesarCipher()
        cls.encode = cipher.encode

    def assertEncoded(self, message: str, shift: int, code: str):
        self.assertEqual(code, self.encode(message, shift))

    def test_test_environment(self):
        self.assertEqual(True, True)

    def test_given_null_or_empty_string_returns_empty_string(self):
        self.assertEqual('', self.encode(None, 3))
        self.assertEqual('', self.encode('', 5))
        self.assertEqual('', self.encode('test', None))
        self.assertEqual('', self.encode('test', ''))

    def test_one_letter(self):
        self.assertEncoded('a', 1, 'b')
        self.assertEncoded('z', 1, 'a')
        self.assertEncoded('t', 10, 'd')

    def test_normal_cases(self):
        self.assertEncoded('abc', 4, 'efg')
        self.assertEncoded('zap', 10, 'jkz')

    def test_handle_spaces(self):
        self.assertEncoded('hello there', 2, 'jgnnq vjgtg')
        self.assertEncoded('hi there idiot', 3, 'kl wkhuh lglrw')


class CaesarCipherDecode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cipher = CaesarCipher()
        cls.decode = cipher.decode

    def assertDecoded(self, message: str, shift: int, code: str):
        self.assertEqual(code, self.decode(message, shift))

    def test_test_environment(self):
        self.assertEqual(True, True)

    def test_given_null_or_empty_string_returns_empty_string(self):
        self.assertDecoded(None, 3, '')
        self.assertDecoded('', 5, '')
        self.assertDecoded('test', None, '')
        self.assertDecoded('test', '', '')


    def test_one_letter(self):
        self.assertDecoded('b', 1, 'a')
        self.assertDecoded('a', 1, 'z')
        self.assertDecoded('d', 10, 't')

    def test_normal_cases(self):
        self.assertDecoded('efg', 4, 'abc')
        self.assertDecoded('jkz', 10, 'zap')

    def test_handle_spaces(self):
        self.assertDecoded('jgnnq vjgtg', 2, 'hello there')
        self.assertDecoded('kl wkhuh lglrw', 3, 'hi there idiot')




if __name__ == '__main__':
    unittest.main()
