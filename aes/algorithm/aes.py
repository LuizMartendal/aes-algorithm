from rijndael import Rijndael


class AES:
    @staticmethod
    def encrypt(data, key):
        key = AES.parse_key(key)
        expanded_key = AES.expand_key(key)
        roted_key = AES.rot_word(expanded_key[:][-1])
        subword = AES.sub_word(roted_key)
        return data

    @staticmethod
    def decrypt(data, key):
        return data

    @staticmethod
    def expand_key(key):
        matriz = [[None for _ in range(4)] for _ in range(4)]

        index = 0
        for col in range(4):
            for row in range(4):
                matriz[row][col] = key[index]
                index += 1

        return matriz

    @staticmethod
    def parse_key(key_text):
        parts = key_text.strip().split(',')
        if len(parts) != 16:
            raise ValueError("A chave deve ter exatamente 16 números (bytes) separados por vírgula.")
        # key_bytes = bytes(int(b.strip()) for b in parts)
        return parts

    @staticmethod
    def rot_word(word):
        return word[1:] + word[:1]

    @staticmethod
    def sub_word(word):
        r = Rijndael(key=bytes([0] * 16), block_size=16)

        substituidos = [r.sub_byte(b) for b in word]

        print(substituidos)
        return substituidos
