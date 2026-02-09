import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from maze import Maze
import maze_move
# TODO: Write code to make the maze interactive.
class Mover:
    def __init__(self, Maze,figure):
        self.maze=Maze
        self.fig=figure
    def up_move(self, event):
        self.maze.up()
        self.fig.canvas.draw()
    def down_move(self, event):
        self.maze.down()
        self.fig.canvas.draw()
    def right_move(self, event):
        self.maze.right()
        self.fig.canvas.draw()
    def left_move(self, event):
        self.maze.left()
        self.fig.canvas.draw()

# TODO: Visualize the maze using matplotlib.
player_position=(1,1)
if __name__ == "__main__":
    labyrinth= Maze(10)
    color_map=mpl.colors.ListedColormap(['Gray','Black','Blue','Red'])
    end_position=(9,9)
    labyrinth.maze[1][1]=2
    labyrinth.maze[9][9]=4
    fig,ax=plt.subplots()
    helper=Mover(labyrinth,fig)
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
    bdown.on_clicked(helper.down_move)
    bright.on_clicked(helper.right_move)
    bleft.on_clicked(helper.left_move)
    bup.on_clicked(helper.up_move)
    mpl.pyplot.show()
    plt.ion()


