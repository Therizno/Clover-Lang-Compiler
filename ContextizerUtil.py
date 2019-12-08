import MainUtil as mtl
import Parser as par

statmList = []

curStatement = None
lastStatement = None 

i = 0


def parse(fileName):

    global statmList

    statmList = par.parse(fileName)

    iterate()



# Statement data structure iterator


def nextStatement():        #never visits the same statement twice

    global curStatement, lastStatement, i 

    if isinstance(curStatement, str):
 
        curStatement = lastStatement.nextNode() 

    else:

        lastStatement = curStatement
        curStatement = curStatement.nextNode()

    #skip visited parents
    if isinstance(curStatement, Statement):

        while curStatement != None and curStatement.visited():

            curStatement = curStatement.parent 
    
    
    
    if curStatement == None and i < len(statmList): 

        curStatement = statmList[i]
        i += 1


    return curStatement



def hasNext():

    return i < len(statmList)



def nextToken():

    s = nextStatement()

    while not isinstance(s, str):

        s = nextStatement()

    return s 



class ContextException(mtl.CompileException):

    def __init__(self, text):

        self.message = "Context Error: " + text 



