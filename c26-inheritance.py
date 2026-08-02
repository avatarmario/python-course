class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def display_info(self):
        return f"{self.brand} {self.model} - ${self.price}"

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"The car '{self.brand} {self.model}' has been sold.")
        else:
            print(f"The car '{self.brand} {self.model}' is not available.")

    def check_availability(self):
        return self.is_available

    def get_price(self):
        return self.price

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_cars = []

    def purchase_car(self, car):
        if car.check_availability():
            car.sell()
            self.purchased_cars.append(car)
        else:
            print(f"{self.name} cannot purchase '{car.brand} {car.model}' because it is not available.")

    def inquire_car(self, car):
        if car.check_availability():
            print(f"The car '{car.brand} {car.model}' is available for ${car.get_price()}.")
        else:
            print(f"The car '{car.brand} {car.model}' is not available.")

class DealerShip:
    def __init__(self, name):
        self.name = name
        self.cars = []
        self.customers = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"The car '{car.brand} {car.model}' has been added to the dealership '{self.name}'.")

    def sell_car(self, car, customer):
        if car in self.cars and customer in self.customers:
            customer.purchase_car(car)
        else:
            print(f"Either the car '{car.brand} {car.model}' or the customer '{customer.name}' is not registered in the dealership '{self.name}'.")

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"The customer '{customer.name}' has been added to the dealership '{self.name}'.")

    def show_available_cars(self):
        available_cars = [car for car in self.cars if car.check_availability()]
        if available_cars:
            print(f"Available cars in the dealership '{self.name}':")
            for car in available_cars:
                print(f"- {car.display_info()}")
        else:
            print(f"No cars are currently available in the dealership '{self.name}'.")

# Create Instances of Cars, Customers, and Dealership
car1 = Car("Toyota", "Corolla", 20000)
car2 = Car("Honda", "Civic", 22000)
car3 = Car("Ford", "Focus", 21000)

customer1 = Customer("Mario")
customer2 = Customer("Adriana")

dealership = DealerShip("Super Cars")
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)
dealership.add_customer(customer1)
dealership.add_customer(customer2)

# Show available cars in the dealership
dealership.show_available_cars()

# Mario purchases the Toyota Corolla
dealership.sell_car(car1, customer1)

# Show available cars after the purchase
dealership.show_available_cars()

# Adriana purchases the Honda Civic
dealership.sell_car(car2, customer2)

# Show available cars after the second purchase
dealership.show_available_cars()

# Mario attempts to purchase the Ford Focus
dealership.sell_car(car2, customer1)

# Show available cars after the third purchase attempt
dealership.show_available_cars()