#UVa 401
dict={"A":"A","B":"","C":"","D":"","E":"3","F":"","G":"","H":"H","I":"I","J":"L","K":"","L":"J","M":"M","N":"","O":"O","P":"","Q":"","R":"","S":"2","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"5","1":"1","2":"S","3":"E","4":"","5":"Z","6":"","7":"","8":"8","9":""}
while True:
    try:
        x=input()
        y=x[::-1]
        z=""
        for i in range(len(y)):
            z+=dict[y[i]]
        if x==y and x==z:
            print(x+" -- is a mirrored palindrome.")
        elif x==y and x!=z:
            print(x+" -- is a regular palindrome.")
        elif x!=y and x==z:
            print(x+" -- is a mirrored string.")
        else:
            print(x+" -- is not a palindrome.")
    except EOFError:
        break
    else:
        print("")
