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

        #parent node 
        self.parent = None

        #for use by contextizer 
        self.i = 0
        

    def add(self, statm):

        statm.parent = self
        self.subList.append(statm)
        

    def addToken(self, tokenEntry):

        s = Statement(tokenEntry.kind)
        s.parent = self
        s.subList.append(tokenEntry.token)
        self.subList.append(s)

    # used for iteration 
    def nextNode(self):

        if self.i < len(self.subList):

            self.i += 1
            return self.subList[i-1]

        return self.parent

    def visited(self):

        return i >= len(self.subList) 

    



def endOfLine():

    return utl.tokensLeft() <= 0 or utl.peek() == "NEWLINE"



#verifies that this TokenEntry fits some requirements, and returns it 
def verify(tokenEntry, tokenString, isValid=lambda x, y : x.token==y):

    if isValid(tokenEntry, tokenString):

        return tokenEntry

    raise utl.ParserException("expected "+tokenString+", found " +tokenEntry.token+" at line "+str(line))



def parseStatement():

    global line

    if utl.peek() == "NEWLINE":

        utl.pop()
        line += 1

    #handle variable declarations and assignments
    elif utl.peek().token in mtl.types or (utl.tokensLeft() > 1 and utl.peekX(2)[1].token == "="):

        statementList.append(parseVarAssignment())

    else:
        raise utl.ParserException("unexpected token: "+utl.peek().token)




def parseVarAssignment():

    varAssignment = Statement("var_assign")

    if utl.peek().token in mtl.types:

        varAssignment.addToken(utl.pop())

    varAssignment.addToken(verify(utl.pop(), "identifier", lambda x, y : x.kind == y))
    varAssignment.addToken(verify(utl.pop(), "="))
    varAssignment.add(parseExpression())

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


    return exp 



def parse(fileName):

    global line

    utl.tokenize(fileName)

    while utl.tokensLeft() > 0:

        parseStatement()

    line -= 1             # avoids line overcount
    return statementList



#test 


def printStatements(l):

    if isinstance(l, str):

        print(l)

    elif isinstance(l, Statement):

        print(l.kind + ": ")
        printStatements(l.subList)

    else:

        for st in l:

            printStatements(st)


parse("test/test_4.leaf")
print("printing:")
printStatements(statementList)
print(str(line) + " lines")
