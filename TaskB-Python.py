import random

colour = ["red", "blue", "green", "yellow", "purple", "orange", "white", "black"]
random_colours = (list(map(lambda x: colour[random.randint(0,len(colour)-1)], range(0,50))))
colourCount = (list(filter(lambda x: x == 'red', random_colours)))
print(colourCount)