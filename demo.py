#!/usr/bin/env python
import paperplot
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    
    # create some random data
    x = np.arange(100)
    y = np.random.randn(100)

    # load the setup (with some specific update)
    paperplot.setup({'font.size':8})   

    # create a figure of the correct size
    fig = paperplot.paper_figure(300,200)

    # plotting
    plt.plot(x,y,'-', color=(0.22, 0.42, 0.69))
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('A simple demo figure')
    plt.grid(True)

    # output
    plt.savefig('figure.pdf')

