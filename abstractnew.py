lst = [3,4,5,6,7,9]
print(lst[0])


for i in range(4):
    for j in range(4):
        print("Trinesh",end = " ")
    print()




for k in range(5):
    if k == 2:
        break
    print("trinesh",k)



for k in range(5):
    if k == 2:
        continue
    print("trinesh",k)



for i in range(4):
    print("Trinesh", end=" ")
print()
for j in range(4):
        print("Trinesh",end = " ")
print()




for b in range(1,21):
    if b %5!=0:
        print(b)


        


num = int(input(print("enter a number ")))
for a in range(2,num):
    if num % a == 0:
        print("not prime")
        break
    else:
        print("prime")




