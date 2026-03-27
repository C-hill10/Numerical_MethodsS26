import sounddevice as sd
#https://realpython.com/playing-and-recording-sound-python/ review this later if i have issues
fs=44100
seconds=4

print(f"starting recording for {seconds} seconds")
myrecording=sd.rec((int(seconds * fs)),samplerate=fs,channels=1)
sd.wait()
sd.play(myrecording,fs)
sd.wait()
