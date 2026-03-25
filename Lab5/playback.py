import sounddevice as sd
#https://realpython.com/playing-and-recording-sound-python/ review this later if i have issues
fs=44100
seconds=5

myrecording=sd.rec((int(seconds*fs)),samperate=fs,channels=1)
sd.wait()

