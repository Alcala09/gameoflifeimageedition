# cell_behavior.py
import random
from PIL import ImageColor, Image
import numpy as np
import os

class cell_behavior:
    

    def find_neighbors(board, position):

        # left, right, up, down
        valid_neighbor_spaces = []
        board_size = int(len(board)**0.5)

        # Checking left wall
        if position % board_size != 0:
            valid_neighbor_spaces.append(position - 1)
        
        # Checking right wall
        if position % board_size != board_size - 1:
            valid_neighbor_spaces.append(position + 1)
        
        # Checking up wall
        if position > board_size - 1:
            valid_neighbor_spaces.append(position - board_size)
        
        # Checking down wall
        if position < ((board_size**2) - board_size):
            valid_neighbor_spaces.append(position + board_size)
        
        valid_neighbor_spaces.sort()

        enemy_neighbors = []
        for i in range(len(valid_neighbor_spaces)):
            if not ( cell_behavior.get_color_value(board, position) == cell_behavior.get_color_value(board, valid_neighbor_spaces[i]) ):
                enemy_neighbors.append(valid_neighbor_spaces[i])
        return valid_neighbor_spaces
    
    # Find color value of a selected cell position
    def get_color_value(board, position):
        return board[position]
    
    # Convert board hex value to tuple RGB
    def hex_to_rgb(hex_color_value, color_number):
        if not hex_color_value.startswith('#'):
            hex_color_value = '#' + hex_color_value
        if color_number != -1:
            return ImageColor.getcolor(hex_color_value, "RGB")[color_number]
        else:
            rgb_tuple = ImageColor.getcolor(hex_color_value, "RGB")
            modified_rgb_tuple = tuple(value + 1 for value in rgb_tuple)
            return modified_rgb_tuple
    
    def get_decision(hex_color_value):
        decisions = [1, 2, 3]
        return random.choices(decisions, weights=cell_behavior.hex_to_rgb(hex_color_value, -1))
    
    def update_color(board, position):
        neighbors = cell_behavior.find_neighbors(board, position)

        chosen_target_list = random.choices(neighbors) # fights a random neighbor
        chosen_target = chosen_target_list[0] # cause it decides to put the choice in a list
        
        current_choice_list = cell_behavior.get_decision(cell_behavior.get_color_value(board, position))
        current_choice = current_choice_list[0]

        target_choice_list = cell_behavior.get_decision(cell_behavior.get_color_value(board, chosen_target))
        target_choice = target_choice_list[0]

        if (target_choice == current_choice+1 or target_choice == current_choice-2): #win

            return [chosen_target, position, cell_behavior.get_color_value(board, position)]
            
        
        elif (target_choice == current_choice): #tie

            return [position, chosen_target, cell_behavior.get_color_value(board, position)]

        else: # lose

            return [position, chosen_target, cell_behavior.get_color_value(board, chosen_target)]
    
    def update_board(board):
        made_move = [False for i in range(len(board))]
        board_updated = board

        for i in range(len(board)):
            if not made_move[i]:
                result = cell_behavior.update_color(board, i)
                if result != None:
                    board_updated[result[0]] = result[2]
                    made_move[result[0]] = True
                    made_move[result[1]] = True

        return board_updated
    
    def image_to_board(file_name):
        
        image = Image.open(file_name).convert("RGB")

        width, height = image.size
        min_size = min(width, height)

        left = (width - min_size) // 2
        up = (height - min_size) // 2
        right = left + min_size
        down = up + min_size

        image = image.crop((left, up, right, down))

        image_array = np.array(image)

        board = []
        for row in image_array:
            for pixel in row:
                hex_color = '{:02X}{:02X}{:02X}'.format(pixel[0], pixel[1], pixel[2])
                board.append(hex_color)
        return board
    
    def images_to_gif(folder_path, output_file, duration):
        images = []
        counter = 1
        while True:
            filename = f"{counter}.png"
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                img = Image.open(file_path)

                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                images.append(img)
                print(f"Added frame: {filename}")
                counter += 1
            else:
                print(f"Frame {filename} not found. Stopping.")
                break
        
        if images:
            images[0].save(output_file, save_all=True, append_images=images[1:], duration=duration, loop=0)  # loop=0 for infinite looping
            print(f"GIF saved as {output_file}")
        else:
            print("No images found")

    



        

        
