#Q1
#1.1
class Vehicle():
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
a = Vehicle(120, 18)
print(a.max_speed, a.mileage)

#1.2
class Vehicle():
    pass

#Q2
#2.1
class Vehicle():
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

bus = Bus('School Volvo', 120, 18)
print('Vehicle name: ',bus.name, 'Speed: ',bus.max_speed, 'Mileage: ',bus.mileage)

#2.2
class Vehicle():
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity=4):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


bus = Bus('School Volvo', 120, 18)
print(bus.seating_capacity())  

#Q3
#3.1
class Vehicle():
    def __init__(self, name, max_speed, mileage, color=None):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = 'White'

    def display_info(self):
        print(f"Vehicle Name: {self.color+ ' ' +self.name}")
        #print(f"Color: {self.color}")
        print(f"Max Speed: {self.max_speed}")
        print(f"Mileage: {self.mileage}")


class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


a = Bus('School Volvo', 120, 12)
b = Car('Audi Q8', 240, 18)

a.display_info()
b.display_info()

#3.2
class Vehicle():
    def __init__(self, name, capacity, mileage, color=None):
        self.name = name
        self.capacity = capacity
        self.mileage = mileage
        
    def fare(self):
        return self.capacity * 100
    
class Bus(Vehicle):
    def fare(self):
        return super().fare() * 1.1
    pass

School_bus = Bus('School Volvo', 50, 12)
print("Total Bus fare is: ", School_bus.fare())

#Q4
#4.1
class Vehicle():
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

bus = Bus('School Volvo', 120, 18)
print(type(bus))
#4.2
print(isinstance(bus, Vehicle))