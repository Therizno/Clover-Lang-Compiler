
#basic compiler exception
class CompileException(Exception):

    def __init__(self, text):
        self.message = "Compile Error: " + text 
