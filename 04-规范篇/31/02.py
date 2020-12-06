#! /usr/bin/env python3
# coding=utf-8

def func():
    print('enter func()')

a = 1
b = 2
import pdb
pdb.set_trace()
func()
c = 3
print(a + b + c)
