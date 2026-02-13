import numpy as np
from maze import Maze

# TODO: Write code to compute a solution to the maze.
def solve_maze(Maze.maze):
    visited=np.zeros(shape=(Maze.maze.size*2+1,Maze.maze.size*2+1),dtype=int)
    checkpointlist=[]
    def maze_solve_recursive(position):
        x,y=position
        visited[x][y]=1
        path_counter=0
        neighbor_coords = (x+1, y), (x, y+1), (x-1, y), (x, y-1)
        for neighbor in neighbor_coords
            neighborx,neighbory=neighbor
            if Maze.maze[neighborx][neighbory]==1
                path_counter+=1
            if Maze.maze[neighborx][neighbory]
        if path_counter==1:
            #This is a dead end, would want to backtrack to the last crossroads
        if path_counter==2:
            #go to the next open spot
        if path_counter>=3:
            #at a crossroads, we want to save our spot so we can look again later
            checkpointlist.append((visited,x,y))

