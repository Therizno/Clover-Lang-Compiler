import MainUtil as mtl
import ParserUtil as utl

statementList = []

line = 1 


#possible kinds of statements:
#"var_assign"
#"expression"
#"function_dec"
#"function_call"
#"conditional"
#"loop"
#
#also any kind of TokenEntry can also be a kind of statement


class Statement:

    def __init__(self, kind, subList=[]):

        self.kind = kind
        self.subList = subList

    def addToken(tokenEntry):

        subList.append(Statement(tokenEntry.kind, [tokenEntry.token]))
    



def parseStatement():

    #handle variable declarations and assignments
    if utl.peek().token in mtl.types or (utl.tokensLeft() > 1 and utl.peek(2)[1].token == "="):

        parseVarAssignment()



def parseVarAssignment():

    varAssignment = Statement("var_assign")

    if utl.peek().token in mtl.types:

        varAssignment.addToken(utl.pop())



def parse(fileName):

    global line 

    utl.tokenize(fileName)

    while utl.tokensLeft() > 0:

        parseStatement()

        line += 1
