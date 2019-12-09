import MainUtil as mtl
import Parser as par

from Parser import Statement

statmList = []

curStatement = None
lastStatement = None

# root Statement node
root = None

i = 0


def parse(fileName):

    global statmList, curStatement, root

    statmList = par.parse(fileName)

    # dummy statement node to hold statement list 
    curStatement = Statement("dummy")
    curStatement.subList = statmList

    root = curStatement 





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

        while curStatement.visited():

            curStatement = curStatement.parent 
    

    return curStatement




def hasNext():

    return curStatement != None 




def nextToken():

    s = nextStatement()

    while not isinstance(s, str):

        s = nextStatement()

    return s 



class ContextException(mtl.CompileException):

    def __init__(self, text):

        self.message = "Context Error: " + text 



