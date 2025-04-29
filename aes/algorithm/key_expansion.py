from algorithm import constants


def rot_word(word):
    return word[1:] + word[:1]


def sub_word(word):
    return [constants.S_BOX[b] for b in word]


def get_round_constant(index):
    return [constants.ROUND_CONSTANT_VECTOR[index], 0x00, 0x00, 0x00]


def key_expansion(key_bytes):
    num_words = 44
    expanded_key = []

    for i in range(4):
        word = key_bytes[4 * i: 4 * (i + 1)]
        expanded_key.append(word)

    for i in range(4, num_words):
        temp = expanded_key[i - 1]

        if i % 4 == 0:
            temp = sub_word(rot_word(temp))
            rcon = get_round_constant(i // 4 - 1)
            temp = [b ^ r for b, r in zip(temp, rcon)]

        word = [b1 ^ b2 for b1, b2 in zip(expanded_key[i - 4], temp)]
        expanded_key.append(word)

    return expanded_key
