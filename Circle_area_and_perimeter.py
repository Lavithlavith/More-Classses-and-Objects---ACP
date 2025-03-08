class Circle():
    def __init__(self):
        self.circle = ""
    
    def get_string(self):
        self.circle = int(input("Enter Radius in number:"))
    
    def area(self):
        print("Result in area is: ",self.circle * 3.14)

    def perimeter(self):
        print("Result in perimeter is: ",self.circle * (2*3.14))

str1 = Circle()

str1.get_string()
str1.area()
str1.perimeter()