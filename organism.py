
# parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None  
    arms = None
    dna = "sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrgin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

#child class
class Human(Organism):
    name = "Billy"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth"

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paperclip, chewing gum, and a roll of duct tape!"
        return msg

#another child class
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "sequence B"
    origin = "Earth"

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
        return msg

#another child class instence
class Bacterium(Organism):
    name = "Joe"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "sequence C"
    origin = "Mars"

    def replication(self):
        msg = "\nThe cells began to divide and multiply into two seperate organisms!"
        return msg




if __name__ == "__main__":

    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())













    
