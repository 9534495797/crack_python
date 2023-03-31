#perimeter of rectangle
class rectangle(object):
    def _init_(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
a=rectangle()

print(a.area())
