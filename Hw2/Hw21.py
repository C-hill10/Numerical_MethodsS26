import numpy as np
R1=1000
R2=1000
R3=9000
R4=10000
V1=10
def Gaussian_Elim(matrix,solution_vector):
    #this assumes square matrix and solution vector that is n x 1
    for n in range(0,len(matrix)-1):
        max_num=matrix[n][n]
        for i in range(n,len(matrix)): #iterate over matrix and find highest element in first spot
            if matrix[i][n]>max_num:
                max_num=matrix[i][n] #if you find a bigger number, swap the rows
                matrix[[n,i]]=matrix[[i,n]]
                solution_vector[[n,i]]=solution_vector[[i,n]]
        print(matrix)
        for row in range(n+1,len(matrix)):
            a=np.array(matrix[row])
            b=np.array(matrix[n])
            if a[n]!=0:
                scaling_number=a[n]/b[n]
                b=b*scaling_number
                b=a-b
                for cell in range(0,len(matrix[row])):
                    matrix[row][cell]=b[cell]
                solution_vector[row][0]=solution_vector[row][0]-(solution_vector[n][0]*scaling_number)
    print(matrix)
    print(solution_vector)
    return (matrix,solution_vector)
def back_substitute(upper_triangle,solution_vector):
    n=len(upper_triangle)
    final_answer=np.zeros(shape=(n,1))
    final_answer[n-1]=solution_vector[n-1][0]/upper_triangle[n-1][n-1]
    for index in reversed(range(0,n-1)):
        intermediate_sum=0
        for i in reversed(range(0,n)):
            intermediate_sum+=upper_triangle[index][i]*final_answer[i][0]
        final_answer[index]=(solution_vector[index]-intermediate_sum)/upper_triangle[index][index]
    print(final_answer)
    return final_answer

        

if __name__=="__main__":
    system=np.array([[1/R1,-1*(1/R2+1/R4+1/R1)],[-1/(R3)-1/R1,1/R1]])
    answers=np.array([[-V1/R2],[0]])
    test1=np.array([[-1,-5,-5],[4,-5,4],[1,5,-1]],dtype='float')
    test2=np.array([[2],[19],[-20]],dtype='float')
    solution=np.linalg.solve(system,answers)
    test3=np.array([1,2,3])
    test4=np.array([4,5,6])
    elim,elim_solution=Gaussian_Elim(test1,test2)
    back_substitute(elim,elim_solution)