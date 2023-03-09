# UVa10035
load=1
while load==1:
    ans=0
    x,y=(int(v) for v in input().split())
    if x==0 and y==0:
        load=0
        break
    elif x==0 and y!=0:
        print("No carry operation.")
    elif x!=0 and y==0:
        print("No carry operation.")
    else:
        x_s=str(x)
        y_s=str(y)
        if len(x_s)>len(y_s):
            y_s="0"*(len(x_s)-len(y_s))+y_s
        elif len(x_s)<len(y_s):
            x_s="0"*(len(y_s)-len(x_s))+x_s
        else:
            pass
        x_r=x_s[::-1]
        y_r=y_s[::-1]
        total=str(x+y)
        total_r=total[::-1]
        for i in range(len(x_r)):
            if int(x_r[i])+int(y_r[i])>9:
                ans+=1
            elif int(x_r[i])+int(y_r[i])==9 and int(total_r[i])==0:
                ans+=1
            else:
                pass
        if ans==0:
            print("No carry operation.")
        elif ans==1:
            print("1 carry operation.")
        else:
            print(str(ans)+" carry operations.")
