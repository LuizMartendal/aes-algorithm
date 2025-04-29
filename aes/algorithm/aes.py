from algorithm import constants


def expand_key(key):
    matriz = [[None for _ in range(4)] for _ in range(4)]

    index = 0
    for col in range(4):
        for row in range(4):
            matriz[row][col] = key[index]
            index += 1

    return matriz


def parse_key(key_text):
    parts = key_text.strip().split(',')
    if len(parts) != 16:
        raise ValueError("A chave deve ter exatamente 16 números (bytes) separados por vírgula.")
    key_bytes = [
        int(p.strip(), 16) if 'x' in p.strip() or any(c.isalpha() for c in p.strip())
        else int(p.strip())
        for p in parts
    ]
    return key_bytes


def rot_word(word):
    return word[1:] + word[:1]


def get_sub_word(word):
    sub_w = [constants.S_BOX[b] for b in word]
    return sub_w


def get_round_constant(index):
    return [constants.ROUND_CONSTANT_VECTOR[index], 0x00, 0x00, 0x00]


def do_xor(vector1, vector2):
    return [a ^ b for a, b in zip(vector1, vector2)]


class AES:
    def __init__(self, key_text):
        self.key = parse_key(key_text)
        self.expanded_key = expand_key(self.key)

    def encrypt(self, data):
        expanded_key_matrix = self.expanded_key

        last_column = [row[-1] for row in expanded_key_matrix]
        rotated_column = rot_word(last_column)

        substituted_column = get_sub_word(rotated_column)

        rcon = get_round_constant(0)

        transformed_column = do_xor(substituted_column, rcon)

        first_column = [row[0] for row in expanded_key_matrix]
        new_key_column = do_xor(first_column, transformed_column)

        # Debug
        # print("Expanded key matrix:", expanded_key_matrix)
        # print("Last column (W3):", last_column)
        # print("Rotated column:", rotated_column)
        # print("Substituted column:", substituted_column)
        # print("Round constant (Rcon):", rcon)
        # print("Transformed column:", transformed_column)
        # print("New key column (W0 ^ T(W3)):", new_key_column)

        return data

    def decrypt(self, data):
        return data
