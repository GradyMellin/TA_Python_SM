
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def carFacts(self):
        facts = "\nMake: {}\nModel: {}\nColor: {}\nYear: {}\n".format(self.make,self.model,self.color,self.year)
        return facts

class Truck(Car):
    def __init__(self, make, model, year, color, bed_length, cab):
        super().__init__(make, model, year, color)
        self.bed_length = bed_length
        self.cab = cab

    def carFacts(self):
        facts = "\nMake: {}\nModel: {}\nColor: {}\nYear: {}\nBed Length: {}\nCab Type: {}\n".format(self.make,self.model,self.color,self.year,self.bed_length,self.cab)
        return facts

class Bus(Car):
    def __init__(self, make, model, year, color, length, capacity):
        super().__init__(make, model, year, color)
        self.length = length
        self.capacity = capacity
        
    def carFacts(self):
        facts = "\nMake: {}\nModel: {}\nColor: {}\nYear: {}\nLength: {}\nCapacity: {}\n".format(self.make,self.model,self.color,self.year,self.length,self.capacity)
        return facts
        


if __name__ == "__main__":

    car = Car('toyota','prius',2010,'silver')
    print(car.carFacts())

    truck = Truck('toyota','tacoma',2015,'grey','6 foot','access cab')
    print(truck.carFacts())

    bus = Bus('bluebird','all american',2013,'yellow','35 feet',90)
    print(bus.carFacts())
    
