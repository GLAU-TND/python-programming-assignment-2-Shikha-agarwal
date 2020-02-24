y=eval(input())
y=[str(i) for i in y]
y.sort()
n=''
for i in range(len(y)-1):
       if y[i][0]==y[i+1][0] and len(y[i]<len(y[i+1])):
               a=y[i]
               y[i]=y[i+1]
               y[i+1]=a

for i in range(len(y)-1,-1,-1):
       n=n+y[i]
print(int(n))
