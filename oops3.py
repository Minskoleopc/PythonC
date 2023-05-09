



# class Vechicle:
#     def __init__(self,color , type):
#         self.color = color
#         self.type = type
#
#     def start(self):
#         print('vehicle start')
#
#     def stop(self):
#         print('vehicle stop')
#
#
# audi = Vechicle('red','sedane')
# print(audi.color)
# print(audi.type)
#
# audi.start()
# audi.stop()


# setting the values using get and set method
class Vehicle2 :
    def setColor(self,color):
       self.color = color

    def setType(self,type):
        self.type = type

    def getColor(self):
        return self.color
    def getType(self):
        return self.type

bmw = Vehicle2()
bmw.setColor("red")
bmw.setType("sedane")

print(bmw.getType())
print(bmw.getColor())


# Inheritance

# class Student:
#     firstName = "chinmay"
#     lastName = "deshpande"
#
#     def displayName(self):
#         print(self.firstName+self.lastName)
#
# class Teacher(Student):
#     salary = 1000
#
#
# amit = Teacher()
# print(amit.salary)
# print(amit.firstName)
# print(amit.lastName)
#amit.displayName()


# class Student:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
# class Teacher(Student):
#     salary = 10000
#
# amol = Teacher("chinmay","deshpande")


class Student:

    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def display(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self,firstName,lastName,salary):
        super().__init__(firstName,lastName)
        self.salary = salary
    def displaySalary(self):
        print(self.salary)

aman = Teacher("aman","sharma",1000)
aman.display()
aman.displaySalary()

class GrandFather:

    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayName(self):
        print(self.firstName+ self.lastName)

class Father(GrandFather):
    def __init__(self,firstName,lastName,fname):
        super().__init__(firstName,lastName)
        self.fname = fname

    def displayFather(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self,firstName,lastName,fname,sname):
        super().__init__(firstName,lastName,fname)
        self.sname = sname

    def displaySonName(self):
        print(self.sname + self.lastName)

chinmay = Son("manohar","deshpande","shirish","chinmay")

# chinmay.fname
# chinmay.firstName
# chinmay.lastName
# chinmay.sname

chinmay.displayName()
chinmay.displaySonName()
chinmay.displayFather()


















