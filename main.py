import os

from board import renderMap
from utility import readFile, readLevels
from game import gameInit

levels = readLevels()

# Choose lvl
print("Levels:")
for level in levels:
    print(level.replace('.json', ''))
userChoose = input("Choose lvl: ")

# Render map
data = readFile('./levels/' + userChoose + '.json')
renderMap(data)

# Game loop
gameInit(data)