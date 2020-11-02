#This is a sudoku solver script


sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


def verificar_posibilidad(y, x, test_number):
    pos = True
    if sudoku[y][x] == 0:
        for i in range(9):
            if sudoku[i][x] == test_number:
                pos = False
            elif sudoku[y][i] == test_number:
                pos = False
    else:
        pos = False
        
    return pos


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(verificar_posibilidad(0, 2, 9))


