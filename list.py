x = "chinmay"
print(x)
print(type(x))

x = 10
print(x)
print(type(x))

x = 40.0
print(x)
print(type(x))

x = True
print(x)
print(type(x))


# list
#           0       1        2        3
fruits = ["apple","mango","banana","chikoo"]
print(fruits[0])

# Duplicate
fruits = ["apple","mango","banana","chikoo","apple"]
print(fruits)

# len()
fN = "chinmay"
print(len(fN))

count = len(fruits)
print(count)

# mixed list
info = ["chinmay","deshpande",32,["python","java","javscript"],True]
print(info)


#accessing the list item
#              0            1          2        3
vegetable = ["cabbge","cauliflower","brinjal","carrot"]
#              -4         -3            -2         -1
print(vegetable)

#firstelement
print(vegetable[0])
print(vegetable[-4])


# slicing of list
#              0            1          2        3
vegetable = ["cabbge","cauliflower","brinjal","carrot","ladyflower"]
#              -4          -3          -2         -1
print(vegetable)
print(vegetable[2])
print(vegetable[2:])
print(vegetable[0:3])
print(vegetable[-4:-2])
print(vegetable[0:-1])
print(vegetable[0:len(vegetable):2])


# Check whether particulat element is available in string

vegetable = ["cabbage","cauliflower","brinjal","carrot","ladyflower"]
print("cabbage" in vegetable)  # True
print("potato" not in vegetable) # True

userInput = "Potato"
if userInput in vegetable:
    print('vegetable is available')
else:
    print('vegetable not available')


# Updating the list
#         0       1        2          3        4
city = ["pune","mumbai","banglore","kolkata","madras"]
print(city)
city[0] = "nagpur"
print(city[0])
print(city)

city[1:3] = ["wardha","amravati"]
print(city)

# Looping through
#            0         1          2            3
country = ["India","Pakistan","Bangladesh","Srilanka"]

# 1st method
for item in country:
    print(item)

# 2nd method

for x in range(4):
    # print(x)
    print(country[x])


#           0  1  2  3  4
number  = [11,22,33,44,55]
for item in number:
    print(item)

for x in range(len(number)):
    #print(x)
    print(number[x])


# Methods
#            0        1      2        3        4        5
animals = ["tiger","lion","giraffe","snake","rabbit","snake"]
animals.append("panthar")
print(animals)

# count
q1 = animals.count("snake")
print(q1)

#index()
q2 = animals.index("lion")
print(q2)

#insert()
animals[4] = "wolf"
#animals.insert(4,"wolf")
print(animals)

# remove()
animals.remove("snake")
print(animals)

#####################################  DAY 2 ###################################

#          0         1        2      3
fruits = ["apple","mango","banana","grapes"]
#          -4         -3         -2        -1
print(fruits)
print(fruits[0])
# len()
print(len(fruits))
#slice
print(fruits[1:])
print(fruits[1:3])
print(fruits[1:-1])

# loop
#              0          1         2        3
vegetable = ["potato", "tomato","brinjal","cabbage"]
print(vegetable)

for item in vegetable:
    print(item)

for item in range(len(vegetable)):
    #print(item)
    print(vegetable[item])

print("potato" in vegetable)
print("cauliflower" not in vegetable)


# methods
listA = [11,22,33]
listB = listA
listB[0] = 99
print(listA)
print(listB)

# Methods
# index()
#        0        1        2          3
city = ["pune","mumbai","banglore","kolkala"]
a = city.index("mumbai")
print(a)

# append()
city.append("nagpur")
print(city)

# insert()
city.insert(2,"goa")
print(city)

# copy()
numA  = [11,22,33]
numC = numA.copy()
numC[1] = 100
print(numC)
print(numA)

#extend()

listC = [33,44,55]
listD  =[66,77,88]
listD.extend(listC)
print(listD)

#count()
cities = ["nagpur","wardha","chennai","banglore","kolkata","nagpur"]
q1 = cities.count("nagpur")
print(q1)

#remove()
cities.remove("wardha")
print(cities)

#pop()
cities.pop(3)
print(cities)

#sort()
names = ["chinmay","sarika","ram","abhisha","sachin","suresh"]
names.sort()
print(names)

# revers()
numsC  = [11,22,33,44]
numsC.reverse()
print(numsC)

#clear()
numC.clear()
print(numC)

numV = [55,66,77]

















































































































