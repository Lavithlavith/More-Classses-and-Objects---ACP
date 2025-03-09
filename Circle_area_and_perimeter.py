class Circle:
    def _init_(self):
        self.radius = None

    def get_radius(self):
        try:
            self.radius = float(input("Enter the radius (numeric value): "))
        except ValueError:
            print("Error: The value entered is not numeric. Please enter a numeric value.")
            self.radius = None

    def area(self):
        if self.radius is not None:
            print("Area is:", 3.14 * self.radius ** 2)
        else:
            print("Cannot calculate area: radius is invalid.")

    def perimeter(self):
        if self.radius is not None:
            print("Perimeter is:", 2 * 3.14 * self.radius)
        else:
            print("Cannot calculate perimeter: radius is invalid.")


# Usage
circle = Circle()
circle.get_radius()
circle.area()
circle.perimeter()