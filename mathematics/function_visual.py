#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def printTwoDimension():
    plt.figure(1)
    ax = plt.subplot(111)
    x = np.linspace(0, np.pi * 2, 200)  # 在0到2pi之间，均匀产生200点的数组

    # r = 2cosθ
    r = 2 * np.cos(x)  # 半径
    ax.plot(r * np.cos(x), r * np.sin(x))

    # r = 1
    r = 1
    ax.plot(r * np.cos(x), r * np.sin(x))
    plt.show()

def printThreeDimension():
    fig = plt.figure(1)
    ax = fig.add_subplot(1, 1, 1, projection='3d')  # 指定三维空间做图

    t = np.linspace(0, 4, 200)  # 在0到4之间，均匀产生200点的数组
    theta = t * 2 * np.pi  # 角度

    # r(t)=(sint,cost,t)
    z = t
    x = np.sin(theta)
    y = np.cos(theta)
    ax.plot(x, y, z, label='r(t)')

    # r’(t)
    z = 1
    x = np.cos(theta)
    y = -np.sin(theta)
    ax.plot(x, y, z, label='r\'(t)')

    ax.legend()
    plt.show()

def printCurve():
    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(-2, 2, 0.1)
    Y = np.arange(-2, 2, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = X ** 2 + Y ** 2
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    plt.show()

#printThreeDimension()
#printCurve()



def fun():
    x = np.arange(-50,50,0.1)
    y = np.arange(-50,50,0.1)
    z = np.power(x,2)+np.sin(y)
    return (x,y,z)

def functionShow():
    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(-10, 10, 0.2)
    Y = np.arange(-10, 10, 0.2)
    X, Y = np.meshgrid(X, Y)
    Z = np.cos(X) + np.sin(Y)* 2
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    plt.show()

functionShow()

