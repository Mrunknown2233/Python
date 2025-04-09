class Circle:
    def __init__(self,radius):
        self._radius = radius
    
    @property
    def radius(self):
        print("Radius property is called")
        return self._radius

    @radius.setter
    def radius(self,value):
        print("Radius setter is called")
        if value>=0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")
    
    @radius.deleter
    def radius(self):
        print("Deleting radius")
        del self._radius

c = Circle(10)
print(c.radius)
c.radius = 20
print(c.radius)
del c.radius
# c.radius = -1
# print(c.radius)
# The above 2 lines will cause error on their own as assigining negative values to radius will raise ValueError (ref line 16)
#And after deleting the radius if we try to use it in any way like printing it will result in AttributeError
