from jogo_da_velha import blank, token, checkWinner


def movimentAI(board, player):
    possibilities = getPositions(board)
    bestValue = None
    bestMovement = None
    for possibility in possibilities:
        board[possibility[0]][possibility[1]] = token[player]
        value = minimax(board, player, 0)
        board[possibility[0]][possibility[1]] = blank

        if (bestValue is None):
            bestValue = value
            bestMovement = possibility
        elif (player == 0):
            if (value > bestValue):
                bestValue = value
                bestMovement = possibility
        elif (player == 1):
            if (value < bestValue):
                bestValue = value
                bestMovement = possibility

    return bestMovement[0], bestMovement[1]


def getPositions(board):
    positions = []
    for i in range(7):
        for j in range(7):
            if (board[i][j] == blank):
                positions.append([i, j])

    return positions


score = {
    "Empate": 0,
    "X": 1,
    "O": -1
}


def minimax(board, player, depth):
    if depth > 2:
        return 0

    winner = checkWinner(board)
    if (winner):
        return score[winner]

    player = (player + 1) % 2

    possibilities = getPositions(board)
    bestValue = None
    for possibility in possibilities:
        board[possibility[0]][possibility[1]] = token[player]
        value = minimax(board, player, depth + 1)
        board[possibility[0]][possibility[1]] = blank

        if (bestValue is None):
            bestValue = value
        elif (player == 0):
            if (value > bestValue):
                bestValue = value
        elif (player == 1):
            if (value < bestValue):
                bestValue = value

    return bestValue
