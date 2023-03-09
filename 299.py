# UVA 299
x=input()
try:
    while True:
        y=int(input())
        if y==0 or y==1:
            a=[int(v) for v in input().split()]
            print("Optimal train swapping takes 0 swaps.")
        else:
            a=[int(v) for v in input().split()]
            b=[]
            for i in range (1,y):
                b.append(sum([(1 if u > a[i] else 0) for u in a[:i]]))
            print("Optimal train swapping takes "+str(sum(b))+" swaps.")
except EOFError:
    pass
