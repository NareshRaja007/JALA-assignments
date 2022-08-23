# 1. Write a program to print your name.

print("Naresh Raja")

# 2. Write a program for a Single line comment and multi-line comments.

#Single line comment

print("'#' will be used before a comment that is single line comment")\

#Multi line comment

print(" ''' these symbols is used for multi line comment when a comment expands for more than a line ''' ")

# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

a = 5
b = True
c = 'Raja'
d = 10.5
print("Type of a : ", type(a),
      "\nType of b : ", type(b),
      "\nType of c : ", type(c),
      "\nType of d : ", type(d))

# 4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables.

a = 5
# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)
# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a) 
# Uses global keyword to modify global 'a'
def h():
    global a
    a = 4      #Value of 'a' modified
    print('Inside h() : ', a)  
# Global scope
print('global     : ', a)
f()
print('global     : ', a)
g()
print('global     : ', a)
h()
print('global     : ', a)