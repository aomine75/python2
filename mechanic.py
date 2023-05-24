class Mechanic:
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

    def repair(self, car):
        print(f"{self.name} is repairing the car: {car.make} {car.model}")

    def perform_maintenance(self, car):
        car.update_mileage(10000)
        print(f"{self.name} performed maintenance on the car: {car.make} {car.model}")

    def schedule_service(self, showroom, car):
        showroom.schedule_service(car, self)

    def notify_ready_for_pickup(self, car):
        print(f"The car {car.make} {car.model} is ready for pickup.")
