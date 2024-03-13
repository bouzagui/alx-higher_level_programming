#!/usr/bin/python3
ascii_start = 97
ascii_end = 122
ascii_output = ""

for ascii_value in range(ascii_start, ascii_end + 1):
    ascii_output = ascii_output + chr(ascii_value)

print("{}".format(ascii_output), end="")
