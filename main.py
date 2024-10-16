import sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from cell_behavior import cell_behavior

test_board = ["30c55e", "d60601", "b1fdfd", "9435c6",
              "c8d551", "24eadc", "ef8871", "ad6696",
              "783d7e", "008a96", "9a11b3", "2051c3",
              "1b7dba", "4075af", "d25f51", "0ad9ce"]

game_ended = False
iterations = 0
while not game_ended:
    test_board = cell_behavior.update_board(test_board)
    print(str(test_board))

    game_ended = test_board[1:] == test_board[:-1]
    iterations += 1

print(iterations)
"""
Rock Paper Scissors system, RGB percents is the hcance to use each color.
Loser becomes the winning color
"""
