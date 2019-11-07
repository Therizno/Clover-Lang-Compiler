import Tokenizer as tkner

tokenList = []


def tokenize(fileName):

    tokenList = tkner.tokenize(fileName)
