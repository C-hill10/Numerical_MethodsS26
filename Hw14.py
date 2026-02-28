import matplotlib.pyplot as plt
import numpy as np
import math
def derive1(x):
    return -1.74*x+1.65
def derive2(x):
    return 1.4*x**2-7.4*x+6.31
if __name__=="__main__":
    x=np.arange(-10,10,1)
    plt.plot(x,(-0.87*x**2+1.65*x+8.25),x,(0.7*x**3-3.7*x**2+6.31*x-1.9))
    plt.grid()
    plt.show()
    #based on plot, zeros at 4 for first one and around 0 for 2nd
    done=False
    guess1=4
    guess2=0
    guess1new=0
    guess2new=0
    while not done:
        guess1new=guess1-(-0.87*guess1**2+1.65*guess1+8.25)/(derive1(guess1))
        if abs(guess1new-guess1)<=1e-8:
            done=True
        else:
            guess1=guess1new
    done= False
    while not done:
        guess2new=guess2-(0.7*guess2**3-3.7*guess2**2+6.31*guess2-1.9)/(derive2(guess2))
        if abs(guess2new-guess2)<=1e-8:
            done=True
        else:
            guess2=guess2new
    # result1=bisection1(-0.1,0.1)
    # result2=bisection1(0.7,1)
    print(f"checking my solution f1({guess1new})={-0.87*guess1new**2+1.65*guess1new+8.25}")
    print(f"checking my solution f1({guess2new})={0.7*guess2**3-3.7*guess2**2+6.31*guess2-1.9}")
