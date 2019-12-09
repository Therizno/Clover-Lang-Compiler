import Contextizer as cont
import ContextizerUtil as ctutl



def leafCompile(fileName):

    cont.contextize(fileName)
    ctutl.reset()

    

#test 
leafCompile("test/test_4.leaf")
