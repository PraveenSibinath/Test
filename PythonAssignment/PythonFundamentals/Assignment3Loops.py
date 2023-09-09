from array import *
b=array('i',[])
a = int(input("Enter the length of array:"))

for i in range(a):
    num = int(input("Enter the numbers:"))
    b.append(num)

for nume in b:
    for prime in range(2, nume):
        if nume%prime ==0:
            print (nume, "Is not a prime number")
            break
    else:
        print(nume, "Is a prime number")


