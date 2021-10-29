#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

import sys
sys.path.append("..")
import dynPerty

MAX_DIST = 10
X_SCALE = 1
HIST_Y_SCALE = 20

def plotInformation(perCurve, rvsFunc):
    # The parametrized function to be plotted
    def customPlot(t, alpha, beta):
        return perCurve(t, alpha, beta)

    def rvsPlot(t, alpha, beta):
        return rvsFunc(t, alpha, beta, 1000)

    def redrawHist(axs, t2, a, b):
        axs.cla()
        axs.set_ylim(0,HIST_Y_SCALE)
        axs.set_xlim(0,X_SCALE)
        axs.hist(rvsPlot(t2, a, b), density=True, bins=20)

    t2 = np.linspace(0.0, 1.0, 100)
    init_alpha = 1.3
    init_beta = 2.0

    # Create the figure and the line that we will manipulate
    fig, axs = plt.subplots(nrows=1, ncols=2)
    line1, = axs[0].plot(t2, customPlot(t2, init_alpha, init_beta), lw=2)
    line2, bin, patches = axs[1].hist(rvsPlot(t2, init_alpha, init_beta), density=True, bins=10)
    axs[0].set_ylim(0,5.0)
    axs[0].set_xlim(0,X_SCALE)
    axs[1].set_ylim(0,HIST_Y_SCALE)
    axs[1].set_xlim(0,X_SCALE)
    axs[0].set_xlabel('Units [x]')

    axcolor = 'lightgoldenrodyellow'
    axs[0].margins(x=0)

    # adjust the main plot to make room for the sliders
    plt.subplots_adjust(bottom=0.35)

    # Make a horizontal slider to control the frequency.
    axalpha = plt.axes([0.2, 0.20, 0.65, 0.03], facecolor=axcolor)
    alpha_slider = Slider(
        ax=axalpha,
        label='Alpha',
        valmin=0.01,
        valmax=MAX_DIST,
        valinit=init_alpha,
    )

    # Make a vertically oriented slider to control the amplitude
    axbeta = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor=axcolor)
    beta_slider = Slider(
        ax=axbeta,
        label="Beta",
        valmin=0.01,
        valmax=MAX_DIST,
        valinit=init_beta,
    )

    axoverall = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
    skew_slider = Slider(
        ax=axoverall,
        label="Skew %",
        valmin=-MAX_DIST,
        valmax=MAX_DIST,
        valinit=0.0,
    )

    # The function to be called anytime a slider's value changes
    def update(val):
        a, b = alpha_slider.val, beta_slider.val
        line1.set_ydata(customPlot(t2, a, b))
        redrawHist(axs[1], t2, a, b)
        skew_slider.reset()
        fig.canvas.draw_idle()

    def updateOverall(val):
        a = max(0.01, alpha_slider.val + skew_slider.val)
        b = max(0.01, beta_slider.val - skew_slider.val)
        print(skew_slider.val)
        print(alpha_slider.val, beta_slider.val)
        print(a,b)
        line1.set_ydata(customPlot(t2, a, b))
        redrawHist(axs[1], t2, a, b)
        fig.canvas.draw_idle()

    # register the update function with each slider
    alpha_slider.on_changed(update)
    beta_slider.on_changed(update)
    skew_slider.on_changed(updateOverall)

    # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.875')

    def reset(event):
        skew_slider.reset()
        alpha_slider.reset()
        beta_slider.reset()
    button.on_clicked(reset)

    plt.show()

def scatter_hist(data, ax):
    # bins = np.arange(data, x)
    ax.hist(data, bins="auto", alpha=0.4)

if __name__ == '__main__':
    personality = dynPerty.DynamicPersonality()
    plotInformation(personality.genCurve, personality.getIndex)
