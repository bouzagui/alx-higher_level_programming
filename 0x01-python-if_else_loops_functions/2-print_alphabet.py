#!/usr/bin/python3
ascii_start = 97
ascii_end = 122

for ascii_value in range(ascii_start, ascii_end + 1):
    print("{}".format(chr(ascii_value)), end="")
