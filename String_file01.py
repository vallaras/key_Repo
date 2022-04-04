
d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d4={}
for d in(d1,d2,d3):d4.update(d)
print(d4)

d1={1:10,2:20,3:30,4:40}
for i in d1:
    print(d1[i])

a="vallaras'u" "laptop"
print(a)
b='c:\new'
print(b)

s = "I am A pRoGraMMer"
s.swapcase()
print(s)

a=int(input("Enter the number:"))
for i in range(1,11):
    print(i,"x",a,"=",a*i)

a=int(input("Enter the number:"))
for i in range(1,a+1):
    if (i%2==0):
        print("even number:",i)

count=1
while count<=5:
    print("welcome")
    count=count+1

def test(a):
    l=[]
    for i in a:
        l.append(i)
    return l
print(test((1,2,3,4,5,6,7,8,9,10)))

for k in range(1,10):
    for y in range(1,10):
        print(k*y,end="")
    print()

def myfun():
    a="hyundai multinational company"
    b="i20"
    return[a,b]
l=myfun()
print(l)
def myfun(a):
    ding = len(a)
    count = 0
    for char in a:
        count=count+1
    return count
print(myfun('TheNorthernLights   '))

def myfun(a):
    d={}
    #a="google.com"
    for i in a:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    return d
    #b=[i.lower() for i in a]
    #print(b)
print(myfun("vallarasu"))

def string(a):
    d={}
    for i in a:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    return d
print(string("google.com"))



def myfun(a):
    if len(a) < 2:
        print("")
    return a[0] + a[-1]


print(myfun("good"))

lst=[]
for i in range(0,3):
    a=int(input("enter the student id:"))
    b=input("enter the student name:")
    c=input("enter the student dep:")
    d=int(input("enter the student year:"))
    lst.append([a,b,c,d])
    print(lst)
class py_solution:
    def myfun(self, s):
        return ' '.join(reversed(s.split()))
print(py_solution().myfun('vallarasu M'))




string = "tutorialspoint"
duplicates = []
for char in string:
   if string.count(char) > 1:
       if char not in duplicates:
          duplicates.append(char)
print(duplicates)



str1="teen"
lis=list(str1)
res=[]
for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]==lis[j] and lis[i] not in res:
            res.append(lis[i])

print(res)



str1="search the word in the sentance"
lis=str1.split(" ")
res=[]
for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]==lis[j] and lis[i] not in res:
            res.append(lis[i])

print(res)


lis=[1,1,1,1]
a=[]
for i in range(0,len(lis)):
    print(i)
    print('____________')
    for j in range(i+1,len(lis)):
        print(j)
        print('___')
        if lis[i]==lis[j] and lis[i] not in a :
            a.append(lis[i])
print(a)



