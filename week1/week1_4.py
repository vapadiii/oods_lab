print('*** Minesweeper ***')
field = [ word.split(' ') for word in input('Enter input(5x5) : ').split(',') ]

print('\n')
for arr in field:
  print(arr)
print('\n')

def checkBoom(nfield, row, col):
    if (row == 0 and col == 0):
      nfield[row][col+1] += 1
      nfield[row+1][col] += 1
      nfield[row+1][col+1] += 1
    elif (row == 0 and col == 4):
      nfield[row][col-1] += 1
      nfield[row+1][col-1] += 1
      nfield[row+1][col] += 1
    elif (row == 4 and col == 0):
      nfield[row-1][col] += 1
      nfield[row-1][col+1] += 1
      nfield[row][col+1] += 1
    elif (row == 4 and col == 4):
      nfield[row-1][col] += 1
      nfield[row-1][col-1] += 1
      nfield[row][col-1] += 1
    elif (row == 0):
      nfield[row][col-1] += 1
      nfield[row][col+1] += 1
      nfield[row+1][col-1] += 1
      nfield[row+1][col] += 1
      nfield[row+1][col+1] += 1
    elif (row == 4):
      nfield[row][col-1] += 1
      nfield[row][col+1] += 1
      nfield[row-1][col-1] += 1
      nfield[row-1][col] += 1
      nfield[row-1][col+1] += 1
    elif (col == 0):
      nfield[row-1][col] += 1
      nfield[row-1][col+1] += 1
      nfield[row][col+1] += 1
      nfield[row+1][col] += 1
      nfield[row+1][col+1] += 1
    elif (col == 4):
      nfield[row-1][col-1] += 1
      nfield[row-1][col] += 1
      nfield[row][col-1] += 1
      nfield[row+1][col-1] += 1
      nfield[row+1][col] += 1
    else:
      nfield[row][col-1] += 1
      nfield[row][col+1] += 1
      nfield[row+1][col-1] += 1
      nfield[row+1][col] += 1
      nfield[row+1][col+1] += 1
      nfield[row-1][col-1] += 1
      nfield[row-1][col] += 1
      nfield[row-1][col+1] += 1
      
    
newField = [[], [], [], [], []]
for ele, new_ele in zip(field, newField):
    for char in ele:
      if (char == '-'):
        new_ele.append(0)
      elif (char == '#'):
        new_ele.append(-100)

for row, arr in enumerate(newField):
  for col, ele in enumerate(arr):
    if (newField[row][col]) < 0:
      checkBoom(newField, row, col)
  
for i, arr in enumerate(newField):
  for j, ele in enumerate(arr):
    if ele < 0:
      newField[i][j] = '#'
    else:
      newField[i][j] = str(newField[i][j]) 

for arr in newField:
  print(arr)