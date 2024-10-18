"""#identity operatos 
->  is and is not are the identity operators 
->  is will returns True if the variables points to same object (same address)
    orelse returns False
->  is not will return True if the variables points to different objects(different address)
"""
#program:

x=10
y=10
z=20
res=x is not z
print(id(x),id(y),id(z))
print(res)
print(x is y)

"""
output:

131364162978320 131364162978320 131364162978640
True
True
"""
""" Bitwise operators
->  &  - and 
->  |  -  or
->  ~  - negation
->  ^  - EOR
->  << - left shift
->  >> - right shift
=>  we have binary octal decimal and hexadecimal number system
    we usually use decimal number system in our daily life but,
    computer owns only binary number system. 
    Internally bitwise operators helps to perform operation on binary numbers
"""
# & - operator
# program 
rs= 42 & 26
print(rs)

"""
Explaination:
32    16   8     4    2     1
2^5   2^4  2^3  2^2   2^1   2^0
1     0    1     0    1     0     = 42
0     1    1     0    1     0     = 26
_______________________________________
0     0    1     0    1     0     = 10

output:

10

"""

#OR program
res = 15 | 12
print(res)


"""
Explaination:
32    16   8    4    2     1
2^5   2^4  2^3  2^2  2^1   2^0
0     0    1    1    1     1   = 15
0     0    1    1    0     0   = 12
___________________________________
0     0    1    1    1     1   = 15

output:

15

"""

#EOX program
res = 12 ^ 10
print(res)

"""
Explanation:
32    16   8    4    2     1
2^5   2^4  2^3  2^2  2^1   2^0
0     0    1    1    0     0   = 12
0     0    1    0    1     0   = 0
____________________________________
0     0    0    1    1     0   = 6

output:
6
"""
#Negation prograsm
res=~2
print(res)

"""
Explanation:===>  ~2=~(2+1)=-3
32    16   8    4    2     1
2^5   2^4  2^3  2^2  2^1   2^0
  0     1    0    0    1     0    = 18
                          +   1
        1    0     0   1     1    
        ________________1_______
             1     1    1     0
output:
-3




"""
"""One way selection

=>if statement 
   if can be used if there is only one possible condition


   expression--->true---->statement_
      |                             |
      |-> false------------>end<----|
"""
#if program for order a food if it exceeds the amount(500) "here is discount of 10% and checkout the bill"
Bill=int(input("Enter the amount:"))
Total_bill=Bill
if(Bill>500):
  print("you got discount of 10%")
  Total_bill=Bill-Bill*0.1
  print("--------------------")
  print("Bill amount=",Bill)
print("Total bill=",Total_bill)

"""
output:

Enter the amount:340
Total bill= 340


Enter the amount:540
you got discount of 10%
--------------------
Bill amount= 540
Total bill= 486.0
"""


#program to get message if the charging is below 30% to plugin charger
charge=int(input("Enter the ")














"""
two way selection
if else statement
syntax:
if <expression>:
  staement block
else:
  statement block


"""
# program to get bill 
amount=int(input("Enter the amount;"))
if(amount>500):
  pass
else:
  amount+=40
print("Total amount:",amount)



"""
output:

Enter the amount:340
Total amount: 380

Enter the amount:520
Total amount: 520
"""
#program to print the login successful alert
user_ID=input("User ID:")
password=input("Password:")
user_details="23481A4289  webcap"
if(user_ID in user_details and password in user_details):
  print("You have successfully logged in.\nWelcome to my python programming")
else:
  print("Invalid User ID or Password")

"""
output:

User ID:23481A4289
Password:webcap
You have successfully logged in.
Welcome to my python programming

"""
"""
Multiway selection
syntax:
if <expression>:
   statement block
elif <expression1>:
   statement1 block
else:
   statement2 block
"""
#program to print whether the given number is positive,negative or zero
number=int(input("Enter any Integer Number:"))
if(number>0):
  print("It's  a positive number")
elif(number<0):
  print("It's a negative number")
else:
  print("It's Zero")

"""
output:

Enter any Integer Number:3
It's  a positive number

Enter any Integer Number:0
It's Zero

Enter any Integer Number:-9
It's a negative number

"""
#program to print direction for symbol
Symbol=input("Enter direction:").upper()
if(Symbol=='N'):
  print("North")
elif(Symbol=='S'):
  print("South")
elif(Symbol=='E'):
  print("East")
elif(Symbol=='W'):
  print("West")
else:
  print("Invalid input")

"""
output:

Enter direction:n
North


"""




