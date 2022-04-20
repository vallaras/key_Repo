letter='z'
a=letter*10
print(a)

x='Hello World'
c=x.upper()
c=x.lower()
c=x.split()
t='hi this is a string'
c=t.split('i')
print(c)

print('this is a string{}'.format('INSERT'))
print('this {2} {1} {0}'.format('Bike','quick','pickup'))
print('this {c} {b} {a}'.format(a='color',b='very',c='good'))

a=1000
b=12
c=a/b
#print(c)
print("the result was {e:15.1f}".format(e=c))

name='vallarasu'
print("He is name {}".format(name))
print(f"Hello, he is name was {name}")

n='gopi'
age=18
print(f"{n} is a {age} year old.")
print('This is a string with an {p}'.format(p='insert'))
