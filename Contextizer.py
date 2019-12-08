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

    ctutl.nextStatement()       #move into varStatement object

    stmt = ctutl.nextStatement()    #grab the first token

    if stmt.kind in mtl.types:

        name = ctutl.nextStatement()

        if name in varTable:

            raise ContextException(name + " declared twice")

        varTable[stmt2] = stmt.kind 

        expType =




def contextizeExpression(expStatement):

    




        
