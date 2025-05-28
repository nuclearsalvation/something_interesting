import matplotlib.pyplot as plt
from math import sin

def sin_figure(a=0,b=3140,w=1.0,dx=0.001):
    fig, ax = plt.subplots()
    ax.plot([(float(x)+float(a))/(dx/w) for x in range(b)], [sin((float(x)+float(a))/(dx/w)) for x in range(b)])
    plt.savefig('app_zero/static/graph.png')
    return fig