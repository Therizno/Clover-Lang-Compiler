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
    

#verifies that this TokenEntry fits some requirements, and returns it 
def verify(tokenEntry, tokenString, isValid=lambda x, y : x.token==y):

    if isValid(tokenEntry, tokenString):

        return tokenEntry

    raise utl.ParserException("expected "+tokenString+", found " +tokenEntry.token+" at line "+line)



def parseStatement():

    #handle variable declarations and assignments
    if utl.peek().token in mtl.types or (utl.tokensLeft() > 1 and utl.peek(2)[1].token == "="):

        parseVarAssignment()


    if utl.peek() == "NEWLINE":

        utl.pop()



def parseVarAssignment():

    varAssignment = Statement("var_assign")

    if utl.peek().token in mtl.types:

        varAssignment.addToken(utl.pop())

    varAssignment.addToken(verify(utl.pop(), "identifier", lambda x, y : x.kind == y))
    varAssignment.addToken(verify(utl.pop(), "="))

    varAssignment.subList.append(parseExpression())

    return varAssignment



def parseExpression():

    perenValue = 0

    exp = Statement("expression")
    

    while True:

        while utl.peek().token == "(":

            exp.addToken(verify(utl.pop(), "("))
            perenValue += 1

        exp.addToken(verify(utl.pop(), "a value", lambda x, y : x.kind == "identifier" or x.token in mtl.special_values))

        while utl.peek().token == ")":

            perenValue -= 1

            if perenValue < 0:
                break

            exp.addToken(verify(utl.pop(), ")"))



        if utl.peek().kind == "operator":
            
            exp.addToken(verify(utl.pop(), "operator", lambda x, y : x.kind == y))
            
        else:
            break

    return exp 



def parse(fileName):

    global line 

    utl.tokenize(fileName)

    while utl.tokensLeft() > 0:

        parseStatement()

        line += 1
