class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

# ------------using classes---------------

v1 = Vector(4, 8)
v2 = Vector(2,5)

v3 = v1 + v2
v4 = v1 * v2

print("1st  ", v1)
print("2nd  ", v2)
print("3rd  ", v3)
print("4th  ", v4)