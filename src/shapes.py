class Shapes:
    """Base class for shapes."""
    def __init__(self, val1=0, val2=0, val3=0):
        """Initialize the shape with dimensions."""
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3

    def set_dimensions(self, val1, val2):
        """Set the dimensions of the shape."""
        self.val1 = val1
        self.val2 = val2

    def get_dimensions(self):
        """Get the dimensions of the shape."""
        return self.val1, self.val2

class Rectangle(Shapes):
    """Class for rectangle shape."""
    def __init__(self, val1=0, val2=0):
        """Initialize the rectangle with width and height."""
        super().__init__(val1, val2)

    def area(self):
        """Calculate the area of the rectangle."""
        area = self.val1 * self.val2
        return area
    
    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        perimeter = 2 * (self.val1 + self.val2)
        return perimeter
    
class Circle(Shapes):
    """Class for circle shape."""
    def __init__(self, radius=0):
        """Initialize the circle with radius."""
        super().__init__(radius)
        self.radius = radius
        self.pi = 3.14159
    
    def area(self):
        """Calculate the area of the circle."""
        area = self.pi * (self.radius ** 2)
        return area
    
    def circumference(self):
        """Calculate the circumference of the circle."""
        circumference = 2 * self.pi * self.radius
        return circumference