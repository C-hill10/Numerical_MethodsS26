import maze

def up(Maze,player_position):
    x,y=player_position
    if y-1<0 and Maze.maze[x][y-1] !=0:
        Maze.maze[x][y-1]=2
        Maze.maze[x][y]=1
        player_position=x,y-1
        plt.show()
def down(Maze,player_position):
    x,y=player_position
    if y+1<Maze.size*2-2 and Maze.maze[x][y+1] !=0:
        Maze.maze[x][y+1]=2
        Maze.maze[x][y]=1
        player_position=x,y+1
        plt.show()        