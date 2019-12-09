
compilerWarnings = [] 

#keywords
types = ("bool", "char", "int", "float", "double")      #don't change this order unless you have a really good reason
special_values = {"null", "true", "false"}
control_statements = {"while", "for", "if", "else"}

keywords = set(types) | special_values | control_statements | {"static", "member", "function", "method", "mod"}

#operators
operators = {"==", ">", "<", "+", "-", "*", "/", "^", "%", "&", "|", "!", "~"}


#symbols
brackets = {"[", "]", "{", "}", "(", ")"}

symbols = brackets | {",", ".", "="} 



#returns the rank of the type represented by the string s,
#ordered by smallest to largest memory footprint 
def typeRank(s):

    return types.index(s)



#basic compiling exception
class CompileException(Exception):

    def __init__(self, text):
        self.message = "Compile Error: " + text 
