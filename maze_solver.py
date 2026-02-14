import numpy as np
from maze import Maze
import time
# TODO: Write code to compute a solution to the maze.
class Maze_solver:
    def __init__(self,Maze):
        self.Maze=Maze
        self.solution=np.zeros(shape=(self.Maze.size*2+1,self.Maze.size*2+1),dtype=int)
    def solve_maze(self):
        visited=np.zeros(shape=(self.Maze.size*2+1,self.Maze.size*2+1),dtype=int)
        checkpointlist=[] #holds the locations of branching paths to return back to
        maze_state_list=[visited] #intending this to hold the state of the maze at each checkpoint, doesnt work
        dead_ends=[]
        current_trial=[]
        position=(1,1) #starting position
        done=False
        justjumped=False
        while not done:
            x,y=position
            visited[x][y]=1
            path_counter=0
            neighbor_coords = (x+1, y), (x, y+1), (x-1, y), (x, y-1)
            for neighbor in neighbor_coords:
                neighborx,neighbory=neighbor
                if self.Maze.maze[neighborx][neighbory]==1 and visited[neighborx][neighbory]==0 and neighbor not in dead_ends:
                    path_counter+=1
                if neighbor==self.Maze.goal_position:
                    self.solution=visited
                    done=True
                    break
            if not done:
                if path_counter==0:
                    #This is a dead end, would want to backtrack to the last crossroads
                    dead_ends.append(current_trial.pop())
                    position = checkpointlist.pop()
                    visited=maze_state_list.pop()
                    justjumped=True

                elif path_counter==1:
                    #go to the next open spot
                    for neighbor in neighbor_coords:
                        neighborx,neighbory=neighbor
                        if visited[neighborx][neighbory]==0 and self.Maze.maze[neighborx][neighbory]==1 and neighbor not in dead_ends:
                            position=neighbor
                            if justjumped:  #ensure the new path gets marked in case its also wrong
                                current_trial.append(neighbor)
                                justjumped=False
                            break
                elif path_counter==2:
                    #at a crossroads, we want to save our spot so we can look again later
                    checkpointlist.append((x,y))
                    maze_state_list.append(np.zeros(shape=(self.Maze.size*2+1,self.Maze.size*2+1),dtype=int)+visited)
                    for neighbor in neighbor_coords:
                        neighborx,neighbory=neighbor
                        if visited[neighborx][neighbory]==0 and self.Maze.maze[neighborx][neighbory]==1 and neighbor not in dead_ends:
                            position=neighbor
                            current_trial.append(neighbor)
                            break

if __name__ == "__main__":
    place=Maze(5)
    solver=Maze_solver(place)
    solver.solve_maze()
    print(solver.solution)