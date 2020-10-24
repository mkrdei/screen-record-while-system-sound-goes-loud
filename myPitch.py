import parselmouth
import numpy as np
import matplotlib.pyplot as plt
from pynput.keyboard import Key, Controller
# If the sound in wav is louder than how we set the treshold, it will press GeForce Experience keyboard shortcuts.
snd = parselmouth.Sound("demo.wav")
if(snd!=[]):
    plt.figure()
    plt.plot(snd.xs(), snd.values.T, linewidth=0.5)
    plt.xlim([snd.xmin, snd.xmax])
    treshold = 0.42
    if len(snd.values.T[np.where(snd.values.T > treshold)])!=0:
        keyboard = Controller()
        keyboard.press(Key.alt_l)
        keyboard.press(Key.f10)
        keyboard.release(Key.alt_l)
        keyboard.release(Key.f10)
        print("I heard it!")
    else:
        print("Haven't heard anything!")
#plt.xlabel("time [s]")
#plt.ylabel("amplitude")
#plt.show() # or plt.savefig("sound.png"), or plt.savefig("sound.pdf")