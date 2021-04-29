def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst=[20,30,40,50,60,70,80,90,1000,657,879]
even,odd = count(lst)

def fib(n):
    a =0
    b=1

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for j in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)


fib(5)



def fact(k):
    f=1

    for j in range(1,k+1):
        f=f*j
    return f
x=4

result = fact(x)
print(result)

import sys
sys.setrecursionlimit(250)
print(sys.getrecursionlimit())

i=0

def greet():
    global i
    i+=1
    print("Hello",i)
    greet()


greet()


