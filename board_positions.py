# BOF#######################################################################BOF
import time
from tic_tac_toe import TicTacToe
from game import Game
from copy import deepcopy

#  Board represented by vector:
#  0 1 2 | 6 3 0 | 2 1 0
#  3 4 5 | 7 4 1 | 5 4 3
#  6 7 8 | 8 5 2 | 8 7 6
#
#  . . . | . . . | . O X | . O X | X . . |
#  . O O | O O . | . O X | . O X | X O . |
#  X X X | X X X | . . X | . . X | X O . |


rotation_clockwise = [6, 3, 0, 7, 4, 1, 8, 5, 2]
rotation_vertical_flip = [2, 1, 0, 5, 4, 3, 8, 7, 6]


def rotate(board, rotation):
    return ''.join([board[index] for index in rotation])


def unique_rotations(original_board):
    # _1_ _2_ _3_ _4_ _5_ _6_ _7_ _8_
    # XO. ..X ... ... .OX ... ... X..
    # ... ..O ... O.. ... ..O ... O..
    # ... ... .OX X.. ... ..X XO. ...
    rotations = [original_board]

    for i in range(3):
        rotations.append(rotate(rotations[i], rotation_clockwise))
    rotations.append(rotate(original_board, rotation_vertical_flip))
    for i in range(4, 7):
        rotations.append(rotate(rotations[i], rotation_clockwise))
    rotations.sort()

    unique = []
    for rotation in rotations:
        try:
            unique.index(rotation)
        except ValueError:
            unique.append(rotation)
    return unique

node_depth_counters = [0 for _ in range(10)]
result_counters = [0, 0, 0]
print_flag = [True, True, True]
dictionary = {}
winning_boards = []


def sort_dictionary():
    grand_total = 0
    n = 0
    while len(dictionary) > 0:
        key, value = dictionary.popitem()
        dictionary[key] = value
        rotations = unique_rotations(key)

        total = 0
        values = [0 for _ in range(len(rotations))]
        for i, r in enumerate(rotations):
            if r in dictionary:
                values[i] = dictionary[r]
                total += values[i]
                del dictionary[r]
        grand_total += total
        n += 1
        print(n, rotations[0], total, len(rotations), values)
    print('grand_total = ', grand_total)

def negation_maximize(game, color, depth):  # #################################
    node_depth_counters[depth] += 1
    state = game.get_state()
    if state != Game.play:
        v = 1.0 if state == Game.won else -1.0 if state == Game.lost else 0.0
        result_counters[int(v)] += 1
        if v == 1.0:
            s = str(game)
            if s in dictionary:
                dictionary[s] += 1
            else:
                dictionary[s] = 1
        return color * v, None
    v = float("-inf")
    best_move = []
    moves = game.get_possible_moves()
    for m in moves:
        new_board = deepcopy(game)
        new_board.make_move(m)
        x, _ = negation_maximize(new_board, -color, depth + 1)
        x = - x
        if x >= v:
            if x > v:
                best_move = []
            v = x
            best_move.append(m)
    return v, best_move

# /usr/local/bin/python3.7 /Users/alex/PycharmProjects/test2/board_positions.py
# 1 ['X', 'O', 'X',
#    'O', 'X', 'O',
#    'X', '.', '.']
# 0 ['X', 'O', 'X',
#    'O', 'X', 'X',
#    'O', 'X', 'O']
# -1 ['X', 'O', 'X',
#     'O', 'O', 'X',
#     'X', 'O', '.']
# [1, 9, 72, 504, 3024, 15120, 54720, 148176, 200448, 127872] = 549946
# [46080, 131184, 77904] = 255168
# total_time 12.077525917
# [1, 9, 72, 504, 3024, 15120, 54720, 148176, 200448, 127872] = 549946
# [46080, 131184, 77904] = 255168
# total_time 12.086202097


if __name__ == '__main__':  # Testing ... #####################################
    def main():
        game = TicTacToe()
        negation_maximize(game, 1, 0)
        print(node_depth_counters, '=', sum(node_depth_counters))
        print(result_counters, '=', sum(result_counters))
        print(dictionary)
        sort_dictionary()

    start_time = time.perf_counter()
    main()
    total_time = time.perf_counter() - start_time
    print('total_time', total_time)
    exit(0)

