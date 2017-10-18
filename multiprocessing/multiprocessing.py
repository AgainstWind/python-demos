#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
#from multiprocessing import Process # windows

def unixTest():
    print 'Process (%s) start...' %os.getpid()
    pid = os.fork()
    if pid==0:
        print 'I\'m child process: %s, and my parent is %s.' %(os.getpid(),os.getppid())
    else:
        print 'I\'m parent process: %s, child process: %s.' %(os.getpid(),pid)

def windowsTest():
    print '...'

if __name__=='__main__':
    unixTest()
    windowsTest()
