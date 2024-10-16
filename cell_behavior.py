# cell_behavior.py
import random
from PIL import ImageColor, Image
import numpy as np
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
        return valid_neighbor_spaces
    
    # Find color value of a selected cell position
    def get_color_value(board, position):
        return board[position]
    
    # Convert board hex value to tuple RGB
    def hex_to_rgb(hex_color_value):
        if not hex_color_value.startswith('#'):
            hex_color_value = '#' + hex_color_value
        return ImageColor.getcolor(hex_color_value, "RGB")
    
    def get_decision(hex_color_value):
        decisions = [1, 2, 3]
        return random.choices(decisions, weights=cell_behavior.hex_to_rgb(hex_color_value))
    
    def update_color(board, position):
        neighbors = cell_behavior.find_neighbors(board, position)
        chosen_target_list = random.choices(neighbors) # fights a random neighbor
        chosen_target = chosen_target_list[0] # cause it decides to put the choice in a list
        
        current_choice_list = cell_behavior.get_decision(cell_behavior.get_color_value(board, position))
        current_choice = current_choice_list[0]

        target_choice_list = cell_behavior.get_decision(cell_behavior.get_color_value(board, chosen_target))
        target_choice = target_choice_list[0]

        if (target_choice == current_choice+1 or target_choice == current_choice-2): #win
            print(str(position) + " wins against " + str(chosen_target))
            return [chosen_target, position, cell_behavior.get_color_value(board, position)]
            
        
        elif (target_choice == current_choice): #tie
            print(str(position) + " ties with " + str(chosen_target))
            return [position, chosen_target, cell_behavior.get_color_value(board, position)]

        else: # lose
            print(str(position) + " loses against " + str(chosen_target))
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
        image = Image.open(file_name)


        

        
