#-*- coding: utf-8 -*-

def listarPares(ultimo):
  for x in range(0,ultimo+1,2):
      print x

def listarPares2(ultimo):
    x = 0
    while x < ultimo + 1:
        print x
        x  = x + 2

listarPares2(101)
