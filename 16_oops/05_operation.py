class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,p):
        return Point(self.x+p.x,self.y+p.y)

    def print_point(self):
        return print(f"X is {self.x} and y is {self.y}")
    def __add__(self, p):
        return Point(self.x+p.x,self.y+p.y)
    
p1=Point(3,2)
p2=Point(4,3)

print(p1.x)
print(p1.y)

p=p1+p2
p.print_point()