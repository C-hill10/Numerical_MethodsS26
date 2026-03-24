import math


def FFT(sequence):

    if abs(math.log(len(sequence),2)-math.floor(math.log(len(sequence),2))) > 1e-9:
        raise ValueError("input sequence does not have length of power of 2")

    def _recursiveFFT(Sequence):
        return 0