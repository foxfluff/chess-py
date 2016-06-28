
class chess_piece(object):

    def __init__(self, coordinate, color):
        self.position = coordinate
        self.color = color

    def avaliable_moves(self):
        # applies conditions to legal_moves()
        raise NotImplementedError

    @staticmethod
    def legal_moves(cls):
        # returns lists of all legal moves for a piece, regardless of any
        # conditions (ie queens can move 7 squares in any direction, pawns can
        # move two squares, etc)
        raise NotImplementedError

    @property
    def position(self):
        # might want to return as "A8, D5, etc"
        return self._x, self._y

    @position.setter
    def position(self, coordinate):
        # TODO - implement position.setter (accept tuples or strings?)
        raise NotImplementedError

    @property
    def color(self):
        # is this really necessary to have a property for this
        return self._color

    @color.setter
    def color(self, color):
        # TODO - piece color setting
        self._color = color
