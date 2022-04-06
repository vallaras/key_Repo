str='vallarasu'
l=list(str)
d=[]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j] and l[i] not in d:
            d.append(l[i])
print(d)


str1="search the word in the sentance"
lis=str1.split(" ")
print(lis)
txt=[]
for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]==lis[j] and lis[i] not in txt:
            txt.append(lis[i])

print(txt)



def string(a):
    d={}
    for i in a:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    return d
print(string("aabbccc"))





txt="aabbccc"
d=list(txt)
c=[]
cou=[]

for i in range(0,len(d)):
    for j in range(i+1,len(d)):
        if d[i]==d[j]:
            if d[i] not in c:
                c.append(d[i])

for i in range(0,len(c)):
    count=0
    for j in range(0,len(d)):
        if c[i]==d[j]:
            count=count+1
    cou.append([c[i],count])

print(cou)



txt="aabbccc"
lis=list(txt)
lis1=list(set(lis))
res=[]
for i in range(0,len(lis1)):
    res.append([lis1[i],lis.count(lis1[i])])
print(res)
print(lis1)



txt="teen"
print(list(set(list(txt))))
