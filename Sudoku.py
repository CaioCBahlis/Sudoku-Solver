Running = 1


def Screen(Table): #Prints the Solved Sudoku Board (totally optional)
    print("―" * 13)
    for i in range(len(Table)):
        if i % 3 == 0:
            print("―" * 13)
        for j in range(len(Table[i])):
            if (j) % 3 == 0:
                print("|", end="")
            print(Table[i][j], end="")
        print("|")
    print("―" * 13)
    return 0



#Verification Part, check for empty squares in the board
# In case it doesnt find any, it means the boards is complete and the game is won
def FindEmptySpace(Table):
    for i in range(len(Table)):
        for j in range(len(Table[i])):
            if Table[i][j] == 0:
                return [i, j]
    return False


def ValidateNum(num, Table): #Validates if a num can go in a square
    Linha, Coluna = FindEmptySpace(Table)

    if num in Table[Linha]:
        return False

    if num in [Table[i][Coluna] for i in range(len(Table))]:
        return False

    Box = [
        [Table[(((Linha // 3) * 3) + i)][(Coluna // 3) * 3], Table[(((Linha // 3) * 3) + i)][(3 * (Coluna // 3)) + 1],
         Table[(((Linha // 3) * 3) + i)][(3 * (Coluna // 3)) + 2]] for i in range(3)]

    for i in range(len(Box)):
        if num in Box[i]:
            return False

    return True

#Systematically guesses valid numbers and in case none of them are valid
# Backtracks and tries other numbers
def BackTrack(Table):
    global Running
    if FindEmptySpace(Table) == False:
        Running = 0
        return 0

    Line, Col = FindEmptySpace(Table)

    for num in range(1, 10):
        if ValidateNum(num, Table):
            Table[Line][Col] = num
            BackTrack(Table)

        if Running == 1:
            Table[Line][Col] = 0
        else:
            return Table
