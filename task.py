
str1="abcdd"
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


txt="python is a interpatter language, python quick to learn"
a=txt.find('language')
b=txt.capitalize()
c=txt.split()
d=txt.casefold()
e=txt.center(150)
f=txt.count('python',5,10)
str=('hello,welcome to my world.')
o=str.isascii()
print(o)


n=int(input("Enter the value:"))
fact = 1
while(n > 1):
	fact=fact * n
	n -= 1
print(fact)


def math(a):
	count=1
	for i in range(2,a+1):
		a=i+1
		count=count+i
		print(a)


l=math((10))
print(l)

def math(x):
	sum=0
	for i in range(0,x+1):
		sum=sum+i*i*i
	return sum
x=int(input("Enter the value:"))

print(math(x))




