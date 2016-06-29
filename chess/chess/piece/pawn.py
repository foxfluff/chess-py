
from ._piece import chess_piece

class pawn(chess_piece):

    def avaliable_moves(self):
        raise NotImplementedError

    @staticmethod
    def legal_moves():
        return [[x, 1] for x in range(-1, 2)] + [[0, 2]]

