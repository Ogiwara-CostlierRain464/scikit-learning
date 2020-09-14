#!/usr/bin/python3
import sys

# LAX, SFO, JFK
AIRPORT_LIST = ["12892", "14771", "12478"]

lax_count = 0
sfo_count = 0
jfk_count = 0

for line in sys.stdin:
    line = line.strip()
    if line == AIRPORT_LIST[0]:
        lax_count += 1
    if line == AIRPORT_LIST[1]:
        sfo_count += 1
    if line == AIRPORT_LIST[2]:
        jfk_count += 1

print("LAX", "\t", lax_count)
print("SFO", "\t", sfo_count)
print("JFK", "\t", jfk_count)
