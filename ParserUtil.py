import Tokenizer as tkner

tokenList = []



def tokenize(fileName):

    tokenList.append(tkner.tokenize(fileName))



#utility functions

def tokensLeft():

    return len(tokenList)


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



