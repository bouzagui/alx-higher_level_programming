#!/usr/bin/python3
for i in range(25, -1, -1):
    mem = i + 65
    if i % 2 == 1:
        mem = mem + 32
    print("{:c}".format(mem), end="")
