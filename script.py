a=0
b=1

print(a,b)
for x in range(7):
    temp=a+b
    a=b
    b=temp
    
    print(temp)