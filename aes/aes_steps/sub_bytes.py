from utils.constants import S_BOX


def sub_bytes(state):
    return [S_BOX[b] for b in state]
