# 1.Create a list containing squares of numbers from 1 to 10 (HINT: use List Comprehension)
num = [1,2,3,4,5,6,7,8,9,10]
square = []

for x in num:
    a = x * x
    square.append(a)
print (square)

# 2. Write a Function to check if year number is a leap year
a = int(input("Enter a year to find if it is a leap year:"))

if a%4 == 0:
    print(a, "is a Leap Year")
else:
    print(a, "is not a Leap Year")

#3. Write a function to take an array and return another array that contains the members of first array that are even
from array import *
b=array('i',[])
c=array('i',[])
a = int(input("Enter the length of array:"))

for i in range(a):
    num = int(input("Enter the numbers:"))
    b.append(num)

for nums in b:
    if nums%2==0:
        c.append(nums)

print(c)

#4. Write a function that takes 2 arrays and prints the members of first array that are present of second array

from array import *
b=array('i',[])
c=array('i',[])
a = int(input("Enter the length of array:"))

for i in range(a):
    num = int(input("Enter the numbers:"))
    b.append(num)


d = int(input("Enter the length of array:"))
for i in range(d):
    num = int(input("Enter the numbers:"))
    c.append(num)
print(b, "--Your first array")
print(c, "--Your second array")

def first_and_second_element():
    similar = [element for element in b if element in c]
    print("Numbers of first array elements present in second array", similar)

first_and_second_element()

