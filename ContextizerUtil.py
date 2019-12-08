import Parser as par

statmList = []

def parse(fileName):

    global statmList

    statmList = par.parse(fileName)

    iterate()



# Statement data structure iterator 

def iterate():

    for item in statmList:

        iterateRecursive(item)



def iterateRecursive(state):

    global nextStatement

    for item in state.subList:

        if isinstance(item, str):

            
