import Tokenizer as tkner
import TokenizerUtil as utl

while True:
    
    fileName = input("Input the file you want to compile: \n")

    try:
        tkner.tokenize(fileName)
        print("Success!")
        print(tkner.tokenList)
        
    except utl.TokenException as e:
        print("Error: "+e.message)

    

