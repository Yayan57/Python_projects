# from tkinter import *
from Chess_Pieces import *
from Game_Board import *


def main():
    pawnW0 = Pawn('Pawn', 0, 1, 'yes', 'white', 'no',   'filler', 'no', 'no')
''' pawnW1 = Pawn('Pawn', 1, 1, 'yes', 'white', 'no',   'filler', 'no', 'no')
    pawnW2 = Pawn('Pawn', 2, 1, 'yes', 'white', 'no',   'filler', 'no', 'no')
    pawnW3 = Pawn('Pawn', 3, 1, 'yes', 'white', 'no',   'filler', 'no', 'no')
    pawnW4 = Pawn('Pawn', 4, 1, 'yes', 'white', 'no',   'filler', 'no', 'no')
    pawnW5 = Pawn('Pawn', 5, 1, 'yes', 'white', 'no',   'filler', 'no', 'no')
    pawnW6 = Pawn('Pawn', 6, 1, 'yes', 'white', 'no',   'filler', 'no', 'no')
    pawnW7 = Pawn('Pawn', 7, 1, 'yes', 'white', 'no',   'filler', 'no', 'no')
    pawnB0 = Pawn('Pawn', 0, 7, 'yes', 'black', 'no',   'filler', 'no', 'no')
    pawnB1 = Pawn('Pawn', 1, 7, 'yes', 'black', 'no',   'filler', 'no', 'no')
    pawnB2 = Pawn('Pawn', 2, 7, 'yes', 'black', 'no',   'filler', 'no', 'no')
    pawnB3 = Pawn('Pawn', 3, 7, 'yes', 'black', 'no',   'filler', 'no', 'no')
    pawnB4 = Pawn('Pawn', 4, 7, 'yes', 'black', 'no',   'filler', 'no', 'no')
    pawnB5 = Pawn('Pawn', 5, 7, 'yes', 'black', 'no',   'filler', 'no', 'no')
    pawnB6 = Pawn('Pawn', 6, 7, 'yes', 'black', 'no',   'filler', 'no', 'no')
    pawnB7 = Pawn('Pawn', 7, 7, 'yes', 'black', 'no',   'filler', 'no', 'no')
    RookW1 = Rook('Rook', 0, 0, 'yes', 'white', 'no',   'filler', 'no', 'no')
    RookW2 = Rook('Rook', 7, 0, 'yes', 'white', 'no',   'filler', 'no', 'no')
    RookB1 = Rook('Rook', 0, 8, 'yes', 'black', 'no',   'filler', 'no', 'no')
    RookB2 = Rook('Rook', 7, 8, 'yes', 'black', 'no',   'filler', 'no', 'no')
    KnightW1 = Knight('Knight', 1, 0, 'yes', 'white', 'no',   'filler', 'no', 'no')
    KnightW2 = Knight('Knight', 6, 0, 'yes', 'white', 'no',   'filler', 'no', 'no')
    KnightB1 = Knight('Knight', 1, 8, 'yes', 'black', 'no',   'filler', 'no', 'no')
    KnightB2 = Knight('Knight', 6, 8, 'yes', 'black', 'no',   'filler', 'no', 'no')
    BishopW1 = Bishop('Bishop', 2, 0, 'yes', 'white', 'no',   'filler', 'no', 'no')
    BishopW2 = Bishop('Bishop', 5, 0, 'yes', 'white', 'no',   'filler', 'no', 'no')
    BishopB1 = Bishop('Bishop', 2, 8, 'yes', 'black', 'no',   'filler', 'no', 'no')
    BishopB2 = Bishop('Bishop', 5, 8, 'yes', 'black', 'no',   'filler', 'no', 'no')
    QueenW1 = Queen('Queen', 3, 0, 'yes', 'white', 'no',   'filler', 'no', 'no')
    QueenB1 = Queen('Queen', 3, 8, 'yes', 'black', 'no',   'filler', 'no', 'no')
    KingW1 = King('King', 4, 0, 'yes', 'white', 'no',   'filler', 'no', 'no')
    KingB1 = King('King', 4, 8, 'yes', 'black', 'no',   'filler', 'no', 'no')

'''
    # print(pawnW3.name)

#   window = Tk()

for row in arr:
    for col in row:
        print(col, end=" ")  # print each element separated by space
    print()  # Add newline
#   window.mainloop()


if __name__ == '__main__':
    main()
