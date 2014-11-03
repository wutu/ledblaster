#!/usr/bin/env python

import os
import sys
from time import sleep
from array import array

# Check number of strings passed
if len(sys.argv) != 5:
    print("Usage: python ledblaster.py <gpio> <time(s)> <from(0-100)> <to(0-100)>")
    sys.exit()

gpio = int(sys.argv[1])
pause_time = float(sys.argv[2])
od = int(sys.argv[3]) * 10
do = int(sys.argv[4]) * 10

INPUT_SIZE = 1000   # Input integer size
OUTPUT_SIZE = 1000    # Output integer size
INT_TYPE = 'const unsigned char'
TABLE_NAME = 'cie';

def cie1931(L):
    L = L*100.0
    if L <= 8:
        return (L/902.3)
    else:
        return ((L+16.0)/116.0)**3

x = range(0,int(INPUT_SIZE+1))
y = [round(cie1931(float(L)/INPUT_SIZE)*OUTPUT_SIZE) for L in x]

cie1931=[]

for i,L in enumerate(y):
    l = (int(L)*0.001)
    l = round(l, 3)
    cie1931.append(l)

print cie1931

FIFO = open('/dev/pi-blaster', 'w', buffering=0)

def set(gpio, value):
    s = "%s=%s\n" % (gpio, value)
    FIFO.write(s)

if od < do:
    cie1931=cie1931[od:do]
    for i in cie1931:
        set (gpio, i)
        sleep(pause_time)

else:
    cie1931=cie1931[do:od]
    for i in reversed(cie1931):
        set (gpio, i)
        sleep(pause_time)
