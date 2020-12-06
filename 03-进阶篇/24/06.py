#! /usr/bin/env python3
# coding=utf-8

import gc
import psutil
import os


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


show_memory_info('initial')
a = [i for i in range(10000000)]
show_memory_info('after a created')

del a
gc.collect()

show_memory_info('finish')
print(a)