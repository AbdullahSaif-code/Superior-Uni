import math
def minimax(depth, nodeIndex, max_player, values):
    if depth == 3:
        return values[nodeIndex]

    if max_player:
        best = -math.inf # negative infinity
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values)
            best = max(best, val)
        return best
    else:
        best = math.inf # positive infinity
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values)
            best = min(best, val)
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
print("The optimal value is:", minimax(0, 0, True, values))