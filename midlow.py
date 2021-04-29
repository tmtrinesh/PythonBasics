pos = -1

def search(list,n):

    l= 0
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid;
            else:
                u = mid;






list = [5,8,4,9,7,1,7,4,4,5,6,66,6,67,7,76,7,]
n = 7

if search(list,n):
    print("Found at",pos+1)
else:
    print("Not found")