import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
def forward_substitution(lower_triangle,b_vector):
    d_vector=np.array(shape=(len(lower_triangle,1)))
    #first one
    d_vector[0][0]=b_vector[0][0]/lower_triangle[0][0]
    for entry in range(1,len(d_vector)):
        intermediate_sum=0
        for index in range(0,entry):
            intermediate_sum+=lower_triangle[entry][index]*b_vector[index][0]
        d_vector[entry]=(b_vector[entry][0]-intermediate_sum)/lower_triangle[entry][entry]
    return d_vector
def make_T_matrix(num_rows):
    t_matrix=np.identity(num_rows)
    t_matrix=t_matrix*-4
    t_matrix[0][1]=1
    for i in range(1,num_rows):
        if i<=num_rows-2:
            t_matrix[i][i+1]=1
        t_matrix[i][i-1]=1
    return t_matrix

def make_b_vector(num_points):
    b_vector=np.zeros((num_points**2,1))
    total_points=num_points+2 #account for grid spacing counting as points
    point_values=np.linspace(-1,1,total_points)
    print(point_values)
    
    f= lambda x,y: 25-x**2+y**2
    for y in range(0,num_points):
        for x in range(0,num_points):
            if y==0:
                b_vector[y*num_points+x][0]+=f(point_values[x+1],-1)
            if y==num_points-1:
                b_vector[y*num_points+x][0]+=f(point_values[x+1],1)
            if x==0:
                b_vector[y*num_points+x][0]+=f(-1,point_values[y+1])
            if x==num_points-1:
                b_vector[y*num_points+x][0]+=f(1,point_values[y+1])
    print(f"spacing is {point_values[1]}")
    b_vector=b_vector*(-1/(point_values[1]**2))
    return b_vector


def make_A_matrix(num_rows_a,num_rows_t):
    t_matrix=make_T_matrix(num_rows_t)
    a_matrix=np.zeros(shape=(num_rows_a,num_rows_a,num_rows_a,num_rows_a))
    a_matrix[0][1]=np.identity(num_rows_a)
    for i in range(0,num_rows_a):
        a_matrix[i][i]=t_matrix
    for i in range(1,num_rows_a):
        if i<=num_rows_a-2:
            a_matrix[i][i+1]=np.identity(num_rows_a)
        a_matrix[i][i-1]=np.identity(num_rows_a)
    return a_matrix

def cholesky_decomp(Symmetric_matrix):
    n=len(Symmetric_matrix)
    Upper_triangle=np.zeros((n,n))
    #this loop will handle the main diagonal
    for row in range(0,len(Symmetric_matrix)):
        intermediate_sum=0
        for index in range(0,row):
            intermediate_sum+=(Upper_triangle[index][row])**2
        Upper_triangle[row][row]=(Symmetric_matrix[row][row]-intermediate_sum)**0.5
        #handle the rest of the row
        for j in range(row+1,n):
            intermediate_sum=0
            for sigma in range(0,row):
                intermediate_sum+=(Upper_triangle[sigma][row])*(Upper_triangle[sigma][j])
            Upper_triangle[row][j]=(Symmetric_matrix[row][j]-intermediate_sum)/Upper_triangle[row][row]
    print(Upper_triangle)
    return Upper_triangle
def make_big(matrix,size_square):
    matrix=np.block([*matrix])
    return np.reshape(matrix,(size_square**2,size_square**2))
if __name__=="__main__":
    mymatrix=make_A_matrix(10,10)
    mymatrix=make_big(mymatrix)
    #testmatrix=np.array([[6,15,55],[15,55,225],[55,225,979]])
    #cholesky_decomp(testmatrix)
    b_vector=make_b_vector(10)
    mymatrix=cholesky_decomp(mymatrix)
    d_vector=forward_substitution(mymatrix,b_vector)
    print(b_vector)


