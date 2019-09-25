import TokenizerUtil as utl

keywords = ["static"]
symbols = ["="]

#possible tokenList entries:
#("keyword", x)
#("identifier", x)
#("number", x)
#("string", x)
#("symbol", x)
#"NEWLINE"

tokenList = []



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

            utl.popUntil(lambda x : utl.peek(2) == "*/")
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

            s = utl.popUntil(lambda x : x == " " or x in symbols or endOfLine())

            tokenList.append(("number", s))


        #handle strings
        elif utl.peek(1) == '"':

            utl.pop(1)
            s = utl.popUntil(lambda x : x == '"')
            utl.pop(1)

            tokenList.append(("string", s))
            

        #handle symbols
        elif utl.peek(1) in symbols:

            s = utl.popUntil(lambda x : x not in symbols)

            tokenList.append(("symbol", s))


        #else the token is invalid, raise exception
        else:
            raise utl.InvalidToken(utl.peek(1))
                

        
    if utl.peek(1) == "\n":

        utl.pop(1)

        


def endOfLine():

    return utl.peek(1) == "\n" or utl.peek(1) == "EOF"


def tokenize():

    while utl.peek(1) != "EOF":

        try:
            tokenizeLine()
            
        except utl.InvalidToken as e:
            print(e.message)
            break

        tokenList.append("NEWLINE")




#test
utl.readFile("test_1")

tokenize()

print(tokenList)



