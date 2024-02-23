# P1421 小玉买文具
import math

a,b = map(int,input().split())
a = a*10
count = math.floor((a+b)/19)
print(count)