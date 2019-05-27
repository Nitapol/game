# BOF#######################################################################BOF
import random
from game import Game
from player import Player
from copy import deepcopy


def negation_maximize(game, color):  # ########################################
    state = game.get_state()
    if state != Game.play:
        v = 1.0 if state == Game.won else -1.0 if state == Game.lost else 0.0
        return color * v, None
    v = float("-inf")
    best_move = []
    moves = game.get_possible_moves()
    for m in moves:
        new_board = deepcopy(game)
        new_board.make_move(m)
        x, _ = negation_maximize(new_board, -color)
        x = - x
        if x >= v:
            if x > v:
                best_move = []
            v = x
            best_move.append(m)
    return v, best_move


class PlayerNegation(Player):  # ##############################################
    def best_move(self, game):
        m = game.get_possible_moves()
        if len(m) != 9:
            _, m = negation_maximize(
                game, 1 if game.get_player() == Game.player1 else - 1)
        return game.make_move(random.choice(m))
# EOF#######################################################################EOF
