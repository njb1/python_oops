from pytest import mark


class Student:
    def __init__(self, first_name, last_name):
        """Initialize the student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
    
    def set_name(self, first_name, last_name):
        """Set the student's first and last name."""
        self.first_name = first_name
        self.last_name = last_name
    
    def get_name(self):
        """Get the student's full name."""
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        """Return the full name of the student."""
        full_name = self.get_name()
        return full_name
    
    def set_address(self, address):
        """Set the student's address."""
        self.address = address

    def get_address(self):
        """Get the student's address."""
        return self.address
    
    def set_age(self, age):
        """Set the student's age."""
        self.age = age
    
    def get_age(self):
        """Get the student's age."""
        return self.age


class StudentCalculator(Student):
    """Class for student calculator."""
    def __init__(self, first_name, last_name, marks=[]):
        """Initialize the student calculator with first name and last name."""
        super().__init__(first_name, last_name)  
        self.marks = marks
    
    def calculate_average(self):
        """Calculate the average of the student's grades."""
        self.total = sum(self.marks)
        self.count = len(self.marks)
        self.average = self.total // self.count
        return self.average
    
    def get_grade(self):
        """Get the letter grade based on the average score."""
        if self.average >= 90:
            return 'A'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'
        
