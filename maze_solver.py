import numpy as np
from maze import Maze
import time
# TODO: Write code to compute a solution to the maze.
class Maze_solver:
    def __init__(self,Maze):
        self.Maze=Maze
        self.solution=0
    def solve_maze(self):
        visited=np.zeros(shape=(self.Maze.size*2+1,self.Maze.size*2+1),dtype=int)
        checkpointlist=[(1,1)]
        position=(1,1)
        done=False
        while not done:
            x,y=position
            visited[x][y]=1
            print(visited)
            path_counter=0
            neighbor_coords = (x+1, y), (x, y+1), (x-1, y), (x, y-1)
            for neighbor in neighbor_coords:
                neighborx,neighbory=neighbor
                if self.Maze.maze[neighborx][neighbory]==1 and visited[neighborx][neighbory]==0:
                    path_counter+=1
                if neighbor==self.Maze.goal_position:
                    self.solution=visited
                    done=True
                    continue
            if path_counter==0:
                #This is a dead end, would want to backtrack to the last crossroads
                position = checkpointlist.pop(-1)
                continue
            if path_counter==1:
                #go to the next open spot
                for neighbor in neighbor_coords:
                    neighborx,neighbory=neighbor
                    if visited[neighborx][neighbory]==0 and self.Maze.maze[neighborx][neighbory]==1:
                        position=neighbor
                        continue
            if path_counter==2:
                #at a crossroads, we want to save our spot so we can look again later
                checkpointlist.append((x,y))
                for neighbor in neighbor_coords:
                    neighborx,neighbory=neighbor
                    if visited[neighborx][neighbory]==0 and self.Maze.maze[neighborx][neighbory]==1:
                        position=neighbor
        print("This is in solver")
        print(self.solution)
if __name__ == "__main__":
    place=Maze(5)
    solver=Maze_solver(place)
    solver.solve_maze()
    print(solver.solution)