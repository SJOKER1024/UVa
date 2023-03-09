# UVa10110
try:
    while True:
        x=int(input())
        if x==0:
            break
        else:
            if (x**0.5)-int(x**0.5)==0:
                print("yes")
            else:
                print("no")
except EOFError:
    pass
