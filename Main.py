import Tokenizer as tkner
import MainUtil as mtl

while True:
    
    fileName = input("Input the file you want to compile: \n")

    if fileName[-5:] != ".leaf":

        print("Error: must be a .leaf file")

    else:
        try:
            tokens = tkner.tokenize(fileName)
            print("Success! " + str(tkner.line) + " lines compiled")
            print(tokens)
        
        except mtl.CompileException as e:
            print("Error: "+e.message)

        tkner.tokenList.clear()

