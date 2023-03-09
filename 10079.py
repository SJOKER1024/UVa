# UVa10079
try:
    while True:
        x=int(input())
        if x<0:
            break
        else:
            print(1+(x*(x+1)//2))
except EOFError:
    pass
