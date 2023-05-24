from car import Car
from driver import Driver
from mechanic import Mechanic
from showroom import Showroom

if __name__ == '__main__':
    
    car = Car('Tesla', 'Model 3', 'Electric', 2021, 50000, ['Red', 'White', 'Black'])
    driver = Driver('John Doe', 35, 'Male', 'john@example.com')
    mechanic = Mechanic('Jane Smith', 45, 'Female', 'jane@example.com')
    showroom = Showroom('Car Showroom', '123 Main Street', 'Los Angeles')

    
    car.display_info()
    driver.drive(car)
    mechanic.repair(car)
    showroom.add_car(car)
