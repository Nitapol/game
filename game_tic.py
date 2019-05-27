# BOF#######################################################################BOF
from game import Game


class GameTicTacToe(Game):  # #################################################
    #  0 1 2
    #  3 4 5
    #  6 7 8
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
    square_X = 'X'
    square_O = 'O'

    def __init__(self, player=Game.player1):
        super().__init__()
        self._player_X = player
        self._board = [GameTicTacToe.square_free for _ in range(9)]

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
