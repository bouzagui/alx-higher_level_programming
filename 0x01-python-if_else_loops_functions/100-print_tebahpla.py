#!/usr/bin/python3
for i in range(25, -1, -1):
    memory = i + 65
    if i % 2 == 1:
        memory = memory + 32
    print("{:memory}".format(memory), end="")
