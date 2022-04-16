
a=int(input("Enter the number:"))
for i in range(1,a+1):
    if (i%2==0):
        print(i)

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


def test(a):
    for i in a:
        if (i%2==0):
            print(i)

print(test((1,2,3,4,5,6,7,8,9,10)))


for i in range(7):
    if (i==3 or i==6 or i==1):
        continue
    print(i,end="")
print()

#Expected Output : 1 1 2 3 5 8 13 21 34
def test(a):
    x,y=0,1
    for i in range(a):
        if i==1:
            x,y=y,x+y
            print(x,y)
    print(i,end="")
print(test(10))

n=int(input("Enter the number:"))
for i in range(1,101):
    print(i,'x',n,'=',i*n)

