#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import time

print "------------------------"
print sys.copyright
print "------------------------"

print "Hello, World!"

a, b, c = 1, 2, 'test'
print a,b,c

str = 'Hello World!'

print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个的元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值


print time.time()

def  f(param):
    return 'hello'+param

print f("world!")


import module
module.print_func("test")

from mathematics import sin
print sin(9)

# !/usr/bin/python
# -*- coding: UTF-8 -*-

#str = raw_input("请输入：");
#print "你输入的内容是: ", str

fileObject = open('test.txt','r',0)
print fileObject.read()
print fileObject.tell()
fileObject.close()

with open("test.txt") as file2:
    print  file2.read()

try:
    print 5/0
except ZeroDivisionError:
    print ('you can\'t divide by zero')