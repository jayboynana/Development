n = int(input())
s = list(map(int, input().split(" ")))
for i in range(len(s)-1):
    min_index = i
    for j in range(i+1,len(s)):
        if s[j] < s[min_index]:
            min_index = j
    s[i],s[min_index] = s[min_index],s[i]
for i in s:
    print(i,end=' ')