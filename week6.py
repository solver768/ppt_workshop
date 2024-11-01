for row in range(1,6):
  for col in range(1,6):
    print(col,end="")
  print()
"""
output:
12345
12345
12345
12345
12345
"""

for row in range(1,7):
  for col in range(1,row):
    print(col,end="")
  print()
"""
output:

1
12
123
1234
12345
"""

for row in range(6,1,-1):
  for col in range(1,row):
    print(col,end="")
  print()

"""
output:
12345
1234
123
12
1
"""
import pandas as pd
import matplotlib.pyplot as plt
data={
    'scores'=[88,95,78,92,85,89,94,87,91,86],
    'years'=[3,7,10,5,15,8,6,11,13,4]
}
df=pd.DataFrame(data)
plt.figure(figsize=(10,6))
plt.scatter(df['years'],df['scores'])






for row in range(1,7):
  for col in range(1,row):
    print(col,end="")
  print()
for i in range(row-1,1,-1):
    for col in range(1,i):
        print(col,end="")
    print()
"""
output
1
12
123
1234
12345
1234
123
12
1
"""
for row in range(5,0,-1):
    for col in range(row,0,-1):
        print(col,end="")
    print()
"""
output:
54321
4321
321
21
1
"""
for row in range(1,6):
  for col in range(1,6):
    print("%2d"%(col*row),"\t",end="")
  print()

"""
output:
 1 	 2 	 3 	 4 	 5 	
 2 	 4 	 6 	 8 	10 	
 3 	 6 	 9 	12 	15 	
 4 	 8 	12 	16 	20 	
 5 	10 	15 	20 	25 	
 """
"""
Strings:sequence of characters deliminated by single,double or triple quotes
name="India"
grade='N'
nationality=str(name)

3 ways to write Strings
all but the last line ends with \ ==>print("Welocome to \python\Programming")

enclosed within \""" =========\"""==>print(\"""Welcome to python\""")
                \''' =========\'''
('one msg' 'another msg'        ==>print(\'welcome' 'to' 'python'\)

accesing through index:name[0]=>I
if we exceed the index than the range rise error

slicing =>to get sub array:
A substring can be sliced out of a string 
s[st:end]#==>staring to end-1 
s[st:]#==>starting to end
s[:end]#==>beginning to end-1
s[-st:]#==>endding to start-1
s[:-end]#==>first to end-1
in slicing we can write exceed range of indexes
"""

s="Hello everyone hi"
st=2
end=7
print(s[st:end])#==>staring to end-1 
print(s[st:])#==>starting to end
print(s[:end])#==>beginning to end-1
print(s[-st:])#==>endding to start-1
print(s[:-end])#==>first to end-1


llo e
llo everyone hi
Hello e
hi
Hello ever
"""
cannot be changed
String is immutable

+ is used to concatenate
"""
