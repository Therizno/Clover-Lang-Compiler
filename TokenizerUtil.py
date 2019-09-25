
#get the raw code
rawInput = []

def readFile(fileName):

    rawInput.clear()
    
    file = open(fileName + ".leaf", "r")

    for line in file:

        for char in line:
            
            rawInput.append(char)

    rawInput.append("EOF")





#utility functions

def charsLeft():

    return len(rawInput)


#peek the first x elements 
def peek(x):

    s = ""

    for i in range(0, x):

        s += rawInput[i]

    return s

        


def peekUntil(stop):

    s = ""
    i = 0

    while not stop(rawInput[i]):

        s += rawInput[i]
        i += 1
        
    return s



#pop x elements from raw input
def pop(x):

    s = ""

    for i in range(0, x):

        s += rawInput.pop(0)

    return s



def popUntil(stop):

    s = ""

    while not stop(rawInput[0]):

        s += rawInput.pop(0)

    return s


def popWhitespace():

    return popUntil(lambda x : x != " ")


#exceptions

class InvalidToken(Exception):

    def __init__(self, token):
        self.message = token + " is not a valid token"



