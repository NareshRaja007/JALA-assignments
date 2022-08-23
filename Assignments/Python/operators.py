# 1. Write a function for arithmetic operators(+,-,*,/)

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))

print("The sum of and is                : ", a+b)
print("The difference of a and b is     : ", a-b)
print("The multiplication of a and b is : ", a*b)
print("The division of a and b is       : ", a/b)

# 2. Write a method for increment and decrement operators(++, --)

# increasing the variable value one by one
a = 0
a += 1 # =>a = a+1
print("The value of a is ", a)

# Use of increment operator, here start = 0,step = 1(by default) and stop = 5 
print("INCREMENTED FOR LOOP")
for i in range(0, 5):
   print(i)
#Use of decrement operator, here start = 4, step = -1 and  stop = -1
print("\nDECREMENTED FOR LOOP")
for i in range(4, -1, -1):
   print(i)

# 3. Write a program to find the two numbers equal or not.

c = int(input("Enter the 1st num : ")) 
d = int(input("Enter the 2nd num : "))
if (c==d):
    print("Numbers are Equal")
else:
    print("Numbers are not Equal")

# 4. Program for relational operators (<,<==, >, >==)

a = int(input("Number 1 : "))
b = int(input("Number 2 : "))
print(a < b)  #This operator(<) returns True if the left operand is less than the right operand.
print(a <= b) #This operator(<=)returns True if the left operand is less than or equal to the right operand.
print(a > b)  #This operator(>) returns True if the left operand is greater than the right operand.
print(a >= b) #This operator(>=)returns True if the left operand is greater than or equal to the right operand.   
print(a == b) #This operator(==)returns True if both the operands are equal i.e. if both the left and the right operand are equal to each other.
print(a != b) #This operator(!=)returns True if both the operands are not equal.

# 5. Print the smaller and larger number

a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
#To print larger number
if a > b: 
     print(a, "is greater ")
else:
    print(b, " is greater ")
#To print samller number
if a < b:
     print(a, "is smaller ")
else:
    print(b, " is smaller ")   
