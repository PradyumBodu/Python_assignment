l=[10,20,20,10,50,60,10]
d={}

for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)