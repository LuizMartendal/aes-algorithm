from utils.constants import S_BOX, ROUND_CONSTANT_VECTOR


def rot_word(word):
    return word[1:] + word[:1]


def sub_word(word):
    return [S_BOX[b] for b in word]


def get_round_constant(index):
    return ROUND_CONSTANT_VECTOR[index]


def key_expansion(key):
    expanded_key = []
    expanded_key += key

    for i in range(4, 4 * 11):
        temp = expanded_key[-4:]
        if i % 4 == 0:
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp[0] ^= get_round_constant((i // 4) - 1)

        for j in range(4):
            temp[j] ^= expanded_key[-16 + j]

        expanded_key += temp
    return expanded_key

