blanks = [ (x,y) for x in range(1,4) for y in range(1,4)]
matrix = [[ " " for x in range(3)] for y in range(3)]
symbols = ['X', 'O']
def afficher():
    print("---------")
    print("|" ,' '.join(matrix[0][0:3]), "|")
    print("|" ,' '.join(matrix[1][0:3]), "|")
    print("|" ,' '.join(matrix[2][0:3]), "|")
    print("---------")
def game_state():
    for x in range(0, len(matrix)):
        #rows
        if all([matrix[0][x] == matrix[x][y] for y in range(len(matrix))]) and matrix[0][x] in symbols:
            print(matrix[0][x],"wins")
            return 1
        #cols
        if all([matrix[x][0] == matrix[y][x] for y in range(len(matrix))]) and matrix[x][0] in symbols:
            print(matrix[x][0],"wins")
            return 1
        #diagonals
        if x == 1:
            if matrix[0][0] == matrix[x][x] and  matrix[2][2] == matrix[x][x] and matrix[x][x] in symbols:
                print(matrix[x][x],"wins")
                return 1
            elif matrix[0][2] == matrix[x][x] and  matrix[2][0] == matrix[x][x] and matrix[x][x] in symbols:
                print(matrix[x][x],"wins")
                return 1
    return 0
afficher()
while len(blanks) > 0:
    z = input("Enter the coordinates:")
    x = z.split()[0]
    y = z.split()[1]
    if x.isnumeric() and y.isnumeric():
        x = int(x)
        y = int(y)
        if 1 <= x <= 3 and 1 <= y <= 3:
            if (x,y) in blanks:
                blanks.remove((x,y))
                matrix[x-1][y-1] = symbols[len(blanks) % 2 -1]
                afficher()
                if game_state() == 1:
                    break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")
else:
    if game_state() == 0:
        print("Draw")
