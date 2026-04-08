try: 
    from PyQt6.QtCore import QThread, pyqtSignal, QObject, QTimer
    from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
    print("Using PyQT6")
except:
    print("Using PyQT5")
    from PyQt5.QtCore import QThread, pyqtSignal, QObject, QTimer
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import time
from WindowingFFTUi import Ui_MainWindow
import numpy as np
import scipy
import pyqtgraph as pg

def gaussian(M, std):
    gaussian = scipy.signal.windows.gaussian(M=M, std=std)
    s = sum(gaussian)
    return gaussian,s

def hanning(M):
    hann = scipy.signal.windows.hann(M)
    s = sum(hann)    
    return hann, s

def hamming(M):
    ham = scipy.signal.windows.hamming(M)
    s = sum(ham)  
    return ham, s

def blackman(M):
    blackman = scipy.signal.windows.blackman(M)
    s = sum(blackman)
    return blackman, s

def kaiser(M, beta):
    kais = scipy.signal.windows.kaiser(M,beta)
    s = sum(kais)
    return kais, s

class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.fs.setDisabled(True)
        self.spinBox.setRange(100, 2048) #Number of points
        self.maxTime.setRange(10, 2000)
        self.betaSlider1.setRange(0,100)
        self.betaSlider2.setRange(0,100)
        self.betaSlider3.setRange(0,100)
        self.stdSlider.setRange(1,100)
        self.display = False
        self.timePlot = self.timeDomain.plot([])        
        self.freqPlot = self.frequencyDomain.plot([])
        self.connectSignalSlots()
        self.fs.setRange(0,1000)
        self.spinBox.setRange(1,2048)

    def makeSignals(self):
        N = self.spinBox.value()
        dt = self.maxTime.value() / N
        self.time = np.linspace(0, self.maxTime.value() - dt, N)
        fs = 1 / dt
        self.fs.setValue(fs)
        self.frequency = np.linspace(0, fs/2, 2048)
        self.output = self.a1.value()*np.cos(self.f1.value()*2*np.pi * self.time + self.p1.value())
        self.output = self.output + self.a2.value()*np.cos(self.f2.value()*2*np.pi * self.time + self.p2.value())
        self.output = self.output + self.a3.value()*np.cos(self.f3.value()*2*np.pi * self.time + self.p3.value())
        nWindows = 0
        w = np.ones(N)
        self.fDomain = np.zeros([4096, 2])
        if(self.useRect.isChecked()):
            nWindows += 1
            s = N
            self.fDomain[:,0] = np.abs(np.fft.fft(self.output, 4096)) * 2 / s #correct the vertical axis
        if(self.useGuass.isChecked()):
            w, s = gaussian(N, self.stdSlider.value()/100 * N)
            self.fDomain[:,1] = np.abs(np.fft.fft(self.output*w, 4096)) * 2 / s #correct the vertical axis by dividing by half the sum of the window function
            if(nWindows > 0):
                for i in range(2048):
                    self.fDomain[i,0] = min(self.fDomain[i,0], self.fDomain[i,1])
            else:
                self.fDomain[:,0] = self.fDomain[:,1]
            nWindows += 1
        if(self.useHann.isChecked()):
            w, s = hanning(N)
            self.fDomain[:,1] = np.abs(np.fft.fft(self.output*w, 4096)) * 2 / s #correct the vertical axis by dividing by half the sum of the window function
            if(nWindows > 0):
                for i in range(2048):
                    self.fDomain[i,0] = min(self.fDomain[i,0], self.fDomain[i,1])
            else:
                self.fDomain[:,0] = self.fDomain[:,1]
            nWindows += 1
        if(self.useHamm.isChecked()):
            w, s = hamming(N)
            self.fDomain[:,1] = np.abs(np.fft.fft(self.output*w, 4096)) * 2 / s #correct the vertical axis by dividing by half the sum of the window function
            if(nWindows > 0):
                for i in range(2048):
                    self.fDomain[i,0] = min(self.fDomain[i,0], self.fDomain[i,1])
            else:
                self.fDomain[:,0] = self.fDomain[:,1]
            nWindows += 1
        if(self.useBlackman.isChecked()):
            w, s = blackman(N)
            self.fDomain[:,1] = np.abs(np.fft.fft(self.output*w, 4096)) * 2 / s #correct the vertical axis by dividing by half the sum of the window function
            if(nWindows > 0):
                for i in range(2048):
                    self.fDomain[i,0] = min(self.fDomain[i,0], self.fDomain[i,1])
            else:
                self.fDomain[:,0] = self.fDomain[:,1]
            nWindows += 1
        if(self.useK1.isChecked()):
            w, s = kaiser(N, self.betaSlider1.value()/10)
            self.fDomain[:,1] = np.abs(np.fft.fft(self.output*w, 4096)) * 2 / s #correct the vertical axis by dividing by half the sum of the window function
            if(nWindows > 0):
                for i in range(2048):
                    self.fDomain[i,0] = min(self.fDomain[i,0], self.fDomain[i,1])
            else:
                self.fDomain[:,0] = self.fDomain[:,1]
            nWindows += 1
        if(self.useK2.isChecked()):
            w, s = kaiser(N, self.betaSlider2.value()/10)
            self.fDomain[:,1] = np.abs(np.fft.fft(self.output*w, 4096)) * 2 / s #correct the vertical axis by dividing by half the sum of the window function
            if(nWindows > 0):
                for i in range(2048):
                    self.fDomain[i,0] = min(self.fDomain[i,0], self.fDomain[i,1])
            else:
                self.fDomain[:,0] = self.fDomain[:,1]
            nWindows += 1
        if(self.useK3.isChecked()):
            w, s = kaiser(N, self.betaSlider3.value()/10)
            self.fDomain[:,1] = np.abs(np.fft.fft(self.output*w, 4096)) * 2 / s #correct the vertical axis by dividing by half the sum of the window function
            if(nWindows > 0):
                for i in range(2048):
                    self.fDomain[i,0] = min(self.fDomain[i,0], self.fDomain[i,1])
            else:
                self.fDomain[:,0] = self.fDomain[:,1]
            nWindows += 1
        if(nWindows > 0):
            self.display = True
            self.timePlot.setData(self.time,self.output*w)
            if(self.plotdB.isChecked()):
                self.freqPlot.setData(self.frequency,20*np.log10(self.fDomain[0:2048,0]+1))
            else:
                self.freqPlot.setData(self.frequency,self.fDomain[0:2048,0])
            
        else:
            self.display = False
            self.timePlot.setData([])
            self.freqPlot.setData([])

    def updateValues(self):
        if(self.display):
            self.makeSignals()
    def updateG(self):
        if(self.useGuass.isChecked()):
            self.makeSignals()
    def updateK1(self):
        if(self.useK1.isChecked()):
            self.makeSignals()
    def updateK2(self):
        if(self.useK2.isChecked()):
            self.makeSignals()
    def updateK3(self):
        if(self.useK3.isChecked()):
            self.makeSignals()
    def update(self):
        self.display = self.useBlackman.isChecked() or self.useGuass.isChecked() or self.useRect.isChecked()
        self.display = self.display or self.useHann.isChecked() or self.useHamm.isChecked() or self.useK1.isChecked()
        self.display = self.display or self.useK2.isChecked() or self.useK3.isChecked()
        if(self.display):
            self.makeSignals()

    def connectSignalSlots(self):
        self.a1.valueChanged.connect(self.updateValues)
        self.f1.valueChanged.connect(self.updateValues)
        self.p1.valueChanged.connect(self.updateValues)
        self.a2.valueChanged.connect(self.updateValues)
        self.f2.valueChanged.connect(self.updateValues)
        self.p2.valueChanged.connect(self.updateValues)
        self.a3.valueChanged.connect(self.updateValues)
        self.f3.valueChanged.connect(self.updateValues)
        self.p3.valueChanged.connect(self.updateValues)
        self.plotdB.stateChanged.connect(self.updateValues)
        self.spinBox.valueChanged.connect(self.updateValues)
        self.maxTime.valueChanged.connect(self.updateValues)
        self.stdSlider.valueChanged.connect(self.updateG)
        self.betaSlider1.valueChanged.connect(self.updateK1)
        self.betaSlider2.valueChanged.connect(self.updateK2)
        self.betaSlider3.valueChanged.connect(self.updateK3)
        self.useGuass.stateChanged.connect(self.update)
        self.useRect.stateChanged.connect(self.update)
        self.useHamm.stateChanged.connect(self.update)
        self.useBlackman.stateChanged.connect(self.update)
        self.useHann.stateChanged.connect(self.update)
        self.useK1.stateChanged.connect(self.update)
        self.useK2.stateChanged.connect(self.update)    
        self.useK3.stateChanged.connect(self.update)

app = QApplication([])
window = UserInterface()
window.show() # Windows are hidden by default
app.exec() # Start the event loop