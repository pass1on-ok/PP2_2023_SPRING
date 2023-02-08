class SM:
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input()
        print(self.string)
    def printString(self):
        print(self.string.upper())

obj = SM()
obj.getString()
obj.printString()
