def add_round_key(state, round_key):
    return [state[i] ^ round_key[i] for i in range(16)]
