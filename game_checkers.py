# BOF#######################################################################BOF
from game import Game


class GameCheckers(Game):  # #################################################
    #  🏁 https://en.wikipedia.org/wiki/English_draughts (British English) or checkers (American English;
    #  also called American checkers or straight checkers
    #  ⬜️🟩⬜️🟩⬜️🟩⬜️🟩  ..01..02..03..04
    #  🟩⬜️🟩⬜️🟩⬜️🟩⬜️  05..06..07..08..
    #  ⬜️🟩⬜️🟩⬜️🟩⬜️🟩  ..09..10..11..12
    #  🟩⬜️🟩⬜️🟩⬜️🟩⬜️  13..14..15..16..
    #  ⬜️🟩⬜️🟩⬜️🟩⬜️🟩  ..17..18..19..20
    #  🟩⬜️🟩⬜️🟩⬜️🟩⬜️  21..22..23..24..
    #  ⬜️🟩⬜️🟩⬜️🟩⬜️🟩  ..25..26..27..28
    #  🟩⬜️🟩⬜️🟩⬜️🟩⬜️  29..30..31..32..
    #  ...(X)...(X)...(X)...(X)
    #  (X)...(X)...(X)...(X)...
    #  ...(X)...(X)...(X)...(X)
    #  ___...___...___...___...
    #  ...___...___...___...
    #  ...(X)...(X)...(x)...(X)
    #
    board_size_x = 4
    board_size_y = 8
    board_size = board_size_x * board_size_y
    pieces_per_side = 12
    #  00 01 02 03 04 05 06 07 .x.x.x.x
    #  08 09 10 11 12 13 14 15 🟥⬜️🟩
    #  16
    #  24
    #  32
    #  40
    #
    #  56 57 58 59 60 61 62 63
    #
    #

    #  ┌───┬───┬───┬───┐
    #  │ . │ X │ . │ X │
    #  ├───┼───┼───┼───┤
    #  │   │   │   │┼┼┼│
    #  ├───┼───┼───┼───┤
    #  │   │   │   │   │
    #  └───┴───┴───┴───┘

    #  0123456789_123456789__123456789   1234_1234_1234_1234_1234_1234_1234_1234_
    #  ┌───┬───┬───┬───┬───┬───┬───┬───┐ ┌────┬────┬────┬────┬────┬────┬────┬────┐
    #  │   │ X │   │ X │   │ X │   │ X │ │    │ 01 │    │ 02 │    │ 03 │    │ 04 │
    #  ├───┼───┼───┼───┼───┼───┼───┼───┤ ├────┼────┼────┼────┼────┼────┼────┼────┤
    #  │ X │   │ X │   │ X │   │ X │   │ │ 05 │    │ 06 │    │ 07 │    │ 08 │    │
    #  ├───┼───┼───┼───┼───┼───┼───┼───┤ ├────┼────┼────┼────┼────┼────┼────┼────┤
    #  │   │ X │   │ X │   │ X │   │ X │ │    │ 09 │    │ 10 │    │ 11 │    │ 12 │
    #  ├───┼───┼───┼───┼───┼───┼───┼───┤ ├────┼────┼────┼────┼────┼────┼────┼────┤
    #  │ . │   │ . │   │ . │   │ . │   │ │    │ 01 │    │ 02 │    │ 03 │    │ 04 │
    #  ├───┼───┼───┼───┼───┼───┼───┼───┤ ├────┼────┼────┼────┼────┼────┼────┼────┤
    #  │   │ . │   │ . │   │ . │   │ . │ │    │ 01 │    │ 02 │    │ 03 │    │ 04 │
    #  ├───┼───┼───┼───┼───┼───┼───┼───┤ ├────┼────┼────┼────┼────┼────┼────┼────┤
    #  │ O │   │ O │   │ O │   │ O │   │ │    │ 01 │    │ 02 │    │ 03 │    │ 04 │
    #  ├───┼───┼───┼───┼───┼───┼───┼───┤ ├────┼────┼────┼────┼────┼────┼────┼────┤
    #  │   │ O │   │ O │   │ O │   │ O │ │    │ 01 │    │ 02 │    │ 03 │    │ 04 │
    #  ├───┼───┼───┼───┼───┼───┼───┼───┤ ├────┼────┼────┼────┼────┼────┼────┼────┤
    #  │ O │   │ O │   │ O │   │ O │   │ │    │ 01 │    │ 02 │    │ 03 │    │ 04 │
    #  └───┴───┴───┴───┴───┴───┴───┴───┘ └────┴────┴────┴────┴────┴────┴────┴────┘





    winning_pairs = [[[1, 2], [4, 8], [3, 6]],  # for 0
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
    square_red = 'X'
    square_white = 'O'

    def __init__(self, player=Game.player1):
        super().__init__()
        self._player_X = player
        self._board = [
            GameCheckers.square_red if i < GameCheckers.pieces_per_side else GameCheckers.square_white
            if i >= GameCheckers.board_size - GameCheckers.pieces_per_side else GameCheckers.square_free
            for i in range(GameCheckers.board_size)
        ]

    def get_board(self):
        return self._board

    def get_possible_moves(self):
        if self._state is not Game.play:
            return []
        return [
            index
            for index, square in enumerate(self._board)
            if square == GameCheckers.square_free
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
        if self._board[index] != GameCheckers.square_free:
            raise ValueError
        if self._state != Game.play:
            raise ValueError
        if self._player_X == self._player:
            piece = GameCheckers.square_X
        else:
            piece = GameCheckers.square_O
        self._board[index] = piece
        for index1, index2 in GameCheckers.winning_pairs[index]:
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
        print(s)
        i = 0
        for y in range(GameCheckers.board_size_y):
            y_odd = (y % 2) == 1
            for x in range(GameCheckers.board_size_x):
                print("..." + s[i] if y_odd else s[i] + "..", end='\n' if x == GameCheckers.board_size_x - 1 else '')
                i = i + 1
# EOF#######################################################################EOF
