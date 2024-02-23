n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

n_ = n
count1 = 1
count2 = 1
count3 = 1
while n_-a[0] > a[0]:
    n_ -= a[0]
    count1 += 1
# print(count1)
n_ = n
while n_-b[0] > b[0]:
    n_ -= b[0]
    count2 += 1
# print(count2)
n_ = n
while n_-c[0] > c[0]:
    n_ -= c[0]
    count3 += 1
# print(count3)
print(min([(count1+1)*a[1],(count2+1)*b[1],(count3+1)*c[1]]))