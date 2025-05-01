def parse_key(key_text):
    parts = key_text.strip().split(',')
    if len(parts) != 16:
        raise ValueError("A chave deve ter exatamente 16 números (bytes) separados por vírgula.")

    key_bytes = bytes([int(n) for n in parts])

    return key_bytes


def pad_pkcs7(data):
    block_size = 16
    padding = block_size - len(data) % block_size
    if padding == 0:
        padding = block_size
    return data + bytes([padding] * padding)


def bytes_to_state_matrices(data: bytes) -> list:
    return [data[i:i + 16] for i in range(0, len(data), 16)]


def join_blocks(states):
    return bytes([byte for state in states for byte in state])

