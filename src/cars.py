class Car:
    def __init__(self, make, model, year):
        """Initialize the car with make, model, and year."""
        self.make = make
        self.model = model
        self.year = year
    
    def set_make(self, make):
        """Set the car's make."""
        self.make = make

    def get_make(self):
        """Get the car's make."""
        return self.make
    
    def set_model(self, model):
        """Set the car's model."""
        self.model = model
    
    def get_model(self):
        """Get the car's model."""
        return self.model
    
    def set_year(self, year):
        """Set the car's year."""
        self.year = year
    
    def get_year(self):
        """Get the car's year."""
        return self.year
    
    def get_description(self):
        """Get a description of the car."""
        return f"Year: {self.year}, Make: {self.make}, Model {self.model}"
    
    def set_mileage(self, mileage):
        """Set the car's mileage."""
        self.mileage = mileage

    def get_mileage(self):
        """Get the car's mileage."""
        return self.mileage
    
    def set_color(self, color):
        """Set the car's color."""
        self.color = color
    
    def get_color(self):
        """Get the car's color."""
        return self.color
    
    def set_engine_type(self, engine_type):
        """Set the car's engine type."""
        if engine_type not in ['petrol', 'diesel', 'electric']:
            raise ValueError("Engine type must be 'petrol', 'diesel', or 'electric'.")
        self.engine_type = engine_type

    def get_engine_type(self):
        """Get the car's engine type."""
        return self.engine_type
    

