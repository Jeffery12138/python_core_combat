#! /usr/bin/env python3
# coding=utf-8

def solve(arr, target):
    l, r = 0, len(arr) -1
    ret = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] * arr[m] > target:
            ret = m
            r = m - 1
        else:
            l = m + 1
    if ret == -1:
        return -1
    else:
        return arr[ret]


print(solve([1, 2, 3, 4, 5, 6], 8))
print(solve([1, 2, 3, 4, 5, 6], 9))
print(solve([1, 2, 3, 4, 5, 6], 0))
print(solve([1, 2, 3, 4, 5, 6], 40))
