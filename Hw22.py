import numpy as np

def make_T_matrix(num_rows):
    t_matrix=np.identity(num_rows)
    t_matrix=t_matrix*-4
    t_matrix[0][1]=1
    for i in range(1,num_rows):
        if i<=num_rows-2:
            t_matrix[i][i+1]=1
        t_matrix[i][i-1]=1
    print(t_matrix)
    



if __name__=="__main__":
    mymatrix=make_T_matrix(10)
