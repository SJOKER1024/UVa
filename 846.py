#UVa 846
case=int(input())
for i in range(case):
    x,y = (int(v) for v in input().split())
    if x==y:
        print("0")
    else:
        d=int((y-x)**(0.5))
        if d**2==y-x:
            print(2*d-1)
        elif y-x-d**2 <= d:
            print(2*d)
        else:
            print(2*d+1)
