# 1. Write a function to add integer values of an array.

def sum(num):
    total=0
    for i in num:
        total += i
    print("The sum of an array is : ",total )
num=[10,20,30,40,50]
sum(num)

# 2. Write a function to calculate the average value of an array of integers.

def average(num):
    sum=0
    for i in num:
        sum += i
    avg = sum / len(num)
    print("The average of an array is : ",avg)
num=[10,20,30,40,50]
average(num)

# 3. Write a program to find the index of an array element.

arr = [22,55,21,45,64,67,83,23]

index = arr.index(55)
print("The index of 55 is ", index)

index = arr.index(83)
print("The index of 83 is ", index)

# 4. Write a function to test if array contains a specific value.

arr = [33,54,64,21,43,78]
for num in arr:
    if num == 64:
        print("Value exist")
        
# 5. Write a function to remove a specific element from an array.

def remove_ar(arr):
    a=arr.remove(45)
    print("Value removed successfully")

arr=[23,34,55,65,45]
remove_ar(arr)
print(arr)

# 6. Write a function to copy an array to another array.

arr = [33,54,64,21,43,78]
arr_1=[]
arr_1=arr.copy()
print("Values copied : ", arr_1)

# 7. Write a function to insert an element at a specific position in the array.

arr = [33,54,64,21,43,78]
arr.insert(1,3)
print("Value added : ", arr)

# 8. Write a function to find the minimum and maximum value of an array.

arr = [33,54,64,21,43,78]
b=max(arr)
c=min(arr)
print("Maximum value in an array : ",b)
print("Minimum value in an array : ",c)

# 9. Write a function to reverse an array of integer values.

arr = [33,54,64,21,43,78]
arr.reverse()
print("Reverse of an array : ",arr)

# 10. Write a function to find the duplicate values of an array.

arr = [33,54,43,21,43,78]
for i in range(0,len(arr)):
    for k in range(i + 1,len(arr)):
        if arr[i] == arr[k]:
            print("Duplicate element in given array:",arr[k])

# 11. Write a program to find the common values between two arrays.

arr = [33,54,43,21,43,78]
arr1 = [88,45,32,54]
print("Common values in given arrays:",set(arr).intersection(arr1))

# 12. Write a method to remove duplicate elements from an array.

arr = [11,22,33,11,44,55]
duplicate = [] 
for i in arr:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)

# 13. Write a method to find the second largest number in an array.

arr = [101,404,202,909,606,505,808,303,707]
arr.sort()
print("Second largest number:",arr[-2])

# 15. Write a method to find number of even number and odd numbers in an array.

arr = [1,2,3,4,5,6,7,8,9]
evennum = 0
oddnum = 0
for i in arr:
    if i % 2 == 0:
        evennum += 1
    else:
        oddnum += 1 
print("Even Numbers in given array:",evennum)
print("Odd Numbers in given array:",oddnum)

# 16. Write a function to get the difference of largest and smallest value.

arr = [10,6,11,13,14]
arr.sort() 
print("Difference of largest and smallest value:",arr[4]-arr[0])

# 17. Write a method to verify if the array contains two specified elements(12,23)

arr = [1,12,19,23,33,54]
for i in arr:
    if i == 12:
        print("Exist in array")
    if i == 23:
        print("Exist in array")