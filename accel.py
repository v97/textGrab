import serial
import matplotlib.pyplot as plt
import numpy as np
from time import sleep


values = []
plt.ion()
s = serial.Serial('COM7',9600) # check your arduino code baudrate
#plt.ion()
#plt.show()


#while True:
#   print([float(item) for item in str(s.readline()).split(',')[1:-1]])
import time
from matplotlib import pyplot as plt
import numpy as np

data = np.random.random(100)

def live_update_demo():
    global data
    redraw_figure()

    t_start = time.time()
    for i in range(1000):
        data = np.roll(data, -1)
        try:
            data[-1] = [float(item) for item in str(s.readline()).split(',')[1:-1]][0]
        except:
            data[-1] = 0
        plot.set_ydata(data)
        redraw_figure()
        print('Mean Frame Rate: %.3gFPS' % ((i+1) / (time.time() - t_start)))

def redraw_figure():
    plt.draw()
    plt.pause(0.05)

live_update_demo()
