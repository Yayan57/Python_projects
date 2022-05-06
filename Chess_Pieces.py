from Game_Board import *

class Pawn:
    PIECE_IMG = 'pawn.png'
    NAME = 'Pawn'

    def __init__(self, name, position_i, position_j, alive, color, has_moved_yet, available_moves, checking_king, blocking_check):
        self.position = position_i
        self.position = position_j
        self.alive = alive
        self.color = color
        self.has_moved_yet = has_moved_yet
        self.available_moves = available_moves
        self.checking_king = checking_king
        self.blocking_check = blocking_check
        self.name = name


class Rook:
    PIECE_IMG = 'rook.png'

    def __init__(self, name, position_i, position_j, alive, color, has_moved_yet, available_moves, checking_king, blocking_check):
        self.position = position_i
        self.position = position_j
        self.alive = alive
        self.color = color
        self.has_moved_yet = has_moved_yet
        self.available_moves = available_moves
        self.checking_king = checking_king
        self.blocking_check = blocking_check
        self.name = name



class Knight:
    PIECE_IMG = 'knight.png'

    def __init__(self, name, position_i, position_j, alive, color, has_moved_yet, available_moves, checking_king, blocking_check):
        self.position = position_i
        self.position = position_j
        self.alive = alive
        self.color = color
        self.has_moved_yet = has_moved_yet
        self.available_moves = available_moves
        self.checking_king = checking_king
        self.blocking_check = blocking_check
        self.name = name


class Bishop:
    PIECE_IMG = 'pawn.png'

    def __init__(self, name, position_i, position_j, alive, color, has_moved_yet, available_moves, checking_king, blocking_check):
        self.position = position_i
        self.position = position_j
        self.alive = alive
        self.color = color
        self.has_moved_yet = has_moved_yet
        self.available_moves = available_moves
        self.checking_king = checking_king
        self.blocking_check = blocking_check
        self.name = name


class Queen:
    PIECE_IMG = 'pawn.png'

    def __init__(self, name, position_i, position_j, alive, color, has_moved_yet, available_moves, checking_king, blocking_check):
        self.position = position_i
        self.position = position_j
        self.alive = alive
        self.color = color
        self.has_moved_yet = has_moved_yet
        self.available_moves = available_moves
        self.checking_king = checking_king
        self.blocking_check = blocking_check
        self.name = name


class King:
    PIECE_IMG = 'pawn.png'

    def __init__(self, name, position_i, position_j, alive, color, has_moved_yet, available_moves, checking_king, is_in_check):
        self.position = position_i
        self.position = position_j
        self.alive = alive
        self.color = color
        self.has_moved_yet = has_moved_yet
        self.available_moves = available_moves
        self.checking_king = checking_king
        self.is_in_check = is_in_check
        self.name = name