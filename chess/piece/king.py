
from ._piece import chess_piece

class king(chess_piece):

    def avaliable_moves(self):
        raise NotImplementedError

    @staticmethod
    def legal_moves():
        return [[x, y]
            for x in range(-1, 2)
            for y in range(-1, 2) if x != 0 or y != 0)]
