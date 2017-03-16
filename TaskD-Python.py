from functools import reduce

squaresRange = list(map(lambda z: z * z, range(1,31)))
print(squaresRange)

l=[15, 18, 2, 36, 12, 78, 5, 6, 9]
print (reduce(lambda x, y: x + y, l) / len(l))

