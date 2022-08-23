# 1. Write a program to print “Bright IT Career” ten times using for loop.

a = "Bright IT career"
for i in range(10):
 print(a)

# 2. Write a program to print 1 to 20 numbers using the while loop.

a = 1
while(a<=20):
    print(a)
    a+=1

# 3. Program to equal operator and not equal operators.

a = 100
b = 50
print(a ==b) #Equal operator
print(a != b) #Not Equal operator

# 4. Write a program to print the odd and even numbers.

Numbers = [1,2,3,4,5,6,7,8,9,10]
print("Even Numbers: ")  
for i in Numbers:     
    if i % 2 == 0:       
        print(i, end =" ")    
print("\nOdd Numbers:")
for i in Numbers:
    if i % 2 != 0:
        print(i, end =" ")
print()

# 5. Write a program to print largest number among three numbers.
'''
a = int(input("Enter the 1st num : "))
b = int(input("Enter the 2nd num : "))
c = int(input("Enter the 3rd num : "))
if a >= b and k >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest number is: ",largest)
'''
# 6. Write a program to print even number between 10 and 20 using while

a = 10
b = 20
print("Even Numbers Between 10 to 20 : ",end=" ")
while a <= b:
    if(a % 2 == 0):
        print("{0}".format(a),end=" ")
    a += 1
print()

# 7. Write a program to print 1 to 10 using the do-while loop statement.

a = 1
print("Print 1 to 10 using do-while loop statement : ",end=" ")
while True:
    print(a,end=" ")
    a += 1
    if(a > 10):
        break 
print()

# 8. Write a program to find Armstrong number or not.

a = int(input('Enter a number : '))
sum = 0
temp = 0
temp = a
while temp > 0:
    r = temp % 10
    sum += r ** 3
    temp //= 10
if a == sum:
    print(a," is an amstrong number")
else:
    print(a," is not an amstrong number")

# 9. Write a program to find the prime or not.

number = int(input("Enter any number to check prime number or not: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")

# 10. Write a program to palindrome or not.   


n = int(input("Enter number to check palindrome or not:"))
temp = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if(temp == rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!") 

# 11. Program to check whether a number is EVEN or ODD.

a = int(input('Enter Number to check is EVEN or ODD: '))
if a % 2 == 0:
    print("{0} is Even ".format(a))
else:
    print("{0} is Odd ".format(a))  

# 12. Print gender (Male/Female) program according to given M/F

a = input()

if (a == 'Male'):
    print("M")
elif (a == 'Female'):
    print("F")
else:
    print("Incorrect text")



