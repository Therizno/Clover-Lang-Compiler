import MainUtil as mtl
import Tokenizer as tkner

tokenList = []



def tokenize(fileName):

    tokenList.append(tkner.tokenize(fileName))



#utility functions

def tokensLeft():

    return len(tokenList)


def peek():

    return tokenList[0]


#peek the first x elements 
def peek(x):

    l = []

    for i in range(0, x):

        l.append(tokenList[i])

    return l



def peekUntil(stop):

    l = []
    i = 0

    while not stop(tokenList[i]):

        l.append(tokenList[i])
        i += 1

    return l




def pop():

    return tokenList.pop(0)
    

#pop the firt x elements 
def pop(x):

    l = []

    for i in range(0, x):

        l.append(tokenList.pop(0))

    return l



def popUntil(stop):

    l = []

    while not stop(tokenList[0]):

        l.append(tokenList.pop(0))

    return l



#exceptions

class ParserException(mtl.CompileException):

    def __init__(self, text):
        self.message = "Parser Error: " + text


