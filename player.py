# BOF#######################################################################BOF
from abc import ABCMeta, abstractmethod
import random


class Player(metaclass=ABCMeta):  # Abstract prototype. #######################
    def __init__(self, arguments=None):
        self._arguments = arguments

    @abstractmethod
    def best_move(self, game):
        pass


class PlayerRandom(Player):  # ################################################
    def best_move(self, game):
        m = random.choice(game.get_possible_moves())
        return game.make_move(m)


class PlayerHuman(Player):  # #################################################
    def best_move(self, game):
        moves = game.get_possible_moves()
        while True:
            try:
                m = int(input("Your move " + str(moves) + " : "))
                return game.make_move(m)
            except ValueError:
                pass
# EOF#######################################################################EOF
