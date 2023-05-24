class Driver:
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

    def drive(self, car):
        print(f"{self.name} is driving the car: {car.make} {car.model}")

    def request_test_drive(self, showroom, car):
        showroom.schedule_test_drive(car, self)

    def send_inquiry(self, showroom, message):
        showroom.send_inquiry(self, message)

    def purchase_car(self, showroom, car):
        showroom.sell_car(car, self)
