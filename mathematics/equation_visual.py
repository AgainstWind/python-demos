# -*- coding: utf-8 -*-
import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-30, 30, 10000)
y = (x ** 2 - 5 * x + 10)
z = (2 * x - 5)  # µ¼Êý·½³Ì
z = (-5 * x + 10)  # ¶þ´Îº¯ÊýµÄ0µãÇÐÏß·½³Ì

plt.figure(figsize=(8, 4))
plt.plot(x, y, color="red", linewidth=2)
plt.plot(x, z, color="blue")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-100, 400)
plt.legend()
plt.show()