import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
def back_substitute(upper_triangle,solution_vector):
    n=len(upper_triangle)
    final_answer=np.zeros(shape=(n,1))
    final_answer[n-1]=solution_vector[n-1][0]/upper_triangle[n-1][n-1]
    for index in reversed(range(0,n-1)):
        intermediate_sum=0
        for i in reversed(range(0,n)):
            intermediate_sum+=upper_triangle[index][i]*final_answer[i][0]
        final_answer[index]=(solution_vector[index]-intermediate_sum)/upper_triangle[index][index]
    return final_answer
def forward_substitution(lower_triangle,b_vector):
    d_vector=np.zeros(shape=(len(lower_triangle),1))
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
def draw_picture(matrix):
    plt.imshow(matrix, cmap='inferno')
    plt.colorbar()
    plt.show()
if __name__=="__main__":
    mymatrix=make_A_matrix(10,10)
    mymatrix=make_big(mymatrix,10)
    print(mymatrix)
    testmatrix=-1*cholesky_decomp(-1*mymatrix)
    #testmatrix=np.array([[6,15,55],[15,55,225],[55,225,979]])
    b_vector10=make_b_vector(10)
    answer=np.linalg.solve(mymatrix,b_vector10)
    answer=answer.reshape((10,10))
    draw_picture(answer)
    A25=make_A_matrix(25,25)
    A25=make_big(A25,25)
    B25=make_b_vector(25)
    answer25=np.linalg.solve(A25,B25)
    draw_picture(answer25)
    # d_vector=forward_substitution(np.transpose(mymatrix),b_vector)
    # b_vector=back_substitute(mymatrix,d_vector)
    # b_vector=b_vector.reshape((10,10))
    # draw_picture(b_vector)


