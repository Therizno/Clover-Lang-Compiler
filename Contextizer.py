import MainUtil as mtl
import ContextizerUtil as utl

from Parser import Statement
from Tokenizer import TokenEntry


#key: var name, value: var type
varTable = {} 



def contextizeVar(varStatement):

    if utl.nextStatement().kind == "keyword": 

        typ = utl.nextToken()
        name = utl.nextToken()

        if name in varTable:

            raise utl.ContextException(name + " declared twice")

        varTable[name] = typ 

        utl.nextToken()     #skip the "="
        utl.nextStatement() #skip to expression statement 

        expType = contextizeExpression(utl.nextStatement()) 

        if mtl.typeRank(expType) > mtl.typeRank(typ):

            mtl.compilerWarnings.append("possible loss of information when initializing "+name)

    else:

        name = utl.nextToken()

        utl.nextToken()     #skip the "=" 
        utl.nextStatement() #skip to expression statement 

        expType = contextizeExpression(utl.nextStatement())

        # case for assigning new value to old variable
        if name in varTable:

            if mtl.typeRank(expType) > mtl.typeRank(varTable[name]):

                mtl.compilerWarnings.append("possible loss of information when initializing "+name)


        # case for creation of new variable        
        else:

            #add type token to var dec
            s = Statement("keyword")
            s.subList.append(expType)
            s.parent = varStatement
            varStatement.subList.insert(0, s) 

            #add to symbol table
            varTable[name] = expType 


#returns the return type of this expression

def contextizeExpression(expStatement):

    maxVar = None
    

    #compare a variable type string to the current maximum variable type found 
    def newMax(type1):

        nonlocal maxVar 

        if maxVar == None or mtl.typeRank(type1) > mtl.typeRank(maxVar):

            maxVar = type1

            
    st = utl.nextStatement()

    while isinstance(st, str) or isinstance(st, Statement) and (st.parent == expStatement or st == expStatement): 

        if not isinstance(st, str):
        
            if st.kind == "number":

                if "." in utl.nextToken():

                    newMax("float")

                else:

                    newMax("int")

            elif st.kind == "keyword":

                #add "null" case later (when objects are implemented)

                newMax("bool")

            elif st.kind == "identifier":

                name = utl.nextToken()

                try:
                    newMax(varTable[name])

                except:
                    raise utl.ContextException(name + " is not defined")

            elif st.kind == "char":

                newMax("char")



        st = utl.nextStatement()
            

    return maxVar




def contextize(fileName):

    utl.parse(fileName)

    while utl.hasNext():

        s = utl.nextStatement()


        # deals with Statement object only, no tokens 
        if not isinstance(s, Statement):

            raise utl.ContextException("unexpected token: "+str(s)+" (this should never occur)")


        if s.kind == "var_assign":

            contextizeVar(s)




        
