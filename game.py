import os

from board import renderMap

def gameInit(data):
  # Setup
  position = [1, 1]
  data[1][1] = '*'
  os.system('clear')
  renderMap(data)

  # Game loop
  while True:
      # Input
      userMove = input("Move: ")
      # Logic
      if userMove == 'w':
          if (data[position[0]-1][position[1]] == '1'):
              break
          data[position[0]][position[1]] = '0'
          data[position[0]-1][position[1]] = '*'
          position[0] -= 1
      elif userMove == 's':
          if (data[position[0]+1][position[1]] == '1'):
              break
          data[position[0]][position[1]] = '0'
          data[position[0]+1][position[1]] = '*'
          position[0] += 1
      elif userMove == 'a':
          if (data[position[0]][position[1]-1] == '1'):
              break
          data[position[0]][position[1]] = '0'
          data[position[0]][position[1]-1] = '*'
          position[1] -= 1
      elif userMove == 'd':
          if (data[position[0]][position[1]+1] == '1'):
              break
          data[position[0]][position[1]] = '0'
          data[position[0]][position[1]+1] = '*'
          position[1] += 1
      elif userMove == 'q':
          break
      # Render
      os.system('clear')
      renderMap(data)