
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def printCarFacts(self):
        print(self.color, self.make, self.model, self.year, self.color)

class Truck(Car):
    def __init__(self, make, model, year, color, bed_length, cab):
        super().__init__(make, model, year, color)
        self.bed_length = bed_length
        self.cab = cab


class Bus(Car):
    def __init__(self, make, model, year, color, length, capacity):
        super().__init__(make, model, year, color)
        self.length = length
        self.capacity = capacity
