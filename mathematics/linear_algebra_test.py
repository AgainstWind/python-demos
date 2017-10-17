#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np


def matrix_test():
    a = np.matrix([[1,4,3],[6,3,8]])
    print a.shape
    print a
    print a.T
    print a.A
    print a.A1
    print np.linalg.det(a)

matrix_test()