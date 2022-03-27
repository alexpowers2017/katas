import unittest
import ciphers.AlphabetCipher as ac


class TestEncode(unittest.TestCase):
    def test_test_environment(self):
        self.assertEqual(True, True)

    @classmethod
    def setUpClass(cls) -> None:
        cipher = ac.AlphaCipher()
        cls.encode = cipher.encode

    def assertEncoded(self, message: str, keyword: str, expected_output: str):
        self.assertEqual(expected_output, self.encode(message, keyword))

    def test_given_none_returns_empty_string(self):
        self.assertEncoded(None, '', '')
        self.assertEncoded('', None, '')

    def test_given_empty_string_returns_empty_string(self):
        self.assertEncoded('', 'keyword', '')
        self.assertEncoded('message', '', '')

    def test_given_numbers_returns_empty_string(self):
        self.assertEncoded('message', 'k3yword', '')
        self.assertEncoded('hell0', 'keyword', '')

    def test_given_special_chars_returns_empty_string(self):
        self.assertEncoded('mes.sage', 'keyword', 'wiqooxh')
        self.assertEncoded('message', 'key*word', 'wiqooxh')
        self.assertEncoded('mes#sage', 'keyword', 'wiqooxh')
        self.assertEncoded('message', 'keyword?', 'wiqooxh')
        self.assertEncoded('messa(ge', 'keyword', 'wiqooxh')
        self.assertEncoded('message', 'k:eyword', 'wiqooxh')

    def test_one_letter_message_and_keyword(self):
        self.assertEncoded('b', 'e', 'f')
        self.assertEncoded('k', 'j', 't')
        self.assertEncoded('w', 'd', 'z')
        self.assertEncoded('t', 'i', 'b')
        self.assertEncoded('z', 'z', 'y')
        self.assertEncoded('l', 't', 'e')

    def test_message_with_one_letter_keyword(self):
        self.assertEncoded('bcd', 'r', 'stu')
        self.assertEncoded('hello', 'z', 'gdkkn')
        self.assertEncoded('why', 'e', 'alc')

    def test_long_messages_and_keywords(self):
        self.assertEncoded('bird', 'bars', 'ciiv')
        self.assertEncoded('irk', 'babble', 'jrl')
        self.assertEncoded('meetmebythetree', 'scones', 'egsgqwtahuiljgs')
        self.assertEncoded('message', 'keyword', 'wiqooxh')

    def test_spaces_removed(self):
        self.assertEncoded('bi rd', 'bars', 'ciiv')
        self.assertEncoded('irk', 'bab ble', 'jrl')
        self.assertEncoded('meet me by the tree', 'scones', 'egsgqwtahuiljgs')


class TestDecode(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cipher = ac.AlphaCipher()
        cls.decode = cipher.decode

    def assertDecoded(self, message: str, keyword: str, expected_output: str):
        self.assertEqual(expected_output, self.decode(message, keyword))

    def test_given_none_returns_empty_string(self):
        self.assertDecoded(None, '', '')
        self.assertDecoded('', None, '')

    def test_given_empty_string_returns_empty_string(self):
        self.assertDecoded('', 'keyword', '')
        self.assertDecoded('message', '', '')

    def test_given_numbers_returns_empty_string(self):
        self.assertDecoded('message', 'k3yword', '')
        self.assertDecoded('hell0', 'keyword', '')

    def test_given_special_chars_returns_empty_string(self):
        self.assertDecoded('wiqo.oxh', 'keyword', 'message')
        self.assertDecoded('wiqooxh', 'key*word', 'message')
        self.assertDecoded('w#iqooxh', 'keyword', 'message')
        self.assertDecoded('wiqooxh', 'keyword?', 'message')
        self.assertDecoded('wiq(ooxh', 'keyword', 'message')
        self.assertDecoded('wiqooxh', 'k:eyword', 'message')

    def test_one_letter_message_and_keyword(self):
        self.assertDecoded('f', 'e', 'b')
        self.assertDecoded('t', 'j', 'k')
        self.assertDecoded('z', 'd', 'w')
        self.assertDecoded('b', 'i', 't')
        self.assertDecoded('y', 'z', 'z')
        self.assertDecoded('e', 't', 'l')

    def test_message_with_one_letter_keyword(self):
        self.assertDecoded('stu', 'r', 'bcd')
        self.assertDecoded('gdkkn', 'z', 'hello')
        self.assertDecoded('alc', 'e', 'why')

    def test_long_messages_and_keywords(self):
        self.assertDecoded('ciiv', 'bars', 'bird')
        self.assertDecoded('jrl', 'babble', 'irk')
        self.assertDecoded('egsgqwtahuiljgs', 'scones', 'meetmebythetree')
        self.assertDecoded('wiqooxh', 'keyword', 'message')

if __name__ == '__main__':
    unittest.main()
