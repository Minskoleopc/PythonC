# inbuild data
# string tuple set dictionary list
# methods
#
# program

class Person:
    # property
    fullName = None
    age = None
    adharNo = None

    # methods
    def displayName(self):
        print(self.fullName)

    def calB(self):
        print(2023 - self.age)

chinmay = Person()
#print(chinmay.fullName)

chinmay.fullName = 'chinmay'
chinmay.age = 32
chinmay.adharNo = 123

chinmay.displayName()
chinmay.calB()

 #program 2
class PersonB:
    def __init__(self,fn,age,adNo):
         self.fullName = fn
         self.age = age
         self.adhaNo =  adNo

    def  displayFullName(self):
        print(self.fullName)

    def calB(self):
        print(2023- self.age)

amol = PersonB("amol rao",23,123)
chinmay = PersonB("chinmay D",34,678)

amol.displayFullName()
amol.calB()
chinmay.displayFullName()
chinmay.calB()

class Vehicle:
    def __init__(self,color,type):
        self.color = color
        self.type = type
    def displayColor(self):
        print(self.color)
    def displayType(self):
        print(self.type)

audi = Vehicle("red","SUV")
bmw = Vehicle("black","sedane")
print(audi.color)
print(audi.type)

audi.displayType()
audi.displayColor()

print(bmw.color)
print(bmw.type)

bmw.displayType()
bmw.displayColor()


# Oops concept

 #inheritance

# polmorphism

# Encapsulation

# abstractio



































