import random

print(sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0))

colour = ["red", "blue", "green", "yellow", "purple", "orange", "white", "black"]
cols = (list(map(lambda x: colour[random.randint(0,len(colour)-1)], range(0,50))))
print(cols)
