import Tokenizer as tkner
import TokenizerUtil as utl

while True:
    
    fileName = input("Input the file you want to compile: \n")

    if fileName[-5:] != ".leaf":

        print("Error: must be a .leaf file")

    else:
        try:
            tkner.tokenize(fileName)
            print("Success! " + str(tkner.line) + " lines compiled")
            print(tkner.tokenList)
        
        except utl.TokenException as e:
            print("Error: "+e.message)

        tkner.tokenList.clear()

