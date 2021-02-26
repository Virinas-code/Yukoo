# -*- coding: utf-8 -*-
from __future__ import print_function
"""
MyEngine Engine base.

Base engine
"""
import chess

PAWN_VALUE = 100
KNIGHT_VALUE = 300
BISHOP_VALUE = 300
ROOK_VALUE = 500
QUEEN_VALUE = 900
PIECES_VALUES = {"p": PAWN_VALUE, "n": KNIGHT_VALUE, "b": BISHOP_VALUE,
                 "r": ROOK_VALUE, "q": QUEEN_VALUE}


def printi(*args):
    """Debug mode printer."""
    print("info string", (arg for arg in args))


class EngineBase:
    """Engine base."""

    def __init__(self, name, author, board=chess.Board()):
        """Initialise engine."""
        self.name = name
        self.author = author
        self.board = board

    def evaluate(self, depth, board=None):
        """Evaluate position."""
        if board is None:
            board = self.board
        depth = int(depth)
        # printi(board.piece_map())
        transpos = list()
        white_score = 0
        black_score = 0
        for piece in board.piece_map().values():
            if piece.symbol().isupper():
                if piece.symbol().lower() in PIECES_VALUES.keys():
                    white_score += PIECES_VALUES[piece.symbol().lower()]
            else:
                if piece.symbol() in PIECES_VALUES.keys():
                    black_score += PIECES_VALUES[piece.symbol()]

        if depth != 1:
            best_evaluation = (0-float('inf')) if board.turn == chess.WHITE else (float('inf'))
            printi("best evaluation", best_evaluation)
            for move in board.generate_legal_moves():
                test = chess.Board(fen=board.fen())
                test.push(move)
                hsh = hash(test.fen())
                if hsh not in transpos:
                    if test.board_fen() == "3Q3k/8/8/8/8/8/8/7K":
                        printi("yes!")
                    # printi("board\n", test)
                    evaluation = self.evaluate(depth-1, board=test)
                    # printi("evaluation", evaluation)
                    best_evaluation = max(evaluation, best_evaluation) if test.turn == chess.WHITE else min(evaluation, best_evaluation)
                    # printi("best evaluation", bestEvaluation)
                    transpos.append(hsh)
                else:
                    printi("transpos", test.fen(), "move", move)
            return best_evaluation
        return white_score-black_score
