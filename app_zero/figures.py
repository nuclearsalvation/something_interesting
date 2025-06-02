import matplotlib.pyplot as plt
from math import sin

def sin_figure(a=0,b=3140,w=1,dx=0.001):
    fig, ax = plt.subplots()
    ax.plot([(float(x*dx)+float(a)) for x in range(b)], [sin((float(x*dx)+float(a))*(w)) for x in range(b)])
    #plt.savefig('app_zero/static/graph.png')
    return fig