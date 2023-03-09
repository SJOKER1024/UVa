#UVa 10300
x=int(input())
for i in range(x):
    p=0
    f=int(input())
    for j in range(f):
        a,b,c=(int(v) for v in input().split())
        p+=a*c
    print(p)
