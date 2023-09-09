a = int(input("Enter your 1st value: "))
b = int(input("Enter your 2st value: "))
c = int(input("Enter your 3st value: "))

if a>b and a>c:
    print(f'Value of a-{a} is greater than b and c')
elif b>a and b>c:
    print(f'Value of b-{b} is greater than a and c')
else:
    print(f'Value of c-{c} is greater than a and b')