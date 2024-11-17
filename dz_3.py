#ex_1
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def abs(self):
        print((self.x**2+self.y**2+self.z**2)**0.5)
    def add(self,other):
        v=(Vector(self.x+other.x,self.y+other.y,self.z+other.z))
        print(v.x,v.y,v.z)
    def sub(self,other):
        v=Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        print(v.x,v.y,v.z)
    def dot(self,other):
        print(self.x*other.x+self.y*other.y+self.z*other.z)

    def mult(self,other):
        v=Vector(self.x*other,self.y*other,self.z*other)
        print(v.x,v.y,v.z)

#tests
v1=Vector(1,1,1)
v2=Vector(2,2,2)
v1.abs(),v2.abs()
v1.add(v2)
v1.sub(v2),v2.sub(v1)
v1.dot(v2)
v1.mult(37)



