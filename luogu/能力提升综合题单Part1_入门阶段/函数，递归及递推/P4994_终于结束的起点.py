# ac 80% 超时

m = int(input())

a ,b = 0,1
flag = True
n = 1
while flag:
    a,b = b,a+b
    if a != 1:
        if a%m==0 and b%m==1:
            print(n)
            break
    n += 1

# fp = [0] * 100000
# i = 1
# # flag = True
# def ff(i):
#     if fp[i]:
#         return fp[i]
#     if i == 1 or i == 2:
#         fp[i] = 1 % m
#         return fp[i]
#     else:
#         fp[i] = (ff(i-1) + ff(i-2)) % m
#         return fp[i]
# while (ff(i) != 0 or ff(i+1) != 1):
#     i += 1
# print(i)