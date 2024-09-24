class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
input_rectangle = Rectangle(width, height)
print(f"Area of rectangle: {input_rectangle.area()}")
print(f"Perimeter of rectangle: {input_rectangle.perimeter()}")
