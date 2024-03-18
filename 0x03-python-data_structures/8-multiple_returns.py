#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    first_char = sentence
    leng = len(sentence)
    return leng, first_char
