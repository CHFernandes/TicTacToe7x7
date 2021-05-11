from jogo_da_velha import blank, token, checkWinner


def movimentAI(board, player):
    possibilities = getPositions(board)
    bestValue = None
    bestMovement = None
    alfa = -2
    beta = 2
    for possibility in possibilities:
        board[possibility[0]][possibility[1]] = token[player]
        value = minimax(board, player, 0, alfa, beta)
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


def minimax(board, player, depth, alfa, beta):
    if depth > 4:
        return 0
    winner = checkWinner(board)
    if (winner):
        return score[winner]

    possibilities = getPositions(board)
    player = (player + 1) % 2
    if (player == 0):
        maxValue = -2
        for possibility in possibilities:
            if maxValue == 1:
                return maxValue
            board[possibility[0]][possibility[1]] = token[player]
            value = minimax(board, player, depth + 1, alfa, beta)
            board[possibility[0]][possibility[1]] = blank
            maxValue = max(maxValue, value)
            alfa = max(value, alfa)
            if beta <= alfa:
                break
            if maxValue == 1:
                    return maxValue
        return maxValue
    else:
        minValue = 2
        for possibility in possibilities:
            if minValue == -1:
                return minValue
            board[possibility[0]][possibility[1]] = token[player]
            value = minimax(board, player, depth + 1, alfa, beta)
            board[possibility[0]][possibility[1]] = blank
            minValue = min(minValue, value)
            beta = min(beta, value)
            if beta <= alfa:
                break
            if minValue == -1:
                    return minValue
        return minValue
