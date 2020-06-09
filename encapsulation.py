#### Python ver: 3.8.3
##
#### Author: Grady Mellin
##
#### Purpose: to learn about encapsulation, private and protected methods


class Car:
    def __init__(self, make, model, year, color):
        self.__make = make
        self.__model = model
        self.__year = year
        self._color = color

    def carFacts(self):
        facts = "\nMake: {}\nModel: {}\nColor: {}\nYear: {}\n".format(self.__make,self.__model,self._color,self.__year)
        return facts

if __name__ == "__main__":
    myCar = Car('Toyota','Tacoma',2015,'Grey')
    print(myCar.carFacts())

