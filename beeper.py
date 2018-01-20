import pyaudio
import numpy as np


class Beeper:
    def __init__(self):

        self.p = pyaudio.PyAudio()
        self.volume = 0.5 
        self.fs = 44100       # sampling rate, Hz, must be integer
        self.stream = None

    def makeSound(self,feelings):
        duration = 0
        f = 0

        maxFeeling = None
        maxValue = 0
        for key in feelings:
            value = feelings[key]
            if maxValue < value:
                maxValue = value
                maxFeeling = key
        #print(maxValue)
        print("Feeling detected: "+maxFeeling)

        
        if maxFeeling == "anger":

            duration = 3.0   # in seconds, may be float
            f = 600.0        # sine frequency, Hz, may be float

        elif maxFeeling == "contempt":

            duration = 1.0
            f = 400.0  

        elif maxFeeling == "disgust":

            duration = 2.0   # in seconds, may be float
            f = 200.0        # sine frequency, Hz, may be float

        elif maxFeeling == "fear":

            duration = 5.0   # in seconds, may be float
            f = 700.0        # sine frequency, Hz, may be float

        elif maxFeeling == "happiness":

            duration = 0.5   # in seconds, may be float
            f = 500.0        # sine frequency, Hz, may be float    

        elif maxFeeling == "neutral":

            duration = 1.0   # in seconds, may be float
            f = 300.0        # sine frequency, Hz, may be float   

        elif maxFeeling == "sadness":

            duration = 1.0   # in seconds, may be float
            f = 200.0        # sine frequency, Hz, may be float   

        elif maxFeeling == "surprise":

            duration = 0.5   # in seconds, may be float
            f = 500.0        # sine frequency, Hz, may be float     

        # generate samples, note conversion to float32 array
        samples = (np.sin(2*np.pi*np.arange(self.fs*duration)*f/self.fs)).astype(np.float32)

        # for paFloat32 sample values must be in range [-1.0, 1.0]
        self.stream = self.p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=self.fs,
                        output=True)

        # play. May repeat with different volume values (if done interactively) 
        self.stream.write(self.volume*samples)

        self.stream.stop_stream()


    def close(self):

        self.stream.close()

        self.p.terminate()