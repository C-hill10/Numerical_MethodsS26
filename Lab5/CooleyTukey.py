import math
import numpy as np

def FFT(sequence,num_samples=len(sequence),stride=1):
    final_answer=np.zeros(shape=(num_samples))
    if abs(math.log(len(sequence),2)-math.floor(math.log(len(sequence),2))) > 1e-9:
        raise ValueError("input sequence does not have length of power of 2")
    if num_samples=1:
        final_answer[0]=sequence
    else:
        fft(sequence(0::2)) # even indices
        fft(sequence(1::2))
        for k in range(0,(num_samples/2)-1):
            p=sequence(k)
            q=math.exp((-2*math.pi*1j/num_samples)*k)*sequence(k+num_samples/2)
            final_answer[k]=p+q
            final_answer[k+num_samples/2]=p-q
        
    

    def _recursiveFFT(Sequence):
        return 0
    
    #trying to just exactly match the wikipedia article
def FFT(sequence,num_samples,stride):
    if num_samples==1:
        answer[0]= sequence[0] # not sure how to get the right index in here
    else:
        #need to do some array slicing to make this work
        FFT(sequence[],num_samples/2,2*stride)
        FFT(sequence[],num_samples/2,2*stride)
        for k in range(0,(num_samples/2)): #the -1 is taken care of by the range function
            p=answer[k]
            q=math.exp(-2*math.pi*1j*k/num_samples)*answer[k+num_samples/2]
            answer[k]=p+q
            answer[k+num_samples/2]=p-q