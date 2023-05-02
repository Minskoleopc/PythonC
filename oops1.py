# type
# Human
# Properties - age , weight  , height , gender , color
# Methods - walk() ,talk() , sleep()

class Human:
    fullName = None
    age = None
    city = None

    def displayFullName(self):
        print(self.fullName)


ravi = Human()
print(ravi.fullName)
print(ravi.age)
print(ravi.city)

ravi.fullName  = "ravi mehra"
ravi.age = 19
ravi.city = "pune"
print(ravi.fullName)
print(ravi.age)
print(ravi.city)
ravi.displayFullName()



# Class with constructor
# Class fields values to be set at the time of object creation

class HumanB :
    def __init__(self,fn,age,city):
        self.fullName = fn
        self.age = age
        self.city = city

    def displayFullName(self):
        print(self.fullName)

amolB = HumanB("amol rao",35,"pune")
chinmayB = HumanB("chinmay deshpabde",22,"nagpur")
amolB.displayFullName()



















