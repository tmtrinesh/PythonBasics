f = lambda a,b: a+b

result = f(5,6)

print(result)


from functools import reduce


nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n :n%2==0,nums)) #finds the evens
doubles = list(map(lambda n : n*2,evens))  #doubles the evens
print(doubles)
sum = reduce(lambda a,b : a+b,doubles)   #adds the doubles
print(sum)


class Computer:
    def __init__(self):
        print("in init")

    def config(self):
        print("i5,16gb,1TB")


com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)



Computer.config(com1)
Computer.config(com2)


com1.config()
com2.config()

print(type(com1))