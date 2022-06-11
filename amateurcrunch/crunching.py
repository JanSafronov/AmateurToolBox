from codecs import StreamReader
import io
from multiprocessing import Array
from turtle import textinput
from typing import IO, Text
from venv import create

from matplotlib.pyplot import text
from numpy import array, array2string, savetxt

print("Enter path of the file to read and rewrite")

file = open(input())

print("Optional: Enter the number of lines to rewrite to a new file 'output'")

lines = input()

entries = file.readlines()
print(entries)
elen = len(entries[0])
keys = open("output.txt", 'w+').readlines()

for i in range(int(lines)):
    keys.append("crunch " + str(elen - 1) + " " + str(elen - 1) + " -o crunched" + str(i) + ".txt -t " + entries[i])

garbage = open("garbage.txt", 'w+').readlines()
garbage.extend(entries[:int(lines)])
print(garbage)

entries = entries[int(lines):]

savetxt(file.name, entries, '%s', newline='')
savetxt("garbage.txt", garbage, '%s', newline='')
savetxt("output.txt", keys, '%s', newline='')