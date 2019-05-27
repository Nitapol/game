# BOF#######################################################################BOF
from abc import ABCMeta, abstractmethod


class Game(metaclass=ABCMeta):  # Game for two players. Abstract prototype. ###
    player1 = 1
    player2 = 2
    play = 0  # game in progress
    won = 1   # player1 won and player2 lost
    lost = 2  # player1 lost and player2 won
    draw = 3

    def __init__(self, player=player1):
        self._state = Game.play
        self._player = player

    def next_player(self, player=None):
        self._player = player if player is not None else \
            Game.player2 if self._player == Game.player1 else Game.player1

    def get_state(self):
        return self._state

    def get_player(self):
        return self._player

    @abstractmethod
    def get_possible_moves(self) -> list:
        pass

    @abstractmethod
    def make_move(self, move, player=None) -> bool:
        pass

    @abstractmethod
    def print_game(self) -> None:
        pass
# EOF#######################################################################EOF
