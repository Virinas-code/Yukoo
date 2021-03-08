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
                 "r": ROOK_VALUE, "q": QUEEN_VALUE, "k": 0}


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
        piece_map = board.piece_map()
        for piece in piece_map:
            if piece_map[piece].symbol().isupper():
                white_score += PIECES_VALUES[piece_map[piece].symbol().lower()]
            else:
                black_score += PIECES_VALUES[piece_map[piece].symbol()]

        return white_score-black_score

    def search(self, depth, board):
        """Search best move (Minimax from wikipedia)."""

    def minimax(self, board, depth, maximimize_white):
        """Minimax algorithm from Wikipedia."""
        if depth == 0 or board.is_game_over():
            return self.evaluate(board), chess.Move.from_uci("0000")
        if maximimize_white:
            value = -float('inf')
            for move in board.legal_moves:
                best_move = move
                break
            for move in board.legal_moves:
                e = chess.Board(fen=board.fen())
                e.push(move)
                evaluation = self.minimax(e, depth-1, False)[0]
                if value < evaluation:
                    value = evaluation
                    best_move = move
            return value, best_move
        else:
            # minimizing white
            value = float('inf')
            for move in board.legal_moves:
                best_move = move
                break
            for move in board.legal_moves:
                e = chess.Board(fen=board.fen())
                e.push(move)
                evaluation = self.minimax(e, depth-1, True)[0]
                if value > evaluation:
                    value = evaluation
                    best_move = move
            return value, best_move
        """depth = int(depth)
        if depth == 1:
            return self.evaluate(board)
        else:
            moves_to_get = list()
            eval = -float("inf") if board.turn == chess.BLACK else float('inf')
            for move in board.legal_moves:
                printi("move", move)
                test = chess.Board(fen=board.fen())
                moves_to_get.append(move)
                test.push(move)
                print(test)
                score = self.evaluate(test)
                if board.turn == chess.WHITE:
                    eval = max(score, eval)
                else:
                    eval = min(score, eval)
            return eval"""
