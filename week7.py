"""String properties"""
"""
1.immutable-they cannot be changed 
whenever you try to modify new address is generated.
2.String concatination :joining two string with'+'
"""
msg1="hello "
msg2="world"
msg=msg1+msg2
print(msg)
ouput:
hello world
"""
3.String can be  repitiotion (multiplying string)
str="PYTHON"
print(3*str)#PYTHONPYTHONPYTHON
print(str*3)#PYTHONPYTHONPYTHON
print(3.5*str)#TypeError:can't multiply sequence by non-int of tye 'float'

****4.String Methods******
isalpha()-checks if all characters in string are alphabets
str.isalpha()#Returns True
isdigit()-checks if all characters in string are digits 
str.isdigit()-#Returns False
isalnum()-checks if all characters in string are alphabets or digits
islower()-checks if all characters in string are lower case characters 
isupper()-checks if all characters in string are uppercase characters
startswith()-checks if string starts with a value
endswith()-checks if string ends with a value"""
lang="Python"
print(lang.isalpha())
#True
num="12345"
print(num.isdigit())
#True
print(lang.isdigit())
#False
print(num.isalpha())
#False
pwd="hello123"
print(pwd.isalnum())
#True
print(num.isalnum())
#True
print(lang.isalnum())
#True
"""
5.Search and replace
find()-searches for a value,returns its position
replace()-replace one value with another
"""
s="Welcome to python programming"
print(s.find("python"))
#11
print(s.find("Python"))
#-1
print(s.replace("p","P"))
#Welcome to Python Programming 
print(s.find("Python",0,20))

"""
6.#trims whitespaces
lstrip()-removes whitespace from the left of string including \t
rstrip()-removes whitespace from the right of string including \t
strip()-removes whitespace from the left and right of string

"""
s="          welcome to python      programming"
print(s)
#          welcome to python      programming
print(s.lstrip())
#welcome to python      programming
s="welcome to python      programming                 "
print(s.rstrip())
#welcome to python      programming
s="                welcome to python      programming                 "
print(s.strip())
#welcome to python      programming


"""
7.split and partition
split()-split the string at a specified separator string
partition()-partitions string into 3 parts at first occurrence of specified string
"""
s="welcome to python programming"
print(s.split())
#['welcome', 'to', 'python', 'programming']
print(s.partition("python")
#('welcome to ', 'python', ' programming')

"""
8.join():
different than concatenation ,it joins string to each element of string except last.
"""
print("_".join(s))



"""
upper()-converts string to upper case 
lower()-converts string to lower case
capitialize()-converts first character of string to upper case
title()-converts first character of each word of string to upper case
swapcase()-swaps cases in the string
"""
fn="Ponduri "
ln="venkata Sai lakshmi Deepthi"
print(fn+ln)
#Ponduri venkata Sai lakshmi Deepthi
print(fn.upper())
#PONDURI 
print(ln.lower())
#venkata sai lakshmi deepthi
print(fn.lower().capitatalize())
#Ponduri 
print(ln.title())
#Venkata Sai Lakshmi Deepthi
print(ln.swapcase())
#VENKATA sAI LAKSHMI dEEPTHI

"""
9.
str()-converts an int,float or complex to string
int()-converts a numeric string to int
float()-converts a numeric string to float
complex()-converts a numeric string to complex

The built-in function chr() returns a string representating its Unicode value (known as code point)
ord()-does the reverse Unicode to string
"""
ord('a')
#97
ord('1')
#49
chr(99)
#c
chr(66)
#B
chr(65)
#A
chr(67)
#C
chr(90)
#Z

for i in range(65,90+1):
  print(i,"=",chr(i),end=" ")
  """
  65 = A 66 = B 67 = C 68 = D 69 = E 70 = F 71 = G 72 = H 73 = I 74 = J 75 = K 76 = L 77 = M
  78 = N 79 = O 80 = P 81 = Q 82 = R 83 = S 84 = T 85 = U 86 = V 87 = W 88 = X 89 = Y 90 = Z 
"""
  for i in range(1,127+1):
    print(i,'=',chr(i),end=" ")

name="deepthi"
for i in name:
  if(i!=name[len(name)-1]):
    print(i,"=",ord(i),end=",")
  else:
      print(i,'=',ord(i))
# d= 100,e = 101,e = 101,p = 112,t = 116,h = 104,i = 105


name="ponduri venkata sai lakshmi deepthi"
str=""
x=name[0]
for i in range(1,len(name)):
    if(x==(name[i].lower() or name[i].upper())):
       str+='$'
    else:
        str+=name[i]
print(x+str)
#ponduri venkata sai lakshmi dee$thi

"""
s=input()
fc=s[0]
r=fc+s[1:].replace(fc.lower(),'$').replace(fc.upper(),$)
print(r)
"""
#ponduri $enkata $ai $akshmi $eepthi 

s=input()
fc=s[0]
for i in range(len(s)):
    if(s[i]==fc.upper() or s[i]==fc.lower()):
        s=s[ :i]+'$'+s[i+1:]
r=fc+s[1:]
print(r)

"""
#rama raju ranga Raju
#rama $aju $anga $aju
"""

name="i am currently working on Python Programming"
str=""
word=name.split()
for s in word:
    if(len(s)>=3):
        if(s.endswith("ing")):
            str+=s.replace('ing','ly')
        else:
            str+=s+'ing'
    else:
        str+=s
    str+=" "
print(str)
#i am currentlying workly on Pythoning Programmly 
name="i am currently working on Python Programming"
str=""
word=name.split()
for s in word:
    if(len(s)>=3):
        if(s.endswith("ing")):
            str+=s+'ly'
        else:
            str+=s+'ing'
    else:
        str+=s
    str+=" "
print(str)

#i am currentlying workingly on Pythoning Programmingly 

"""









