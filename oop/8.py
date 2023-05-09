

class String:
    
    def __init__(self, string):
        self.string = string
        
    def __add__(self, other):
        return String(self.string + other.string)
    
    def toLower(self):
        return String(self.string.lower())
    
    def toUpper(self):
        return String(self.string.upper())
        
a = String("HELLO")
b = String("WORLD")

print(a + b)
print(a.toLower())
print(a.toUpper())