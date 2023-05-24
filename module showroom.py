class Showroom:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.make} {car.model} added to the showroom.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.make} {car.model} removed from the showroom.")
        else:
            print(f"{car.make} {car.model} not found in the showroom.")

    def schedule_test_drive(self, car, driver):
        print(f"Test drive scheduled for {car.make} {car.model} with driver: {driver.name}")

    def send_inquiry(self, driver, message):
        print(f"Inquiry sent to the showroom: {message}\nFrom: {driver.name}")

    def sell_car(self, car, buyer):
        if car.is_available and not car.is_sold:
            car.sell()
            print(f"The car {car.make} {car.model} sold to {buyer.name}.")
        else:
            print(f"The car {car.make} {car.model} is not available for sale.")
