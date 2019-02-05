import pieces
import players
import numpy as np

class tile:

    def __init__(self):
        self.type = "tile"

    def getType(self):
        return self.type

class board:

    def __init__(self, sizeX=8, sizeY=8):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.board = np.ndarray([sizeX, sizeY], dtype=object)
        for cx in range(self.sizeX):
            for cy in range(self.sizeY):
                self.board[cx, cy] = tile

    def getSizeX(self):
        return self.sizeX

    def getSizeY(self):
        return self.sizeY

    def getBoard(self):
        return self.board

    def setPos(self, posX, posY, obj):
        self.board[posX, posY] = obj

    def getPos(self, posX, posY):
        return self.board[posX, posY]

    def checkDirections(self, posX1, posY1, posX2, posY2, cboard, opplayer):
        obj = cboard.getPos(posX1, posY1)
        obj2 = cboard.getPos(posX2, posY2)
        dSignX = mathFuncs.getdsign(posX1, posX2)
        dSignY = mathFuncs.getdsign(posY1, posY2)
        destIsPiece = False
        pieceBlock = False
        if issubclass(cboard.getPos(posX2, posY2).__class__, pieces.piece):
            destIsPiece = True
        for cpos in range((posX2 - posX1) - 1):
            if issubclass(cboard.getPos(posX1 + (cpos * dSignX), posY1 + (cpos * dSignY)).__class__, pieces.piece):
                pieceBlock = True
            else:
                pieceBlock = False
        if destIsPiece == True and pieceBlock == False and obj2.getColour() != obj.getColour():
            cboard.setPos(posX2, posY2, obj)
            opplayer.delPieceCount(str(obj.getType()), - 1)
            cboard.setPos(posX1, posY1, tile)
        elif destIsPiece == True and pieceBlock == False and obj2.getColour() == obj.getColour():
            pass
        elif pieceBlock == False and destIsPiece == False:
            cboard.setPos(posX2, posY2, obj)
            cboard.setPos(posX1, posY1, tile)
        elif pieceBlock == True:
            pass
        else:
            pass

    def checkAttack(self, posX1, posY1, posX2, posY2, cboard, opplayer, obj, obj2):
        if issubclass(obj2.__class__, pieces.piece) and obj2.getColour() != obj.getColour():
            cboard.setPos(posX2, posY2, obj)
            opplayer.delPieceCount(str(obj.getType()), opplayer.getPieceCount(str(obj.getType())) - 1)
            cboard.setPos(posX1, posY1, tile)
        elif issubclass(obj2.__class__, pieces.piece) and obj2.getColour() == obj.getColour():
            pass
        elif not issubclass(obj2.__class__, pieces.piece):
            cboard.setPos(posX2, posY2, obj)
            cboard.setPos(posX1, posY1, tile)
        else:
            pass

    def moveTo(self, posX1, posY1, posX2, posY2, cboard, opplayer):
        obj = cboard.getPos(posX1, posY1)
        obj2 = cboard.getPos(posX2, posY2)
        pieceBlock = False
        if issubclass(obj.__class__, pieces.bishop) and posX2 - posX1 == posY2 - posY1:
            board.checkDirections(self, posX1, posY1, posX2, posY2, cboard, opplayer)
        elif issubclass(obj.__class__, pieces.rook) and (posX2 - posX1 == 0 or posY2 - posY1 == 0):
            board.checkDirections(self, posX1, posY1, posX2, posY2, cboard, opplayer)
        elif issubclass(obj.__class__, pieces.queen) and (posX2 - posX1 == 0 or posY2 - posY1 == 0 or posX2 - posX1 == posY2 - posY1):
            board.checkDirections(self, posX1, posY1, posX2, posY2, cboard, opplayer)
        elif issubclass(obj.__class__, pieces.king) and  (-1 < posX2 - posX1 < 2 or -1 < posY2 - posY1 < 2):
            board.checkAttack(self, posX1, posY1, posX2, posY2, cboard, opplayer, obj ,obj2)
        elif issubclass(obj.__class__, pieces.knight) and ((abs(posX2 - posX1) == 2 and abs(posY2 - posY1) == 1 ) or (abs(posY2 - posY1) == 2 and abs(posX2 - posX1) == 1)):
            board.checkAttack(self, posX1, posY1, posX2, posY2, cboard, opplayer, obj ,obj2)
        elif issubclass(obj.__class__, pieces.pawn) and obj.getColour() == "white" and ((posY2 - posY1 == -1 and posX2 - posX1 == 0) or (posY2 - posY1 == -1 and abs(posX2 - posX1) == 1)):
            board.checkAttack(self, posX1, posY1, posX2, posY2, cboard, opplayer, obj ,obj2)
        elif issubclass(obj.__class__, pieces.pawn) and obj.getColour() == "black" and ((posY2 - posY1 == 1 and posX2 - posX1 == 0) or (posY2 - posY1 == 1 and abs(posX2 - posX1) == 1)):
            board.checkAttack(self, posX1, posY1, posX2, posY2, cboard, opplayer, obj ,obj2)

class mathFuncs:

    def getdsign(pos1, pos2):
        value = pos2 - pos1
        if value < 0:
            return -1
        elif value == 0:
            return 0
        else:
            return 1

    def retMove(posX1, posY1, posX2, posY2, limDist=True):
        dx = posX2 - posX1
        dy = posY2 - posY1
        distMult = 1
        if limDist == False:
            distMult = 9
        if dx < 0 and dy < 0:
            return [-1 * distMult, -1 * distMult]
        elif dx == 0 and dy < 0:
            return [0, -1 * distMult]
        elif dx < 0 and dy == 0:
            return [-1 * distMult, 0]
        elif dx > 0 and dy > 0:
            return [1 * distMult, 1 * distMult]
        elif dx == 0 and dy > 0:
            return [0, 1 * distMult]
        elif dx > 0 and dy == 0:
            return [1 * distMult, 0]
        elif dx < 0 and dy > 0:
            return [-1 * distMult, 1 * distMult]
        elif dx > 0 and dy < 0:
            return [1 * distMult, -1 * distMult]
        else:
            pass
