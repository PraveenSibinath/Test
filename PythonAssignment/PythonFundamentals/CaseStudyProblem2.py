#1.Create 1st tuple with values -> (10,20,30), 2nd tuple with values -> (40,50,60).
tup1 = (10,20,30)
tup2 = (40,50,60)

#a.Concatenate the two tuples and store it in “t_combine”

t_combine = tup1+tup2
print(t_combine)
#b.Repeat the elements of “t_combine” 3 times

multiples = t_combine*3
print(multiples)
#c.Access the 3rd element from “t_combine”

print(t_combine[2])
#d.Access the first three elements from “t_combine”

print(t_combine[:3])
#e.Access the last three elements from “t_combine”

print(t_combine[-3:])

#2.Create a list ‘my_list’ with these elements:
#a,b,c:

my_list = [(1,2,3),("a","b","c"),(True,False)]
print(my_list)

#3.Append a new tuple – (1,’a’,True) to ‘my_list’

my_list.append((1,'a',True))
#a.Append a new list – *“sparta”,123+ to my_list

my_list.append(["sparta",123])
print(my_list)

#4.Create a dictionary ‘fruit’ where
#a,b,c,d
fruit = {"Fruit": ("Apple", "Banana", "Mango", "Guava")}
cost = {"Cost":(85,54,120,70)}

key=fruit.keys()
value=fruit.values()
print(key)
print(value)

#5.Crete a set named ‘my_set’ with values (1,1,”a”,”a”,True,True) and print the result
my_set = {1, 1, "a", "a", True, True}
print(my_set)
