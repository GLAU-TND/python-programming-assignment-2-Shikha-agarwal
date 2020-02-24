y=eval(input())
b=[min(y)]
a=min(y)[-1]
y.remove(min(y))
for i in y:
      for j in y:
            if a==j[0]and j[-1]!=b[0][0]:
                  b.append(j)
                  a=j[-1]
                  y.remove(j)
                  break
b=b+y
print(b)
