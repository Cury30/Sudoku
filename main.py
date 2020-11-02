#This is a sudoku solver script
import numpy as np

sudoku = [[0,0,0,0,0,0,0,0,0],
          [0,4,5,0,7,0,9,2,0],
          [0,6,0,1,0,5,0,3,0],
          [0,0,4,3,8,1,6,0,0],
          [0,2,0,6,0,7,0,5,0],
          [0,0,3,5,9,2,4,0,0],
          [0,5,0,2,0,9,0,4,0],
          [0,9,6,0,1,0,7,8,0],
          [0,0,0,0,0,0,0,0,0]]


def possibility(y, x, test_number):
    for i in range(9):
        if sudoku[i][x] == test_number:
            return False
        elif sudoku[y][i] == test_number:
            return False
    grid_x = (x // 3) * 3
    grid_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[grid_y][grid_x] == test_number:
                return False
    return True


def solve_sudoku():
    for x in range(9):
        for y in range(9):
            if sudoku[y][x] == 0:
                for number in range(1,10):
                    if possibility(y,x,number):
                        sudoku[y][x] = number
                        solve_sudoku()
                        sudoku[y][x] = 0
                return
    print(np.matrix(sudoku))
    seguir= input("Mas?")
    if seguir == "n":
        exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solve_sudoku())


