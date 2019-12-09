import MainUtil as mtl
import Parser as par


statmList = []

curStatement = None
lastStatement = None

# root Statement node
root = None

i = 0


def parse(fileName):

    global curStatement, root

    curStatement = par.parse(fileName)
    root = curStatement 





# Statement data structure iterator


def nextStatement(): 

    global curStatement, lastStatement, i

    if isinstance(curStatement, str):
 
        curStatement = lastStatement.nextNode() 

    else:

        lastStatement = curStatement
        curStatement = curStatement.nextNode()

    #skip visited parents
    if isinstance(curStatement, par.Statement):

        while hasNext() and curStatement.visited():

            curStatement = curStatement.parent 
    

    return curStatement




def hasNext():

    return curStatement != None 




def nextToken():

    s = nextStatement()

    while not isinstance(s, str):

        s = nextStatement()

    return s



def reset():

    resetRecursive(root)


def resetRecursive(s):

    if isinstance(s, par.Statement):

        s.i = 0

        for item in s.subList:

            resetRecursive(item)

            


class ContextException(mtl.CompileException):

    def __init__(self, text):

        self.message = "Context Error: " + text 



