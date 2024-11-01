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
    'scores'=[]
}







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
