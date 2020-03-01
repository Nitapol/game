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
# BOF#######################################################################BOF
from game import Game


class GameStoneGameII(Game):  # ###############################################
    #  0 1 2
    #  3 4 5
    #  6 7 8
    piles = [[[1, 2], [4, 8], [3, 6]],  # for 0
                     [[0, 2], [4, 7]],  # for 1
                     [[0, 1], [4, 6], [5, 8]],  # for 2
                     [[0, 6], [4, 5]],  # for 3
                     [[0, 8], [1, 7], [2, 6], [3, 5]],  # for 4
                     [[2, 8], [3, 4]],  # for 5
                     [[0, 3], [4, 2], [7, 8]],  # for 6
                     [[6, 8], [1, 4]],  # for 7
                     [[6, 7], [0, 4], [2, 5]],  # for 8
                     ]
    square_free = '.'
    square_X = 'X'
    square_O = 'O'

    def __init__(self, player=Game.player1):
        super().__init__()
        self._player_X = player
        self._board = [2, 7, 9, 4, 4]

    def get_board(self):
        return self._board

    def get_possible_moves(self):
        if self._state is not Game.play:
            return []
        return [
            index
            for index, square in enumerate(self._board)
            if square == GameTicTacToe.square_free
        ]

    def make_move(self, index, player=None):  # return True if can continue
        # can play out of order(future feature)
        if not isinstance(index, int) or 0 < index > 8:
            raise ValueError
        if player is not None:
            if not isinstance(player, int)\
                    or Game.player1 < player > Game.player2:
                raise ValueError
            self._player = player
        if self._board[index] != GameTicTacToe.square_free:
            raise ValueError
        if self._state != Game.play:
            raise ValueError
        if self._player_X == self._player:
            piece = GameTicTacToe.square_X
        else:
            piece = GameTicTacToe.square_O
        self._board[index] = piece
        for index1, index2 in GameTicTacToe.winning_pairs[index]:
            if piece == self._board[index1] == self._board[index2]:
                if self._player == Game.player1:
                    self._state = Game.won
                else:
                    self._state = Game.lost
                return False
        if len(self.get_possible_moves()) == 0:
            self._state = Game.draw
            return False
        self.next_player()
        return True

    def __str__(self):
        return ''.join(self._board)

    def print_game(self):
        print()
        s = str(self)
        for i in range(0, 9, 3):
            print(s[i] + " " + s[i + 1] + " " + s[i + 2])
# EOF#######################################################################EOF

# BOF#######################################################################BOF
from game import Game
from game_tic import GameTicTacToe
from player import PlayerHuman, PlayerRandom
from player_negation import PlayerNegation
from player_monte import PlayerMonte
import random
import time
import argparse

if __name__ == '__main__':  # Testing ... #####################################
    def main():
        list_of_players = [
            PlayerHuman, PlayerRandom, PlayerNegation, PlayerMonte]

        def get_player(player_string_name):
            for p in list_of_players:
                if player_string_name == p.__name__:
                    return p

        player_choices = []
        help_string = ''
        next_player = False
        for player in list_of_players:
            name = player.__name__
            player_choices.append(name)
            help_string += name + ' | ' if next_player else ''
            next_player = True
        parser = argparse.ArgumentParser()
        for player in [1, 2]:
            s = str(player)
            parser.add_argument(
                'player'+s, choices=player_choices,
                help='selection for player #'+s,
                default=list_of_players[1+player].__name__
            )
            parser.add_argument(
                '-a'+s, '--arguments'+s, help='arguments for player'+s
            )

        parser.add_argument('--verbose', '-v', action='store_true',
                            help='print an additional information')
        parser.add_argument('--silent', '-s', action='store_true',
                            help='print only the result at the end')
        parser.add_argument('--random_seed', '-r', type=int,
                            help='use this number in random.seed(number)')
        parser.add_argument('--games', '-g', type=int, default=1,
                            help='number of games to play')
        args = parser.parse_args()
        print(args)

        if args.random_seed is not None:
            random.seed(args.random_seed)
        won = 0
        lost = 0
        draw = 0
        game_number = 0
        verbose = True
        two_players = [get_player(args.player1)(args.arguments1),
                       get_player(args.player2)(args.arguments2)]
        for player in two_players:
            if player.__class__ == PlayerHuman:
                verbose = True

        while True:
            odd_game_number = game_number % 2 == 1
            if odd_game_number:
                game = GameTicTacToe(player=Game.player2)
            else:
                game = GameTicTacToe()
            if verbose:
                game.print_game()
            state = game.get_state()
            move_number = 0
            while state == Game.play:
                odd_move_number = move_number % 2 == 1
                index = 0 if odd_game_number == odd_move_number else 1
                two_players[index].best_move(game)
                if verbose:
                    game.print_game()
                state = game.get_state()
                move_number += 1
            if odd_game_number:
                if state == Game.won:
                    state = Game.lost
                elif state == Game.lost:
                    state = Game.won
            if state == Game.won:
                if verbose:
                    print('Congratulation! You made impossible be possible!')
                won += 1
            elif state == Game.lost:
                if verbose:
                    print('Next time!')
                lost += 1
            elif state == Game.draw:
                if verbose:
                    print('Friendship won!')
                draw += 1
            game_number += 1
            if verbose or game_number == args.games:
                print('won', won, 'lost', lost, 'draw', draw)
            if game_number == args.games:
                break

    start_time = time.perf_counter()
    main()
    total_time = time.perf_counter() - start_time
    print('total_time', total_time)
# EOF#######################################################################EOF
