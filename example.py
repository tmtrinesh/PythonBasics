a = 6
b = 0
k = int(input("Ente a number"))
print(k)


try:
    print("resource open")
    print(a/b)

except ZeroDivisionError as e:
    print("Hey , you cannot devide  a number by zero")
except ValueError  as e  :
    print("invalid input")


except Exception as e:
    print ("Trinesh")

finally:
    print("resorce closed")