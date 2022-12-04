#!/usr/bin/python3
def multiple_returns(sentence):
    len = len(sentence)
    if len == 0:
        return (len, )
    else:
        return (len, sentence[0])
