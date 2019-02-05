class piece:

    def __init__(self, types, moves, attacks, limitdist, colour):
        self.type = types
        self.moves = moves
        self.attacks = attacks
        self.limitdist = limitdist
        self.colour = colour
        self.location = []

    def getLimitdist(self):
        return self.limitdist

    def getAttacks(self):
        return self.attacks

    def getMoves(self):
        return self.validmoves

    def getType(self):
        return self.type

    def getColour(self):
        return self.colour

    def getLocation(self):
        return self.location

class pawn(piece):

    def __init__(self, colour):
        moves = [[1, 0]]
        attacks = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        piece.__init__(self, "pawn", moves, attacks, True, colour)

class rook(piece):

    def __init__(self, colour):
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        attacks = [[1, 0], [-1, 0], [0, -1], [0, -1]]
        piece.__init__(self, "rook", moves, attacks, False, colour)

class bishop(piece):

    def __init__(self, colour):
        moves = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        attacks = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        piece.__init__(self, "bishop", moves, attacks, False, colour)

class knight(piece):

    def __init__(self, colour):
        moves = [[3, 1], [3, -1], [-3, 1], [-3, -1]]
        attacks = [[3, 1], [3, -1], [-3, 1], [-3, -1]]
        piece.__init__(self, "knight", moves, attacks, True, colour)

class king(piece):

    def __init__(self, colour):
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        attacks = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        piece.__init__(self, "king", moves, attacks, True, colour)

class queen(piece):

    def __init__(self, colour):
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        attacks = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        piece.__init__(self, "queen", moves, attacks, False, colour)
