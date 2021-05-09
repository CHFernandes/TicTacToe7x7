blank = " "
token = ["X", "O"]

def make_board():
    board = [
        [blank, blank , blank, blank, blank, blank, blank],
        [blank, blank , blank, blank, blank, blank, blank],
        [blank, blank , blank, blank, blank, blank, blank],
        [blank, blank , blank, blank, blank, blank, blank],
        [blank, blank , blank, blank, blank, blank, blank],
        [blank, blank , blank, blank, blank, blank, blank],
        [blank, blank , blank, blank, blank, blank, blank],
    ]
    return board
    

def printBoard(board):
    for i in range(7): 
        print("|".join(board[i]))
        if(i < 6):
            print("-------------")

def getValidInput(mensagem):
    try:
        n = int(input(mensagem))
        if (n >= 1 and n <= 7):
            return n - 1
        else:
            print("Numero precisa estar entre 1 e 7")
            return getValidInput(mensagem)
    except:
        print("Numero não valido")
        return getValidInput(mensagem)

def checkMovement(board, i , j):
    if(board[i][j] == blank):
        return True
    else:
        return False
    pass

def make_Movement(board, i , j, jogador):
    board[i][j] = token[jogador]

def checkWinner(board):
    #linha
    for i in range(7):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] 
        and board[i][2] == board[i][3] and board[i][3] == board[i][4] 
        and board[i][4] == board[i][5] and board[i][5] == board[i][6] 
        and board[i][0] != blank):
            return board[i][0]

    #coluna
    for j in range(7):
        if(board [0][j] == board[1][j] and board [1][j] == board [2][j] 
        and board [2][j] == board[3][j] and board [3][j] == board [4][j] 
        and board [4][j] == board[5][j] and board [5][j] == board [6][j] 
        and board[0][j] != blank):
            return board [0][j]

    #diagonal primaria
    if (board [0][0] != blank and board[0][0] == board[1][1] and board[1][1] == board[2][2]
        and board[2][2] == board[3][3] and board[3][3] == board[4][4]
        and board[4][4] == board[5][5] and board[5][5] == board[6][6]):
        return board [0][0]
    
    #diagonal secundaria
    if (board [0][6] != blank and board[0][6] == board[1][5] and board[1][5] == board[2][4]
        and board[2][4] == board[3][3] and board[3][3] == board[4][2]
        and board[4][2] == board[5][1] and board[5][1] == board[6][0]):
        return board [0][6]

    #verifica se ninguem ganhou
    for i in range (7):
        for j in range(7):
            if(board[i][j] == blank):
                return False

    return "Empate"
