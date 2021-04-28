from jogo_da_velha import cria_board, fazMovimento,getInputValido, printBoard, verificaGanhador, verificaMovimento



jogador = 0 #controla também jogador 1
board = cria_board()
print(board)
ganhador = verificaGanhador(board)
while (not ganhador):
    printBoard(board)
    i = getInputValido("Digita a linha: ")
    j = getInputValido("Digita a coluna: ")

    if(verificaMovimento(board, i , j)):
        fazMovimento(board, i , j, jogador)
        jogador = (jogador + 1)%2
    else:
        print("Posição já ocupada")
    
    ganhador = verificaGanhador(board)

print("---------------------")
printBoard(board)
print("Ganhador é o Jogador: ", ganhador)
print("---------------------")
