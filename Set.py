
# Set cannot store  duplicate
# Set does stores the value by index (Sets are not prdered)


fruits = {"apple","mango","banana","mango"}
print(type(fruits))

# lenght of set

q1 = len(fruits)
print(q1)

# duplicate values
print(fruits)

# True and 1  are considered as same value in python
setB = {1,True, "chinmay","deshpande",7709192441}
print(setB)

# set of String
setA = {"apple","mango","banana"}
# set if number
setB = {1,2,3,4,5,6}
# set of boolean values
setC = {True,False,True, True ,False}

# constructor way to defined set
vegetables = set(("cabbage","cauliflower","brinjal"))
print(vegetables)


# program 2

# retrive (access the value)
# update the value
# add the value
# delete the value

# looping through set
setE = {11,22,33,44,55,66}
for x in setE:
    print(x)

# Check whether a particular element is present in set
print(55 in setE)
if(55 in setE):
    print('available')
else:
    print('non available')
print(66 not in setE)

# Add the value to set
setF = {'pune',"mumbai","banglore","kolkata"}
setF.add("nagpur")
print(setF)

SetG  = {111,222,333}
SetH = {444,555,666}
SetI = [777,888,999]

SetG.update(SetH)
print(SetG)
SetG.update(SetI)
print(SetG)

SetG.remove(555)
print(SetG)

# SetG.remove(5556)
# print(SetG)

SetG.discard(666)
print(SetG)

#{777, 333, 222, 999, 111, 888, 444}
SetG.pop()
print(SetG)
#
# SetG.clear()
# print(SetG)

# del SetG
# print(SetG)


setJ = {22,33,44,55}
setK = {66,77,88,99,66}

setL = setJ.union(setK)
print(setL)
print(setJ)
print(setK)

setJ = {22,33,44,55}
setK = {66,77,88,99,22,33}

print(setJ.intersection(setK))
setJ.intersection_update(setK)
print(setJ)


setJ = {22,33,44,55}
setK = {66,77,88,99,22,33}

print(setJ.symmetric_difference(setK))
setJ.symmetric_difference_update(setK)

#{44,55,66,77,88,99}
print(setJ)


setJ = {22,33,44,55}
setK = {66,77,88,99,22,33}
print(setJ.difference(setK))
setJ.difference_update(setK)
print(setJ)


setJ = {22,33}
setK = {22,33,44}

print(setJ.issubset(setK))
print(setK.issuperset(setJ))

setJ = {22,33}
setK = {22,33,44}

setJ = {22,33}
setK = {44,55}

print(setJ.isdisjoint(setK))


setN = {22,33,44}
# setM = setN
# setN.remove(22)
#
# print(setM)
# print(setN)

setK = setN.copy()
setK.remove(33)

print(setK)
print(setN)

# list , string , set , dict























