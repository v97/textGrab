import serial
import matplotlib.pyplot as plt
import numpy as np
from time import sleep, time


values = []
plt.ion()
s = serial.Serial('COM7',9600) # check your arduino code baudrate
#plt.ion()
#plt.show()


#while True:
#   print([float(item) for item in str(s.readline()).split(',')[1:-1]])

data = np.random.random(50)

def live_update_demo():
    global data
    plot, = plt.plot(np.random.randn(50))
    redraw_figure()

    t_start = time()
    for i in range(1000):
        data = np.roll(data, -1)
        try:
            serialdata = str(s.readline())
            print(serialdata)
            read = serialdata.split(',')[1:-1:2]
            #nums = [float(item.split(':')[1]) for item in read]
            data[-1] = read[0]
            print(read)
            #data[-1] = num[0]
        except:
            data[-1] = 0
        plot.set_ydata(data)
        redraw_figure()
        print('Mean Frame Rate: %.3gFPS' % ((i+1) / (time() - t_start)))

def redraw_figure():
    plt.draw()
    plt.pause(0.05)

live_update_demo()
     