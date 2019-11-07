import Tokenizer as tkner

tokenList = []



def tokenize(fileName):

    tokenList.append(tkner.tokenize(fileName))



#utility functions

def tokensLeft():

    return len(tokenList)


