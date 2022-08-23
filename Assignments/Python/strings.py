# 1. Different ways creating a string

string = 'Hello'
print(string)

string = "Hello"
print(string)

string1 = '''World'''
print(string1)

string2 = """Welcome to 
             the world of Python""" # triple quotes string can extend multiple lines
print(string2)
print("\n")

# 2. Concatenating two strings using + operator

str1 = string + string1
print("Concatenated two different strings:",str1)
print("\n")

# 3. Finding the length of the string

print("length of the string:",len(str1))
print("\n")

# 4. Extract a string using Substring

string = "Naresh_Raja"
print(string[0:5])
print()

# 5. Searching in strings using index()

str3 = 'kashish'
str1 = 'ish'
str2 = 'h'
print("Position of ish:",str3.index(str1))
print("Position of h:",str3.index(str2))
print("\n")

# 6. Matching a String Against a Regular Expression With matches()

from ast import Str
import re
Substr = 'Naresh raja'
str6 = 'Naresh raja once said- Wake up to relity nothing goes as planned in this cursed world'
print(re.match(Substr,str6))
print()

# 7. Comparing strings

str8 = 'Itachi uchiha'
str1 = 'Madara uchiha'
str2 = str8
print(str8 == str1)
print(str8 == str2)
print(str1 == str2)
print(str8 != str1)
print()

# 8. startsWith(), endsWith() 

string = 'Naresh Raja'
print(string.startswith("Naresh"))
print(string.endswith("Raja"))
print()

# 9. Trimming strings with strip()

str7 = 'Hello World hi'
print(str7.strip("hi"))
print()

# 10. Replacing characters in strings with replace()

string = 'Welcome to the Kingdom'
print(string.replace("Kingdom","World"))
print()

# 11. Splitting strings with split()
string = 'Welcome to the Kingdom'
print(string.split( ))
print()

# 12. Converting integer objects to Strings

num = 10
num_1 = str(num)
print(num_1)
print(type(num_1))
print()

# 13. Converting to uppercase and lowercase

str = 'hello'
str_1 = 'WORLD'
print(str.upper())
print(str_1.lower())