# BOF#######################################################################BOF
from game import Game
from game_tic import GameTicTacToe
from game_checkers import GameCheckers
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

        verbose = False
        parser.add_argument('--verbose', '-v', action='store_false',
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
        two_players = [get_player(args.player1)(args.arguments1),
                       get_player(args.player2)(args.arguments2)]
        for player in two_players:
            if player.__class__ == PlayerHuman:
                verbose = True

        while True:
            odd_game_number = game_number % 2 == 1
            if odd_game_number:
                game = GameCheckers(player=Game.player2)
            else:
                game = GameCheckers()
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
