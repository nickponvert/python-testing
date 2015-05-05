import numpy as np
import matplotlib.pyplot as plt

#Make up some random points to test the program.


class ClusterCutter(object):

    def __init__(self, shape)
        self.fig = plt.figure()
        self.points=np.random.random([10, 3])
        self.ax = self.axfig.add_subplot(111)
        self.ax.scatter(points[:, 0], points[:, 1])

    #This returns the location of mouse clicks
    def onclick(event):
        print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
            event.button, event.x, event.y, event.xdata, event.ydata)

    #This returns the last key pressed
    def on_key(event):
        print('you pressed', event.key, event.xdata, event.ydata)

    def press(event):
        print('press', event.key)
        sys.stdout.flush()
        if event.key=='x':
            visible = xl.get_visible()
            xl.set_visible(not visible)
            fig.canvas.draw()



    cid = fig.canvas.mpl_connect('key_press_event', press)

    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    fig.show()

