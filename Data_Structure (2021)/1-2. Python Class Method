# Magic Method
def add(self, other):
    return Point(self.x + other.x, self.y + other.y)
p = Point(1, 2)
q = Point(3, 4)
r = p.add(q)
print(r)    # r = (4, 6)

# Operator Overloading
def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)
r = p + q
print(r)     # r = (4, 6)

# Operator Overloading to Point Class.
def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)
    
    # Self, Other type 달라도 가능
    def __rmul__(self, other):
    return Point(self.x * other, self.y * other)
