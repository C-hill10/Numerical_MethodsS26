import numpy as np
R1=1000
R2=1000
R3=9000
R4=10000
V1=10
if __name__=="__main__":
    system=np.array([[1/R1,-1*(1/R2+1/R4+1/R1)],[-1/(R3)-1/R1,1/R1]])
    print(system)
    answers=np.array([[-V1/R2],[0]])
    print(answers)
    solution=np.linalg.solve(system,answers)
    print(f"Va is {solution[0][0]:.3f}, Vb is {solution[1][0]:.3f}")