#! /usr/bin/python3
# coding=utf-8


import sys


sys.path.append('..')

from utils.class_utils import *


encoder = Encoder()
decoder = Decoder()


print(encoder.encode('abcde'))
print(decoder.decode('edcba'))
