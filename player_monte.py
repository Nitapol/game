# BOF#######################################################################BOF
import random
from game import Game
from player import Player
from copy import deepcopy
from math import log, sqrt
import argparse


class Node:  # ################################################################
    def __init__(self, parent, move, possible_moves):
        self.parent = parent
        self.move = move
        self.possible_moves = possible_moves
        self.children = []
        self.wins = 0
        self.visits = 0

    def add_child(self, m, possible_moves):
        n = Node(self, m, possible_moves)
        self.possible_moves.remove(m)
        self.children.append(n)
        return n

    def update(self, result):
        self.visits += 1
        self.wins += result

    def __repr__(self):
        return "[M:" + str(self.move) + " W/V:" + str(self.wins) + "/" + \
               str(self.visits) + " U:" + str(self.possible_moves) + "]"

    def tree_to_string(self, indent):
        s = '\n' + '| ' * indent + str(self)
        for c in self.children:
            s += c.tree_to_string(indent + 1)
        return s

    def children_to_string(self):
        return ''.join(str(c) + '\n' for c in self.children)


def tree_search(game, playouts, verbose=False, silent=True):  # ###############
    root = Node(None, None, game.get_possible_moves())

    for _ in range(playouts):
        node = root
        state = deepcopy(game)
        # Selection
        while not node.possible_moves and node.children:
            best_value = float("-inf")
            nodes = []
            for c in node.children:
                value = c.wins / c.visits + 0.2 * sqrt(
                    2 * log(node.visits) / c.visits)
                if value >= best_value:
                    if value > best_value:
                        nodes = []
                    best_value = value
                    nodes.append(c)
            node = random.choice(nodes)
            state.make_move(node.move)
        # Expansion
        if node.possible_moves:
            move = random.choice(node.possible_moves)
            state.make_move(move)
            node = node.add_child(move, state.get_possible_moves())
        # Simulation
        while True:
            moves = state.get_possible_moves()
            if not moves:
                break
            state.make_move(random.choice(moves))
        # Backpropagation
        s = state.get_state()
        result = 1.0 if s is Game.won else 0.0 if s is Game.lost else 0.5
        if game.get_player() != Game.player1:
            result = 1.0 - result
        while node is not None:
            node.update(result)
            node = node.parent
    if not silent:
        if verbose:
            print(root.tree_to_string(0))
        else:
            print(root.children_to_string())
    best_moves = []
    max_visits = 0
    for c in root.children:
        if c.visits >= max_visits:
            if c.visits > max_visits:
                best_moves = []
            max_visits = c.visits
            best_moves.append(c.move)
    return random.choice(best_moves)


class PlayerMonte(Player):  # short from PlayerMonteCarloTreeSearch############
    def __init__(self, arguments=None):
        super().__init__(arguments)
        self._arguments = arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('--playouts', '-p', type=int, default=1,
                            help='number of games to play')
        parser.add_argument('--verbose', '-v', action='store_true',
                            help='print an additional information')
        parser.add_argument('--silent', '-s', action='store_false',
                            help='print only the result at the end')
        self._args = parser.parse_args(
            arguments.split() if arguments is not None else '')
        print(self._args)

    def best_move(self, game):
        m = tree_search(game, playouts=self._args.playouts,
                        verbose=self._args.verbose, silent=self._args.silent)
        return game.make_move(m)
# EOF#######################################################################EOF
