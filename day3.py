

# condition statements


# conditional statements are used when 1 i/p and multiple outcomes


# program 1
# numT > 0 and  numT <= 5   ===> 5 % discount
# numT > 5 and  numT <= 10  ===> 10 % discount
# numT > 10                 ===> 30 % discount

# if(condition):
#     #staments
numT = 12
# if(numT > 0 and numT <= 5):
#     print('5 % discount')
# if(numT > 5 and numT <= 10):
#     print('10 % disocunt')
# if(numT > 10):
#     print('30 % discount')

numT = -71
if(numT > 0 and numT <= 5):
    print('5 % discount')
elif(numT > 5 and numT <= 10):
    print('10 % disocunt')
elif(numT > 10):
    print('30 % discount')
else:
    print('Please enter correct values')


# program 2
marks = 50
# if(marks > 90):
#     print("Grade A")
# if(marks > 75):
#     print("Grade B")
# if(marks > 65):
#     print('Grade C')

# if(marks > 90):
#     print("Grade A")
# elif(marks > 75):
#     print("Grade B")
# elif(marks > 65):
#     print('Grade C')
# else:
#     print('Try again')


# program 3

a  = 10
b = 5

if(a > b):
    print('a is greater')
else :
    print('b is greater')

# program 4
x = 10
y = 50
z = 300
if x > y and x > z:
    print('x is greater')
elif y > z and y > x:
    print('y is greater')
else:
    print('z is greater')

# program5

i = 10
j = 50

# if(i > j):
#     print('i is greater')
# else:
#     print('j is greater')

# shorthand , ternary conditions to write this
print("i is greater") if i > j else print("j is greater")
age = 18
x1 = "canDrive" if age >= 18 else "cannot drive"
print(x1)

# program 6
# Nested if else block
s1 = 90
s2 = 450
s3 = 670

if(s1 > s2):
    if(s1 > s3):
        print('s1 is greater')
    else:
        print('s3 is greater')
elif (s2 > s3):
    print('s2 is greater')
else :
    print('s3 is greater')


# program 7 (pass keyword)
if( 5 < 7):
    pass


# Loops  (when to use loops)
# for loop and while loop
# range function


# print "hello"  3 types

# for x in range(startPosition, endPosition ,stepSize):
#     print(x)

# for x in range(2,10):
#     print(x)
#
# for x in range(2,7):
#     print(x)
#
# for x in range(8):
#     print(x)


for x in range(3):
    #print(x)
    print("hello")

# print 1 to 5
for x in range(1,6):
    print(x)

# print table of 2
for x in range(2,21,2):
    print(x)

# print table of 3
for x in range(3,31,3):
    print(x)


# break with for
for x in range(1,30):
    if x == 15:
        break
    print(x)


# continuw with for
for x  in range(1,11):
    if  x == 6:
        continue
    print(x)

for x  in range(1,10):
    print(x)
else :
    print('Python ends')













# for loop

































































