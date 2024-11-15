#List is a sequence of comma separated values or elements
#syntax:list_name=[value1,value2,value3,....valueN]
#example:

List=[1,2,3,4,5]
print(List)#[1,2,3,4,5]

#list elements are accessed through indexing 
#list can have both the positive indexing and negative indexing 
print(List[0])#1
print(List[-1])#5

#list has slice operation same as strings
print(List[1:3])#[2,3]

#list has concatenation operation(+)
List2=List+[10,20,30]
print(List2)#[1,2,3,4,5,10,20,30]

#list as repetition(*)
List3=List*2
print(List3)#[1,2,3,4,5,1,2,3,4,5]

#list has nested list
List4=[1,[2,3,4,5],6,7,8,9]
print(List4)#[1,[2,3,4,5],6,7,8,9]

#nested list can be accessed through indexing
print(List4[1][3])#5

#built-in functions:


#len()-returns length
print(len(List))#5

#max()-returns maximum value in the list
print(max(List2))#30

#min()-returns minimum value in the list
print(min(List2))#1

#sum()-returns xum of the values in the list
print(sum(List))#15

#any()-returns True if any elementis True
print(any(List2))#True

#all()-returns True if all elements are True
print(all(List3))#True

#del()- deletes the element or slice or entire list
del List3
#print(List3)#NameError 'List3' is not defined

#sort(lst)-sorts the list elements and returns sorted list
List4=[4,2,5,23,8]
print(sorted(List4))#[2,4,5,8,23]

#reversed()-returns the list of reverse elements
print(reversed(List2))

#methods
#append()-add element at end of the list
#modifies the list does not returns new list
List.append(45)
print(List)#[1,2,3,4,5,45]

#count()-returns the count value of elments(no.of occurrences)

List5=[2,1,3,4,2,1,4,5,2,5,7,2]
print("Count of 1",List5.count(1))#2


#take input from user and add to the list 
#List is a sequence of comma separated values or elements
#syntax:list_name=[value1,value2,value3,....valueN]
#example:

List=[1,2,3,4,5]
print(List)

#list elements are accessed through indexing 
#list can have both the positive indexing and negative indexing 
print(List[0])#1
print(List[-1])#5

#list has slice operation same as strings
print(List[1:3])#[2,3]

#list has concatenation operation(+)
List2=List+[10,20,30]
print(List2)

#list as repetition(*)
List3=List*2
print(List3)

#list has nested list
List4=[1,[2,3,4,5],6,7,8,9]
print(List4)

#nested list can be accessed through indexing
print(List4[1][3])

#built-in functions:


#len()-returns length
print(len(List))

#max()-returns maximum value in the list
print(max(List2))

#min()-returns minimum value in the list
print(min(List2))

#sum()-returns xum of the values in the list
print(sum(List))

#any()-returns True if any elementis True
print(any(List2))

#all()-returns True if all elements are True
print(all(List3))

#del()- deletes the element or slice or entire list
del List3
#print(List3)#error not defined

#sort(lst)-sorts the list elements and returns sorted list
List4=[4,2,5,23,8]
print(sorted(List4))

#reversed()-returns the list of reverse elements
print(reversed(List2))

#methods
#append()-add element at end of the list
#modifies the list does not returns new list
List.append(45)
print(List)

#count()-returns the count value of elments(no.of occurrences)

List5=[2,1,3,4,2,1,4,5,2,5,7,2]
print("Count of 1",List5.count(1))


#take input from user and add to the list 
List6=[]
for x in range(5):
    value=input("Enter value to add to the list:")
    List6.append(x)
print(List6)
"""
ouput:
Enter value to add to the list:23
Enter value to add to the list:324
Enter value to add to the list:56
Enter value to add to the list:12
Enter value to add to the list:54
[23, 324, 56, 12, 54]
"""
#index()-find the index of first occurence of a specified value within a list
#if the specified element is not present in the list will raise ValueError
a=[1,2,45,1,23,56,2,1,45,23,7,9,1]
print(a)
print(a.index(1))
print(a.index(1,6))
print(a.index(45,4,9))
"""
output:
[1, 2, 45, 1, 23, 56, 2, 1, 45, 23, 7, 9, 1]
0
7
8
"""
insert()-insert element at specified index position
two arguments:first-index,value

a=[45,23,87,21]
print(a)
a.insert(3,12)
a.insert(2,'d')
print(a)
"""
output:
[45, 23, 87, 21]
[45, 23, 'd', 87, 12, 21]
"""
#pop()-removes the specified index value

a=[45,23,87,21]
print(a)
a.pop(2)#delete specified index value from the list
print(a)
a.pop()#delete last values from the list
print(a)
a.pop(20)#IndexError index out of range
"""
output:
[45, 23, 87, 21]
[45, 23, 21]
[45, 23]
"""
#sort()-sorts the list value

a=[23,354,12,65467,245]
print(a)
a.sort()
print(a)

#reverse()-list elements order is reversed
a.reverse()
print(a)
"""
output:

[23, 354, 12, 65467, 245]
[12, 23, 245, 354, 65467]
[65467, 354, 245, 23, 12]
"""

#extend()-to add multiple values like object
a=[1,2,3,4,5]
print("a=",a)
b=[6,7]
print("b=",b)
a.extend(b)
print("a=",a)
"""output:
a= [1, 2, 3, 4, 5]
b= [6, 7]
a= [1, 2, 3, 4, 5, 6, 7]
"""

#remove()-removes the first occurence of a specified value from a list
#specified value is not present in the list will raise a ValueError

a=[23,45,21,78,21,23,45]
print(a)
a.remove(23)
print(a)
"""
output:

[23, 45, 21, 78, 21, 23, 45]
[45, 21, 78, 21, 23, 45]

"""

#copy()-duplicate list is generated without effecting the orginl list
#shallow copy of list
a=[1,2,3,4,5]
print("address a=",id(a))
b=a
print("address b=",id(b))
c=a.copy()
print("address c=",id(c))
"""
output:

address a= 131319499365440
address b= 131319499365440
address c= 131319499442368

"""

#clear()-clear the memory allocated for the list

#note********
#dir(list)-to get all the lsit methods and functions
#help(list.count)#returns the functionality of that methods or function


cloning list:
alows you to work with a copy of the data without affedting the original list 
slice operation is used to clone a list
a=[1,2,3,4,5]
print("address a=",id(a))
b=a[:]
print("address b=",id(b))
"""
output:

address a= 127455096659008
address b= 127455096735936
"""
#looping in list
#a loop is often used to iterate through each element in list
#in each iteration the loop varaiable takes each element
List=[1,2,3,4,5]
for x in List:
  print(x)
"""
output:

1
2
3
4
5
"""

#using enumeration:
#enumerate() ramge()
#to iterate through the list along with index
lst=[1,2,3,4,5]
for i,j in enumerate(lst):
  print(i,j)
"""
output:
0 1
1 2
2 3
3 4
4 5
"""

lst=[3,4,5,6,7]
for i in range(len(lst)):
  print(lst[i],end=" ")
"""
output:
3 4 5 6 7 
"""



