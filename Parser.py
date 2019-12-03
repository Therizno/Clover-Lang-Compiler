import MainUtil as mtl
import ParserUtil as utl

statementList = []

line = 1 


def parseStatement():

    #handle variable declarations and assignments
    if utl.peek().token in mtl.types or (utl.tokensLeft() > 1 and utl.peek(2)[1].token == "="):

        parseVarAssignment()



def parseVarAssignment()

    if utl.peek().token in mtl.types:

        



def parse(fileName):

    global line 

    utl.tokenize(fileName)

    while utl.tokensLeft() > 0:

        parseStatement()

        line += 1
