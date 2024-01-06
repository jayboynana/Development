if __name__=="__main__":    #进制转换
    a=bin(8)#十进制转二进制
    b=hex(9)#十进制转十六进制
    c=oct(10)#十进制转八进制
    print(a,b,c)
    print(int(a,2))#2进制转10进制
    print(int(b,16))
    print(int(c,8))
