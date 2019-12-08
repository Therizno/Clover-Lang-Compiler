import Parser as par

statmList = []

curStatement = None

i = 0


def parse(fileName):

    global statmList

    statmList = par.parse(fileName)

    iterate()



# Statement data structure iterator 

def next():

    global curStatement

    if isinstance(curStatement, str):

        #assumes every token statement has a parent statement 
        curStatement = curStatement.parent.nextNode()

    else:
        
        curStatement = curStatement.nextNode()
    
    if curStatement == None and i < len(statmList): 

        curStatement = statmList[i]
        i += 1


    return curStatement



def hasNext():

    return i < len(statmList)



