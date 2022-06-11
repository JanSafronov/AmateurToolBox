from codecs import StreamReader
import io
from multiprocessing import Array
from turtle import textinput
from typing import IO, Text
from venv import create

from matplotlib.pyplot import text
from numpy import array, array2string, savetxt
from sympy import continued_fraction_convergents

filepath = input()

entries = open(filepath).readlines()
filtered = []

for entry in entries:
    if (entry in filtered):
        continue
    else:
        filtered.append(entry)     

print(filtered)

savetxt(filepath, filtered, '%s', newline='')