#"chinmaydeshpande-7709192441"   ===>  regular expression
# "ram sham satish"              ====> regular expression
# program 1
import re
str = 'man sun mop run'   # m\w\w  - A-Z a-z 0-9
result = re.search(r'm\w\w',str)
print(result)
if(result):
    print(result.group())

# program 2
str2 = 'man sun mop run'
result = re.findall(r'm\w\w',str2)
print(result)

# program3
str3 = 'ram man sun mop run'
result = re.match(r'm\w\w',str3)
print(result)

str4 = "This is chinmay's book$$ for python"  # \W (not a-z A-z 0-9)
result = re.split(r'\W+',str4)
print(result)

# search findall match spilt sub

# program 5
str5 = "I am learning javascript"
result = re.sub(r'javascript','python',str5)
print(result)

# program 6
str6 = "an apple a day keeps doctor away" # an,apple,a away
result = re.findall(r'a[\w]*',str6)
print(result)

# program 7
str6 = "an apple a day keeps doctor away" # an,apple,a away
result = re.findall(r'\ba[\w]*',str6)
print(result)














