
from ._piece import chess_piece

class knight(chess_piece):

    def avaliable_moves(self):
        raise NotImplementedError

    @staticmethod
    def legal_moves():
        return [
            [x, y] for x in range(-2, 3) for y in range(-2, 3)
            if abs(x) + abs(y) == 3
            ]
            # this made me feel good >w<

