#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return 0, None
    first_char = sentence[0]
    leng = len(sentence)
    return leng, first_char
