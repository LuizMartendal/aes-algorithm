from utils.constants import L, E, MIX_COLUMNS_MATRIX, INV_MIX_COLUMNS_MATRIX


def g_mul(a, b):
    if a == 0 or b == 0:
        return 0
    if a == 1 or b == 1:
        return a * b

    return E[(L[a] + L[b]) % 0xff]


def mix_columns(state):
    for i in range(4):
        column = state[i * 4: i * 4 + 4]
        state[i * 4] = g_mul(MIX_COLUMNS_MATRIX[0][0], column[0]) \
                       ^ g_mul(MIX_COLUMNS_MATRIX[0][1], column[1]) \
                       ^ g_mul(MIX_COLUMNS_MATRIX[0][2], column[2]) \
                       ^ g_mul(MIX_COLUMNS_MATRIX[0][3], column[3])

        state[i * 4 + 1] = g_mul(MIX_COLUMNS_MATRIX[1][0], column[0]) \
                           ^ g_mul(MIX_COLUMNS_MATRIX[1][1], column[1]) \
                           ^ g_mul(MIX_COLUMNS_MATRIX[1][2], column[2]) \
                           ^ g_mul(MIX_COLUMNS_MATRIX[1][3], column[3])

        state[i * 4 + 2] = g_mul(MIX_COLUMNS_MATRIX[2][0], column[0]) \
                           ^ g_mul(MIX_COLUMNS_MATRIX[2][1], column[1]) \
                           ^ g_mul(MIX_COLUMNS_MATRIX[2][2], column[2]) \
                           ^ g_mul(MIX_COLUMNS_MATRIX[2][3], column[3])

        state[i * 4 + 3] = g_mul(MIX_COLUMNS_MATRIX[3][0], column[0]) \
                           ^ g_mul(MIX_COLUMNS_MATRIX[3][1], column[1]) \
                           ^ g_mul(MIX_COLUMNS_MATRIX[3][2], column[2]) \
                           ^ g_mul(MIX_COLUMNS_MATRIX[3][3], column[3])
    return state


def inv_mix_columns(state):
    for i in range(4):
        column = state[i * 4: i * 4 + 4]
        state[i * 4] = g_mul(INV_MIX_COLUMNS_MATRIX[0][0], column[0]) \
                       ^ g_mul(INV_MIX_COLUMNS_MATRIX[0][1], column[1]) \
                       ^ g_mul(INV_MIX_COLUMNS_MATRIX[0][2], column[2]) \
                       ^ g_mul(INV_MIX_COLUMNS_MATRIX[0][3], column[3])

        state[i * 4 + 1] = g_mul(INV_MIX_COLUMNS_MATRIX[1][0], column[0]) \
                           ^ g_mul(INV_MIX_COLUMNS_MATRIX[1][1], column[1]) \
                           ^ g_mul(INV_MIX_COLUMNS_MATRIX[1][2], column[2]) \
                           ^ g_mul(INV_MIX_COLUMNS_MATRIX[1][3], column[3])

        state[i * 4 + 2] = g_mul(INV_MIX_COLUMNS_MATRIX[2][0], column[0]) \
                           ^ g_mul(INV_MIX_COLUMNS_MATRIX[2][1], column[1]) \
                           ^ g_mul(INV_MIX_COLUMNS_MATRIX[2][2], column[2]) \
                           ^ g_mul(INV_MIX_COLUMNS_MATRIX[2][3], column[3])

        state[i * 4 + 3] = g_mul(INV_MIX_COLUMNS_MATRIX[3][0], column[0]) \
                           ^ g_mul(INV_MIX_COLUMNS_MATRIX[3][1], column[1]) \
                           ^ g_mul(INV_MIX_COLUMNS_MATRIX[3][2], column[2]) \
                           ^ g_mul(INV_MIX_COLUMNS_MATRIX[3][3], column[3])
    return state
