#!/usr/bin/python3
import sys


AIRPORT_LIST = ["12892", "14771", "12478"]


def is_looking_airport(array):
    if str(array[3]) in AIRPORT_LIST:
        return str(array[3])
    if str(array[4]) in AIRPORT_LIST:
        return str(array[3])
    return None


for line in sys.stdin:
    line = line.strip()
    arr = line.split(",")
    if len(arr) != 8:
        continue
    airport = is_looking_airport(arr)
    if airport is None:
        continue
    print(airport)
