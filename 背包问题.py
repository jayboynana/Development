weight=[1,2,3,4]
prices=[2,4,41,7]
bag=5
my_dict={}
max_price=0
for i in range(len(weight)):
    if my_dict.get(bag-weight[i]) is not None:
        index=my_dict.get(bag-weight[i])
        if prices[index]+prices[i]>max_price or max_price==0:
            max_price=prices[index]+prices[i]
    else:
        my_dict[weight[i]]=i
print(my_dict)
print(max_price)
