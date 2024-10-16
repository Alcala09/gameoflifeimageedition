import sys, os
import random
from PIL import ImageColor, Image
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from cell_behavior import cell_behavior

test_board = ["30c55e", "ad6696", "ad6696", "30c55e",
              "ad6696", "d60601", "d60601", "ad6696",
              "ad6696", "d60601", "d60601", "ad6696",
              "30c55e", "ad6696", "ad6696", "30c55e"]

game_ended = False
frames = 1



while not game_ended:
    test_board_rgb = []
    test_board_rgb.clear()
    for i in range(len(test_board)):
        test_board_rgb.append(cell_behavior.(hex_to_rgb(test_board[i])))

    square_array = np.asarray(test_board_rgb)
    array_size = (len(test_board) ** 0.5)

    square_array = np.resize(square_array, (int(array_size), int(array_size)))
    print(square_array)

    image = Image.fromarray(square_array, 'RGB')
    image.save(str(frames)+".png")


    test_board = cell_behavior.update_board(test_board)

    game_ended = test_board[1:] == test_board[:-1]
    frames += 1


print("Frames: " + str(frames))
"""
Rock Paper Scissors system, RGB percents is the hcance to use each color.
Loser becomes the winning color
"""
