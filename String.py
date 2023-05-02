first_Name = 'chinmay'
last_Name = "deshpande"

print(first_Name)
print(last_Name)

# Multiline string

a = """
    This is a multi line string
    spread over multiple lines
"""
print(a)

# String stores the value by index

# 0 1 2 3 4
# H e l l o

greet = "Hello"
print(greet[0])


# print every charcter od string

city = "chandrapur"

#0   1    2    3     4    5    6    7   8   9
#c   h    a    n     d    r    a    p   u    r
print(city[1])
# for
for char in city:
    print(char)
for char in range(len(city)):
    #print(char)
    print(city[char])

# while
char2 = 0
while(char2 < len(city)):
    print(city[char2])
    char2 = char2 + 1


# program 2

city3 = "pune"

# 0  1  2  3
# p  u  n  e
print(len(city3))  # 4

k = 0
while(k < len(city3)):
    #print(k)
    print(city3[k])
    # k -- 0
    # k -- 1
    # k -- 2
    # k -- 3
    # 0 , 1 , 2 , 3
    k = k + 1 # 1 2 3  4

# program3
# Cheking if available
quote = "An apple a day keeps doctor away"
if "apple" in quote :
    print("available")
else:
    print("not available")
print('h' in "chinmay")

# Check  if not available
fruits = "apple mango banana chikoo payaya"
if "watermelon" not in fruits:
    print('not available')
else:
    print('available')

print("chi" in "chinmay")
print("chi" not in "tanmay")

# Slicing in string

city4 = "chandrapur"

#0   1    2    3    4   5   6   7    8    9
#c   h    a    n    d   r   a   p    u    r
#-10 -9  -8   -7   -6  -5  -4  -3   -2   -1

print(city4[2])
#[startIndex:endIndex:Steps]
a = city4[2:]
print(a)
print(city4[2:8])
print(city4[-6:])
print(city4[-9:-2]) # endIndex in not inclucive
print(city4[1:-1])
print(city4[-8:8])
# endIndex is behind startIndex (blank string)
print(city4[-1:-3])

#[startIndex, endIndex , steps ]  # by default step size is 1
city5 = "nagpur"
# 0      1       2      3    4     5
# n      a       g      p    u     r
print(city5[0:len(city5):3])


##################### Methods for string ################################

# Gym
# action - exercise
# return - health


# upper()
# action - it converts every character of string to uppercase()
# return - string

first_Name = "chinmay"
q1 = first_Name.upper()
print(q1)

last_Name = "Deshpande"
q2 = last_Name.lower()
print(q2)

middName = " shirish "
print(len(middName))
q3 = middName.strip()
print(len(q3))

q4 = middName.lstrip()
print(len(q4))

q5 = middName.rstrip()
print(len(q5))

##" hello "  --- strip() - 'hello'
##" hello "  --- lstrip() - 'hello '
##" hello "  --- rstrip() - ' hello'

# split()
info = "chinmay deshpande 7709192441"
q6 = info.split(" ")
print(q6)

q7 = info.split("a")
print(q7)
#["chinm","y deshp","nde 7709192441"]
# upper(),lower(),  lstrip() ,rstrip() ,split()

# String concatenation
first_s = "hello"
last_s = "world"
print(first_s+ last_s)

# age = 32
# text = "My name is chinmay and My age is "+age
# print(text)
# format()

age = 32
text = "My name is chinmay and My age is {}".format(age)
print(text)


first_name2 = "ninad"
last_name2 = "dani"
# my first_name is ninad and my last_name is dani
text = "my first_name is {} and my last_name is {}".format(first_name2,last_name2);
print(text)

text2 = "I am learning python {1}, and  javascript {0}".format("Es6","3")
print(text2)


fn = "chinmay"
ln = "deshpande"
mn = "shirish"
#"my name is deshpande chinmay shirish"
text3 = "my name is {1} {0} {2}".format(fn,ln,mn)
print(text3)
####################   Methods  set2 for string  ######################################

# capitalize
city = "pune"
txt = city.capitalize()
print(txt)

#count
city2 = "chandrapur"
q1 = city2.count("a")
print(q1)

#islpha()
city3 = "pune"
q2 = city3.isalpha()
print(q2)

#isalnum()  # "123", "qwe", "asd123"
city4 = "$"
q3 = city4.isalnum()
print(q3)

#isdigit()
pincode = "411028"
q4 = pincode.isdigit()
print(q4)

#islower()
city5 = "wardha"
q5 = city5.islower()
print(q5)

#isupper()
city6 = "NAGPUR"
q6 = city6.isupper()
print(q6)

#startsWith()
city7 = "chandrapur"
q7 = city7.startswith("ch")
print(q7)

#endsWith()
q8 = city7.endswith("r")
print(q8)

#replace
str = "I am learning  javascript"
q9 = str.replace("javascript","python")
print(q9)














































#["chinmay","deshpande","7709192441"]


























































