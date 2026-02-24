import matplotlib.pyplot as plt
import numpy as np
import math

if __name__=="__main__":
    done=False
    guess=0.5
    while not done:
        newguess=np.sin(math.sqrt(guess))-guess
        print(newguess)
        if abs(guess-newguess) <1e-4:
            done=True
        else:
            guess=newguess
    print(newguess)