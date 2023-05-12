

# abstraction

# we cannot create the object of abstract class

# what is abstract class ,
# any class with method definition  , not implemtayion will be considered as abdtract class

from abc import ABC , abstractmethod
class Human(ABC):
    @abstractmethod
    def displaycity(self):
        pass

    def displayState(self):
        print('MH')

    def displayCountry(self):
        print('India')

    def nationalLanguage(self):
        print('Hindi')

class Student(Human):

    def displaycity(self):
        print('pune')


amol = Student()
amol.displaycity()
amol.displayState()
amol.nationalLanguage()
amol.displayCountry()




class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

class HumanB(Animal):
    def move(self):
        print('I can walk and run')

    def ageLife(self):
        print('100 years')

class Snake(Animal):

    def move(self):
        print('I can crawl')

class Dog(Animal):

    def move(self):
        print('I can bark')

amit = HumanB()
amit.move()
amit.ageLife()



