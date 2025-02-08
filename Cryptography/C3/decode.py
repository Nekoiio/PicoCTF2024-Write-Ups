'''
out = ""

prev = 0
for char in chars:
    cur = lookup1.index(char)
    out += lookup2[(cur - prev) % 40]
    prev = cur
'''

from fileinput import input
import sys
chars = ""
for line in input():
    chars += line

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

# reverse encoding.
out = ""
first = 0
second = 0

for char in chars:
    first = (lookup2.index(char) + first) % 40
    out += lookup1[first]
    second = first

sys.stdout.write(out)
