import Tokenizer as tkner
import TokenizerUtil as utl

while True:
    
    fileName = input("Input the file you want to compile: \n")

    try:
        tkner.tokenize(fileName)
        print("Success!")
    except utl.TokenException as e:
        print(e.message)

    

