# UVa10127
try:
    while True:
        x=int(input())
        for i in range(1,x+1):   
            if ((10**i)-1)%(9*x)!=0:
                continue
            else:
                print(i)
                break
except EOFError:
    pass
