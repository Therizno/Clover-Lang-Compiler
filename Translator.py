import Contextizer as cont
import ContextizerUtil as ctutl
from Parser import Statement 

file = None


def leafCompile(fileName):

    global file

    cont.contextize(fileName)
    ctutl.reset()
    
    file = open(fileName[0:len(fileName)-5]+".c", "w+")

    file.write("int main() {")

    stringify()

    file.write("}")


def stringify():

    while ctutl.hasNext():

        s = nextStatement()

        if isinstance(s, Statement) and s.kind == "var_assign":

            v = s

            file.write(nextToken())     # write type of var
            
            name = nextToken()
            file.write(name)

            while isinstance(s, str) or isinstance(s, Statement) and (s.parent == v or s == v):

                s = nextStatement()

                if(isinstance(s, str)):

                    file.write(s)


            file.write(";")
            
            file.write("cout << "+ name + ' << " assigned a value";')

        
    

#test 
leafCompile("test/test_4.leaf")
