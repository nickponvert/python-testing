import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
points=np.random.random([10, 3])
ax = fig.add_subplot(111)
ax.scatter(points[:, 0], points[:, 1])

clicked_points=[]

def on_key(event):
    print('you pressed', event.key, event.xdata, event.ydata)

def press(event):
    print('press', event.key)
#    sys.stdout.flush()
    if event.key=='x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.mpl_disconnect(mpid)
        #fig.canvas.mpl_disconnect(kpid)
        point_array=np.array(clicked_points)
        #ax.scatter(point_array[:, 0], point_array[:, 1],'g')
        fig.canvas.draw()

def onclick(event):
    print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
        event.button, event.x, event.y, event.xdata, event.ydata)
    clicked_points.append([event.xdata, event.ydata])

xl = ax.set_xlabel('easy come, easy go')

kpid = fig.canvas.mpl_connect('key_press_event', press)

mpid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
