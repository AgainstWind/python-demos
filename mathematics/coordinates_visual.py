#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def polar_coordinates_test():
    N = 150
    r = 2 * np.random.rand(N)
    theta = 2 * np.pi * np.random.rand(N)
    area = 200 * r ** 2
    colors = theta
    ax = plt.subplot(111, projection='polar')
    c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
    plt.show()


def polar_pie_test():
    # Compute pie slices
    N = 20
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)

    ax = plt.subplot(111, projection='polar')
    bars = ax.bar(theta, radii, width=width, bottom=0.0)

    # Use custom colors and opacity
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.viridis(r / 10.))
        bar.set_alpha(0.5)

    plt.show()

def polar_test():
    theta = np.arange(0, 2 * np.pi, 0.02)
    plt.subplot(121, polar=True)
    plt.plot(theta, 2 * np.ones_like(theta), lw=2)
    plt.plot(theta, theta / 6, '--', lw=2)
    plt.subplot(122, polar=True)
    plt.plot(theta, np.cos(5 * theta), '--', lw=2)
    plt.plot(theta, 2 * np.cos(4 * theta), lw=2)
    plt.rgrids(np.arange(0.5, 2, 0.5), angle=45)
    plt.thetagrids([0, 45, 90])
    plt.show()

if __name__=="__main__":
    polar_test()
