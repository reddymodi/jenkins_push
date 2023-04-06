n=[4,6,7,8,3,12,17,19,22]
k=sorted(n)
e=[]
o=[]
for i in k:
    if i%2==0:
        e += [i]
    else:
        o += [i]
print("your list is : ",n)
print("even largest no:",e[len(e)-1])
print("odd largest no: ",o[len(o)-1])
