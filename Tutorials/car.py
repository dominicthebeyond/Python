class Car:
    def __init__(self, brand):
        self.brand = brand

class Honda(Car):
    def __init__(self, model, year):
        super().__init__("Honda")  # inherits brand from parent class
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

# Example usage
my_car = Honda("Civic", 2022)
my_car.display_info()
