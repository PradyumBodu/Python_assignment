def gen():
    num=0
    count=0
    while count<10:
        yield num
        num+=2
        count+=1

for n in gen():
    print(n)