import math
def mySqrt(x):
    print("{:.2f}".format(x**0.5))

def mySqrt_binary(x):  #二分查找求根
    left=1
    right=x
    while right>=left34:
        mid=(left+right)//2
        if mid**2>x:
            right=mid-1
        elif mid**2<x:
            left=mid+1
        else:
            return mid
    return right
def mySqrt_new_ton(x):
    c=x
    x0=x
    xi=0.5*(x0+c)/x0
    while abs(xi-x0)>1e-2:
        x0 = xi
        xi=0.5*(x0+c/x0)
    return round(xi)
if __name__=="__main__":
    #mySqrt_1(10)
    #mySqrt_binary(x)
    print(mySqrt_new_ton(8))