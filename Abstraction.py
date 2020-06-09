#### Python ver: 3.8.3
##
#### Author: Grady Mellin
##
#### Purpose: to learn about encapsulation, private and protected methods

from abc import ABC, abstractmethod

class Beverage(ABC):
    def __init__(self,amount_oz):
        self.amount_oz = amount_oz

    def size(self):
        szMsg = "You have a {}oz beverage".format(self.amount_oz)
        return szMsg

    @abstractmethod
    def goodFor(self):
        pass

class Coffee(Beverage):
    def __init__(self,amount_oz):
        super().__init__(amount_oz)

    def goodFor(self):
        goodForMsg = "Coffee is good for giving you a nice little boost of energy from the caffine!"
        return goodForMsg

if __name__ == "__main__":

    myCoffee = Coffee(12)
    print(myCoffee.size())
    print(myCoffee.goodFor())
    

    
    
    
