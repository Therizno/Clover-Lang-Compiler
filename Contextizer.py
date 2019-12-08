import MainUtil as mtl
import ContextizerUtil as ctutl
from Parser import Statement

#key: var name, value: var type
varTable = {} 


def contextize():

    while ctutl.hasNext():

        s = ctutl.nextStatement()

        # deals with Statement object only, no tokens 
        if not isinstance(s, Statement):

            raise ContextException("unexpected token: "+str(s)+" (this should never occur)")


        if s.kind == "var_assign":

            contextizeVar(s)




def contextizeVar(varStatement):

    if ctutl.nextStatement().kind == "keyword": 

        typ = ctutl.nextToken()
        name = ctutl.nextToken()

        if name in varTable:

            raise ContextException(name + " declared twice")

        varTable[name] = typ 

        ctutl.nextToken()     #skip the "="

        expType = contextizeExpression(ctutl.nextStatement()) 

        


#returns the return type of this expression

def contextizeExpression(expStatement):

    




        
