class NumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max_number(self):
        max = 0
        for number in self.numbers:
            if number > max:
                max = number
        return max
    
    def find_min_number(self):
        min = self.numbers[0]
        for number in self.numbers:
            if number < min:
                min = number
        return min
    
    def find_average(self):
        total = sum(self.numbers)
        average = total // len(self.numbers)
        return average
    
    def find_total(self):
        total = 0
        for number in self.numbers:
            total += number
        return total


class ExtentedNumberFinder(NumberFinder):
    def __init__(self, numbers):
        super().__init__(numbers)

    def is_in_list(self, number):
        is_in_list = False
        if number in self.numbers:
            is_in_list = True
        return is_in_list

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 51]
    finder = ExtentedNumberFinder(numbers)
    is_it = finder.is_in_list(30)
    print(f"in: {is_it}")
    


    