# -*- coding: utf-8 -*-
"""
MyEngine Engine base.

Base engine
"""
from __future__ import print_function
import chess
import chess.polyglot

PAWN_VALUE = 100
KNIGHT_VALUE = 300
BISHOP_VALUE = 300
ROOK_VALUE = 500
QUEEN_VALUE = 900
PIECES_VALUES = {"p": PAWN_VALUE, "n": KNIGHT_VALUE, "b": BISHOP_VALUE,
                 "r": ROOK_VALUE, "q": QUEEN_VALUE}


def printi(*args):
    """Debug mode printer."""
    print("info string", args)


class EngineBase:
    """Engine base."""

    def __init__(self, name, author, board=chess.Board()):
        """Initialise engine."""
        self.name = name
        self.author = author
        self.board = board

    def evaluate(self, board):
        """Evaluate position."""
        white_score = 0
        black_score = 0
        for piece in board.piece_map().values():
            if piece.symbol().isupper():
                if piece.symbol().lower() in PIECES_VALUES.keys():
                    white_score += PIECES_VALUES[piece.symbol().lower()]
            else:
                if piece.symbol() in PIECES_VALUES.keys():
                    black_score += PIECES_VALUES[piece.symbol()]

        return white_score-black_score
