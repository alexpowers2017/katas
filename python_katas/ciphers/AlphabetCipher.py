#   Alphabet Cipher
#
#   A 26x26 grid creates every possible mapping of one letter to another
#   and two people use unique letters as "keys" to  encode and decode messages.
#   The grid would look like this:
#
#      A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
#  A | a b c d e f g h i j k l m n o p q r s t u v w x y z
#  B | b c d e f g h i j k l m n o p q r s t u v w x y z a
#  C | c d e f g h i j k l m n o p q r s t u v w x y z a b
#  D | d e f g h i j k l m n o p q r s t u v w x y z a b c
#  E | e f g h i j k l m n o p q r s t u v w x y z a b c d
#  F | f g h i j k l m n o p q r s t u v w x y z a b c d e
#  G | g h i j k l m n o p q r s t u v w x y z a b c d e f
#  H | h i j k l m n o p q r s t u v w x y z a b c d e f g
#  I | i j k l m n o p q r s t u v w x y z a b c d e f g h
#  J | j k l m n o p q r s t u v w x y z a b c d e f g h i
#  K | k l m n o p q r s t u v w x y z a b c d e f g h i j
#  L | l m n o p q r s t u v w x y z a b c d e f g h i j k
#  M | m n o p q r s t u v w x y z a b c d e f g h i j k l
#  N | n o p q r s t u v w x y z a b c d e f g h i j k l m
#  O | o p q r s t u v w x y z a b c d e f g h i j k l m n
#  P | p q r s t u v w x y z a b c d e f g h i j k l m n o
#  Q | q r s t u v w x y z a b c d e f g h i j k l m n o p
#  R | r s t u v w x y z a b c d e f g h i j k l m n o p q
#  S | s t u v w x y z a b c d e f g h i j k l m n o p q r
#  T | t u v w x y z a b c d e f g h i j k l m n o p q r s
#  U | u v w x y z a b c d e f g h i j k l m n o p q r s t
#  V | v w x y z a b c d e f g h i j k l m n o p q r s t u
#  W | w x y z a b c d e f g h i j k l m n o p q r s t u v
#  X | x y z a b c d e f g h i j k l m n o p q r s t u v w
#  Y | y z a b c d e f g h i j k l m n o p q r s t u v w x
#  Z | z a b c d e f g h i j k l m n o p q r s t u v w x y


from ciphers.Cipher import Cipher
import ciphers.utils as utils


class AlphaCipher(Cipher):
    def encode(self, text: str, key: str) -> str:
        text, key = utils.remove_non_alpha(text), utils.remove_non_alpha(key)
        return self.encode_message(text, key) if text and key else ''

    def encode_message(self, text: str, key: str) -> str:
        result = ''
        for i in range(len(text)):
            position = utils.position_of(text[i]) + utils.position_of(self.get_next_key(key, i))
            next_position = position if position < 26 else position - 26
            result += utils.letter_at(next_position)
        return result

    def decode(self, text: str, key: str) -> str:
        text, key = utils.remove_non_alpha(text), utils.remove_non_alpha(key)
        return self.decode_code(text, key) if text and key else ''


    def decode_code(self, text: str, key: str) -> str:
        result = ''
        for i in range(len(text)):
            position = utils.position_of(text[i]) - utils.position_of(self.get_next_key(key, i))
            next_position = position if position >= 0 else position + 26
            result += utils.letter_at(next_position)
        return result

    @staticmethod
    def get_next_key(key: str, i: int) -> str:
        return key[i] if i < len(key) else key[i % len(key)]
