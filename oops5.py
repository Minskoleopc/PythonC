# program 1
# overloading
# class Calculator:
#     def addition(self,x,y):
#         print(x+y)
#     def addition(self,x,y,z):
#         print(x+y+z)
#     def addition(self,x,y,z,a):
#         print(x+y+z+a)
#
# a = Calculator()
# a.addition(12,4,4,6)


# program 2
# class Calculator:
#     def addition(self,x = None,y = None ,z =None ,a =None):
#         if x != None and y != None and z != None and  a != None:
#             print(x+y+z+a)
#         elif x != None and y != None and z != None:
#             print(x+y+z)
#         elif x != None and y != None :
#             print(x+y)
#
# a = Calculator()
# a.addition(12,4)
# a.addition(12,4,34)
# a.addition(12,4,34,45)


# program 3


class Vehicle:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print('I am moving from vehicle class')

class Car(Vehicle):
    def move(self):
        print('I am moving from car')
class Boat(Vehicle):
    def move(self):
        print('I am moving from boat')
    def color(self):
        print('I am having white colot')


# different class , same method Name and different signature
audi = Car("audi","q4")

print(audi.brand)
print(audi.model)
audi.move()

boatA =  Boat('Aq','XL')
boatA.move()

# programming 4
class Bird:
    def fly(self):
        print('fly with wings')
class Airplane:
    def fly(self):
        print('fly with iron wings')

class Fish:
    def swim(self):
        print('I swim')


a = Fish()
if hasattr(a,'fly'):
    a.fly()
else:
    a.swim()


# Operator overloading

print(9+9)
print("chinmay"+"deshpande")

class A:
    def __init__(self,x):
        self.x = x
    def __add__(self, o):
        return self.x + o.x


a = A(3)
b = A(4)
print(a+b)

class X:
    def __init__(self,x):
        self.x = x

    def __gt__(self, other,o):
        if(self.x > other.x):
            return True
        else:
            return False


x1 = X(5)
x2 = X(7)

print(5 > 7)
print(x1 > x2)














