import sys, os
import random
from PIL import ImageColor, Image
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from cell_behavior import cell_behavior

test_board = cell_behavior.image_to_board("testimage.png")


test_board_manual = ["FF0000", "00FF00", "0000FF", "FF0000",
              "0000FF", "FF0000", "00FF00", "0000FF",
              "00FF00", "0000FF", "FF0000", "00FF00",
              "FF0000", "00FF00", "0000FF", "FF0000"]

game_ended = False
frames = 1
cell_behavior.images_to_gif(r"images", "final.gif", duration=1)
sys.exit()
while not game_ended:
    test_board_r = []
    test_board_g = []
    test_board_b = []

    for color in test_board:
        test_board_r.append(cell_behavior.hex_to_rgb(color, 0))
        test_board_g.append(cell_behavior.hex_to_rgb(color, 1))
        test_board_b.append(cell_behavior.hex_to_rgb(color, 2))

    square_array_r = np.asarray(test_board_r)
    square_array_g = np.asarray(test_board_g)
    square_array_b = np.asarray(test_board_b)

    array_size = int(len(test_board) ** 0.5)

    square_array_r = np.resize(square_array_r, (array_size, array_size))
    square_array_g = np.resize(square_array_g, (array_size, array_size))
    square_array_b = np.resize(square_array_b, (array_size, array_size))

    image = np.stack((square_array_r, square_array_g, square_array_b), axis=-1)

    image = image.astype(np.uint8)

    img = Image.fromarray(image)
    os.makedirs("images", exist_ok=True)
    img.save(os.path.join("images", f"{frames}.png"))

    game_ended = test_board[1:] == test_board[:-1]
    test_board = cell_behavior.update_board(test_board)
    frames += 1

print("Frames: " + str(frames))
cell_behavior.images_to_gif(r"images", "final.gif", duration=1)
