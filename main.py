"""
Game of Life: Image Edition

Import any image and watch as the colors in your image act as a world of peace/colonization/other awesome ways

Created by Matthew Alcala
"""

# IMPORTS 
import tkinter as tk

# USER INTERFACE

root = tk.Tk()
root.geometry('350x300')
root.resizable(width=False, height=False)

color1 = '#020f12'
color2 = '#05d7ff'
color3 = '#65e7ff'
color4 = 'BLACK'

main_frame = tk.Frame(root, bg=color1, pady=40)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

# BUTTONS

start_button = tk.Button( # START BUTTON
    main_frame,
    background = color2,
    foreground = color4,
    activebackground = color3,
    activeforeground = color4,
    highlightthickness = 2,
    highlightbackground = color2,
    highlightcolor = 'WHITE',
    width = 13,
    height = 2,
    border = 0,
    cursor = 'hand2',
    text = 'START',
    font = ('Arial', 16, 'bold')
)

settings_button = tk.Button( # SETTINGS BUTTON
    main_frame,
    background = color2,
    foreground = color4,
    activebackground = color3,
    activeforeground = color4,
    highlightthickness = 2,
    highlightbackground = color2,
    highlightcolor = 'WHITE',
    width = 13,
    height = 2,
    border = 0,
    cursor = 'hand2',
    text = 'SETTINGS',
    font = ('Arial', 16, 'bold')
)

start_button.grid(column=0, row=0)
settings_button.grid(column=0, row=1)

# BUTTON FUNCTION



root.mainloop()

