# UVA 100
list1=[0]
for i in range(1,1000000):
  c = 1
  while i!=1:
    if i%2==1:
      i=3*i+1
      c += 1
    else:
      i=i//2
      c += 1
  list1.append(c)
try:
  while True:
    x,y = (int(v) for v in input().split())
    a=min(x,y)
    b=max(x,y)
    print(x,y,max(list1[a:b+1]))
except EOFError:
  pass    
