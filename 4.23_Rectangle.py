"""
Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle.
"""

class Rect:

    def getData(self,len1,wid):
        self.len1=len1
        self.wid=wid

    def putData(self):
        print("Length of Rectangle : ",self.len1)
        print("Width of Rectangle : ",self.wid)

    def rect_Area(self):
        print("Area of Rectangle : ",self.len1*self.wid)
    
    

r1=Rect()


r1.getData(20,20)
r1.putData()
r1.rect_Area()
        
        
