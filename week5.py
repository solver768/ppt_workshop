"""  Loops:
----------------------------------------------------
an iterative block of code is know as loops 
loops are while , for 
for loop :
syntax :
for <var> in <sequence> :
    -------------------
    block of statements
    -------------------
sequence:
string:
for <var> in <string>:
      code to be iterate
range:
for<var> in range(<start>,<end>,<step>)
      code to be iterate
"""
#Sum of 5 first five natural numbers
Sum=0
for i in range(1,6,1):#sum 1+2+3+4+5
    print(i,end=" ")
    Sum+=i
print("\nSum of first five natural numbers:",Sum);
"""
output:
-----------------------------------------
1 2 3 4 5 
Sum of first five natural numbers: 15
-----------------------------------------
"""
#program to print numbers from 20 to 11 in reverse order
Sum=0
for i in range(20,10,-1):#20-11
    print(i)

"""
output:
---------------------------------------
20
19
18
17
16
15
14
13
12
11
----------------------------------------
"""
#range without start and step
for i in range(5):#range value
    print(i)
'''
output:
0
1
2
3
4

'''
"""
note: in pyhton print statement include the \n property by default cursor move to next new line
to print multiple print statements in single line we end function 'end=" "'
"""
#range without step
for i in range(5,11):
  print(i,end="  ")
"""
output:
---------------------
5  6  7  8  9  10  
---------------------
"""
#read value form user and print their average
Sum=0                           
print("Enter five numbers to get their average:")
for i in range(5):                  #Sum=0  ,i=0         #Sum=1,i=1   #Sum=3,i=2   #Sum=6,i=3  #Sum=10,i=4 #Sum=15,i=5
  number=int(input("Number:"))      #Number:1            #Number:2     Number:3     Number:4    Number:5    exit
  Sum+=number                       #Sum=0+1=1           #Sum=1+2=3    Sum=3+3=9    Sum=6+4=10  Sum=10+5
average=Sum/5  #calculate average value =>15/5=3.0
print("Average=",average)#prints "Average= 3.0"

"""
output:
---------------------------------------------
Enter five numbers to get their average:
Number:1
Number:2
Number:3
Number:4
Number:5
Average= 3.0
----------------------------------------------
"""
#PRINT A PROGRAM TO PRINT ALL ODD NUMBERS FROM 1 TO 50
for i in range(1,50,2):
  print(i,end=" ")

"""
output:
-------------------------------------------------------------------------------
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 
-------------------------------------------------------------------------------
"""

#PRINT THE FIRST 10 TERM S OF MULTIPLICATION TABLE FOR A GIVEN NUMBER
number=int(input("Enter number:"))#asks user input ( Enter number:5)                                                  5,6,7,8,9,10
for i in range(1,11):                              #i=1              i=2                i=3                i=4               ==>i=10                 ==>i=11
    print("%d * %2d = %2d"%(number,i,number*i))    #print 5 * 1 = 5  prints 5 * 2 = 10  prints 5 * 3 = 15  prints 5 * 4 = 20 ==> prints 5 * 10 = 50     exit

"""
output:
----------------------------
Enter number:5
5 *  1 =  5
5 *  2 = 10
5 *  3 = 15
5 *  4 = 20
5 *  5 = 25
5 *  6 = 30
5 *  7 = 35
5 *  8 = 40
5 *  9 = 45
5 * 10 = 50
---------------------------
"""
#CHECHK WHETHER THE NUMBER IS PRIME OR NOT
number=int(input("Enter number:"))        #case 1,number=4                        case 2,number=5
f=1                                       #f=1 consider flag =1                   f=1 consider flag =1
if(number!=1):                            #number!=1==>4!=1 -->True               number!=1==>5!=1 -->True 
 for i in range(2,int(number/2)+1):       #i=2                                    i=2          =>i=
  if(number%i==0):                        #4%2==0 True                            5%2==0 False
    f=0                                   #f=0                                    skip
    break                                 #break==>exit loop                      skip
if(f and number!=1):                      #f=0 and 4!=1 False and True -->False
  print(number,"is a prime number")       #skip
else :                                    #executed
    print(number,"is not a prime number") #prints 4 is not a prime number

"""
output:
-------------------------------------------
Enter number:4
4 is not a prime number
--------------------------------------------
Enter number:5
5 is a prime number
-------------------------------------------
Enter number:1
1 is not a prime number
------------------------------------------
"""While



i=20
while (i>=11):
  print(i,end=" ")
  i=i-1
print(i)
"""
output:
--------------------------------------
20 19 18 17 16 15 14 13 12 11 10
-----------------------------------
"""
#PRINT SUM OF ALL THE DIGITS OF GIVEN NUMBER
i=1234             #i=1234
sm=0               #sm=0
while (i!=0):      #i!=0  =>1234!=0 ->True              =>i!=0 ->123!=0 ->TRUE  =>i!=0 ->12!=0 ->TRUE  =>i!=0 ->1!=0 ->TRUE     =>i!=0 ->0!=0 ->False     
  sm+=i%10         #sm+=i%10 =>sum=0+1234%10=>0+4=>4    sm=4+123%10 =>4+3  =>7  sm=7+12%10 =>7+2  =>9    sm=9+1%10 =>9+1  =>10
  i=i//10          #i=i//10 =>1234//10 =>123            i=123//10=12            i=12//10=1               i=11//10=0  
print(sm)          #sm=10   => prints 10
"""
ouput:
---------------------------------
10
---------------------------------
"""

#PRINTS REVERSE OF A NUMBER
number=int(input("Enter number:"))#===>number=234
reverse=0                         #reverse=0
while(number!=0):                 #numner!=0 234!=0->True            23!=0->True
  digit=number%10                 #digit=number%10=234%10=4          digit=23%10=3
  reverse=reverse*10+digit        #reverse=0*10+digit=0+4            reverse=4*10+3=40+3=43
  number//=10                     #number//=10->number=234//10=23    number=23//10=
print(reverse)                    #
'''
output:
---------------------------------------
Enter number:234
432
---------------------------------------
"""


