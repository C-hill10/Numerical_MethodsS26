import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from maze import Maze
import keyboard

# TODO: Write code to make the maze interactive.

# TODO: Visualize the maze using matplotlib.

if __name__ == "__main__":
    # Any code in this block will be run when this file is executed directly
    print("You must have run `python interactive_maze.py`\n Generating a maze")
    labyrinth= Maze(10)
    color_map=mpl.colors.ListedColormap(['Gray','Black','Blue','Red'])
    player_position=(1,1)
    end_position=(9,9)
    labyrinth.maze[1][1]=2
    labyrinth.maze[9][9]=4
    mpl.pyplot.imshow(labyrinth.maze,color_map)
    mpl.pyplot.show()
    while player_position != end_position:
        key=keyboard.read_key()
        x,y=player_position
        if key == "w":
            try:
                if labyrinth.maze[x][y+1] != 0:
                    player_position=(x,y+1)
                    labyrinth.maze[x,y]=1
                    labyrinth.maze[x,y+1]=2
            except:
                print("you can't go that way!")
        elif key == "a":
            try:
                if labyrinth.maze[x-1][y] != 0:
                    player_position=(x-1,y)
                    labyrinth.maze[x,y]=1
                    labyrinth.maze[x-1,y]=2
            except:
                print("you can't go that way!")
        elif key == "s":
            try:
                if labyrinth.maze[x][y-1] != 0:
                    player_position=(x,y-1)
                    labyrinth.maze[x,y]=1
                    labyrinth.maze[x,y-1]=2
            except:
                print("you can't go that way!")
        elif key == "d":
            try:
                if labyrinth.maze[x+1][y] != 0:
                    player_position=(x+1,y)
                    labyrinth.maze[x,y]=1
                    labyrinth.maze[x+1,y]=2
            except:
                print("you can't go that way!")
        else:
            print("Invalid keypress, please try again")
        mpl.pyplot.imshow(labyrinth.maze,color_map)
        mpl.pyplot.show()

