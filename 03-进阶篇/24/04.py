#! /usr/bin/env python3
# coding=utf-8

import sys


a = []

# 两次引用，一次来自a，一次来自getrefcount
print(sys.getrefcount(a))


def func(a):
    # 四次引用，a，python的函数调用栈，函数参数，和getrefcount
    print(sys.getrefcount(a))


if __name__ == '__main__':
    func(a)

# 两次引用，一次来自a，一次来自getrefcount
print(sys.getrefcount(a))