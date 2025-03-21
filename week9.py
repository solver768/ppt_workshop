"""
Wap to print maximum value in each and every row of a matrix
"""
l=[[2,9,1],[7,6,5],[3,4,8]]
for i in range(len(l)):
	mx=0
	for j in range(len(l[i])):
		if(l[i][j]>mx):
			mx=l[i][j]
	print(mx)
"""
output:
9
7
8
Saddle point :max element in the column of min element in the row of a matrix vice versa
#wap to print saddle point of a matrix
"""
def saddlePoint (l):
	for i in range(len(l)):
		n=len(l)
		mn=l[i][0]
		col=0
		for j in range(n):
			if l[i][j]<mn:
				mn=l[i][j]
				col=j
		k=0
		while(k<n):
			if l[k][col]>mn:
				break
			k=k+1
		if(k==n):
			print("Saddle point:",mn)
			return True
	return False
l=[[3,2,1],[6,5,4],[9,8,7]]
if not (saddlePoint(l)):
	print('NO saddle point')
"""
Output:
Saddle point: 7

Wap to print row number having maximum number of zeroes
"""
l=[[1,1,0,0],[1,1,1,0],[1,0,0,0],[1,1,1,1]]
mx=0
row=-1
for i in range(len(l)):
	c=0
	for j in range(len(l[i])):
		if l[i][j]==0:
			c+=1
	if(c>mx):
		mx=c
		row=i
print(row)
"""
output:
2

Wap to interchage minor diagonal elements with major diagonal elements values in a matrix:
"""
l=[[1,2,3],[4,5,6],[7,8,9]]
n=len(l)
for i in range(n):
	l[i][i],l[i][n-i-1]=l[i][n-i-1],l[i][i]
for i in range(n):
	for j in range(n):
		print(l[i][j],end=" ")
	print()

"""
output:
3 2 1 
4 5 6 
9 8 7 


Wap tp check given matrix is identity matrix or not
"""
def check_matrix(l,n):
	for i in range(n):
		for j in range(n):
			if((i==j and l[i][j]!=1 )or (i!=j and l[i][j]!=0)):
				return False
	return True 
l=[[1,0,0],[0,1,0],[0,0,1]]
if (check_matrix(l,len(l))):
	print('It is an identity matrix')
else:
	print('It is not an identity matrix')
"""
output:
It is an identity matrix


Wap to check given matrix is symmetric or not
"""
def check_symmetric(l):
	for i in range(len(l)):
		for j in range(len(l)):
			if l[i][j]!=l[j][i]:
				return False
	return True
l=[[1,2,3],[2,4,5],[3,5,3]]
if(check_symmetric(l)!=False):
	print(" Symmetric")
else:
	print("Not a symmetric")
"""
output:
 Symmetric
"""
