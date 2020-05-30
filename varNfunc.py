#
# Python:  3.8.3
#
# Author: Grady Mellin
#
# Purpose: Learning and practicing some python skills
#
#


def start():
    fName = "Sarah"
    lName = "Connor"
    age = 28
    gender = "female"
    getInfo(fName,lName,age,gender)

def getInfo(fName,lName,age,gender):
       print("My name is {0} {1}. I am a {2} year old {3}.".format(fName,lName,age,gender))


def getNumber():
    number = 12
    return number

def getName():
    name = input("What is your name? ")
    return name








if __name__ == "__main__":
    start()
