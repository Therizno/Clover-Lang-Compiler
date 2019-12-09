import MainUtil as mtl
import ContextizerUtil as ctutl

from Parser import Statement
from Tokenizer import TokenEntry


#key: var name, value: var type
varTable = {} 



def contextizeVar(varStatement):

    if ctutl.nextStatement().kind == "keyword": 

        typ = ctutl.nextToken()
        name = ctutl.nextToken()

        if name in varTable:

            raise ContextException(name + " declared twice")

        varTable[name] = typ 

        ctutl.nextToken()     #skip the "="
        ctutl.nextStatement() #skip to expression statement 

        expType = contextizeExpression(ctutl.nextStatement()) 

        if mtl.typeRank(expType) > mtl.typeRank(typ):

            mtl.compilerWarnings.append("possible loss of information when initializing "+name)

    else:

        name = ctutl.nextToken()

        ctutl.nextToken()     #skip the "=" 
        ctutl.nextStatement() #skip to expression statement 

        expType = contextizeExpression(ctutl.nextStatement())

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

            
    st = ctutl.nextStatement()

    while isinstance(st, str) or isinstance(st, Statement) and (st.parent == expStatement or st == expStatement): 

        if not isinstance(st, str):
        
            if st.kind == "number":

                if "." in ctutl.nextToken():

                    newMax("float")

                else:

                    newMax("int")

            elif st.kind == "keyword":

                #add "null" case later (when objects are implemented)

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


        
        #if isinstance(st, Statement):
            #print(st.kind)

        #else:
            #print(st)


        st = ctutl.nextStatement()
            
        
        
    #print(str(st.kind) + " " +str(st.parent))
    #print(expStatement.subList)
    #print("expression value: "+str(maxVar))
    return maxVar




def contextize(fileName):

    ctutl.parse(fileName)

    while ctutl.hasNext():

        s = ctutl.nextStatement()


        # deals with Statement object only, no tokens 
        if not isinstance(s, Statement):

            raise ctutl.ContextException("unexpected token: "+str(s)+" (this should never occur)")


        if s.kind == "var_assign":

            contextizeVar(s)




# test

contextize("test/test_4.leaf")
from Parser import printStatements
printStatements(ctutl.root)
        
