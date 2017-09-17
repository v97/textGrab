from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import serial

app = QtGui.QApplication([])
#p = pg.plot()
#curve = p.plot()
win = pg.GraphicsWindow()
plots = [win.addPlot() for plot in range(3)]
curves = [plot.plot() for plot in plots]
data = np.zeros([3, 50])
s = serial.Serial('COM7',9600) # check your arduino code baudrate

def updater():
    global data
    data = np.roll(data, -1, axis = 1)
    serialdata = str(s.readline())
    #print(serialdata)
    read = serialdata.split(',')[1:-1:2]
    for curveID in range(len(curves)):
        data[curveID][-1] = read[curveID]
        curves[curveID].setData(data[curveID])

timer = QtCore.QTimer()
timer.timeout.connect(updater)
timer.start(0)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()