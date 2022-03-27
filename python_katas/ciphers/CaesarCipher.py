from ciphers.Cipher import Cipher
import ciphers.utils as utils


class CaesarCipher(Cipher):

    def encode(self, message: str, shift: int) -> str:
        result = ''
        if not message or not shift:
            return result
        else:
            for i in range(len(message)):
                result += self.shift_letter(message[i], shift) if message[i] != ' ' else ' '
            return result

    def decode(self, code: str, shift: int) -> str:
        result = ''
        if not code or not shift:
            return result
        else:
            for i in range(len(code)):
                result += self.unshift_letter(code[i], shift) if code[i] != ' ' else ' '
            return result

    @staticmethod
    def shift_letter(letter: chr, shift: int):
        pos = utils.position_of(letter) + shift
        position = pos if pos < 26 else pos - 26
        return utils.letter_at(position)

    @staticmethod
    def unshift_letter(letter: chr, shift: int):
        pos = utils.position_of(letter) - shift
        position = pos if pos >= 0 else pos + 26
        return utils.letter_at(position)
