
#keywords
types = {"int", "float", "double", "char", "bool"}
special_values = {"null", "true", "false"}
control_statements = {"while", "for", "if", "else"}

keywords = types | special_values | control_statements | {"static", "member", "function", "method", "mod"}


#operators
operators = {"==", ">", "<", "+", "-", "*", "/", "^", "%", "&", "|", "!", "~"}


#symbols
brackets = {"[", "]", "{", "}", "(", ")"}

symbols = brackets | {",", ".", "="} 



#basic compiling exception
class CompileException(Exception):

    def __init__(self, text):
        self.message = "Compile Error: " + text 
