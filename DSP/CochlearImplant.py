import numpy as np

def findBW(num_channels):
    speech_channels=round((num_channels*6/10),0)
    other_channels=num_channels-speech_channels
    speechbw=900/speech_channels
    otherbw=3000/other_channels
    return (speechbw,otherbw)

if __name__=="__main__":
    print(findBW(8))