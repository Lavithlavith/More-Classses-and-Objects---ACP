class Circle():
    def __init__(self):
        self.circle = ""
    
    def get_string(self):
        try :
            self.circle = float(input("Enter Radius in number:"))
        except Exception as e:
            print(" The value entered is not a numeric value..please enter numeric value",e)
            return 
    
    def area(self):
        print("Result in area is: ",self.circle * 3.14)

    def perimeter(self):
        print("Result in perimeter is: ",self.circle * (2*3.14))

str1 = Circle()

str1.get_string()
str1.area()
str1.perimeter()