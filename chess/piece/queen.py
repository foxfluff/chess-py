
from ._piece import chess_piece

class queen(chess_piece):

    def avaliable_moves(self):
        raise NotImplementedError

    @staticmethod
    def legal_moves():
        return [[x, x] for x in range(-7, 8) if x != 0] \
            + [[x, -x] for x in range(-7, 8) if x != 0] \
            + [[x, 0] for x in range(-7, 8) if x != 0] \
            + [[0, y] for y in range(-7, 8) if y != 0]