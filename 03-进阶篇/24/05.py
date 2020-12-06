#! /usr/bin/env python3
# coding=utf-8

import sys


a = []

# 两次引用，一次来自a，一次来自getrefcount
print(sys.getrefcount(a))

b = a
print(sys.getrefcount(a))  # 3次

c = b
d = b
e = c
f = e
g = d
print(sys.getrefcount(a)) # 8次