class Rectangle:
    def __init__(self, length = 1, width = 1):
        self.length = length 
        self.width = width
    
    def area(self):
        return self.length * self.width

R1 = Rectangle()
R2 = Rectangle(4)
R3 = Rectangle(4, 6)

print(R1.area())
print(R2.area())
print(R3.area())