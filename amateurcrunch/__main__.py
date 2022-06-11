from codecs import StreamReader
from distutils import text_file
import io
from msilib.schema import File
from multiprocessing import Array
from turtle import textinput
from typing import IO, Text
from venv import create

from matplotlib.pyplot import text
from numpy import array, array2string, savetxt

#print("enter number of letters.")

num = int(3)
entries = "0123456789qwertyuiopasdfghjklzxcvbnm"
keys = []

for i in entries:
    for j in entries:
        for k in entries:
            for l in entries:
                if (l != "0"):
                    break
                for m in entries:
                    for o in entries:
                        for p in entries:
                            for q in entries:
                                keys.append(i + j + k + l + m + o + p + q)
            if (l != "0"):
                break
        if (l != "0"):
            break
    if (l != "0"):
        break

savetxt("D:\Other\crunch8.txt", keys, '%s')

