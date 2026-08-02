class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True

    def check_availability(self):
        return self.available

    def display_info(self):
        return f"{self.brand} {self.model} - ${self.price}"

    def sell(self):
        if self.available:
            self.available = False
            print(f"The vehicle '{self.brand} {self.model}' has been sold.")
        else:
            print(f"The vehicle '{self.brand} {self.model}' is not available.")

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def stop_engine(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def start_engine(self):
        if not self.available:
            print(f"The car '{self.brand} {self.model}' is not available to start the engine.")
        else:
            print(f"The engine of the car '{self.brand} {self.model}' has started.")


    def stop_engine(self):
        if self.available:
            return print(f"The car '{self.brand} {self.model}' is not available to stop the engine.")
        else:
            print(f"The engine of the car '{self.brand} {self.model}' has stopped.")

class Bike(Vehicle):
    def start_engine(self):
        if not self.available:
            print(f"The bike '{self.brand} {self.model}' is not available")
        else:
            print(f"The bike '{self.brand} {self.model}' has started.")

    def stop_engine(self):
        if self.available:
            return print(f"The bike '{self.brand} {self.model}' is not available")
        else:
            print(f"The bike '{self.brand} {self.model}' has stopped.")

class Truck(Vehicle):
    def start_engine(self):
        if not self.available:
            print(f"The truck '{self.brand} {self.model}' is not available")
        else:
            print(f"The truck '{self.brand} {self.model}' has started.")

    def stop_engine(self):
        if self.available:
            return print(f"The truck '{self.brand} {self.model}' is not available")
        else:
            print(f"The truck '{self.brand} {self.model}' has stopped.")

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def purchase_vehicle(self, vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"{self.name} cannot purchase '{vehicle.brand} {vehicle.model}' because it is not available.")

    def inquire_vehicle(self, vehicle):
        if vehicle.check_availability():
            print(f"The vehicle '{vehicle.brand} {vehicle.model}' is available for ${vehicle.get_price()}.")
        else:
            print(f"The vehicle '{vehicle.brand} {vehicle.model}' is not available.")

class Dealership:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
        print(f"The vehicle '{vehicle.brand} {vehicle.model}' has been added to the dealership '{self.name}'.")

    def sell_vehicle(self, vehicle: Vehicle, customer: Customer):
        if vehicle in self.vehicles and customer in self.customers:
            customer.purchase_vehicle(vehicle)
        else:
            print(f"Either the vehicle '{vehicle.brand} {vehicle.model}' or the customer '{customer.name}' is not registered in the dealership '{self.name}'.")

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"The customer '{customer.name}' has been added to the dealership '{self.name}'.")

    def show_available_vehicles(self):
        available_vehicles = [vehicle for vehicle in self.vehicles if vehicle.check_availability()]
        if available_vehicles:
            print(f"Available vehicles in the dealership '{self.name}':")
            for vehicle in available_vehicles:
                print(f"- {vehicle.display_info()}")
        else:
            print(f"No available vehicles in the dealership '{self.name}'.")

# Instance of Dealership
dealership = Dealership("AutoWorld")

# Adding vehicles to the dealership
car1 = Car("Toyota", "Camry", 25000)
bike1 = Bike("Yamaha", "R15", 15000)
truck1 = Truck("Ford", "F-150", 30000)
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)

# Adding customers to the dealership
customer1 = Customer("Mario")
customer2 = Customer("Adriana")
dealership.add_customer(customer1)
dealership.add_customer(customer2)

# Show available vehicles
dealership.show_available_vehicles()

# Customer inquiries about vehicles
customer1.inquire_vehicle(car1)
customer2.inquire_vehicle(bike1)

# Customers purchasing vehicles
customer1.purchase_vehicle(car1)
customer2.purchase_vehicle(bike1)

# Show available vehicles after purchases
dealership.show_available_vehicles()

            