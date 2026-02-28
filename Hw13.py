import matplotlib.pyplot as plt
import numpy as np
import math

if __name__=="__main__":
    done=False
    count=0
    guess=0.5
    guesslist=[]
    while not done:
        guesslist.append(float(guess))
        newguess=np.sin(math.sqrt(guess))
        if abs(guess-newguess) <1e-4:
            done=True
        else:
            guess=newguess
    x=np.arange(0,9,1)
    guess_array=np.array(guesslist)
    rel_error=abs(newguess-guess_array)/newguess
    true_result=0.76865
    abs_error=abs(true_result-guess_array)
    result= np.sin(math.sqrt(newguess))-newguess
    plt.plot(x,np.transpose(rel_error),'b.',label="Relative error")
    plt.plot(x,np.transpose(abs_error),'r',label="abs error")
    plt.legend(loc="upper right")
    plt.show()