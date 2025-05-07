from utils.utils import parse_key, pad_pkcs7, bytes_to_state_matrices, join_blocks, unpad_pkcs7
from aes_steps.add_round_key import add_round_key
from aes_steps.sub_bytes import sub_bytes, inv_sub_bytes
from aes_steps.shift_rows import shift_rows, inv_shift_rows
from aes_steps.mix_columns import mix_columns, inv_mix_columns
from aes_steps.key_expansion import key_expansion


class AES:
    def __init__(self, key_text):
        self.key = parse_key(key_text)
        # print(f'INFO: Chave de criptografia: {self.key}')
        self.round_keys = key_expansion(self.key)

    def encrypt(self, data: bytes):
        # print(f'INFO: Convertendo {data} para blocos de 16 bytes')
        padded = pad_pkcs7(data)
        blocks = bytes_to_state_matrices(padded)
        encrypted_blocks = []

        for state in blocks:
            state = add_round_key(state, self.round_keys[0:16])
            # print(f'INFO: Aplicando rodada 0 com roundKey: {self.round_keys[0:4]} e estado {state}')

            for i in range(1, 10):
                state = sub_bytes(state)
                state = shift_rows(state)
                state = mix_columns(state)
                round_key = self.round_keys[i * 16: (i + 1) * 16]
                # print(f'INFO: Aplicando rodada {i} com roundKey: {round_key} e estado: {state}')
                state = add_round_key(state, round_key)

            state = sub_bytes(state)
            state = shift_rows(state)
            round_key = self.round_keys[10 * 16: (10 + 1) * 16]
            # print(f'INFO: Aplicando rodada 10 com roundKey: {round_key} e estado {state}')
            state = add_round_key(state, round_key)

            encrypted_blocks.append(state)

        # print(f'INFO: Blocos criptografados: {encrypted_blocks}')

        blocks_in_bytes = join_blocks(encrypted_blocks)
        # print(f'INFO: Bytes criptografados: {blocks_in_bytes}')

        return blocks_in_bytes

    def decrypt(self, data):
        blocks = bytes_to_state_matrices(data)
        decrypted_blocks = []

        for state in blocks:
            state = add_round_key(state, self.round_keys[(11 * 16) - 16:])
            state = inv_shift_rows(state)
            state = inv_sub_bytes(state)

            for i in range(9, 0, -1):
                state = add_round_key(state, self.round_keys[i * 16: (i + 1) * 16])
                state = inv_mix_columns(state)
                state = inv_shift_rows(state)
                state = inv_sub_bytes(state)

            state = add_round_key(state, self.round_keys[0:16])

            decrypted_blocks.append(state)

        block_in_bytes = join_blocks(decrypted_blocks)
        return unpad_pkcs7(block_in_bytes)
