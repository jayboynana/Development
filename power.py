def power(x,n):
    if n==0:
        return 1
    if n<0:
        return 1/power(x,-n)
    if n%2==0:
        half=power(x,n/2)
        return half*half
    return x*power(x,n-1)
def power_2(x,n):
    if n==0:
        return 1
    if n<0:
        x=1/x
        n=-n
    ans=1
    ex=x
    while n>0:
        if n%2==1:
            ans*=ex
        ex*=ex
        n//=2
    return ans
#二进制幂求阶乘
def factorial(n):
    result = 1
    base = 2
    while n > 0:
        if n % base == 1:
            result *= base
        base *= base
        n //= 2
    return result
if __name__=="__main__":
    res = power_2(2, 10)
    print(res)
    
    