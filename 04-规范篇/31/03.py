#! /usr/bin/env python3
# coding=utf-8

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n-1))
    res.append(fib(n))
    return res


fib_seq(30)

# 分析方法
# python3 -m cProfile xxx.py
