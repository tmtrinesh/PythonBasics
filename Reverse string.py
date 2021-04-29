txt = ("Trinesh")[::-1]
print(txt)


def my_function(x):
    return x[::-1]
mytxt = my_function("Trinesh")
print(mytxt)


x = lambda a :a+10
print(x(5))


x = lambda  a,b :a*b
print(x(5,6))

def fact(n):

    if n==0:
        return 1
    return n *fact(n-1)
result =fact(5)
print(result)


x = 0 | 1
print(x)


x = 1 | 0
print(x)


x = 1 | 2
print(x)


x = 2 | 5
print(x)


x = 2 & 1
print(x)


def square(a):
    return a*a

result = square(5)
print(result)

f = lambda a :a*a
result = f(5)
print(result)

f = lambda a,b:a+b
result = f(5,6)
print(result)


def update(n):
    return n*2
nums = [1,2,3,4,5,6,]
evens = list(filter(lambda n :n%2==0,nums))
doubles =list(map(update,evens))
print(doubles)
#map reduce

from functools import  reduce


nums = [1,2,3,4,5,6,]
evens = list(filter(lambda n :n%2==0,nums))
doubles =list(map(lambda n: n*2,evens))
print(doubles)
sum = reduce(lambda a,b :a+b,doubles)
print(sum)


#decorators
def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a  #swapping
        return func(a,b)
    return inner

div = smart_div(div)

div(2,4)





