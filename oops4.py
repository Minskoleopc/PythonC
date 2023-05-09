


# Hierarchical interhitance

class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayName(self):
        print(self.firstName + self.lastName)
class Son(Mother):
    def __init__(self,fn,ln,sname):
        super().__init__(fn,ln)
        self.sname = sname

    def displaySname(self):
        print(self.sname + self.lastName)

class Daughter(Mother):
    def __init__(self,fn,ln,dname):
        super().__init__(fn,ln)
        self.dname = dname

    def displayDname(self):
        print(self.dname + self.lastName)

chinmay = Son("shirish","deshpande","chinmay")

print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.sname)
chinmay.displaySname()


gauri  = Daughter("kanchan","deshpande","gauri")
print(gauri.firstName)
print(gauri.lastName)
print(gauri.dname)
gauri.displayDname()


# program 5 (Method order resolution)

class A(object):
    def method(self):
        print("A class method called") # 3
        super().method()
class  B(object):
    def method(self):
        print("B class method called") # 5
        super().method()

class C(object):
    def method(self):
        print('C class method called')  #C


class X(A,B):
    def method(self):
        print('X class method called') # 2
        super().method()

class Y(B,C):
    def method(self):
        print('Y class method is called') # 4
        super().method()

class P(X,Y,C):
    def method(self):
        print('P class method is called') # 1
        super().method()

p = P()
p.method()

# single
# multi-level
# hierarchical
# multiple and hybrid
# parent method and parent constructor (super keyword)


# polymorphism
class Calculator:
        def addition(self,x,y):
            print(x+y)
        def addition(self , x, y, z):
            print(x+y+z)

        def addition(self,x,y,z,a):
            print(x+y+z+a)

c = Calculator()

c.addition(2,4,5,6)



# Polmorphism

# Duck typing

# Operator loading

#Method overload *

#Method overriding


# Monday,Wednesday ,Thursday Friday,Sunday










# multiple inheritance
