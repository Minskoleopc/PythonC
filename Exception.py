
# Exception


# Errors that occurs during the rub time are called exceptions or lofical error

# Open a file and the file does not exist there
# try tp diviide a number by zero
# try to import a module which does a exist

#print(7/0)
#print(dir(locals()['__builtins__']))

# program1
print('hello')
try:
    print(7/0)
except:
    print("Expectiing zero division error")
print("bye")

# program 2
#              0  1  2  3  4  5
listNumbers = [11,22,33,44,55,66]
# list stotes the value by index
try:
    print(listNumbers[6]) # raising a exception
except ZeroDivisionError:
    print('Denominator cannot be zero')
except IndexError:
    print("Index out of Bound exception")
except:
    print('Unknow but the exception is found')

# program 3
# Exception with the else block
try :
    number = 4
    assert number % 2 == 0
except:
    print('It is not even number')
else:
    print('I am running from else block')

# program 4
try:
    num = 10
    numB = 5
    result = num/numB
    print(result)

except:
    print('Error: Denominator cannot be zero exception')

finally:
    print('This is excuted any way')






















