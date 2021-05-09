from jogo_da_velha import make_board, make_Movement,getValidInput, printBoard, checkMovement, checkWinner

from minimax import movimentAI

player = 0 #controla também player 1
board = make_board()
print(board)
ganhador = checkWinner(board)
while (not ganhador):
    printBoard(board)
    print("=========================")

    if(player == 0):
        i,j = movimentAI(board, player)
    else:
        i = getValidInput("Digita a linha: ")
        j = getValidInput("Digita a coluna: ")

    if(checkMovement(board, i , j)):
        make_Movement(board, i , j, player)
        player = (player + 1)%2
    else:
        print("Posição já ocupada")
    
    ganhador = checkWinner(board)

print("=========================")
printBoard(board)
print("Ganhador é o player: ", ganhador)
print("=========================")
