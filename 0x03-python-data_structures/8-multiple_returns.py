#!/usr/bin/python3
def multiple_returns(sentence):
    b = len(sentence)
    if b == 0:
        return (b, None)
    else:
        return(b, sentence[0])
