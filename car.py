class Car:
    def __init__(self, make, model, fuel_type, year, price, colors):
        self.make = make
        self.model = model
        self.fuel_type = fuel_type
        self.year = year
        self.price = price
        self.colors = colors
        self.mileage = 0
        self.is_available = True
        self.is_sold = False
        self.features = []

    def display_info(self):
        print(f"Car: {self.make} {self.model} ({self.year})")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Price: ${self.price}")
        print(f"Available Colors: {', '.join(self.colors)}")

    def add_feature(self, feature):
        self.features.append(feature)

    def update_mileage(self, mileage):
        self.mileage += mileage

    def sell(self):
        self.is_available = False
        self.is_sold = True
