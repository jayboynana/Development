# 成功ac

s = input()
m = s[-1]
if m == 'X':
    m = 10
c = 0
for i,num in enumerate(s[:s.rfind('-')].replace('-',''),1):
    c += i*int(num)
if (c % 11) == int(m):
    print('Right')
elif (c % 11) == 10:
    print(s[:-1]+'X')
else:
    print(s[:-1]+str(c % 11))