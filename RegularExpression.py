# #"chinmaydeshpande-7709192441"   ===>  regular expression
# # "ram sham satish"              ====> regular expression
# # program 1
# import re
# str = 'man sun mop run'   # m\w\w  - A-Z a-z 0-9
# result = re.search(r'm\w\w',str)
# print(result)
# if(result):
#     print(result.group())
#
# # program 2
# str2 = 'man sun mop run'
# result = re.findall(r'm\w\w',str2)
# print(result)
#
# # program3
# str3 = 'ram man sun mop run'
# result = re.match(r'm\w\w',str3)
# print(result)
#
# str4 = "This is chinmay's book$$ for python"  # \W (not a-z A-z 0-9)
# result = re.split(r'\W+',str4)
# print(result)
#
# # search findall match spilt sub
#
# # program 5
# str5 = "I am learning javascript"
# result = re.sub(r'javascript','python',str5)
# print(result)
#
# # program 6
# str6 = "an apple a day keeps doctor away" # an,apple,a away
# result = re.findall(r'a[\w]*',str6)
# print(result)
#
# # program 7
# str6 = "an apple a day keeps doctor away" # an,apple,a away
# result = re.findall(r'\ba[\w]*',str6)
# print(result)
import  re
str  = 'man sun mop run'
result = re.search(r'm\w\w',str)    # w --- a-z A-Z 0-9
if(result):
    print(result.group())

# findAll
result2 = re.findall(r'm\w\w',str)
print(result2)

#match
result3 = re.match(r'm\w\w',str)
if(result3):
    print(result.group())

#split

str2 =  'This: is the :"Core" Python\'s book'
result4 = re.split(r'\W+',str2)
print(result4)


str3 = "I am learning javascript"
result5 = re.sub(r'javascript','python',str3)
print(result5)

# \d   =======>  any digit 0-9
# \D   =======> represent any non-digit
# \s   ======>  represent white space
# \S   ======>  non -white space character
# \w   ======>  (a-z A-Z 0-9)
# \b   ======>  represents a space
# \A   ======> matches at start of strng
# \Z   ======> match only at end

str5 = "an apple a day keeps doctor away"
result6 = re.findall(r'a[\w]*',str5)
result7 = re.findall(r'\ba[\w]*',str5)
print(result6)
print(result7)

str6 = "The meeting will be conducted on 1st and 22nd every month"
result8 = re.findall(r'\d[\w]*',str6)
print(result8)

str7 = 'one two three four five six seven 8 9 10'  # character
result9 = re.findall(r'\b\w{5}\b',str7)
print(result9)

str7 = 'one two three four five six seven 8 9 10'  # character
result10 = re.search(r'\b\w{5}\b',str7)
print(result10.group())


str8 = 'one two three four five six seven 8 9 10'  # character
result10 = re.findall(r'\b\w{4,}\b',str8)
print(result10)


str8 = 'one two three four five six seven 8 9 10'  # character
result10 = re.findall(r'\b\w{3,5}\b',str8)
print(result10)

str9 = 'one two three four five six seven 8 9 10'  # character
result11 = re.findall(r'\b\d\b',str9)
print(result11)

str9 = 'one two three four five six seven 8 9 10 three'
result10 =re.findall(r'\b\w{5}\Z',str9)
print(result10)

#+  1 or more repetation of precefing reqex
#*  0 or more repetation
#?  0 and 1 repetation
#{m}  Exact occurences
#{m,n}

str10 = "Chinmay Deshapande: 7709192441"
result11 = re.search(r'\d+',str10)
if(result11):
    print(result11.group())

result12 = re.search(r'\D+',str10)
if(result12):
    print(result12.group())

str11 = 'anil akhil anant arun abhijit ankur'
result13 = re.findall(r'a[nkr][\w]*',str11)
print(result13)

str12 = 'vijay 07-11-189 chinmay 05-02-1989 amit 08-11-1993'


























































