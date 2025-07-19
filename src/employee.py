class Employee:
    """
    A class representing an employee with basic attributes and methods.
    """
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def get_full_name(self):
        """Return the full name of the employee."""
        fullname = f"{self.firstname} {self.lastname}"
        return fullname
    
    def set_address(self, address):
        """Set the address of the employee."""
        self.address = address
        
    def get_address(self):
        """Return the address of the employee."""
        return self.address
    
    def set_age(self, age):
        """Set the age of the employee."""
        self.age = age
    
    def get_age(self):
        """Return the age of the employee."""
        return self.age
    
    def set_department(self, department):
        """Set the department of the employee. """
        self.department = department

    def get_department(self):
        """Return the department of the employee."""
        return self.department
    

class ExtendedEmployee(Employee):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.firstname = firstname
        self.lastname = lastname
    
    def set_salary(self, salary):
        self.salary = salary
    
    def _get_salary(self):
        return self.salary



if __name__ == "__main__":
    emp = ExtendedEmployee("Neil", "Armstrong")
    emp.set_salary(50000)
    print(emp._get_salary())