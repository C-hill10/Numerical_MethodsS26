import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from maze import Maze
from Maze_solver import Maze_solver
# TODO: Write code to make the maze interactive.
class Imaze:
    def __init__(self,size=5):
        self.size=int(input("please enter the size of maze you want: "))
    def start(self):
        labyrinth= Maze(self.size)
        color_map=mpl.colors.ListedColormap(['Black','Gray','Yellow','Blue','Red'])
        solver=Maze_solver(labyrinth)
        solver.solve_maze()
        labyrinth.maze=labyrinth.maze+solver.solution
        labyrinth.maze[1][1]=3
        labyrinth.maze[self.size*2-1][self.size*2-1]=4
        fig,ax=plt.subplots()
        img = mpl.pyplot.imshow(labyrinth.maze,color_map)
        helper=Mover(labyrinth,fig,color_map,img)
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
class Mover:
    def __init__(self, Maze,figure,Color_map,image):
        self.maze=Maze
        self.fig=figure
        self.map=Color_map
        self.img=image
    def up_move(self, event):
        self.maze.up()
        self.img.set_data(self.maze.maze)
        self.fig.canvas.draw()
        if self.maze.win_check():
            plt.close(self.fig)
    def down_move(self, event):
        self.maze.down()
        self.img.set_data(self.maze.maze)
        self.fig.canvas.draw()
        if self.maze.win_check():
            plt.close(self.fig)
    def right_move(self, event):
        self.maze.right()
        self.img.set_data(self.maze.maze)
        self.fig.canvas.draw()
        if self.maze.win_check():
            plt.close(self.fig)
    def left_move(self, event):
        self.maze.left()
        self.img.set_data(self.maze.maze)
        self.fig.canvas.draw()
        if self.maze.win_check():
            plt.close(self.fig)

# TODO: Visualize the maze using matplotlib.
if __name__ == "__main__":
    game = Imaze()
    play_again=True
    while play_again:
        game.start()
        play_again=input('would you like to play again? (y/N): ').lower().startswith('y')
    
    


