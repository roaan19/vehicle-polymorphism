class BMW:
    def fuel_type(self):
        print("BMW uses Petrol.")

    def max_speed(self):
        print("BMW's top speed is 250 km/h.")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Premium Petrol.")

    def max_speed(self):
        print("Ferrari's top speed is 340 km/h.")

# Polymorphism demonstration
def car_details(car):
    car.fuel_type()
    car.max_speed()

# Create objects of each class
bmw_car = BMW()
ferrari_car = Ferrari()

# Call the same function with different objects
print("BMW Details:")
car_details(bmw_car)

print("\nFerrari Details:")
car_details(ferrari_car)