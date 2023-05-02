info = ["chinmay","deshpande",23,45]
print(info)


info2 = {
    # property :value
    # key:value
    'first_name':"chinmay",
    'last_name':"deshpande",
    'age':23,
    'rollNo':45,
    'age':56
}
print(info2)
print(len(info2))
print(type(info2))
# retrive
q1 = info2.get('age')
print(q1)
q2 = info2['first_name']
print(q2)
# update
#info2['age'] = 55
print(info2)
# can dict store duplicate values
# no
# add property value
info2['city'] = "pune"
print(info2)
# delete
del(info2)
#print(info2)



# program 2

vehicle = {
    'color':"red",
    'type':"sedane",
    'model':'q6',
    'name':'audi'
}

# program1
print(vehicle)
print(vehicle.get('color'))
print(vehicle['type'])

# program 2
vehicle.pop('model')
print(vehicle)

#program3
# vehicle.clear()
# print(vehicle)

#program4
print(vehicle.keys())
print(vehicle.values())
print(vehicle.items())

# printing all the keys
for key in vehicle.keys():
    print(key)

for val in vehicle.values():
    print(val)

for item in vehicle.items():
    print(item)

# program 6
country = {
    'MH':'mumbai',
    'RJ':'Jaipur'
}
print(country)

countryB = country
print(countryB)
print(country)

countryB['MH'] = 'bombay'
print(countryB)
print(country)

coutryD = countryB.copy()
print(country)
print(coutryD)

coutryD['MH'] = "mumbai"
print(countryB)
print(coutryD)


# program7

info3 = {
    'firstName':"rasika",
    'lastName':"kulkarni"
}
info3.popitem()
print(info3)

#program8
info4  = dict.fromkeys(('first_name','last_name','age','rollNo'))
print(info4)

# program9

info3.update({'firstName':"poorva"})
info3.update({'firstName':"poorva",'lastName':"vyas"})
print(info3)

#program10
info5 = {
    'mobile':7709192441,
    'age':34,
    'rollNo':56
}

print(info5.setdefault('mobile'))
info5.setdefault('rollNo',23)
print(info5)




























