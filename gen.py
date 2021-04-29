def topten():
    n=1

    while n <= 10:
        sq = n*n
        yield sq
        n += 0.5




values = topten()
for i in values:
    print(i)

