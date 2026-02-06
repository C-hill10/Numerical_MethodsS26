import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from maze import Maze
import maze_move
# TODO: Write code to make the maze interactive.

# TODO: Visualize the maze using matplotlib.
player_position=(1,1)
if __name__ == "__main__":
    # Any code in this block will be run when this file is executed directly
    print("You must have run `python interactive_maze.py`\n Generating a maze")
    labyrinth= Maze(10)
    color_map=mpl.colors.ListedColormap(['Gray','Black','Blue','Red'])
    # plt.ion()
    end_position=(9,9)
    labyrinth.maze[1][1]=2
    labyrinth.maze[9][9]=4
    fig,ax=plt.subplots()
    mpl.pyplot.imshow(labyrinth.maze,color_map)
    plt.subplots_adjust(bottom=0.3)
    ax_left=fig.add_axes([0.35, 0.05, 0.1, 0.075])
    ax_down=fig.add_axes([0.46, 0.05, 0.1, 0.075])
    ax_right=fig.add_axes([0.57, 0.05, 0.1, 0.075])
    ax_up=fig.add_axes([0.46, 0.15, 0.1, 0.075])
    bleft=mpl.widgets.Button(ax_left,'Left')
    bdown=mpl.widgets.Button(ax_down,'Down')
    bright=mpl.widgets.Button(ax_right,'Right')
    bup=mpl.widgets.Button(ax_up,'Up')
    bdown.on_clicked(maze_move.down(labyrinth,player_position))
    mpl.pyplot.show()
    # right_button= mpl.widgets.Button()
    # left_button=mpl.widgets.Button()
    # while player_position != end_position:
    #     key=keyboard.read_key()
    #     x,y=player_position
    #     if key == "w":
    #         try:
    #             if labyrinth.maze[x][y+1] != 0:
    #                 player_position=(x,y+1)
    #                 labyrinth.maze[x,y]=1
    #                 labyrinth.maze[x,y+1]=2
    #         except:
    #             print("you can't go that way!")
    #     elif key == "a":
    #         try:
    #             if labyrinth.maze[x-1][y] != 0:
    #                 player_position=(x-1,y)
    #                 labyrinth.maze[x,y]=1
    #                 labyrinth.maze[x-1,y]=2
    #         except:
    #             print("you can't go that way!")
    #     elif key == "s":
    #         try:
    #             if labyrinth.maze[x][y-1] != 0:
    #                 player_position=(x,y-1)
    #                 labyrinth.maze[x,y]=1
    #                 labyrinth.maze[x,y-1]=2
    #         except:
    #             print("you can't go that way!")
    #     elif key == "d":
    #         try:
    #             if labyrinth.maze[x+1][y] != 0:
    #                 player_position=(x+1,y)
    #                 labyrinth.maze[x,y]=1
    #                 labyrinth.maze[x+1,y]=2
    #         except:
    #             print("you can't go that way!")
    #     else:
    #         print("Invalid keypress, please try again")
    #     mpl.pyplot.imshow(labyrinth.maze,color_map)
    #    mpl.pyplot.show()

