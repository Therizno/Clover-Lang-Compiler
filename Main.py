import Translator as compl
import MainUtil as mtl

while True:
    
    fileName = input("Input the file you want to compile: \n")

    if fileName[-5:] != ".leaf":

        print("Error: must be a .leaf file")

    else:
        try:
            compl.leafCompile(fileName)

            for item in mtl.compilerWarnings:
                print("Compiler Warning: "+item)
            
            print("Success!")
        
        except mtl.CompileException as e:
            print("Error: "+e.message)



