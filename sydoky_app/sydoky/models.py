#
# Описывем понятие поле судоку
# а так же функцию или метод для
# проверки корректности решения
grid = [[5, 0, 9, 0, 0, 0, 4, 0, 0],
        [7, 0, 8, 3, 0, 4, 9, 0, 0],
        [6, 0, 1, 0, 0, 0, 7, 3, 0],
        [4, 6, 2, 5, 0, 0, 0, 0, 0],
        [3, 8, 5, 7, 2, 0, 6, 4, 9],
        [1, 0, 7, 4, 0, 8, 2, 0, 0],
        [2, 0, 0, 1, 0, 0, 0, 0, 4],
        [0, 0, 3, 0, 4, 0, 0, 8, 7],
        [0, 7, 0, 0, 5, 3, 0, 0, 6]]

gameOver = False

def victory():
      for i in range(9):
          row = set()
          col = set()
          for j in range(9):
              row.add(grid[i][j])
              col.add(grid[j][i])

          if len(row) != 9 or len(col) != 9:
               return False

      for i in range(0, 9, 3):
          for j in range(0, 9, 3):
              kyb = set()
              for dx in range(3):
                  for dy in range(3):
                      kyb.add(grid[i + dx][j + dy])

              if len(kyb) != 9:
                  return False

      return True