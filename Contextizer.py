import MainUtil as mtl
import ContextizerUtil as ctutl

from Parser import Statement
from Tokenizer import TokenEntry


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

        if mtl.typeRank(expType) > mtl.typeRank(typ):

            mtl.compilerWarnings.append("possible loss of information when initializing "+name)

    else:

        name = ctutl.nextToken()

        ctutl.nextToken()     #skip the "="

        expType = contextizeExpression(ctutl.nextStatement())

        # case for assigning new value to old variable
        if name in varTable:

            if mtl.typeRank(expType) > mtl.typeRank(varTable[name]):

                mtl.compilerWarnings.append("possible loss of information when initializing "+name)


        # case for creation of new variable        
        else:
            
            varStatement.addToken(TokenEntry(expType, name))
            varTable[name] = expType 


#returns the return type of this expression

def contextizeExpression(expStatement):

    st = ctutl.nextStatement()

    maxVar = None
    

    #compare a variable type string to the current maximum variable type found 
    def newMax(type1):

        if mtl.typeRank(type1) > mtl.typeRank(maxVar):

            maxVar = type1

            

    while st.parent == expStatement:

        if st.kind == "number":

            if "." in ctutl.nextToken():

                newMax("float")

            else:

                newMax("int")

        elif st.kind == "keyword":

            #add null case later (when objects are implemented)

            ctutl.nextToken()

            newMax("bool")

        elif st.kind == "identifier":

            name = ctutl.nextToken()

            try:
                newMax(varTable[name])

            except:
                raise ContextException(name + " is not defined")

        elif st.kind == "char":

            newMax("char")
            

        st = ctutl.nextStatement()




        
