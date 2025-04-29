from algorithm.key_expansion import key_expansion


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


class AES:
    def __init__(self, key_text):
        self.key = parse_key(key_text)
        self.round_keys = key_expansion(self.key)

    def encrypt(self, data):
        for round_index in range(11):
            round_key = self.round_keys[round_index * 4: (round_index + 1) * 4]
            print(round_key)
            # TODO add_round_key, sub_bytes, shift_rows, mix_columns etc.
            pass

        return data

    def decrypt(self, data):
        return data
