

print(list(range(-10,-5,2)))

#print(list(range(2,10,2)))
#for i in range(2,10,2):
  #  print(i)

for i in range(5):
   print(i)

#l=[1,2,3,45,9,8,]
#print(l[4])

list1=(44,"Trinesh",59,69)
print(len(list1))
print(list1)

list2=list("Trinesh")
print(list2)

#print(len("trinesh"))
#print(max("abcdegh"))
#print(min("Trinesh"))

s="Trinesh"
for i in s:
    print(i)
    #print(s,end="\n")
    #print(s,end="")
    #print(s,end="foo")
s="welcome to my world"
print("welcome".isupper())

list3 =[2,3,4,1,8]
print(sum(list3))

#class myclass:
   # __a=10
    #def disp(self):
    #    print(self.__a)
     #   obj=myclass()
      #  obj.disp()
       # print(myclass.__a)

class ABC:
    def display(self):
        None


from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def display(self):
        None
        class B(A):
            def display(self):
                print("This is display method")
        obj=B()
        obj.display()









