#!/usr/bin/python3
import sys

# LAX, SFO, JFK
AIRPORT_LIST = ["12892", "14771", "12478"]

lax_count = [0]*12
sfo_count = [0]*12
jfk_count = [0]*12

for line in sys.stdin:
    arr = line.strip().split("\t")
    assert len(arr) == 2

    if arr[0] == AIRPORT_LIST[0]:
        lax_count[int(arr[1]) - 1] += 1
    if arr[0] == AIRPORT_LIST[1]:
        sfo_count[int(arr[1]) - 1] += 1
    if arr[0] == AIRPORT_LIST[2]:
        jfk_count[int(arr[1]) - 1] += 1

print("LAX", "\t", lax_count)
print("SFO", "\t", sfo_count)
print("JFK", "\t", jfk_count)