#UVa 1583
list1=[0] *100100
for i in range(100001,0,-1):
    x=str(i)
    m=i
    for j in range(len(x)):
        m+=int(x[j])
    list1[m]=i
case=int(input())
for k in range(case):
    t=int(input())
    print(list1[t])
