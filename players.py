import pieces

class player:

    def __init__(self, colour):
        self.pawn = 8
        self.knight = 2
        self.bishop = 2
        self.rook = 2
        self.queen = 1
        self.king = 1
        self.colour = colour
        self.pieces = [pieces.pawn(self.colour)] * self.pawn
        self.pieces += [pieces.knight(self.colour)] * self.knight
        self.pieces += [pieces.bishop(self.colour)] * self.bishop
        self.pieces += [pieces.rook(self.colour)] * self.rook
        self.pieces += [pieces.queen(self.colour)] * self.queen
        self.pieces += [pieces.king(self.colour)] * self.king

    def getPieceCount(self, piece):
        #return self.piece
        count = 0
        for i in range(len(self.pieces)):
            if str(self.pieces[i].getType()) == piece:
                count += 1
        return count

    def delPieceCount(self, piece, count):
        #self.piece += count
        numInst = abs(count)
        for i in range(len(self.pieces) - 1):
            if str(self.pieces[i].getType()) == piece and numInst > 0:
                del(self.pieces[i])

    def getColour(self):
        return self.colour

    def getPieces(self):
        return self.pieces

class blackPlayer(player):

    def __init__(self):
        player.__init__(self, "black")

class whitePlayer(player):

    def __init__(self):
        player.__init__(self, "white")
