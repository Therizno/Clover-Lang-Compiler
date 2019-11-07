import TokenizerUtil as utl
import MainUtil as mtl

keywords = mtl.keywords
symbols = mtl.symbols

#possible tokenList entries:
#("keyword", x)
#("identifier", x)
#("number", x)
#("string", x)
#("char", x)
#("symbol", x)
#"NEWLINE"

tokenList = []

line = 1



def tokenizeLine():

    #tokenize until end of line (or file)
    while not endOfLine():

        utl.popWhitespace()

        #recheck loop condition w/o whitespace
        if endOfLine():
            break


        #remove comments
        if utl.charsLeft() > 1 and utl.peek(2) == "//":

            utl.popUntil(lambda x : endOfLine())
            break

        elif utl.charsLeft() > 1 and utl.peek(2) == "/*":

            try:
                utl.popUntil(eraseMultiline)
            except IndexError:
                raise utl.TokenException("unclosed comment")
                
            utl.pop(2)
        

        #handle words
        elif utl.peek(1).isalpha():

            s = utl.popUntil(lambda x : x == " " or x in symbols or endOfLine())

            if s in keywords:

                tokenList.append(("keyword", s))

            else:

                tokenList.append(("identifier", s))

                
        #handle numbers
        elif utl.peek(1).isdigit():

            s = utl.popUntil(lambda x : x == " " or ((not x.isdigit()) and x != ".") or endOfLine())

            tokenList.append(("number", s))


        #handle strings
        elif utl.peek(1) == '"':

            utl.pop(1)
            
            try:
                s = utl.popUntil(lambda x : x == '"')
            except IndexError:
                raise utl.TokenException("unclosed string")
                
            utl.pop(1)

            tokenList.append(("string", s))


        #handle chars
        elif utl.peek(1) == "'":

            utl.pop(1)

            tokenList.append(("char", utl.pop(1)))

            if utl.pop(1) != "'":

                raise utl.TokenException("unclosed char") 
            

        #handle symbols
        elif utl.peek(1) in symbols:

            tokenList.append(("symbol", utl.pop(1)))


        #else the token is invalid, raise exception
        else:
            raise utl.TokenException(utl.peek(1) + " is not a valid token")
                

        
    if utl.peek(1) == "\n":

        utl.pop(1)

        


def endOfLine():

    return utl.peek(1) == "\n" or utl.peek(1) == "EOF"



def eraseMultiline(x):

    global line

    if x == "\n":

        tokenList.append("NEWLINE")
        line += 1

    return utl.peek(2) == "*/" 



def tokenize(fileName):

    global line

    utl.readFile(fileName)

    line = 1

    while utl.peek(1) != "EOF":

        try:
            tokenizeLine()
            
        except utl.TokenException as e:
            e.message += " at line " + str(line)
            raise e

        tokenList.append("NEWLINE")

        line += 1


    line -= 1     #avoids counting one too many lines

    return tokenList







