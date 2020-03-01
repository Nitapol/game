import subprocess
import re

total_games = 0
total_draw = 0
total_lost = 0
command = 'python main.py  --games 1 PlayerRandom PlayerNegation'
# command = 'python main.py  --games 1 PlayerRandom PlayerNegation'
# command = 'python main.py  --games 1 PlayerRandom PlayerRandom'

while True:
    lines = subprocess.getoutput(command)

    if total_games == 0:
        print(lines)
    total_games += 1

    won_lost_draw = re.compile(r'won \d lost \d draw \d')
    match = won_lost_draw.search(lines)
    result = match.group()

    won = 1 if result[4] == '1' else 0
    lost = 1 if result[11] == '1' else 0
    draw = 1 if result[18] == '1' else 0

    def assert_print(true_result):
        if not true_result:
            print(lines)
        assert true_result

    assert_print(won == 0)
    assert_print((lost == 1 and draw == 0) or (lost == 0 and draw == 1))

    total_draw += draw
    total_lost += lost

    assert_print(total_games == total_lost + total_draw)

    print(total_games, 'games played. Lost ', total_lost, 'or', total_lost / total_games * 100.0, '%')