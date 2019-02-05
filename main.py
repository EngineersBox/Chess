import players
import pieces
import board
from tkinter import *
import tkinter as ttk
from PIL import ImageTk, Image
from os.path import dirname, abspath
import os

class game:

    def __init__(self, master):
        self.GameBoard = board.board()
        self.bPlayer = players.blackPlayer()
        self.wPlayer = players.whitePlayer()
        for i in range(16):
            if i < 8: #pawn
                self.GameBoard.setPos(1, i, self.bPlayer.pieces[i])
                self.GameBoard.setPos(6, i, self.wPlayer.pieces[i])
            elif 8 <= i < 10: #knight
                self.GameBoard.setPos(0, 1, self.bPlayer.pieces[i])
                self.GameBoard.setPos(0, 6, self.bPlayer.pieces[i])
                self.GameBoard.setPos(7, 1, self.wPlayer.pieces[i])
                self.GameBoard.setPos(7, 6, self.wPlayer.pieces[i])
            elif 10 <= i < 12: #bishop
                self.GameBoard.setPos(0, 2, self.bPlayer.pieces[i])
                self.GameBoard.setPos(0, 5, self.bPlayer.pieces[i])
                self.GameBoard.setPos(7, 2, self.wPlayer.pieces[i])
                self.GameBoard.setPos(7, 5, self.wPlayer.pieces[i])
            elif 12 <= i < 14: #rook
                self.GameBoard.setPos(0, 0, self.bPlayer.pieces[i])
                self.GameBoard.setPos(0, 7, self.bPlayer.pieces[i])
                self.GameBoard.setPos(7, 0, self.wPlayer.pieces[i])
                self.GameBoard.setPos(7, 7, self.wPlayer.pieces[i])
            elif 14 == i: #queen
                self.GameBoard.setPos(0, 3, self.bPlayer.pieces[i])
                self.GameBoard.setPos(7, 3, self.wPlayer.pieces[i])
            elif 15 == i: #king
                self.GameBoard.setPos(0, 4, self.bPlayer.pieces[i])
                self.GameBoard.setPos(7, 4, self.wPlayer.pieces[i])
        self.master = master
        self.create_widgets()
        self.clickCount = 1
        self.pos1 = []
        self.pos2 = []

    def getGameBoard(self):
        return self.GameBoard

    def getbPlayer(self):
        return self.bPlayer

    def getwPlayer(self):
        return self.wPlayer

    def create_widgets(self):
        self.main_canvas = Canvas(self.master, bg='white', height=400, width=500)
        self.main_canvas.pack(side=TOP, padx=10, pady=10)

        self.f_path = dirname(abspath(__file__))
        count = 1
        dx = 50
        dy = 50

        for cx in range(self.GameBoard.getSizeX()):
            for cy in range(self.GameBoard.getSizeY()):
                if count % 2 == 0:
                    if cx == 1 and 0 <= cy <= 7:
                        #pawn
                        self.bpawn = ImageTk.PhotoImage(file=self.f_path + "/icons/black-pawn.png")
                        self.main_canvas.create_image((cx * dx), (cy * dy), tags=str(str(cx) + "," + str(cy)), image=self.bpawn)
                    elif cx == 0 and (cy == 1 or cy == 6):
                        #knight
                        self.bknight = ImageTk.PhotoImage(file=self.f_path + "/icons/black-knight.png")
                        self.main_canvas.create_image((cx * dx), (cy * dy), tags=str(str(cx) + "," + str(cy)), image=self.bknight)
                    elif cx == 0 and (cy == 2 or cy == 5):
                        #bishop
                        self.bbishop = ImageTk.PhotoImage(file=self.f_path + "/icons/black-bishop.png")
                        self.main_canvas.create_image((cx * dx), (cy * dy), tags=str(str(cx) + "," + str(cy)), image=self.bbishop)
                    elif cx == 0 and (cy == 0 or cy == 7):
                        #rook
                        self.brook = ImageTk.PhotoImage(file=oself.f_path + "/icons/black-rook.png")
                        self.main_canvas.create_image((cx * dx), (cy * dy), tags=str(str(cx) + "," + str(cy)), image=self.brook)
                    elif cx == 0 and cy == 3:
                        #queen
                        self.bqueen = ImageTk.PhotoImage(file=self.f_path + "/icons/black-queen.png")
                        self.main_canvas.create_image((cx * dx), (cy * dy), tags=str(str(cx) + "," + str(cy)), image=self.bqueen)
                    elif cx == 0 and cy == 4:
                        #king
                        self.bking = ImageTk.PhotoImage(file=self.f_path + "/icons/black-king.png")
                        self.main_canvas.create_image((cx * dx), (cy * dy), tags=str(str(cx) + "," + str(cy)), image=self.bking)
                    else:
                        pass
                    self.rect_canv = self.main_canvas.create_rectangle(cx * dx, cy * dy, (cx + 1) * dx, (cy + 1) * dy, fill="black", tags=str(str(cx) + "," + str(cy)))
                    self.main_canvas.tag_bind(self.rect_canv, '<ButtonPress-1>', self.onObjectClick)
                else:
                    if cx == 6 and 0 <= cy <= 7:
                        #pawn
                        self.wpawn = ImageTk.PhotoImage(file=self.f_path + "/icons/white-pawn.png")
                        self.main_canvas.create_image((cx * dx), (cy * dy), tags=str(str(cx) + "," + str(cy)), image=self.wpawn)
                    elif cx == 7 and (cy == 1 or cy == 6):
                        #knight
                        self.wknight = ImageTk.PhotoImage(file=self.f_path + "/icons/white-knight.png")
                        self.main_canvas.create_image((cx * dx), (cy * dy), tags=str(str(cx) + "," + str(cy)), image=self.wknight)
                    elif cx == 7 and (cy == 2 or cy == 5):
                        #bishop
                        self.wbishop = ImageTk.PhotoImage(file=self.f_path + "/icons/white-bishop.png")
                        self.main_canvas.create_image((cx * dx), (cy * dy), tags=str(str(cx) + "," + str(cy)), image=self.wbishop)
                    elif cx == 7 and (cy == 2 or cy == 5):
                        #rook
                        self.wrook = ImageTk.PhotoImage(file=self.f_path + "/icons/white-rook.png")
                        self.main_canvas.create_image((cx * dx), (cy * dy), tags=str(str(cx) + "," + str(cy)), image=self.wrook)
                    elif cx == 7 and cy == 3:
                        #queen
                        self.wqueen = ImageTk.PhotoImage(file=self.f_path + "/icons/white-queen.png")
                        self.main_canvas.create_image((cx * dx), (cy * dy), tags=str(str(cx) + "," + str(cy)), image=self.wqueen)
                    elif cx == 7 and cy == 4:
                        #king
                        self.wking = ImageTk.PhotoImage(file=self.f_path + "/icons/white-king.png")
                        self.main_canvas.create_image((cx * dx), (cy * dy), tags=str(str(cx) + "," + str(cy)), image=self.wking)
                    else:
                        pass
                    self.rect_canv = self.main_canvas.create_rectangle(cx * dx, cy * dy, (cx + 1) * dx, (cy + 1) * dy, fill="white", tags=str(str(cx) + "," + str(cy)))
                    self.main_canvas.tag_bind(self.rect_canv, '<ButtonPress-1>', self.onObjectClick)
                count += 1
            count += 1

        self.quit_button = Button(self.master, text='Quit', width=10, command=self.master.quit)
        self.quit_button.pack(side=RIGHT, padx=10, pady=10)

    def onObjectClick(self, event):
        retTags = str(event.widget.gettags(event.widget.find_closest(event.x, event.y)))[2:5]
        if self.clickCount == 0:
            self.clickCount += 1
            self.pos1 = [int(retTags[0]), int(retTags[2])]
        elif self.clickCount == 1:
            self.clickCount -= 1
            self.pos2 = [int(retTags[0]), int(retTags[2])]
        print(self.clickCount)
        if self.clickCount == 1:
            #print(self.GameBoard.getPos(self.pos1[0], self.pos1[1]), self.GameBoard.getPos(self.pos2[0], self.pos2[1]))
            self.GameBoard.moveTo(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1], self.GameBoard, self.bPlayer)
            #print(self.GameBoard.getPos(self.pos1[0], self.pos1[1]), self.GameBoard.getPos(self.pos2[0], self.pos2[1]))

if __name__ == "__main__":

    root = ttk.Tk()
    app = game(root)
    root.mainloop()
