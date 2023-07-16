#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    if len(sentence) == 0:
        t = (0, None)
    t = (len(sentence), first)
    return t
