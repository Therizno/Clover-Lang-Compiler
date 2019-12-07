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

    def __init__(self, kind):

        self.kind = kind
        self.subList = []

    def addToken(self, tokenEntry):

        s = Statement(tokenEntry.kind)
        s.subList.append(tokenEntry.token)
        self.subList.append(s)
    



def endOfLine():

    return utl.tokensLeft() <= 0 or utl.peek() == "NEWLINE"



#verifies that this TokenEntry fits some requirements, and returns it 
def verify(tokenEntry, tokenString, isValid=lambda x, y : x.token==y):

    if isValid(tokenEntry, tokenString):

        return tokenEntry

    raise utl.ParserException("expected "+tokenString+", found " +tokenEntry.token+" at line "+str(line))



def parseStatement():

    if utl.peek() == "NEWLINE":

        utl.pop()

    #handle variable declarations and assignments
    elif utl.peek().token in mtl.types or (utl.tokensLeft() > 1 and utl.peekX(2)[1].token == "="):

        statementList.append(parseVarAssignment())

    else:
        raise utl.ParserException("unexpected token: "+utl.peek().token)




def parseVarAssignment():

    varAssignment = Statement("var_assign")

    if utl.peek().token in mtl.types:

        varAssignment.addToken(utl.pop())
        print("var assignment objects 1")
        print(len(varAssignment.subList))

    varAssignment.addToken(verify(utl.pop(), "identifier", lambda x, y : x.kind == y))
    print("var assignment objects 2")
    print(len(varAssignment.subList))
    varAssignment.addToken(verify(utl.pop(), "="))
    print("var assignment objects 3")
    print(len(varAssignment.subList))
    varAssignment.subList.append(parseExpression())
    print("var assignment objects 4")
    print(len(varAssignment.subList))
    return varAssignment



def parseExpression():

    perenValue = 0

    exp = Statement("expression")
    

    while not endOfLine():

        while (not endOfLine()) and utl.peek().token == "(":

            exp.addToken(verify(utl.pop(), "("))
            perenValue += 1

        exp.addToken(verify(utl.pop(), "a value", lambda x, y : x.kind in ["identifier", "number", "char"] or x.token in mtl.special_values))

        while (not endOfLine()) and utl.peek().token == ")":

            perenValue -= 1

            if perenValue < 0:
                break

            exp.addToken(verify(utl.pop(), ")"))



        if (not endOfLine()) and utl.peek().kind == "operator":
            
            exp.addToken(verify(utl.pop(), "operator", lambda x, y : x.kind == y))
            
        else:
            break

    print("exp: "+str(exp))
    return exp 



def parse(fileName):

    global line 

    utl.tokenize(fileName)

    while utl.tokensLeft() > 0:

        parseStatement()

        line += 1



#test 


def printStatements(l):

    if isinstance(l, str):

        print(l)

    elif isinstance(l, Statement):

        print("printing: " + l.kind)
        printStatements(l.subList)

    else:

        for st in l:
            print("printing subList: "+str(st))
            printStatements(st)


parse("test/test_4.leaf")
print("printing:")
printStatements(statementList)
