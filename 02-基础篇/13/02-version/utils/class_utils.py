#! /usr/bin/python3
# coding=utf-8

class Encoder(object):
    def encode(self, s):
        return s[::-1]


class Decoder(object):
    def decode(self, s):
       # return ''.join(reverse(list(s)))
       # return ''.join(list(s).reverse())
       return ''.join(reversed(list(s)))
