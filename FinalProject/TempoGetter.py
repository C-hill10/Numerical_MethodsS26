import numpy as np
import math
import wave
import matplotlib.pyplot as plt
import sounddevice as sd
import argparse
#using this site for reading wav file into np array https://www.w3reference.com/blog/python-write-a-wav-file-into-numpy-float-array/
if __name__=="__main__":
    parser=argparse.ArgumentParser(description="reads wav file and outputs a low frequency fourier transform plot to try and guess BPM")
    parser.add_argument('file',type=str)
    args=parser.parse_args()
    try:
        music_file=wave.open(args.file,"rb")
    except FileNotFoundError:
        print("Error: file does not exist")
    else:
        with music_file:
            nchannels = music_file.getnchannels()    # Number of channels (1=mono, 2=stereo)  
            sampwidth = music_file.getsampwidth()    # Bytes per sample (e.g., 2 for 16-bit)  
            framerate = music_file.getframerate()    # Sample rate (Hz)  
            nframes = music_file.getnframes()        # Total samples  
            comptype = music_file.getcomptype()      # Compression type (usually "NONE" for PCM)  
            compname = music_file.getcompname()      # Compression name  
            raw_data=music_file.readframes(nframes)
            if sampwidth==1:
                dtype=np.uint8
            elif sampwidth == 2:  
                dtype = np.int16  
            elif sampwidth == 4:  
                dtype = np.int32  # Assumes 32-bit integer (common for PCM)  
            else:  
                raise ValueError(f"Unsupported sample width: {sampwidth} bytes")  
            
            audio_int = np.frombuffer(raw_data, dtype=dtype)  # Integer array   
            udio_int = audio_int.reshape(-1, nchannels)  # Shape: (nframes, nchannels) 
            print(udio_int)
            sd.play(udio_int,44100) 
            sd.wait()