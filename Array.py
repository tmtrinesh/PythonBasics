def greet():
    print("Hello")
    print("Trinesh")

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
greet()
result1,result2 = add_sub(5,4)
print(result1,result2)


def update(x):
    x=8
    print(id(x))
    print("x",x)
a=10
print(id(a))
update(a)
print("a",a)

def update(lst):
    print(id(lst))

    lst[2]=68
    print(id(lst))
    print("x",lst)

lst = [10,20,30]
print(id(lst))
update(lst)
print("lst",lst)


def add(a,b):
    c=a+b
    print(c)
add(5,6)

def person(name,age=18):
    print(name)
    print(age)

person('Trinesh',30)


def sum(a, *b):
    c=a

    for i in b:
        c = c+i

    print(c)

sum(1,2,3,4)


def emp(name,**data):
    print(name)
    print(data)

emp('trinesh',age=30,city='Davanagere',mob=4556769)

def emp(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)


emp('trinesh',age=30,city='Davanagere',mob=4556769)


n=10
print(id(n))

def something():
    n=9
    s=globals() ['n']
    print(id(s))
    print("in fun",n)


something()
print("outside",n)


