

# tuple

# tuples are ordered , unchangeble , allow duplicate

fruitsL = ["apple","mango","grapes","pineapple"]
print(type(fruitsL)) # list
fruitsL[0] = "papaya"
print(fruitsL)

fruits = ("apple","mango","banana","oranges")
print(type(fruits)) # tuple
#fruits[0] = "papaya"

# Tuples allow duplicate values
fruits = ("apple","mango","banana","oranges","apple")
print(fruits)

print(len(fruits))

# check element is present
fruits = ("apple","mango","banana","oranges","apple")
print("apple"  in fruits)

# check element is not present
print("grapes" not in fruits)

# create tuples for various size and data types

tuplesS = ("chinmay","raj","sameet")
tuplesB = (True,False,True,False)
tuplesN = (11,22,33,44,55,66)
tuplesM = ("Chinmay","Deshpande",7709192441)

newTuple = tuple(("1","2","3","4","5"))
print(newTuple)

# accessing the element
tuplesS = ("chinmay","raj","sameet")
print(tuplesS[0])

# loops
for x in tuplesS:
    print(x)

# looping through the range function
for item in range(len(tuplesS)):
    #print(item)
    print(tuplesS[item])

# Another way yo define tuple

numbers = 33,44
print(numbers)
print(type(numbers))

#Methods for tuple

#                 0            1       2          3        4        5
vegetable = ("cauliflower","cabbage","brinjal","potato","tomato","potato")
print(vegetable.index("cabbage"))
print(vegetable.count("potato"))

animals = ("tiger","lion","rabbit")

a  = animals[0]
b = animals[1]
c = animals[2]

print(a)
print(b)
print(c)

# unpacking of tuples
(x1,x2,x3) = animals
print(x1)
print(x2)
print(x3)


tupA = (11,22,33)
tupB = (44,55,66)

tupC = tupA + tupB
print(tupC)

print(tupA*2)


# types

fi = "amol"

se = {"apple","mango","banana"}

di = {
    'firstName':'chinmay',
    'lastName':'despande'
}
li  = ["1","2","3"]

tA = (22,33,44)

























