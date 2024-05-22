#!/usr/bin/python3
def text_indentation(text):
    if not type(str):
        raise TypeError("text must be a string")
    for char in text:
        if char in ".?:":
            print(char)
            print()
        else:
            print(char, end="")
