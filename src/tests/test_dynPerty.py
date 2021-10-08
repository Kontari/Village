#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

import sys
sys.path.append("..")
import dynPerty


def plotInformation(foo):
    # The parametrized function to be plotted
    def f2(t, alpha, beta):
        return foo(t, alpha, beta)

    t2 = np.linspace(0.0, 1.0, 100)
    init_alpha = 2.0
    init_beta = 5.0

    # Create the figure and the line that we will manipulate
    fig, ax = plt.subplots()
    line, = plt.plot(t2, f2(t2, init_alpha, init_beta), lw=2)
    plt.ylim(0,5.0)
    ax.set_xlabel('Units [x]')

    axcolor = 'lightgoldenrodyellow'
    ax.margins(x=0)

    # adjust the main plot to make room for the sliders
    # plt.subplots_adjust(left=0.25, bottom=0.5)
    plt.subplots_adjust(bottom=0.3)

    # Make a horizontal slider to control the frequency.
    axalpha = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor=axcolor)
    alpha_slider = Slider(
        ax=axalpha,
        label='Alpha',
        valmin=0.01,
        valmax=10.0,
        valinit=init_alpha,
    )

    # Make a vertically oriented slider to control the amplitude
    axbeta = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
    beta_slider = Slider(
        ax=axbeta,
        label="Beta",
        valmin=0.01,
        valmax=10.0,
        valinit=init_beta,
    )

    # The function to be called anytime a slider's value changes
    def update(val):
        line.set_ydata(f2(t2, beta_slider.val, alpha_slider.val))
        fig.canvas.draw_idle()

    # register the update function with each slider
    alpha_slider.on_changed(update)
    beta_slider.on_changed(update)

    # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

    def reset(event):
        alpha_slider.reset()
        beta_slider.reset()
    button.on_clicked(reset)

    plt.show()

if __name__ == '__main__':
    dp = dynPerty.DynamicPersonality()
    plotInformation(dp.getPersonalityIndex)