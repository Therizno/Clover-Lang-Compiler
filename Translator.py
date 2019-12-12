import Contextizer as cont
import ContextizerUtil as ctutl
from Parser import Statement 

file = None


def leafCompile(fileName):

    global file

    cont.contextize(fileName)
    ctutl.reset()
    
    file = open(fileName[0:len(fileName)-5]+".c", "w+")

    file.write("int main() {\n")

    stringify()

    file.write("return 0;\n}")

    file.close()

    cont.reset()


def stringify():
    

    while ctutl.hasNext():

        s = ctutl.nextStatement()

        if isinstance(s, Statement) and s.kind == "var_assign":

            name = None

            while isinstance(s, str) or s.kind != "expression":

                if((not isinstance(s, str)) and s.kind == "identifier"):

                    s = ctutl.nextStatement()
                    file.write(s)
                    name = s

                elif isinstance(s, str):

                    # replace with translations table soon 
                    if s == "bool":

                        file.write("boolean")

                    file.write(s + " ")
                    

                s = ctutl.nextStatement()


            v = s       #v = an expression object

            while isinstance(s, str) or isinstance(s, Statement) and (s.parent == v or s == v):

                s = ctutl.nextStatement()

                if(isinstance(s, str)):

                    file.write(s)


            file.write(";\n")
            
            file.write('cout << "stored " << '+name+' << " in a variable";\n')

        
    



