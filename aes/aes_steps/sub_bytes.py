from utils.constants import S_BOX, INV_S_BOX


def sub_bytes(state):
    return [S_BOX[b] for b in state]


def inv_sub_bytes(state):
    return [INV_S_BOX[b] for b in state]
