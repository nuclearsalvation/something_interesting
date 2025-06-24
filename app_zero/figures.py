import matplotlib.pyplot as plt
from math import sin, sqrt, exp

def sin_figure(a=0,b=3140,w=1,dx=0.001):
    fig, ax = plt.subplots()
    ax.plot([(float(x*dx)+float(a)) for x in range(b)], [sin((float(x*dx)+float(a))*(w)) for x in range(b)])
    #plt.savefig('app_zero/static/graph.png')
    return fig

def response_figure(fin=1,a =1.0, b=1.0,c=1.0, dx=0.001):
    fig, ax= plt.subplots()
    ax.plot([(float(x*dx)) for x in range(fin)],[(1/sqrt(((c-a*(x*dx)) ** 2) +(b ** 2)*(x*dx)**2)) for x in range(fin)])
    return fig

def sin_figure_damping(a=0,b=3140,w=1,dx=0.001, mu=0.5):
    fig, ax = plt.subplots()
    ax.plot([(float(x*dx)+float(a)) for x in range(b)], [sin((float(x*dx)+float(a))*(w))*exp(-mu*x*dx) for x in range(b)])
    #plt.savefig('app_zero/static/graph.png')
    return fig