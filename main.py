from render import renderMap
from utility import readFile, readLevels

levels = readLevels()

# Choose lvl
print("Levels:")
for level in levels:
    print(level.replace('.json', ''))
userChoose = input("Choose lvl: ")

# Render map
data = readFile('./levels/' + userChoose + '.json')
renderMap(data)






