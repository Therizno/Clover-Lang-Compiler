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

def nextStatement():

    global curStatement, lastStatement

    if isinstance(curStatement, str):
 
        curStatement = lastStatement.nextNode() 

    else:

        lastStatement = curStatement
        curStatement = curStatement.nextNode()
    
    
    if curStatement == None and i < len(statmList): 

        curStatement = statmList[i]
        i += 1


    return curStatement



def hasNext():

    return i < len(statmList)



class ContextException(mtl.CompileException):

    def __init__(self, text):

        self.message = "Context Error: " + text 



