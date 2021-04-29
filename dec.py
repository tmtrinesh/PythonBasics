nums = [7,8,9,5,0,9,8,6,4]
it = iter(nums)
print(it.__next__())
print(it.__next__())# for every iteration one num ll be added
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

print(next(it))





class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1


            return val
        else:
            raise StopIteration

values = TopTen()

for i in values:
    print(i)