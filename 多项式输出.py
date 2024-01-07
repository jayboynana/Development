n = int(input())
input_data = list(map(int, input().split()))
result = ""
if n >= 1:
    j=0
    for i in range(n,0,-1):
        if input_data[j]!=0:
            if abs(input_data[j])!=1:
                result = result + str(input_data[j])

            if input_data[j]==-1:
                result=result+"-"
            result=result+"x^"+str(i)
        j+=1
        if input_data[j]>0:
            result=result+"+"

last_data = input_data[len(input_data) - 1]

if last_data!=0:
    result = result + str(last_data)
print(result)

